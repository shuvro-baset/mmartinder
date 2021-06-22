import requests
import json
import pandas as pd

url = "https://api.propertydata.co.uk/flood-risk?key=XSOVV5OFQ5&postcode=DE217AP"
data = requests.get(url)
if data.status_code != 200:
    print(data.content)

json_data = json.loads(data.content)
result = [json_data]

df = pd.DataFrame(result)
df.to_excel('flood_risk.xlsx',sheet_name='flood_risk', index=False)
