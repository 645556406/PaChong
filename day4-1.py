
#mysql Moudle test
import pymysql
conn = pymysql.connect(host='192.168.1.141',unix_socket='/tmp/mysql.sock',user='root',passwd="wangye,.633733@!Z",db='mysql')
cur = conn.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=1")
print(cur.fetchone())
cur.close()
conn.close()
