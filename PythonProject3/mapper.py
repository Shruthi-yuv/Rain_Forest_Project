import os
import json
from typing import TypedDict, Annotated, List
from dotenv import load_dotenv
from langgraph.constants import START, END
from langgraph.graph import StateGraph, add_messages
from langchain_openai import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OpenAI API key is missing. Check your .env file or environment variables.")


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
        print("Messages received:", state["messages"])
        response = self.llm.invoke(state["messages"])

        response_text = response.content if isinstance(response, AIMessage) else str(response)
        try:
            structured_response = json.loads(response_text)
        except json.JSONDecodeError:
            structured_response = {"error": "Invalid response format from LLM"}

        return {"messages": state["messages"] + [AIMessage(content=json.dumps(structured_response, indent=2))]}

    def run(self, system_prompt: str, user_input: str):
        self.system_prompt = system_prompt
        self.user_input = user_input
        graph = self.graph_builder.compile()

        events = graph.stream(
            {"messages": [SystemMessage(content=self.system_prompt), HumanMessage(content=self.user_input)]},
            {"configurable": {"thread_id": "1"}},
            stream_mode="values",
        )

        for event in events:
            print("Raw event:", event)
            last_message = event["messages"][-1]
            if isinstance(last_message, AIMessage):
                print("Assistant Response:", last_message.content)
            else:
                print("Assistant Response:", last_message)


# Run chatbot
if __name__ == "__main__":
    system_prompt = """
    You are an expert in matching e-commerce field names from one source to the destination fields based on their semantic meaning.

    Given the user lhs (source fields) and rhs (destination fields), match the lhs fields to the rhs fields.
    If you do not find a matching field, leave the value for rhs as null. Do not generate unwanted field names.
    Additionally, extract product specifications and provide them in the following format:

    Example Input:
    {
        "lhs": [
            "lhs_field_y"
        ],

        "rhs": [
            "rhs_field_x"
        ]
    }

    ### Example Output:
    {
        "response": [
            { "lhs": "lhs_field_y", "rhs": "rhs_field_x" }
        ]
    }

    Add all the fields from lhs to the output even if the you could not find the rhs fields for the given lhs field, keep the rhs value as null

    The google category Id is nothing but the category of the product, if the source (lhs) contains the category map it to this field

    If the source(lhs) contains any product links then map them to the externalUrl of the rhs

    Even if the lhs values are duplicated and different set of rhs fields then add them to the response

    Before adding the lhs fields check if they exists in the lhs list provided by the user. 

    """
    # User Input JSON
    user_input = """
    Map the below lhs fields to the rhs fields

    {
    "lhs": [
    "product.title",
    "product.description",
    "product.long_description",
    "product.brand",
    "product.heroImage",
    "product.frontImage",
    "product.backImage",
    "product.boxImage",
    "product.bottomImage",
    "product.topImage",
    "product.rightImage",
    "product.leftImage",
    "product.sizeChartImage",
    "product.swatchImage",
    "product.additionalImages",
    "product.certificationImages",
    "product.videoURL",
    "product.googleCategoryId",
    "product.brandCategory",
    "product.countryOfOrigin",
    "product.externalURL",
    "product.itemCondition",
    "product.itemPrice",
    "product.salePrice",
    "product.currency",
    "product.upc",
    "product.gTIN",
    "product.mpn",
    "product.productType",
    "product.model",
    "product.variation",
    "product.size",
    "product.color",
    "product.resistance",
    "product.material",
    "product.pattern",
    "product.shape",
    "product.finish",
    "product.capacity",
    "product.batteryLife",
    "product.style",
    "product.gender",
    "product.ageGroup",
    "product.isBundled",
    "product.dimensions.length",
    "product.dimensions.height",
    "product.dimensions.unit",
    "product.weight",
    "product.weight.unit",
    "product.packageWeight",
    "product.shippingWeight",
    "product.packageDepth",
    "product.packageHeight",
    "product.packageWidth",
    "product.warranty",
    "product.warrantyType",
    "product.whatsInTheBox",
    "product.asin",
    "product.feature_bullets",
    "product.attributes",
    "product.specifications",
    "product.attributeName",
    "product.attributeValues"
]


    "rhs": [
    "productTitle",
    "description",
    "longDescription",
    "brand",
    "heroImage",
    "frontImage",
    "backImage",
    "boxImage",
    "bottomImage",
    "topImage",
    "rightImage",
    "leftImage",
    "sizeChartImage",
    "swatchImage",
    "additionalImageLinks",
    "productCertificationImages",
    "videoURL",
    "googleCategoryId",
    "brandCategory",
    "countryOfOrigin",
    "externalURL",
    "itemCondition",
    "itemPrice",
    "salePrice",
    "currency",
    "upc",
    "gTIN",
    "mpn",
    "productType",
    "model",
    "variation",
    "size",
    "color",
    "resistance",
    "material",
    "pattern",
    "shape",
    "finish",
    "capacity",
    "batteryLife",
    "style",
    "gender",
    "ageGroup",
    "isBundled",
    "length",
    "height",
    "dimensionUnit",
    "weight",
    "weightUnit",
    "packageWeight",
    "shippingWeight",
    "packageDepth",
    "packageHeight",
    "packageWidth",
    "warranty",
    "warrantType",
    "whatsInTheBox",
    "ASIN",
    "featureBullets",
    "productAttributes",
    "productSpecifications",
    "attributeName",
    "attributeValues"
]

    }"""


    chatbot = LangGraphChatbot()
    chatbot.run(system_prompt, user_input)


class ProductMapper:
    pass