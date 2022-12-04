from Main import *
from 数据库.Login_Data import Login_affair,register_affair
import Tool.Current_variate as Share

def LoginPage():
    layout = [[sg.Text('小学生口算题')],
              [sg.Text('账号:'), sg.InputText()],
              [sg.Text("密码:"), sg.InputText(password_char='*')],
              [sg.Button('登录')],
              [sg.Button('注册')],
              ]
    window = sg.Window('登录与注册', layout, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            exit()
        elif event == '登录':
            account = values[0]
            password = values[1]
            if Login_affair(account, password):
                Share.Current_Account = account
                window.close()
                MainPage()
                break

        elif event == '注册':
            registerPage()
        print('you entered', values[0])


def registerPage():
    # !/usr/bin/python/数据库/
    left_lay = [[sg.Text('账号:')],
                [sg.Text("密码:")],
                [sg.Text("确认密码:")], ]
    right_layout = [[sg.InputText()],
                    [sg.InputText(password_char='*')],
                    [sg.InputText(password_char='*')], ]
    layout = [[sg.Text('小学生口算题')],
              [sg.Column(left_lay), sg.Column(right_layout)],
              [sg.Button('注册')]
              ]
    window = sg.Window('windows', layout, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        elif event == "注册":
            account = values[0]
            password = values[1]
            password_ok = values[2]
            print(account, password, password_ok)
            register_affair(account, password, password_ok)


def mistakesPage():
    layout = []




