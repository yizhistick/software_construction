import PySimpleGUI as sg


import _thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))


def prograss():
    for i in range(1000):
        sg.one_line_progress_meter(
            '做题倒计时',
            i + 1,
            1000,
            '进度条走完就要自动交题啦',
            orientation='h',
            no_button=True
        )
    exit()
# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( prograss())
except:
   print ("Error: 无法启动线程")

while 1:
   pass
