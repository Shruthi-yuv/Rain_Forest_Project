# import json
# from typing import List, Dict, Tuple, Callable, Optional
#
#
# class ProductAttribute:
#     def __init__(self, name: str, values: List[str]):
#         self.attributeName: str = name
#         self.attributeValues: List[str] = values
#
#
# class ProductMapper:
#     PRODUCT_DATA_DATATYPE_CONFIG: Dict[str, type] = {
#         "productId": str,
#         "skuId": str,
#         "productTitle": str,
#         "description": str,
#         "longDescription": str,
#         "brand": str,
#         "heroImage": str,
#         "frontImage": str,
#         "backImage": str,
#         "boxImage": str,
#         "bottomImage": str,
#         "topImage": str,
#         "rightImage": str,
#         "leftImage": str,
#         "sizeChartImage": str,
#         "swatchImage": str,
#         "additionalImageLinks": List[str],
#         "productCertificationImages": List[str],
#         "videoURL": str,
#         "googleCategoryId": str,
#         "brandCategory": str,
#         "countryOfOrigin": str,
#         "externalURL": str,
#         "itemCondition": str,
#         "itemPrice": str,
#         "salePrice": str,
#         "currency": str,
#         "upc": str,
#         "gTIN": str,
#         "mpn": str,
#         "productType": str,
#         "model": str,
#         "variation": str,
#         "size": str,
#         "color": str,
#         "resistance": str,
#         "material": str,
#         "pattern": str,
#         "shape": str,
#         "finish": str,
#         "capacity": str,
#         "batteryLife": str,
#         "style": str,
#         "gender": str,
#         "ageGroup": str,
#         "isBundled": str,
#         "length": str,
#         "height": str,
#         "dimensionUnit": str,
#         "weight": str,
#         "weightUnit": str,
#         "packageWeight": str,
#         "shippingWeight": str,
#         "packageDepth": str,
#         "packageHeight": str,
#         "packageWidth": str,
#         "warranty": str,
#         "warrantType": str,
#         "whatsInTheBox": str,
#         "ASIN": str,
#         "featureBullets": List[str],
#         "productAttributes": List[ProductAttribute],
#         "productSpecifications": List[ProductAttribute],
#     }
#
#     def __init__(self, mapping_file: str, data_file: str):
#         with open(mapping_file, "r", encoding="utf-8") as file:
#             self.mapping_dict = json.load(file)
#
#         # 🔹 Ensure self.mapping_dict is a dictionary
#         if isinstance(self.mapping_dict, list):
#             self.mapping_dict = {"response": self.mapping_dict}
#
#         with open(data_file, "r", encoding="utf-8") as file:
#             self.data_dict = json.load(file)
#
#     @staticmethod
#     def get_nested_value(data: dict, key_path: str) -> Optional[object]:
#         keys = key_path.split(".")
#         for key in keys:
#             if isinstance(data, dict) and key in data:
#                 data = data[key]
#             else:
#                 print(f"WARNING: '{key_path}' not found in data.json")
#                 return None
#         return data
#
#     @staticmethod
#     def attr_mapper(spec_object: dict) -> Optional[Dict[str, object]]:
#         if not isinstance(spec_object, dict) or "name" not in spec_object or "value" not in spec_object:
#             print(f"WARNING: Invalid specification format: {spec_object}")
#             return None
#         return {"attributeName": spec_object["name"], "attributeValues": [spec_object["value"]]}
#
#     @staticmethod
#     def additional_image_mapper(images: object) -> List[str]:
#         if isinstance(images, list):
#             return [img["link"] for img in images if isinstance(img, dict) and "link" in img]
#         elif isinstance(images, str):  # Handle case where it's a single string
#             return [images]
#         return []
#
#     @staticmethod
#     def buybox_price_mapper(price_data: object) -> Optional[str]:
#         return price_data.get("value") if isinstance(price_data, dict) else None
#
#     def map_values(
#         self,
#         source_field: str,
#         destination_field: str,
#         destination_field_type: type,
#         value: object,
#         product_data: dict
#     ) -> None:
#         if value is None:
#             print(f"WARNING: Missing value for '{source_field}'")
#             return
#
#         if (source_field, destination_field) in self.FIELD_TUPLE_DICT:
#             value = self.FIELD_TUPLE_DICT[(source_field, destination_field)](value)
#
#         # Store the mapped value
#         product_data[destination_field] = value
#
#     FIELD_TUPLE_DICT: Dict[Tuple[str, str], Callable] = {
#         ("product.images", "additionalImageLinks"): additional_image_mapper,
#         ("product.specifications", "productSpecifications"): lambda x: [
#             ProductMapper.attr_mapper(item) for item in x if isinstance(item, dict)
#         ],
#         ("product.buybox_winner.price", "itemPrice"): buybox_price_mapper,
#     }
#
#     def get_product(self) -> Dict[str, object]:
#         product_data = {}
#
#         for field_map_dict in self.mapping_dict.get("response", []):
#             source_field = field_map_dict.get("lhs")
#             destination_field = field_map_dict.get("rhs")
#
#             if not source_field or not destination_field:
#                 continue
#
#             source_value = self.get_nested_value(self.data_dict, source_field)
#             print(f"Mapping '{source_field}' → '{destination_field}' | Found: {source_value}")
#
#             self.map_values(
#                 source_field,
#                 destination_field,
#                 self.PRODUCT_DATA_DATATYPE_CONFIG.get(destination_field, str),
#                 source_value,
#                 product_data,
#             )
#
#         print("\nFINAL MAPPED DATA:\n", json.dumps(product_data, indent=2))
#         return product_data
#
#
# if __name__ == "__main__":
#     mapper = ProductMapper("mapping.json", "data.json")
#     mapped_data = mapper.get_product()




from langgraph.graph import StateGraph
from langgraph.graph import StateGraph
from typing import Dict, Any
import json
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4", temperature=0)

class MapperState:
    def __init__(self, value_object: Dict[str, Any], target_schema: Dict[str, Any]):
        self.value_object = value_object
        self.target_schema = target_schema
        self.generated_function = None

def detect_mismatches(state: MapperState):
    mismatches = {}
    for key, value in state.value_object.items():
        if key in state.target_schema:
            expected_type = type(state.target_schema[key]).__name__
            actual_type = type(value).__name__
            if expected_type and expected_type != actual_type:
                mismatches[key] = (actual_type, expected_type)
    return {"mismatches": mismatches}


def generate_mapping_function(state: MapperState, mismatches: Dict[str, tuple]):
    prompt = f"""
Given the following mismatches between an input data object and a target JSON schema, generate a Python function to correctly map the values.

Mismatches:
{json.dumps(mismatches, indent=2)}

If the expected type is a list of strings, extract the relevant string values from the input data.
For example, if the input data contains a list of objects with a 'link' key, transform them into a list of their 'link' values.

The function should take 'input_data' as an argument and return a dictionary with correctly formatted values.
"""
    response = llm.invoke(prompt)
    state.generated_function = response.content
    return state

workflow = StateGraph(MapperState)
workflow.add_node("detect_mismatches", detect_mismatches)
workflow.add_node("generate_function", generate_mapping_function)

workflow.add_edge("detect_mismatches", "generate_function")
workflow.set_entry_point("detect_mismatches")

app = workflow.compile()

def chatbot(value_object, target_schema):
    initial_state = MapperState(value_object, target_schema)
    final_state = app.invoke(initial_state.__dict__)
    return final_state.generated_function

if __name__ == "__main__":
    value_object = {
        "images": [
            {"link": "https://some.thing.com/image1/jpg", "type": "MAIN"},
            {"link": "https://some.thing.com/image2/jpg", "type": "SIDE"},
            {"link": "https://some.thing.com/image3/jpg", "type": "BACK"}
        ]
    }
    target_schema = {"additionalImages": []}
    generated_function_code = chatbot(value_object, target_schema)
    print("Generated Mapping Function:\n", generated_function_code)






