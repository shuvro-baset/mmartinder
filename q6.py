import requests
import json
import pandas as pd

url = "https://api.propertydata.co.uk/valuation-rent?key=XSOVV5OFQ5&postcode=DE217AP&internal_area=656&property_type=flat&construction_date=pre_1914&bedrooms=3&bathrooms=1&finish_quality=below_average&outdoor_space=garden&off_street_parking=0"
data = requests.get(url)
if data.status_code != 200:
    print(data.content)

json_data = json.loads(data.content)
postcode = {"postcode": json_data['postcode']}
postcode_type = {"postcode_type": json_data['postcode_type']}
process_time = {"process_time": json_data['process_time']}

estimate = {"estimate": json_data['result']['estimate']}
unit = {"unit": json_data['result']['unit']}

result1 = {**postcode, **postcode_type,
          **process_time,
          **estimate,
          **unit}

result = [json_data['params']]
df = pd.DataFrame([result1])
df2 = pd.DataFrame(result)

concate_dfs = pd.concat([df, df2], ignore_index=False, axis=1)

concate_dfs.to_excel('rental_valuation.xlsx', index=False)

# print(json_data)
