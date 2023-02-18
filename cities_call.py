import http.client

conn = http.client.HTTPConnection("localhost:5000")
conn.request("GET", "/")
response = conn.getresponse()
if response.status == 200:
    print(response.read().decode())
    # res_data = response.read().decode()
    # res_json = json.load(res_data)

else:
    print("Request failed with status code", response.status)

