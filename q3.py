import requests
import json
import pandas as pd

url = "https://api.propertydata.co.uk/politics?key=XSOVV5OFQ5&postcode=DE217AP"
data = requests.get(url)
if data.status_code != 200:
    print(data.content)

json_data = data.json()

first_three_data = {"postcode": json_data["postcode"], "postcode_type": json_data['postcode_type'],
                    "url": json_data['url'], }
data_obj = json_data['data']
constituency = {"constituency": data_obj['constituency']}
constituency_code = {"constituency_code": data_obj['constituency_code']}
event_name = {"event_name": data_obj['last_result']['event_name']}
vote_counts = data_obj['last_result']['vote_counts']

result = {**first_three_data, **constituency, **constituency_code, **event_name, **vote_counts, }
df = pd.DataFrame([result])
df.to_excel('politics.xlsx', index=False)
