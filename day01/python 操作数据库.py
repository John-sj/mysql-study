import pymysql
# print(pymysql)
'''
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", charset="utf8")
cursor = conn.cursor()
cursor.execute("show databases")
result = cursor.fetchall()
print(result)

# cursor.execute("create database day01 default charset utf8 collate utf8_general_ci ")
# conn.commit()
cursor.execute("show databases")
result = cursor.fetchall()
print(result)

cursor.execute("drop database day01")
conn.commit()

cursor.execute("show databases")
result = cursor.fetchall()
print(result)  
cursor.close()
conn.close()
'''



def create_db(conn, cursor, db_name):
    print(db_name)
    cursor.execute("create database {} default charset utf8 collate utf8_general_ci".format(db_name))
    conn.commit()


def del_db(conn, cursor, db_name):
    cursor.execute("drop database {}".format(db_name))
    conn.commit()


def create_table():
    pass


def del_tables():
    pass


def show_databases(cursor):
    cursor.execute("show databases")
    result = cursor.fetchall()
    return result


def open_db(cursor, db_name):
    cursor.execute("use {}".format(db_name))
    cursor.execute("show tables")
    result = cursor.fetchall()
    return result

def run():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", charset="utf8")
    cursor = conn.cursor()
    res = show_databases(cursor)
    print(res)
    # create_db(conn, cursor, "day37")
    # res = show_databases(cursor)
    # del_db(conn, cursor, "day37")
    # res = show_databases(cursor, )
    res = open_db(cursor, "day37")
    print(res)


if __name__ == '__main__':
    run()
