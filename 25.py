from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import OrderedDict
from collections import Counter

def cleanInput(input):
    input = re.sub('\n+'," ",input)
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +'," ",input)
    input = bytes(input,"utf-8")
    input = input.decode('ascii',"ignore")
    cleanInput=[]
    input = input.split(" ")
    for item in input:
        #删除指定的字符，string.strip，这里用来删除标点符号
        item = item.strip(string.punctuation)
        if len(item)>1 or (item.lower()=='a' or item.lower()=='i'):
            cleanInput.append(item)
    return cleanInput

def ngarms(input,n):
    input = cleanInput(input)
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
    return output

html= urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj= BeautifulSoup(html.read())
content = bsObj.find('div',{'id':'mw-content-text'})
content=content.get_text()

ngramsresult=ngarms(content,2)
#print (Counter(str(i) for i in ngramsresult))   # 以字典形式返回统计结果
#print (Counter(str(i) for i in ngramsresult).items())  # 以列表形式返回统计结果

#
#通过counter()获取了一个带有频率的字典
#
ngramsresult = Counter(str(i) for i in ngramsresult)



# -------------- map方法 --------
#print (Counter(map(str, ngramsresult)))   # 以字典形式返回统计结果
#print (Counter(map(str, ngramsresult)).items()) # 以列表形式返回统计结果
#print(ngramsresult)


#因为对字典排序，由于字典内的元素的位置不是固定的，排序之后还是会发生变化，除非把排过序的字典里面的值复制到其他的类型值进行排序，python里面有一个orderddict可以解决这个问题
ngramsresult = OrderedDict(sorted(ngramsresult.items(),key=lambda t:t[1],reverse=True))
print(ngramsresult)
print("2-grams count is:"+str(len(ngramsresult)))

