import threading
import time
import PySimpleGUI as sg

THREAD_EVENT = '-THREAD-'

cp = sg.cprint


def the_thread(window):
    i = 0
    while True:
        time.sleep(1)
        window.write_event_value('-THREAD-', (
            threading.current_thread().name, i))  # Data sent is a tuple of thread name and counter
        cp('This is cheating from the thread', c='white on green')
        i += 1


def main():
    layout = [[sg.Text('Output Area - cprint\'s route to here', font='Any 15')],
              [sg.Multiline(size=(65, 20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True,
                            reroute_cprint=True)],
              [sg.T('Input so you can see data in your dictionary')],
              [sg.Input(key='-IN-', size=(30, 1))],
              [sg.B('Start A Thread'), sg.B('Dummy'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:  # Event Loop
        event, values = window.read()
        cp(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event.startswith('Start'):
            threading.Thread(target=the_thread, args=(window,), daemon=True).start()
        if event == THREAD_EVENT:
            cp(f'Data from the thread ', colors='white on purple', end='')
            cp(f'{values[THREAD_EVENT]}', colors='white on red')
    window.close()


if __name__ == '__main__':
    main()
