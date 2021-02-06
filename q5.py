import requests
import json
import pandas as pd

url = "https://api.propertydata.co.uk/prices?key=XSOVV5OFQ5&postcode=DE217AP&bedrooms=3"
data = requests.get(url)
if data.status_code != 200:
    print(data.content)

json_data = data.json()

first_four_data = {"postcode": json_data["postcode"], "postcode_type": json_data['postcode_type'],
                   "url": json_data['url']}

points_analysed = {"points_analysed": json_data['data']['points_analysed']}
radius = {"radius": json_data['data']['radius']}
average = {"average": json_data['data']['average']}

pc_range70 = {"pc_range70": json_data['data']['70pc_range']}
pc_range80 = {"pc_range80": json_data['data']['80pc_range']}
pc_range90 = {"pc_range90": json_data['data']['90pc_range']}
pc_range100 = {"pc_range100": json_data['data']['100pc_range']}
raw_data = json_data['data']['raw_data']
# raw_dict = {}
# for dict_data in raw_data:
#     temp_dict = dic

result = {**first_four_data, **points_analysed, **radius, **average, **pc_range70, **pc_range80, **pc_range90,
          **pc_range100, }

df = pd.DataFrame(result)
df2  = pd.DataFrame(raw_data)
# df2.dropna()

concate_dfs = pd.concat([df,df2], ignore_index=False, axis=1)
concate_dfs.to_excel('property_valuation.xlsx', index=False)

# print(json_data)
