# import os
# from datetime import time
# from random import random
#
# import PySimpleGUI as sg
# from docx import Document
# import docx

# sg.theme('DarkAmber')
#
#
# def MainPage():
#     layout = [[sg.Text('小学生口算题')],
#               [sg.Text('选择年级:'), sg.InputCombo([1, 2, 3, 4, 5, 6]), sg.Text("选择题目数量:"),
#                sg.InputCombo([10, 20, 40, 60, 80, 100])],
#               [sg.Text('请选择下面一个操作：')],
#               [sg.Button('限时练习')],
#               [sg.Button('易错题练习')],
#               [sg.Button('导入题目')],
#               [sg.Button('导出题目')],
#               [sg.Button('ok', ), sg.Button('Cancel')]]
#
#     window = sg.Window('windows', layout,element_justification="center")
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Cancel':
#             break
#         elif event == '导入题目':
#             window.close()
#             ImportPage()
#         elif event == '导出题目':
#             ExportPage()
#         print('you entered', values)
#
#     window.close()
#
#
# def time_limitPage(exercises_list: list):
#     layout = []
#
#
# # 练习习题
# def exercisePage(exercises_list: list):
#     list_box = [
#         [sg.Text(exercises_list[i], size=(13, 0)), sg.Input(size=(10, 200)),
#          sg.Text(exercises_list[i + 1], size=(13, 0)), sg.Input(size=(10, 200))
#          ] for i in range(0, len(exercises_list), 2)]
#
#     layout = [[sg.Column(list_box, size=(500, 600), scrollable=True,
#                          vertical_scroll_only=True, key='test')],
#               [sg.Button("提交")]]
#     print(list)
#     window = sg.Window('window', layout, element_justification="center")
#     while True:
#         event, values = window.read()
#         if event == sg.WIN_CLOSED or event == 'Cancel':
#             break
#         if event == '提交':
#             print()
#
#     print(values)
#
#
# def mistakesPage():
#     layout = []
#
#
# # 导入习题
# def ImportPage():
#     layout = [[sg.Input(), sg.FileBrowse("选择文件", file_types=(("word File", "*.docx"),))],
#               [sg.Button("开始导入")]]
#     window = sg.Window('window', layout)
#     event, values = window.read()
#     if event == "开始导入":
#         window.close()
#         print(values[0])
#         file = docx.Document(values[0])
#         exercises_list = []
#         for table in file.tables:
#             for row in table.rows:
#                 for cell in row.cells:
#                     exercises_list.append(cell.text)
#         exercisePage(exercises_list)
#
#
# def ExportPage():
#     layout = [[sg.Input(), sg.FolderBrowse("选择文件夹")],
#               [sg.Button("开始导出")]]
#     window = sg.Window('window', layout)
#     event, values = window.read()
#
#
# def LoginPage():
#     layout = [[sg.Text('小学生口算题')],
#               [sg.Text('账号:'), sg.InputText()],
#               [sg.Text("密码:"), sg.InputText(password_char='*')],
#               [sg.Button('登录')],
#               [sg.Button('注册')],
#               ]
#     window = sg.Window('windows', layout,element_justification="center")
#
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         window.close()
#     if event == '登录':
#         window.close()
#         MainPage()
#     print('you entered', values[0])
#
#


#


# import time
# import PySimpleGUI as sg
# import threading
#
#
# # 定义计时器线程函数
# def timer_thread(time_seconds, window):
#     # 初始化计时器
#     timer = time_seconds
#
#     # 不断更新计时器显示
#     while timer > 0:
#         window["timer"].update(timer)
#         timer -= 1
#         time.sleep(1)
#
#     # 计时完毕，显示结束信息
#     window["timer"].update("计时完毕！")
#
#
# # 创建 PySimpleGUI 窗口
# layout = [[sg.Text("计时器：")],
#           [sg.Input("", key="time"), sg.Button("开始计时")],
#           [sg.Text("", size=(10, 1), key="timer")]]
# window = sg.Window("计时器", layout)
#
# # 循环等待用户事件
# while True:
#     event, values = window.read()
#     # 如果用户点击了按钮
#     if event == "开始计时":
#         # 获取计时时长
#         time_seconds = int(values["time"])
#         # 创建并启动计时器线程
#         t = threading.Thread(target=timer_thread, args=(time_seconds, window))
#         t.start()
#     # 如果用户关闭窗口，退出循环
#     if event == sg.WIN_CLOSED:
#         break
#
# # 关闭窗口
# window.close()
import time

import PySimpleGUI as sg
import threading


#
#
# #定义计时函数
# def countdown(timer,window):
#     for i in range(timer):
#         # 使用进度条显示计时进度
#         window.write_event_value('-THREAD-', (
#             threading.current_thread().name, i))
#         sg.one_line_progress_meter('计时器', i, timer)
#         # timer -= 1
#         time.sleep(1)
#
# def prograss(window):
#     window.read()
#     for i in range(10000):
#         event1, values1 = window.read(timeout=10)
#         if event1 == 'Cancel':
#             break
#         window['prograssbar'].UpdateBar(i + 1)
#     window.close()
#     # exitflag = False
#     pass
#
#
# # 定义窗口布局
# layout = [
#     [sg.ProgressBar(max_value=10000, orientation='h', size=(50, 20), key='prograssbar')],
#     [sg.Button('开始计时'), sg.Button('停止计时')]
# ]
#
#
# # 创建窗口
# window = sg.Window('多线程计时器', layout)
#
# # 主线程循环
# while True:
#     event, values = window.read()
#     # 如果点击了开始计时按钮
#     if event == '开始计时':
#         # 获取用户输入的计时时长
#
#         # 创建一个新的线程来执行计时任务
#
#         t = threading.Thread(target=prograss, args=(window,))
#         # 开始执行线程
#
#         t.start()
#
#     # 如果点击了停止计时按钮
#     if event == '停止计时':
#         # 终止线程
#         t.stop()
#     # 如果窗口关闭
#     if event is None:
#         # 退出循环
#         break
#
# window.close()

def prograss1(time):
    layout = [[sg.Button("提交")],
              [sg.Text("做题倒计时")],
              [sg.ProgressBar(max_value=time, orientation='h', size=(50, 20), key='prograssbar')],
              [sg.Input()],
              [sg.Cancel()]]
    window = sg.Window("prograss", layout)
    for i in range(time):
        event, values = window.read(timeout=10)
        if event == 'Cancel' or event == sg.WIN_CLOSED or event == "提交":
            break
        window['prograssbar'].UpdateBar(i + 1)
    sg.popup("已经自动提交")
    window.close()


if __name__ == '__main__':
    prograss1(1000)
