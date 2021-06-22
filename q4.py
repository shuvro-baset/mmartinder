import requests
import json
import pandas as pd

url = "https://api.propertydata.co.uk/postcode-key-stats?key=XSOVV5OFQ5&region=north_west"
data = requests.get(url)
if data.status_code != 200:
    print(data.content)

json_data = data.json()

result = json_data['data']
print(result)
df = pd.DataFrame(result)
df.to_excel('postcode_key_status.xlsx',sheet_name='postcode_key_status', index=False)
