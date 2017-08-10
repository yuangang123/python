import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response= urlopen("http://freegeoip.net/json").read().decode("utf-8")
    responseJson = json.loads(response)
    return responseJson.get("country_code")+responseJson.get("city")
print(getCountry("113.222.130.37"))

