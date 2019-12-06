import json
import pandas as pd
with open('source_documents.json', 'r') as f:
    data = json.load(f)

data_df = pd.DataFrame(data)
# print(data_df.columns)
# print(data_df.shape)
print(data_df.head())
