import json
import csv
import re

#  
# 
import json

with open('Extracted_json_files/output23.pdf.json', 'r') as f:
    json_data = json.load(f)

details = ''
for element in json_data['elements']:
    bounds = element['Bounds']
    # print(bounds[0])
    if bounds[0] < 241 and bounds[0] > 240:
        if 'Text' in element:
            if 'DETAILS' in element['Text']:
                continue
            else:
                details += element['Text']

print(details )







        



f
     
      

# #text_data.remove("  ")

# #print(len(text_data))

#  #Print the extracted text data
# #print(type(text_data[8])) 
# # for text in text_data:
# #       print(text)
# #print(text_data[8])


# new_list = []

# for element in text_data:
#      if element.strip():  # Removes leading/trailing whitespace
#          new_list.append(element)

# for text in new_list:
#    print(text) 




# myString = "Kerry Bergnaum Kerry_Bergnaum@yahoo.c om 189-052-5595"

# email = ""
# for i in range(len(myString)):
#   if myString[i] == "@":
#     j = i - 1
#     while j >= 0 and myString[j] != " ":
#       email = myString[j] + email
#       j -= 1
#     email += "@"
#     j = i + 1
#     while j < len(myString) and myString[j] != " ":
#       email += myString[j]
#       j += 1
# #print(email)

# import re
# invoice_id = ''
# for text in new_list:
#     if 'Invoice#' in text:
# #string = "Invoice# TG04EM6808839862502629422968 Issue date"
#       invoice_number = re.findall(r'[A-Z0-9]', text)
#       invoice_number = ''.join(invoice_number)

# # Remove "I" from the first position
#       if invoice_number.startswith("I"):
#         invoice_number = invoice_number[1:]

# # Remove "I" or "I12052023" from the end
#       if invoice_number.endswith("I12052023"):
#         invoice_number = invoice_number[:-9]
#       elif invoice_number.endswith("I"):
#           invoice_number = invoice_number[:-1]

#       invoice_id = invoice_number
# #print(invoice_id)


# import re

# string = "Kerry Bergnaum Kerry_Bergnaum@yahoo.c om 189-052-5595"
# phone_number = re.search(r"\d{3}-\d{3}-\d{4}", string).group()

# #print(phone_number)

# import re

# string = "Due date: 14-06-2023"
# date_pattern = r"\d{2}-\d{2}-\d{4}"
# date = re.search(date_pattern, string).group()

# #print(date)


# new_list = ["hello", "world", "123", "456"]
# index_at_first_occuring_digit = -1 #initialised the index at which a digit first occur in the new_list,

# for index, text in enumerate(new_list):
#     if text.isdigit():
#         index_at_first_occuring_digit = index
#         break

# #print(index_at_first_occuring_digit)


# def check_string(s):
#     return all(c.isupper() or c.isdigit() for c in s)

# # Example usage:
# #print(check_string("A124FBFUFIFM8"))  # True
# #print(check_string("456-951-26641"))  # False

# import re

# s = "QA23GSEDDLR17T5THL7KRIELFWJ9K Issue date"
# code = re.search(r'\b[A-Z0-9]+\b', s).group()

# #print (len(code))  # QA23GSEDDLR17T5THL7KRIELFWJ9K




 








