def DataInitialize():
    # !/usr/bin/python/数据库/

    import sqlite3

    conn = sqlite3.connect('test.db')
    print("数据库打开成功")
    c = conn.cursor()
    c.execute('''CREATE TABLE Users
           (ACCOUNT CHAR(20) PRIMARY KEY     NOT NULL,
           PASSWORD           CHAR(20)    NOT NULL);''')
    print("数据表创建成功")
    conn.commit()
    conn.close()


def Insert():
    # !/usr/bin/python/数据库/

    import sqlite3

    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("数据库打开成功")

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


def register_affair():
    pass

def Login_affair():
    pass

if __name__ == '__main__':
    # DataInitialize()
    Insert()
