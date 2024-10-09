import requests
import json

url = "http://127.0.0.1:8000/predict"  # Make sure this matches your server address and port

data = {
    "values": [1.0, 2.0, 3.0, 4.0, 5.0, 
               12.0, 11.0, 8.0, 7.0, 7.5,
               5.0, 1.0, 2.0, 2.4],  # random 14 points for demonstration
    "timestamps": [ 
        '2001-01-01', '2001-02-01', '2001-03-01', '2001-04-01',
        '2001-05-01', '2001-06-01', '2001-07-01', '2001-08-01',
        '2001-09-01', '2001-10-01', '2001-11-01', '2001-12-01',
        '2002-01-01', '2002-02-01'
    ],
}

params = {
    "horizon": 14
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json={"data": data, "params": params}, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent=2))
else:
    print(f"Error: {response.status_code}")
    print(response.text)