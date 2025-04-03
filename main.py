import json
from key_extractor import JSONKeyExtractor  # Extract LHS fields from JSON
from mapper_1 import map_fields, load_mapping  # Map LHS fields to RHS fields
from prompt import user_input  # Get RHS fields
from data_mapper import LangGraphChatbot  # Match LHS and RHS fields with data types


def main():
    # Step 1: Extract keys from data.json using JSONKeyExtractor
    with open("data.json", "r", encoding="utf-8") as file:
        catalog_json = json.load(file)

    extractor = JSONKeyExtractor(catalog_json)
    lhs_fields = extractor.extract_keys()
    print("Extracted LHS Fields:", lhs_fields)

    # Step 2: Load mapping from mapping.json
    rhs_mapping = load_mapping()
    if not rhs_mapping:
        print("\nError: Mapping file is empty or invalid.")
        return

    print("\nDebug - RHS Mapping Loaded in main.py:")
    print(json.dumps(rhs_mapping, indent=2))  # Print RHS mapping to verify

    # Step 3: Perform the LHS-to-RHS mapping dynamically
    mapped_fields = map_fields(lhs_fields, rhs_mapping)

    # Step 4: Load RHS fields from prompt.py
    rhs_fields = user_input.get("rhs", [])

    # Step 5: Use LangGraphChatbot for final processing
    chatbot = LangGraphChatbot()
    chatbot.run()


if __name__ == "__main__":
    main()


