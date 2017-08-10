from urllib.request import urlopen
from io import StringIO
import csv
data= urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

#for row in csvReader:
    #print(row)
    
#for row in csvReader:
    #print("The ablum \""+row[0]+"\" was releasea in "+str(row[1]))
    
#使用csv.DictReader把第一行处理掉
dictReader = csv.DictReader(dataFile)

print("把字段列表保存在dictReader.fieldnames里面：")
print(dictReader.fieldnames)

#csv.DictReader会把每一行转换为一个字典对象返回
for row in dictReader:
    print(row)
