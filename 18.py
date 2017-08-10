import pymysql
conn = pymysql.connect(host='127.0.0.1',user='root',password='0000',db='mysql')

cur = conn.cursor()
cur.execute("USE scraping")

cur.execute('select * from pages where id= 1 ')
print cur.fetchone()
cur.close()
conn.close()
