# import json
# from key_extractor import JSONKeyExtractor  # Extract LHS fields from JSON
# from mapper_1 import map_fields, load_mapping  # Map LHS fields to RHS fields
# from prompt import user_input  # Get RHS fields
# from data_mapper import LangGraphChatbot  # Match LHS and RHS fields with data types
#
#
# def main():
#     # Step 1: Extract keys from data.json using JSONKeyExtractor
#     with open("data.json", "r", encoding="utf-8") as file:
#         catalog_json = json.load(file)
#
#     extractor = JSONKeyExtractor(catalog_json)
#     lhs_fields = extractor.extract_keys()
#     print("Extracted LHS Fields:", lhs_fields)
#
#     # Step 2: Load mapping from mapping.json
#     rhs_mapping = load_mapping()
#     if not rhs_mapping:
#         print("\nError: Mapping file is empty or invalid.")
#         return
#
#     print("\nDebug - RHS Mapping Loaded in main.py:")
#     print(json.dumps(rhs_mapping, indent=2))  # Print RHS mapping to verify
#
#     # Step 3: Perform the LHS-to-RHS mapping dynamically
#     mapped_fields = map_fields(lhs_fields, rhs_mapping)
#
#     # Step 4: Load RHS fields from prompt.py
#     rhs_fields = user_input.get("rhs", [])
#
#     # Step 5: Use LangGraphChatbot for final processing
#     chatbot = LangGraphChatbot()
#     chatbot.run()
#
#
# if __name__ == "__main__":
#     main()
#
#
import json
from key_extractor import JSONKeyExtractor
from mapper_1 import load_mapping, extract_lhs_fields, map_fields
from data_mapper import ProductMapper


def extract_json_keys(data_file):
    """Extract all keys from the JSON structure."""
    with open(data_file, "r", encoding="utf-8") as file:
        json_data = json.load(file)

    extractor = JSONKeyExtractor(json_data)
    keys = extractor.extract_keys()
    return keys


def get_mapped_fields(keys, mapping_file):
    """Match extracted keys with RHS fields."""
    mapping_data = load_mapping()
    if not mapping_data:
        print("Error: Mapping file is empty or could not be loaded.")
        return []

    mapped_fields = map_fields(keys, mapping_data)
    return mapped_fields


def map_product_data(mapping_file, data_file):
    """Map the extracted and matched fields to product data."""
    mapper = ProductMapper(mapping_file, data_file)
    mapped_data = mapper.get_product()
    return mapped_data


if __name__ == "__main__":
    DATA_FILE = "data.json"
    MAPPING_FILE = "mapping.json"

    extracted_keys = extract_json_keys(DATA_FILE)
    print("\nExtracted Keys:\n", extracted_keys)

    mapped_fields = get_mapped_fields(extracted_keys, MAPPING_FILE)
    print("\nMapped Fields:\n", json.dumps(mapped_fields, indent=2))

    final_mapped_data = map_product_data(MAPPING_FILE, DATA_FILE)
    # print("\nFinal Mapped Product Data:\n", json.dumps(final_mapped_data, indent=2))


