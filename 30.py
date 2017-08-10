import requests

params ={'firstname':'yuan','lastname':'gang'}
r = requests.post("http://pythonscraping.com/pages/files/processing.php",data=params)
print(r.text)
