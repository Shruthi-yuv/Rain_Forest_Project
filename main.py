import json
from key_extractor import JSONKeyExtractor
from mapper_1 import map_fields, load_mapping
# from data_mapper import ProductMapper


def main():
    # Step 1: Extract keys from data.json using JSONKeyExtractor
    with open("data.json", "r", encoding="utf-8") as file:
        catalog_json = json.load(file)

    extractor = JSONKeyExtractor(catalog_json)
    lhs_fields = extractor.extract_keys()  # Extracted keys will be used as lhs_fields
    print("Extracted LHS Fields:", lhs_fields)

    # Step 2: Load mapping from mapping.json
    rhs_mapping = load_mapping()
    if not rhs_mapping:
        print("Error: Mapping file is empty or invalid.")
        return

    # Perform the LHS-to-RHS mapping dynamically
    mapped_fields = map_fields(lhs_fields, rhs_mapping)

    # Format the mapping result
    result = {
        "response": mapped_fields
    }

    # Print the mapping result
    print("\nMapped Fields:")
    print(json.dumps(result, indent=2))

    # Step 3: Call ProductMapper for final data mapping
    # product_mapper = ProductMapper("mapping.json", "data.json")
    # final_product_data = product_mapper.get_product()

    # print("\nFinal Mapped Product Data:")
    # print(json.dumps(final_product_data, indent=2))


if __name__ == "__main__":
    main()
