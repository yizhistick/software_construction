import PySimpleGUI as sg
import threading
from 草稿2 import Operation
sg.theme('DarkAmber')


def MainPage():
    layout = [[sg.Text('小学生口算题')],
              [sg.Text('选择年级:'), sg.InputCombo([1, 2, 3, 4, 5, 6]), sg.Text("选择题目数量:"),
               sg.InputCombo([10, 20, 40, 60, 80, 100])],
              [sg.Text('请选择下面一个操作：')],
              [sg.Button('限时练习')],
              [sg.Button('易错题练习')],
              [sg.Button('导入题目')],
              [sg.Button('导出题目')],
              [sg.Button('ok', ), sg.Button('Cancel')]]

    window = sg.Window('windows', layout,element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == '导入题目':
            ImportPage()
        print('you entered', values)

    window.close()


def time_limitPage(list: list):
    layout = []
    print(list)


def exercisePage(list: list):
    layout = []


def mistakesPage():
    layout = []


def ImportPage():
    layout = [[sg.Input(), sg.FileBrowse("选择文件")],
              [sg.Button("开始导入")]]
    window = sg.Window('window', layout)
    event, values = window.read()
    if event == "开始导入":
        window.close()
        time_limitPage([i for i in range(10)])


def ExportPage():
    layout = [[sg.Input(), sg.FileBrowse("选择文件夹")],
              [sg.Button("开始导出")]]
    window = sg.Window('window', layout)
    event, values = window.read()
    if event == "开始导出":
        window.close()
        time_limitPage([i for i in range(10)])


def LoginPage():
    layout = [[sg.Text('小学生口算题')],
              [sg.Text('账号:'), sg.InputText()],
              [sg.Text("密码:"), sg.InputText(password_char='*')],
              [sg.Button('登录')],
              [sg.Button('注册')],
              ]
    window = sg.Window('windows', layout,element_justification="center")

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()
    if event == '登录':
        window.close()
        MainPage()
    print('you entered', values[0])


if __name__ == '__main__':
    LoginPage()
    Operation.create()