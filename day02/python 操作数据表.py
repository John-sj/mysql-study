import pymysql
import time


def show_databases(cursor):
    cursor.execute("show databases")
    res = cursor.fetchall()
    print("数据库如下>>")
    for item in res:
        print(item[0])


def open_db(cursor, db_name):
    cursor.execute("use {}".format(db_name))
    cursor.execute("show tables")
    res = cursor.fetchall()
    if not res:
        print("无内容!!!")
        return
    print("当前数据库：{} 所包含的表如下>>".format(db_name))
    for item in res:
        print(item[0])


def create_tb(conn, cursor, tb_name):
    sql = """
        create table {} (id int, name varchar(16)) default charset = utf8
    """.format(tb_name)
    cursor.execute(sql)
    conn.commit()


def del_tb():
    pass


def clear_tb():
    pass


def run():
    try:
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", charset="utf8")
        cursor = conn.cursor()
        show_databases(cursor)
        choice = input('请选择：1.删除数据库 2.打开数据库>>')

        db_name = input("请输入要查看的数据库名称>>")
        open_db(cursor, db_name)
        cursor.close()
        conn.close()

    except Exception as error:
        # for item in error:
        #     print(item)
        print('数据库连接失败!!! error:{}'.format(error))


if __name__ == '__main__':
    run()
