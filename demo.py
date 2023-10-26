"This product uses data from the NVD API but is not endorsed or certified by the NVD."

import urllib.request
import json
import pprint

# api_key = '23469821-d382-4689-9cf5-9b4c0cba76f4'
url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode()
    print(response_text)
    j = json.loads(response_text) # j is a dictionary
    # print(j) 

# for i in j['sources']:
#     print(i['name'])