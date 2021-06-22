import json
import pandas
import pandas as pd
import requests

url = "http://reddit.com/.json"

header = {'Accept': '*/*'}
result = requests.get(url=url, headers=header)
print(result.status_code)

json_data = json.loads(result.content)

r = json_data['data']['children']
data_list = []
for data in r:
    title = data['data']['title']
    score = data['data']['score']

    temp_dict = {
        'title': title,
        'score': score
    }

    data_list.append(temp_dict)

df = pd.DataFrame(data_list)
final_data = df.groupby('score', as_index=True).aggregate('max')
d = final_data.sort_values('score', ascending=False).reset_index(drop=True)
f_data = d.head(5)

print(f_data.to_json('data.json', orient='index'))
