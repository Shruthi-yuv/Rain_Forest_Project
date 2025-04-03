import os
import json
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv
from langgraph.constants import START, END
from langgraph.graph import StateGraph, add_messages
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from key_extractor import JSONKeyExtractor  # Import LHS extractor
from prompt import user_input  # Import RHS fields

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key is missing. Check your .env file or environment variables.")

def load_lhs():
    with open("data.json", "r", encoding="utf-8") as file:
        catalog_json = json.load(file)

    extractor = JSONKeyExtractor(catalog_json)
    return extractor.extract_keys()

def load_rhs():
    return user_input.get("rhs", [])

class State(TypedDict):
    messages: Annotated[List, add_messages]

class LangGraphChatbot:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, openai_api_key=api_key)
        self.graph_builder = StateGraph(State)
        self.system_prompt = ""
        self.user_input = ""
        self._setup_graph()

    def _setup_graph(self):
        self.graph_builder.add_edge(START, "init_node")
        self.graph_builder.add_node("init_node", self.init_node)
        self.graph_builder.add_edge("init_node", "chatbot")
        self.graph_builder.add_node("chatbot", self.chatbot)
        self.graph_builder.add_edge("chatbot", END)

    def init_node(self, state: State) -> State:
        return {
            "messages": [
                SystemMessage(content=self.system_prompt),
                HumanMessage(content=self.user_input),
            ]
        }

    def chatbot(self, state: State) -> State:
        print("\nReceived User Input:", self.user_input)
        response = self.llm.invoke(state["messages"])

        response_text = response.content if isinstance(response, AIMessage) else str(response)

        try:
            structured_response = json.loads(response_text)
        except json.JSONDecodeError:
            print("\nError: AI response is not valid JSON. Trying to fix formatting...")
            structured_response = self.fix_json_format(response_text)

        mapped_values = self.get_mapped_values(structured_response)

        # Print final JSON output with actual values
        # print("\nFinal JSON Output:\n", json.dumps(mapped_values, indent=2))

        return {"messages": state["messages"] + [AIMessage(content=json.dumps(mapped_values, indent=2))]}

    def get_mapped_values(self, mappings):
        with open("data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        mapped_data = {}
        for lhs_field, rhs_field in mappings.items():
            keys = lhs_field.split(".")  # Split nested keys
            value = data

            try:
                for key in keys:
                    if "[" in key and "]" in key:  # Handle list indexes
                        key, index = key[:-1].split("[")
                        value = value[key][int(index)]
                    else:
                        value = value[key]

                mapped_data[rhs_field] = value  # Assign actual value
            except (KeyError, IndexError, TypeError):
                mapped_data[rhs_field] = None  # If key not found, set None

        return mapped_data

    def fix_json_format(self, text):
        try:
            start_index = text.find("{")
            end_index = text.rfind("}") + 1
            json_str = text[start_index:end_index]
            return json.loads(json_str)
        except Exception:
            return {"error": "Unable to fix AI response formatting"}

    def run(self):
        lhs_fields = load_lhs()
        rhs_fields = load_rhs()

        self.system_prompt = f"""
        You are an expert in matching e-commerce field names.
        Given the LHS (source fields) and RHS (destination fields), map them based on semantic meaning.
        Ensure that every LHS field is included in the output, even if it doesn't have an RHS match.

        LHS Fields: {json.dumps(lhs_fields, indent=2)}
        RHS Fields: {json.dumps(rhs_fields, indent=2)}
        """

        self.user_input = "Match these fields based on their meanings."

        graph = self.graph_builder.compile()

        events = graph.stream(
            {"messages": [SystemMessage(content=self.system_prompt), HumanMessage(content=self.user_input)]},
            {"configurable": {"thread_id": "1"}},
            stream_mode="values",
        )

        for event in events:
            if "messages" in event and event["messages"]:
                last_message = event["messages"][-1]
                if isinstance(last_message, AIMessage):
                    print("\nAI Output:\n", last_message.content)
            else:
                print("No messages received from AI.")

# Run the chatbot
if __name__ == "__main__":
    chatbot = LangGraphChatbot()
    chatbot.run()

