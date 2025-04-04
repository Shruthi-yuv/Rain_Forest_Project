
E-Commerce Data Mapping Application
Overview:
This application is designed to map seller-provided product data to Mamenta's data structure for seamless integration into the marketplace. It automates the extraction, transformation, and mapping of product fields dynamically, ensuring consistency and accuracy in product listings.

Folder & File Structure 
├── data.py           # Contains seller's product information
├── env               # Stores OpenAI API key for authentication
├── data.json         # Contains raw product details from the seller
├── key_extractor.py  # Extracts keys from seller information
├── mapper.py         # Maps seller (lhs) fields to Mamenta (rhs) fields
├── mapper_1.py       # Dynamically maps lhs and rhs fields without explicitly specifying lhs
├── mapping.json      # Stores mappings of lhs and rhs fields
├── data_mapper.py    # Maps lhs and rhs fields with corresponding data types using an AI functions
├── main.py           # Integrates all components and executes the entire workflow
├── prompt.py         # Contains system prompt and user input rules
└── requirements.txt  # Lists required dependencies


Workflow:
1.Extract Seller Data Fields
  key_extractor.py extracts all field names from data.json (seller's product data).

2.Field Mapping (Seller → Mamenta)
  mapper.py maps the lhs (seller) field to the rhs (Mamenta) field.
  mapper_1.py dynamically maps extracted fields to corresponding Mamenta fields using mapping.json.
  The mapped output is stored in mapping.json.

3.Data Type Mapping
   data_mapper.py processes mapping.json and associates data types with mapped fields.

4️.Final Integration
  main.py calls all components (key_extractor.py, mapper_1.py, data_mapper.py) and generates the final mapped output.

5️.Prompt System:
  prompt.py defines how input and output should be processed during field mapping.

How to Run the Application:
1.Install Dependencies:
Ensure you have Python 3.7+ installed. Then, install the required dependencies using:
pip install -r requirements.txt
2️.Set Up API Key
Store your OpenAI API Key in the env file for authentication.
3️.Run the Application
Execute the main script:
python main.py


Expected Output:
Extracted keys from seller product information.
Mappings of seller fields (lhs) → Mamenta fields (rhs) stored in mapping.json.
Mapped fields along with their data types.

Dependencies:
Refer to requirements.txt for the list of required Python libraries