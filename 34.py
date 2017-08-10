#Http基本介入认证
#在发明cookie之前，处理网站登录最常见的方法就是使用http基本介入，如今在一些安全性比较高的网站上还是能够见到这种认证方式
import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('yuangang','password')
r = requests.post("http://pythonscraping.com/pages/auth/login.php",auth = auth)

print(r.text)
