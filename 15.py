#使用Python的csv库可以非常简单的修改CSV文件，现在从0开始创建一个CSV文件
import csv
csvFile=open("test.csv",'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()
