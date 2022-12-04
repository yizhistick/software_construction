# from random import randint
# import PySimpleGUI as sg
#
# # cols = 3
# # rows = randint(5, 20)
# # rows_show = 10
# # col_width = 15
# #
# # all_listbox = [[sg.Text('col Row 1')],
# #                [sg.Text('col Row 2'), sg.Input()],
# #                [sg.Text('col Row 3'), sg.Input()],
# #                [sg.Text('col Row 4'), sg.Input()],
# #                [sg.Text('col Row 5'), sg.Input()],
# #                [sg.Text('col Row 6'), sg.Input()],
# #                [sg.Text('col Row 7'), sg.Input()]]
# #
# # layout = [
# #     [sg.Text('Product'.center(col_width), pad=(0, 0)),
# #      sg.Text('Unit Price'.center(col_width), pad=(0, 0))],
# #     [sg.Column(all_listbox, scrollable=True, vertical_scroll_only=True, size=(500, 500))],
# #     [sg.Button('Update'), sg.Text(f"Total rows = {rows}", key='Rows')],
# # ]
# # window = sg.Window("Title", layout, finalize=True)
# # while True:
# #     event, values = window.read()
# #     if event == sg.WINDOW_CLOSED:
# #         break
# #
# # window.close()
# import docx
#
# file = docx.Document(r"D:\lx\py\123\software_construction\小学生口算题.docx")
# exercises_list = []
# for table in file.tables:
#     for row in table.rows:
#         for cell in row.cells:
#             exercises_list.append(cell.text)
#
# list_box = [
#     [sg.Text(exercises_list[i]), sg.Input(size=(10, 200)), sg.Text(exercises_list[i + 1]), sg.Input(size=(10, 200))
#      ] for i in range(0, len(exercises_list), 2)]
#
# layout = [[sg.Column(list_box, size=(400, 600), scrollable=True,
#                      vertical_scroll_only=True, key='test')],
#           [sg.Button("提交")]]
# print(list)
# window = sg.Window('window', layout, element_justification="center")
# while True:
#     event, values = window.read()
# print(values)


import PySimpleGUI as sg
import time

# # ----------------  Create Form  ----------------
# sg.ChangeLookAndFeel('Black')
# sg.SetOptions(element_padding=(0, 0))
#
# layout = [[sg.Text('')],
#           [sg.Text(size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
#           [sg.Button('Pause', key='button', button_color=('white', '#001480')),
#            sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
#            sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]
#
# window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True,
#                    grab_anywhere=True)
#
# # ----------------  main loop  ----------------
# current_time = 0
# paused = False
# start_time = int(round(time.time() * 100))
# while (True):
#     # --------- Read and update window --------
#     event, values = window.read(timeout=10)
#     current_time = int(round(time.time() * 100)) - start_time
#     # --------- Display timer in window --------
#     window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
#                                                         (current_time // 100) % 60,
#                                                         current_time % 100))
