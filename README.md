# Data Extraction from PDF Invoices

This project aims to extract invoice data from PDF files and store it in a CSV format. It utilizes the Adobe PDF Services API to perform the PDF extraction operation and extracts specific information from the resulting JSON files.

## Overview Of Repository

- `TestDataSet`folder contains the PDFs
- `Extracted_json_files`folder contains extracted .json files.
- `invoice_data.csv` file is the actual output.
- `extract.py`  extracts the JSON files from the PDFs
- `json_to_csv.py` generates the `invoice_data.csv` file containing the extracted invoice data from the json files

## Requirements

To run this project, you need to have the following dependencies installed:

- Python 3.x
- Adobe PDF Services API credentials (json file)
- Required Python packages (specified in the code)

## Installation

1. Clone the repository to your local machine:
```bash
  git clone https://github.com/riddhiman-ghatak/hackathon_RG.git
```


2. Navigate to the project directory:
```bash
  cd hackathon_RG
```


3. Install the required Python packages:
```bash
  pip install -r requirements.txt
```


## Usage

1. Place your PDF files in the `TestDataSet` folder.

2. Update the `pdfservices-api-credentials.json` file with your Adobe PDF Services API credentials.

3. Run the script to extract data from PDFs and generate JSON files:
```bash
  python extract.py
```


4. Run the script to convert JSON files to CSV format:
```bash
  python json_to_csv.py
```


5. The `extract.py` will extract the JSON files from the PDFs, process the data, and store it in the `Extracted_json_files` folder.

6. Finally, `json_to_csv.py` will generate the `invoice_data.csv` file containing the extracted invoice data from the json files.

## Algorithm

The `json_to_csv.py` script uses the following algorithm to extract invoice data from the JSON files:

1. Iterate through each JSON file in the `Extracted_json_files` folder.

2. Extract the invoice description using the 'bounds' attribute.

3. Extract the text data from the JSON file and store it in a list.

4. Remove leading and trailing whitespace from the text data.

5. Define variables to store the extracted data, such as invoice ID, number of transactions, mobile number, due date, name, customer email, and address.

6. Iterate through the text data list and extract specific information based on patterns and keywords.

7. Filter out unwanted phrases and elements from the list.

8. Extract the customer name from the first element of the filtered list.

9. Remove elements containing email and phone number from the filtered list.

10. Extract address line 1 and address line 2 from the filtered list.

11. Used the number of occurance of '$' sign to calculte the number transaction.

12. Iterate through the filtered list to extract transaction items, quantities, and rates.

13. Write the extracted data to the `invoice_data.csv` file.

## Customization

You can customize the code to fit your specific requirements. Here are some possible modifications:

- Update the list of column names in the `json_to_csv.py` file to match your desired CSV format.
- Modify the data extraction logic to extract additional fields or change the extraction criteria.
- Adjust the file paths and folder names to match your project structure.

## Deployment

If you want to deploy this project to a server or cloud environment, follow these steps:

1. Set up the environment by installing the required dependencies and packages.
2. Configure the server to run the `extract_data.py` and `json_to_csv.py` scripts periodically or on demand.
3. Ensure that the server has access to the necessary PDF files and the Adobe PDF Services API credentials.
4. Configure the output file paths and folder names according to your deployment environment.
5. Monitor the execution and logs to ensure successful extraction and CSV generation.


