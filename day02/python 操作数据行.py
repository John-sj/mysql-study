import pymysql
# 增
def add_data(conn, cursor,*args):
    conn.commit()
    pass
# 删

def del_data(conn, cursor,*args):
    conn.commit()
    pass

# 改
def modify_data(conn, cursor,*args):
    conn.commit()
    pass

# 查
def find_data(cursor,*args):
    pass

def run():
    try:
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", charset="utf8", db='day37')
        # print(conn)
        cursor = conn.cursor()
        cursor.close()
        conn.close()
    except Exception as error:
        print(error)


if __name__ == '__main__':
    run()

