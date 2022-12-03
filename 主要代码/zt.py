import PySimpleGUI as sg
from 数据库 import *


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


def time_limitPage(list: list):
    layout = []
    print(list)


def exercisePage(list: list):
    layout = []
