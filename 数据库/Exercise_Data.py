from 数据库.Base_Data import *


def IfExist(account=str, problem=str):
    query_sql = f"SELECT * from Mistaken_Exercise where Account='{account}' and Problem='{problem}'"
    c, conn = ConnData()
    cusor = conn.execute(query_sql)
    length = len(list(cusor))
    conn.close()
    if length == 1:
        return True
    else:
        return False


def Deposit(problem: str, answer: str, account: str):
    # 判断是否已经存在,存在的话就不存入
    if IfExist(account, problem):
        pass
    else:
        c, conn = ConnData()
        insert_sql = "INSERT INTO Mistaken_Exercise (Problem,Answer,ACCOUNT) \
              VALUES (?,?,?)"
        c.execute(insert_sql, (problem, answer, account))
        conn.commit()
        print("数据插入成功")
        conn.close()


def GetAllWrong(account=str):
    question_list = []
    get_sql = "SELECT PROBLEM from Mistaken_Exercise where Account=?"
    c, conn = ConnData()
    cursor = conn.execute(get_sql, account)
    for row in cursor:
        question_list.append(row[0])
    conn.close()
    return question_list


if __name__ == '__main__':
    # Deposit("3*2","6","2360784351")
    # a = GetAllWrong("2360784351")
    # print(a)
    pass
