import json

# Read JSON data from file
with open('structuredData.json', 'r') as f:
    json_data = json.load(f)

# Extract data with key 'Text'
text_data = [element.get('Text', '') for element in json_data.get('elements', [])]

# Print the extracted text data
# for text in text_data:
#     print(text)
print(text_data[0])

