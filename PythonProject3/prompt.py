# prompt.py
# prompts = {
#     "title": ["productTitle"],
#     "asin": ["skuId", "productId"],
#     "link": ["externalUrl"],
#     "description": ["description"],
#     "brand": ["brand"]
# }

# def match_lhs_rhs(lhs):
#     return prompts.get(lhs, [])
#
# def get_rhs_options(lhs):
#     return prompts.get(lhs, [])
#
# def fetch_product_details(products, product_id):
#     return products.get(product_id, "Product not found!")
#
# print("Debugging in PyCharm")
#
# if __name__ == "__main__":
#     # Get user input
#     lhs_input = input("Enter LHS: ")
#
#     # Find matching RHS values
#     matched_values = match_lhs_rhs(lhs_input)
#
#     # Print the output in JSON-like format
#     response = {"response": [{"lhs": lhs_input, "rhs": rhs} for rhs in matched_values]}
#
#     print(response)


system_prompt = """
You are an expert in matching e-commerce field names from one source to the destination fields based on their semantic meaning.

Given the user lhs (source fields) and rhs (destination fields), match the lhs fields to the rhs fields.
If you do not find a matching field, leave the value for rhs as null. Do not generate unwanted field names.
Additionally, extract product specifications and provide them in the following format:

### Example Output:
{
    "response": [
        { "lhs": "lhs_field_y", "rhs": "rhs_field_x" }
    ]
}

- Add all the fields from lhs to the output even if you could not find the rhs fields for the given lhs field, keeping the rhs value as null.
- The Google category ID is the category of the product; if the source (lhs) contains the category, map it to this field.
- If the source (lhs) contains any product links, map them to the `externalUrl` of the rhs.
- Even if the lhs values are duplicated with different sets of rhs fields, add them to the response.
- Before adding lhs fields, check if they exist in the lhs list provided by the user.
"""

user_input = {
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
}
