from wjc import *
from zt import *
import Tool.Operation as op
import Tool.Current_variate as CV
import 数据库.Exercise_Data as ED

sg.theme('DarkAmber')


def MainPage():
    layout = [[sg.Text('小学生口算题')],
              [sg.Text('选择年级:'), sg.InputCombo([1, 2, 3, 4, 5, 6], default_value=2), sg.Text("选择题目数量:"),
               sg.InputCombo([10, 20, 40, 60, 80, 100], default_value=40)],
              [sg.Text('请选择下面一个操作：')],
              [sg.Button('练习', size=20)],
              [sg.Button('限时练习', size=20)],
              [sg.Button('易错题练习', size=20)],
              [sg.Button('导入题目', size=20)],
              [sg.Button('退出',size=20)]]

    window = sg.Window('小学生口算习题', layout, element_justification="center")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '退出':
            break
        elif event == '限时练习':
            window.disappear()
            exercisePage(op.Operation.Create(values[0], values[1]))
            window.reappear()
            pass
        elif event == '易错题练习':
            window.disappear()
            exercisePage(ED.GetAllWrong(CV.Current_Account))
            window.reappear()
            pass
        elif event == '导入题目':
            window.disappear()
            ImportPage()
            window.reappear()
        elif event == '导出题目':
            window.disappear()
            ExportPage(op.Operation.Create(values[0], values[1]), errors_list=[])
            window.reappear()
            pass
        elif event == '练习':
            window.disappear()
            exercisePage(op.Operation.Create(values[0], values[1]))
            window.reappear()
            pass
        print('you entered', values)

    window.close()


if __name__ == '__main__':
    LoginPage()
