import requests
import json
import pandas as pd

url = "https://api.propertydata.co.uk/council-tax?key=XSOVV5OFQ5&postcode=w149jh"
data = requests.get(url)
if data.status_code != 200:
    print(data.content)

json_data = data.json()
# result = [json_data]

postcode = {"postcode": json_data['postcode']}
postcode_type = {"postcode_type": json_data['postcode_type']}
council = {"council": json_data['council']}
council_rating = {"council_rating": json_data['council_rating']}
year = {"year": json_data['year']}
annual_change = {"annual_change": json_data['annual_change']}
council_tax = json_data['council_tax']
note = {"note": json_data['note']}
properties = json_data['properties']

result = {**postcode, **postcode_type,
          **council,
          **council_rating,
          **year,
          **annual_change,
          **council_tax,
          **note}

df = pd.DataFrame([result])
df2 = pd.DataFrame(properties)
# df['address'] = pd.Series(address_arr)
# df['band'] = pd.Series(band_arr)
concate_dfs = pd.concat([df, df2], ignore_index=False, axis=1)
concate_dfs.to_excel('council_tax.xlsx',sheet_name='council_tax', index=False)

# print(df)

# print(json_data)
