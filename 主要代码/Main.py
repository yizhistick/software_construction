from wjc import *
from zt import *
import Tool.Operation as op

sg.theme('DarkAmber')


def MainPage():
    layout = [[sg.Text('小学生口算题')],
              [sg.Text('选择年级:'), sg.InputCombo([1, 2, 3, 4, 5, 6], default_value=2), sg.Text("选择题目数量:"),
               sg.InputCombo([10, 20, 40, 60, 80, 100], default_value=40)],
              [sg.Text('请选择下面一个操作：')],
              [sg.Button('限时练习', size=20)],
              [sg.Button('易错题练习', size=20)],
              [sg.Button('导入题目', size=20)],
              [sg.Button('导出题目', size=20)],
              [sg.Button('练习', ), sg.Button('退出')]]

    window = sg.Window('windows', layout, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '限时练习':
            exercisePage(op.Operation.Create(values[0], values[1]))
            pass
        elif event == '易错题':
            pass
        elif event == '导入题目':
            ImportPage()
        elif event == '导出题目':
            ExportPage(op.Operation.Create(values[0], values[1]), errors_list=[])
            pass
        elif event == '开始随机生成题目':
            pass
        print('you entered', values)

    window.close()


if __name__ == '__main__':
    LoginPage()
