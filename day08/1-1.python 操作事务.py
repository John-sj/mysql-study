import pymysql
conn = pymysql.connect(host="localhost", port=3306, user="root", password="john5490", charset="utf8", db="day322")
cursor = conn.cursor()
# 开启事务
conn.begin()

try:
    cursor.execute("update user set amount = 1 where id = 1")
    cursor.execute("update user set amount = 2 where id = 2")
except Exception as e:
    print("回滚")
    conn.rollback()
else:
    # 提交
    print("提交")
    conn.commit()
cursor.close()
conn.close()

