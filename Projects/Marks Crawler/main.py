import requests
url = 'http://moed.gov.sy/sharie/result.php'
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
payload = "city=1&stdnum=1&Submit="
r = requests.post(url, data=payload, headers=headers)
print(r)
