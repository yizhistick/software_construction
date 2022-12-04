import PySimpleGUI as sg

import Tool.Current_variate
import Tool.Operation as op
import docx


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


# 导出习题
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
                op.Operation.output(len(exercises_list), exercises_list, values[0],
                                    name=Tool.Current_variate.Current_Account + "易错")
                sg.Popup("导出完成", any_key_closes=True)
            window.close()

        elif event == "导出习题":
            window.close()
            op.Operation.output(len(exercises_list), exercises_list, values[0],
                                name=Tool.Current_variate.Current_Account + "练习")
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
            flag = sg.popup_ok_cancel("确认提交吗")
            print(flag)
            if flag == "OK":
                exercises_dict = {}
                result = list(values.values())
                for i in range(len(result)):
                    exercises_dict[exercises_list[i]] = result[i]
                exercises_dict1 = exercises_dict
                exercises_dict1 = op.Operation.correct(exercises_dict1)
                window.disappear()
                submitPage(exercises_dict1)
                window.close()
            else:
                pass

        if event == '导出':
            window.disappear()
            ExportPage(exercises_list, errors_list=[])
            window.close()


def submitPage(exercises_dict1: dict):
    count = 0
    false = {}
    for K, V in exercises_dict1.items():
        if V:
            count = count + 1
        else:
            false[K] = eval(K)

    x = count / len(list(exercises_dict1.values())) * 100
    x = round(x, 2)
    # print(list(exercises_dict1.values()))
    # print(count)
    # print(false)
    key_list = list(false.keys())
    value_list = list(false.values())
    list_box = []
    for i in range(0, len(key_list) - len(key_list) % 4, 4):
        list_box.append([sg.Text(str(key_list[i]) + " = " + str(value_list[i]), size=(13, 0)),
                         sg.Text(str(key_list[i + 1]) + " = " + str(value_list[i + 1]), size=(13, 0)),
                         sg.Text(str(key_list[i + 2]) + " = " + str(value_list[i + 2]), size=(13, 0)),
                         sg.Text(str(key_list[i + 3]) + " = " + str(value_list[i + 3]), size=(13, 0))])
    if len(key_list) % 4 != 0:
        temp = []
        for i in range((len(key_list) % 4), 0, -1):
            temp.append(sg.Text(str(key_list[-i]) + " = " + str(value_list[-i]), size=(13, 0)))
        list_box.append(temp)

    layout = [[sg.Text("你的正确率为" + str(x) + "%")],
              [sg.Text("    错  题  如  下    ")],
              [sg.Column(list_box, size=(500, 600), scrollable=True,
                         vertical_scroll_only=True, key='test')],
              [sg.Button("返回菜单"), sg.Button("导出")]]

    window = sg.Window('window', layout, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == "返回菜单":
            flag = sg.popup_ok_cancel("确认提交吗")
            if flag == "OK":
                window.close()
            else:
                pass
        elif event == "导出":
            ExportPage(list(exercises_dict1.keys()), errors_list=false.keys())
            window.close()

# if __name__ == '__main__':
#     dic = {'16 -2 ': True, '10 -1 ': True, '18 -13': False, '14 +9 ': True, '18 +15': True, '19 +6 ': False,
#            '6  +6 ': False, '8  -4 ': False, '20 +3 ': False, '14 -5 ': False, '16 -13': False, '18 -6 ': False,
#            '17 +11': False, '5  -1 ': False, '7  +1 ': False, '11 +1 ': False, '16 +15': False, '13 +6 ': False,
#            '13 +11': False, '18 +6 ': False, '20 -3 ': False, '20 +13': False, '17 +1 ': False, '17 -11': False,
#            '6  -3 ': False, '5  -2 ': False, '13 -2 ': False, '19 +12': False, '20 -7 ': False, '19 -17': False,
#            '16 -5 ': False, '11 -6 ': False, '13 -6 ': False, '4  +3 ': False, '12 +6 ': False, '15 -10': False,
#            '8  +3 ': False}
#     submitPage(dic)
