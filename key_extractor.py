import json
from typing import Any, Dict, List, Union


class JSONKeyExtractor:
    def __init__(self, json_data: Union[Dict[str, Any], List[Any]]):
        self.json_data = json_data

    def extract_keys(self, data: Union[Dict[str, Any], List[Any]] = None, parent_key: str = "") -> List[str]:
        data = data if data is not None else self.json_data

        keys = []

        if isinstance(data, dict):
            for key, value in data.items():
                full_key = f"{parent_key}.{key}" if parent_key else key
                keys.append(full_key)
                keys.extend(self.extract_keys(value, full_key))
        elif isinstance(data, list):
            for index, item in enumerate(data):
                child_keys = self.extract_keys(item, f"{parent_key}[{index}]") if parent_key else self.extract_keys(item)
                keys.extend(child_keys)

        return keys

if __name__ == "__main__":
    with open("data.json", "r", encoding="utf-8") as file:
        catalog_json = json.load(file)

    extractor = JSONKeyExtractor(catalog_json)
    keys = extractor.extract_keys()
    print(keys)
