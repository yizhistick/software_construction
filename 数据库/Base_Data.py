# 连接数据库封装
import sqlite3


def ConnData():
    conn = sqlite3.connect('../数据库/Exercise_db')
    print("数据库打开成功")
    c = conn.cursor()
    return c, conn


def DataInitialize():
    # 连接数据库
    c, conn = ConnData()
    # c.execute('''CREATE TABLE Users
    #        (ACCOUNT CHAR(20) PRIMARY KEY     NOT NULL,
    #        PASSWORD           CHAR(20)    NOT NULL,);''')
    # print("数据表Users创建成功")
    c.execute('''CREATE TABLE Mistaken_Exercise
           (PROBLEM CHAR(20) PRIMARY KEY     NOT NULL,
           ANSWER           CHAR(20)    NOT NULL,
           ACCOUNT          CHAR(20)    NOT NULL,
           FOREIGN KEY(ACCOUNT) references Users(ACCOUNT));''')
    print("数据表Mistaken_Exercise创建成功")
    conn.commit()
    conn.close()


# 查询所有用户表的数据
def Query():
    # 连接数据库
    c, conn = ConnData()
    cursor = conn.execute("SELECT account, Password  from Users")
    for row in cursor:
        print("account=", row[0])
        print("password=", row[1], "\n")

    print("数据操作成功")
    conn.close()


# 插入样例数据
def Insert():
    # 连接数据库
    c, conn = ConnData()

    c.execute("INSERT INTO Users (ACCOUNT,PASSWORD) \
          VALUES (2360784351,123456)")

    c.execute("INSERT INTO Users (ACCOUNT,PASSWORD) \
          VALUES (2669107795,345612)")
    c.execute("INSERT INTO Users (ACCOUNT,PASSWORD) \
          VALUES (2123456789,345612)")
    c.execute("INSERT INTO Users (ACCOUNT,PASSWORD) \
          VALUES (3567891234,456123)")

    conn.commit()
    print("数据插入成功")
    conn.close()


if __name__ == '__main__':
    DataInitialize()
