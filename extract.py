



from adobe.pdfservices.operation.auth.credentials import Credentials
from adobe.pdfservices.operation.exception.exceptions import ServiceApiException, ServiceUsageException, SdkException
from adobe.pdfservices.operation.execution_context import ExecutionContext
from adobe.pdfservices.operation.io.file_ref import FileRef
from adobe.pdfservices.operation.pdfops.extract_pdf_operation import ExtractPDFOperation
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_pdf_options import ExtractPDFOptions
from adobe.pdfservices.operation.pdfops.options.extractpdf.extract_element_type import ExtractElementType

import os.path
import zipfile
import json
import os
import shutil


folder_path = "./TestDataSet"
# ...............................Iterate through every pdf file in the folder........................................................

for element in os.listdir(folder_path):
    element_path = os.path.join(folder_path, element)  # Get the full path of the element
    filename = os.path.basename(element_path)  # Get just the filename
    zip_file = filename +".zip"

    # if os.path.isfile(zip_file):
    #     os.remove(zip_file)

    input_pdf = element_path

    try:

        #Initial setup, create credentials instance.
        credentials = Credentials.service_account_credentials_builder()\
            .from_file("./pdfservices-api-credentials.json") \
            .build()

    #Create an ExecutionContext using credentials and create a new operation instance.
        execution_context = ExecutionContext.create(credentials)
        extract_pdf_operation = ExtractPDFOperation.create_new()

    #Set operation input from a source file.
        source = FileRef.create_from_local_file(input_pdf)
        extract_pdf_operation.set_input(source)

    #Build ExtractPDF options and set them into the operation
        extract_pdf_options: ExtractPDFOptions = ExtractPDFOptions.builder() \
            .with_element_to_extract(ExtractElementType.TEXT) \
            .build()
        extract_pdf_operation.set_options(extract_pdf_options)

    #Execute the operation.
        result: FileRef = extract_pdf_operation.execute(execution_context)

    #Save the result to the specified location.
        result.save_as(zip_file)

        print("Successfully extracted information from PDF. Printing H1 Headers:\n");

        archive = zipfile.ZipFile(zip_file, 'r')
        jsonentry = archive.open('structuredData.json')
        jsondata = jsonentry.read()
        data = json.loads(jsondata)
        for element in data["elements"]:
            if(element["Path"].endswith("/H1")):
                print(element["Text"])


    except (ServiceApiException, ServiceUsageException, SdkException):
        logging.exception("Exception encountered while executing operation") 

    #........................extracting json file from the .zip file......................................................      

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()

    #.............................renaming the json file.................................................................    
    
    os.rename('structuredData.json', filename +'.json')

    #...................moving the .json file from root directory to 'Extracted_json_files'.................................


    source_file = filename +'.json'  # Replace with the actual path of the source file
    destination_folder = 'Extracted_json_files'  # Replace with the actual path of the destination folder

    # Cut (move) the file to the destination folder
    shutil.move(source_file, destination_folder)

    print("File moved successfully.") 

                






