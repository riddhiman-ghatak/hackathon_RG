import json
import csv
import os
import re

#......................................define the folder path where extracted json files are stored .............................                                       
folder_path = "./Extracted_json_files"

#..............................define invoice_data.csv file.......................................................................

filename = "invoice_data.csv"
# Define the column names
column_names = [
    "Bussiness__City",
    "Bussiness__Country",
    "Bussiness__Description",
    "Bussiness__Name",
    "Bussiness__StreetAddress",
    "Bussiness__Zipcode",
    "Customer__Address__line1",
    "Customer__Address__line2",
    "Customer__Email",
    "Customer__Name",
    "Customer__PhoneNumber",
    "Invoice__BillDetails__Name",
    "Invoice__BillDetails__Quantity",
    "Invoice__BillDetails__Rate",
    "Invoice__Description",
    "Invoice__DueDate",
    "Invoice__IssueDate",
    "Invoice__Number",
    "Invoice__Tax"
]

# Create a CSV file and write the data
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    
    # Write the column names
    writer.writerow(column_names)
    print("column names updated")
#.............................................................................................................................................

#.................................now iterate through every json file in the extracted_json_files folder..................................

# Iterate through every element in the folder
for element in os.listdir(folder_path):
    element_path = os.path.join(folder_path, element)  # Get the full path of the element
    # Read JSON data from file
    with open(element_path, 'r') as f:
      json_data = json.load(f)

    #............... firstly extract invoice_description using 'bounds' attribute.................................................

    invoice_description = ''
    for element in json_data['elements']:
      if 'Bounds' in element:
        bounds = element['Bounds']
        # print(bounds[0])
        if bounds[0] < 241 and bounds[0] > 240: # got this range from comparing the bounds attribute of invoice_details
          if 'Text' in element:
            if 'DETAILS' in element['Text']:
                continue
            else:
                invoice_description += element['Text']
  
    
    
    # .....................................Extract data with key 'Text'and store in a List............................................................
      
    text_data = [element.get('Text', '') for element in json_data.get('elements', [])]

    #.......................................Remove whitespace from list text_data.................................................. 
    new_list = []
    for element in text_data:
      if element.strip():  # Removes leading/trailing whitespace
          new_list.append(element)

    #.......................... Now let's define some variables, which we are going to extract from the list........................

    invoice_id= ''
    number_of_transaction = -3 #initialised as -3 bcz I will count number of "$" sign and there are another 3 terms with "$" sign (payment , subtotal ,total due) 
    mobile_number = ''
    due_date =''
    name = ''
    customer_email = ''
    address_line_1 =''
    address_line_2 =''
    #invoice_description=''
    business_name='NearBy Electronics'
    street='3741 Glory Road'
    zipcode='38556'
    issue_date = '12-05-2023'
    tax='10'
    city='Jamestown'
    country='Tennessee, USA'
    business_description='We are here to serve you better. Reach out to us in case of any concern or feedbacks'

    #..................................................................................................................................
    #............................let's iterate through every element in new_list[]....................................................
    for text in new_list:
        # ..............................now extract invoice_number................................
        if 'Invoice#' or 'Issue date' in text:
            invoice_number = re.findall(r'[A-Z0-9]', text)
            invoice_number = ''.join(invoice_number)

            # Remove "I" from the first position
            if invoice_number.startswith("I"):
                invoice_number = invoice_number[1:]

            # Remove "I" or "I12052023" from the end {bcz some string contains 'Issue date' or 'Issue date 12-05-2023' at the last}
            if invoice_number.endswith("I12052023"):
              invoice_number = invoice_number[:-9]
            elif invoice_number.endswith("I"):
                invoice_number = invoice_number[:-1]
            if len(invoice_number)>10:
              invoice_id=invoice_number

        

        #...................................now extract email....................................................
        if '@'in text:
            email = ""
            for i in range(len(text)):
              if text[i] == "@":
                  j = i - 1
                  while j >= 0 and text[j] != " ":
                      email = text[j] + email
                      j -= 1
                  email += "@"
                  j = i + 1
                  while j < len(text) and text[j] != " ":
                      email += text[j]
                      j += 1
            customer_email = email

        #............................I am searching for 'XXX-XXX-XXXX' pattern in the string for phone_number.........................
         
        phone_number = re.search(r"\d{3}-\d{3}-\d{4}", text)
        if phone_number:
            mobile_number = phone_number.group()

        #............................searching for due date............................................................    

        if 'Due date' in text:
            date_pattern = r"\d{2}-\d{2}-\d{4}"
            due_date = re.search(date_pattern, text).group()  

        #..............................calculating number of '$' to calculate number of transaction.........................

        if '$' in text:
            number_of_transaction +=1     


    
    # .................Create a new list to store the filtered elements  and remove unwanted phrases................
    filtered_list = []

    # Iterate over each text in the list
    for text in new_list:
        # Check if the text contains any of the unwanted phrases
        if 'NearBy Electronics' in text \
            or '3741 Glory Road, Jamestown' in text \
            or 'Tennessee, USA' in text \
            or '38556' in text \
            or 'We are here to serve you better' in text \
            or 'Invoice#' in text \
            or 'Due date' in text \
            or 'Issue date' in text \
            or '12-05-2023' in text \
            or 'Reach out to us in case of any concern or feedbacks' in text \
            or 'BILL TO' in text \
            or 'DETAILS' in text \
            or 'PAYMENT' in text \
            or 'ITEM' in text \
            or 'QTY' in text \
            or 'RATE' in text \
            or 'AMOUNT' in text \
            or 'Subtotal' in text \
            or 'Tax %' in text \
            or '$' in text \
            or 'Total Due' in text \
            or 'QTY' in text:
                continue  # Skip the current text if it matches any unwanted phrase
        else:
            filtered_list.append(text)  # Add the text to the filtered list

    new_list= filtered_list
    #............................................................................................................................
    
    new_list.pop() # remove the value of tax which is 10 

    #.................................................................................................................................

    # ..........as we have deleted unwanted phrases customer_name should be at index 0..............................................
    first_string = new_list[0]
    words = first_string.split()
    name = words[0] + " " + words[1]

    new_list.remove(new_list[0]) # remove the string with name this string may contain email or phone number but we have extracted that earlier
    #................................................................................................................................

    #...........after extracting names we will remove the elements containg email and phone number.................................

    filtered_list_2 = []

    for text in new_list:
        if '@' in text: # for email
            continue
        elif re.search(r"\d{3}-\d{3}-\d{4}", text): # for phone_number
            continue
        else:
            filtered_list_2.append(text)

    new_list = filtered_list_2 
    #......................................................................................................................

    #..............after removing all unwanted phrases, 1st element may contain  .com / om (part of email)..............................     

    if len(new_list[0].split())==1:
        customer_email = customer_email + new_list[0] # sometiimes little bit portion of emails is getting checked as different text/element
        new_list.remove(new_list[0])

    #...............extracting address_line_1, address_line_2 ...................................................................    

    if len(new_list[0].split())==3:
        address_line_1 = new_list[0]
        address_line_2 = new_list[1]
        new_list.remove(new_list[0])
        new_list.remove(new_list[0])

    elif len(new_list[0].split())>3:
        words = new_list[0].split()
        address_line_1 = words[0]+words[1]+words[2]
        address_line_2 = words[2:]

        new_list.remove(new_list[0])

    #...........................now using a loop we will extract the transaction item, quantity, rate.................................... 
    
    last_index = (len(new_list))-1
    trans_starting_index = last_index - 3*number_of_transaction # we are multiplying with 3 as there are 3 elements item,quantity and rate
    # for i in range(0,(invoice_del_last_index+1)): #the element  just before the first digit of new_list will be name of an item 
    #      invoice_description += new_list[i]
                
    for i in range(0,number_of_transaction):
        item = new_list[((trans_starting_index+1)+ i*3)]
        quantity=new_list[((trans_starting_index+1)+i*3+1)]
        rate = new_list[((trans_starting_index+1)+i*3+2)]

    #.................................................................................................................................
    
    #...............................now update the csv file.............................................................................     

        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            # Write the data rows
            writer.writerow([
              city, country, business_description, business_name, street, zipcode, address_line_1, address_line_2, customer_email, name, mobile_number, item, quantity, rate, invoice_description, due_date, issue_date, invoice_id,tax
            ])
    


                
        
                


     
    # print (invoice_id)
    #print (customer_email)
    # print(mobile_number)
    # print (due_date)
    #print (name)
    #print(address_line_1)
    #print(address_line_2)
    #print(first_digit_index)
    #print(invoice_description)
    #print(number_of_transaction)

    # for text in new_list:
    #     print (type(text))






                          
