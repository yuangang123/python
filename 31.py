import requests
files = {'uploadFile':open('./logo2017-07-21 10:02:44.jpg','rb')}
r = requests.post("http://pythonscraping.com/pages/files/processing2.php",files=files)
print(r.text)
