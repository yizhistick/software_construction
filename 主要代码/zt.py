import PySimpleGUI as sg
from docx import Document
import Tool.Operation as op
import docx
from 数据库 import *


# 导入习题
def ImportPage():
    layout = [[sg.Input(), sg.FileBrowse("选择文件", file_types=(("word File", "*.docx"),))],
              [sg.Button("开始导入")]]
    window = sg.Window('window', layout)
    event, values = window.read()
    if event == "开始导入":
        window.close()
        print(values[0])
        file = docx.Document(values[0])
        exercises_list = []
        for table in file.tables:
            for row in table.rows:
                for cell in row.cells:
                    exercises_list.append(cell.text)
        exercisePage(exercises_list)


def ExportPage(exercises_list: list, errors_list: list = []):
    layout = [[sg.Input(), sg.FolderBrowse("选择文件夹")],
              [sg.Button("导出习题"), sg.Button("导出错题")]]
    window = sg.Window('window', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == "导出错题":
            if len(errors_list) == 0:
                print("无错题")
                # sg.Popup("当前无错题", title='test', custom_text=('确定', '取消'),font=("黑体",20))
                sg.Popup("当前无错题", any_key_closes=True)
                pass
            else:
                op.Operation.output(len(exercises_list), exercises_list, values[0])
                sg.Popup("导出完成", any_key_closes=True)
                break
            window.close()

        elif event == "导出习题":
            window.close()
            op.Operation.output(len(exercises_list), exercises_list, values[0])
            sg.Popup("导出完成", any_key_closes=True)
            print(exercises_list)


def time_limitPage(list: list):
    layout = []
    print(list)


# 练习习题
def exercisePage(exercises_list: list):
    list_box = [
        [sg.Text(exercises_list[i], size=(13, 0)), sg.Input(size=(10, 200)),
         sg.Text(exercises_list[i + 1], size=(13, 0)), sg.Input(size=(10, 200))
         ] for i in range(0, len(exercises_list), 2)]

    layout = [[sg.Column(list_box, size=(500, 600), scrollable=True,
                         vertical_scroll_only=True, key='test')],
              [sg.Button("提交"), sg.Button("导出")]]
    window = sg.Window('window', layout, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        if event == '提交':
            exercises_dict = {}
            result = list(values.values())
            for i in range(len(result)):
                exercises_dict[exercises_list[i]] = result[i]
            exercises_dict1 = exercises_dict
            exercises_dict1 = op.Operation.correct(exercises_dict1)
            print(exercises_dict1)
            print(exercises_dict)

        if event == '导出':
            window.close()
            ExportPage(exercises_list, errors_list=[])
