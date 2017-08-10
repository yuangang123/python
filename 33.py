#如果一开始就不想使用cookie
#毕竟比较复杂的网站，cookie总是变，持续掌握cookie的状态，可以节省很多的时间
import requests
session = requests.Session()
params = {'usename':'Ryan','password':'password'}
r = session.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
print("Cookie is set to :")
print(r.cookies.get_dict())
print("--------------------------")
print("Going to profile page...")
r = session.get("http://pythonscraping.com/pages/cookies/profile.php",cookies= r.cookies)
print(r.text)                                                                                                                             
