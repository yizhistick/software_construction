import threading
import PySimpleGUI as sg

sg.theme('DarkAmber')


def prograss(time):
    layout = [[sg.Button("提交")],
               [sg.Text("做题倒计时")],
               [sg.ProgressBar(max_value=1000, orientation='h', size=(50, 20), key='prograssbar')],
               [sg.Cancel()]]
    window = sg.Window("prograss", layout)
    for i in range(1000):
        event, values = window.read(timeout=time)
        if event == 'Cancel' or event == sg.WIN_CLOSED or event == "提交":
            break
        window['prograssbar'].UpdateBar(i + 1)
    sg.popup("已经自动提交")
    window.close()


if __name__ == '__main__':
    prograss(10)
