# import zipfile
# import json
# import pandas as pd
# from pandas.io.json import json_normalize

# with zipfile.ZipFile('ExtractTextInfoFromPDF.zip') as myzip:
#     with myzip.open('structuredData.json') as myfile:
#         data = json.load(myfile)

# df = pd.json_normalize(data)
# df.to_csv('data.csv', index=False)
import zipfile
with zipfile.ZipFile('ExtractTextInfoFromPDF.zip', 'r') as zip_ref:
    zip_ref.extractall()
