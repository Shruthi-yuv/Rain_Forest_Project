import json
from prompt import system_prompt

def load_mapping():
    """Load field mapping from JSON file."""
    try:
        with open('mapping.json') as f:
            mapping = json.load(f)
        return mapping
    except FileNotFoundError:
        print("Error: 'mapping.json' not found.")
        return {}

def extract_lhs_fields(mapping):
    """Extract lhs fields dynamically from the mapping file."""
    return [entry["lhs"] for entry in mapping.get("response", [])]

def map_fields(lhs_fields, rhs_mapping):
    """Maps lhs fields to rhs fields based on the given mapping."""
    response = []

    for lhs_field in lhs_fields:
        rhs_value = None
        for mapping in rhs_mapping.get("response", []):
            if lhs_field == mapping["lhs"]:
                rhs_value = mapping["rhs"]
                break
        response.append({"lhs": lhs_field, "rhs": rhs_value})

    return response

def main():
    """Main function to process mapping."""
    rhs_mapping = load_mapping()
    if not rhs_mapping:
        print("Error: Mapping file is empty or could not be loaded.")
        return

    lhs_fields = extract_lhs_fields(rhs_mapping)  # Extract fields dynamically

    print("\nSystem Prompt:\n", system_prompt)
    print("\nUser Input (lhs fields):\n", lhs_fields)

    mapped_fields = map_fields(lhs_fields, rhs_mapping)

    result = {
        "system_prompt": system_prompt,
        "response": mapped_fields
    }

    print("\nMapped Fields:\n", json.dumps(result, indent=2))


def run_mapper(lhs_fields, system_prompt, user_input_json):
    rhs_mapping = json.loads(user_input_json).get("rhs", [])
    response = [{"lhs": field, "rhs": field if field in rhs_mapping else None} for field in lhs_fields]
    return json.dumps({"response": response}, indent=2)

# with open("mapping.json", "r", encoding="utf-8") as file:
#     print("Mappings JSON Output:", file.read())


if __name__ == "__main__":
    main()
