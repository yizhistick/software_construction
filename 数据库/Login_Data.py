import PySimpleGUI as sg
from 数据库.Base_Data import ConnData


# 判断是否存在对应用户
def IfExist(account=str):
    c, conn = ConnData()
    cusor = conn.execute("SELECT account, Password from Users where account=?",(account,))
    if len(list(cusor)) == 1:
        return True
    else:
        return False


# 注册事务
def register_affair(account=str, password=str, password_ok=str):
    if len(account) == 0 or len(password) == 0:
        sg.popup_error("账号和密码不可以为空")
        return
    if password != password_ok:
        sg.popup_error("两次密码输入不一致！")
        return
    # 连接数据库
    c, conn = ConnData()
    if IfExist(account):
        sg.popup_error("此账号已经有人注册!")
    else:
        c.execute(f"INSERT INTO Users (ACCOUNT,PASSWORD) \
              VALUES (?,?)",(account,password))
        sg.popup("注册成功！")
        conn.commit()
    # 断开连接
    conn.close()


# 登录事务
def Login_affair(cin_account=str, cin_password=str):
    c, conn = ConnData()
    if len(cin_account) == 0 or len(cin_password) == 0:
        sg.popup_error("账号和密码不可以为空")
        return
    if IfExist(cin_account):
        cusor = conn.execute(f"SELECT account, Password  from Users where account='{cin_account}'")
        password = list(cusor)[0][1]
        if password == cin_password:
            return True
        else:
            sg.popup_error("密码输入不正确")
            return False
    else:
        sg.popup_error("不存在此用户")
        return False


if __name__ == '__main__':
    # DataInitialize()
    # Insert()
    # Query()
    pass
