import os
import random
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import pyplot as plt
import Tool.Current_variate as CV
from 数据库.Exercise_Data import *
from docx import Document
from docx.shared import Pt


def Create(grade=int, quantity=int):
    global Max, operators  # 题目中数字的最大值，运算符
    Exercises = []
    # 年级判断
    if grade <= 3:
        operators = '+-'
        Max = 20
    elif grade == 4:
        operators = '＋－×÷'
        Max = 100
    elif grade == 5 or grade == 6:
        operators = '＋－×÷('
        Max = 100

    for i in range(quantity):
        first = random.randint(1, Max)
        second = random.randint(1, Max)
        operator = random.choice(operators)  # 符号随机
        if operator != '(':  # 不是五年级
            if operator == '-' or '÷':
                if first < second:
                    first, second = second, first
            r = str(first).ljust(2, ' ') + ' ' + operator + str(second).ljust(2, ' ')

        else:  # 是五年级
            third = random.randint(1, 100)
            while True:
                o1 = random.choice(operators)
                o2 = random.choice(operators)
                if o1 != '(' and o2 != '(':
                    break
            # 考虑括号的口算题
            r2 = random.randint(1, 100)
            if r2 > 50:
                if o2 == '-':
                    if second < third:
                        second, third = third, second
                r = str(first).ljust(2, ' ') + o1 + '(' + str(second).ljust(2, ' ') + o2 + str(third).ljust(2,
                                                                                                            ' ') + ')'
            else:
                if o1 == '-':
                    if first < second:
                        first, second = second, first
                r = '(' + str(first).ljust(2, ' ') + o1 + str(second).ljust(2, ' ') + ')' + o2 + str(third).ljust(2,
                                                                                                                  ' ')
        Exercises.append(r)
    return Exercises


def correct(Exercises: dict):
    for question, user_answer in Exercises.items():
        if str(eval(question)) != user_answer:
            Exercises[question] = False
            Deposit(problem=question, answer=str(eval(question)), account=CV.Current_Account)
        else:
            Exercises[question] = True
    return Exercises


def output(rowsNumbers: int, templist: list, path: str, name: str = ""):
    columnsNumber = 4
    document = Document()
    if rowsNumbers / 4 != int(rowsNumbers / 4):
        rowsNumbers = int(rowsNumbers / 4) + 1
    else:
        rowsNumbers = int(rowsNumbers / 4)
    table = document.add_table(rows=rowsNumbers, cols=columnsNumber)
    table.style.font.name = '微软雅黑'
    table.style.font.size = Pt(10)
    for row in range(rowsNumbers):
        for col in range(columnsNumber):
            if row * 4 + col >= len(templist):
                break
            cell = table.cell(row, col)
            cell.text = templist[row * 4 + col]
            print(row, col)
            print(row * 4 + col)
    document.save(path + '/' + name + '口算题.docx')
    os.startfile(path + "/" + name + "口算题.docx")


# 生成一个fig
def make_figure(true_count, flase_count):
    fig = plt.figure(facecolor='#2C2825')
    plt.pie([true_count, flase_count], autopct='%.2f%%')
    plt.legend(["正确", "错误"], loc="center left", bbox_to_anchor=(0.90, 0, 0.3, 1))
    plt.title(u"正确率")

    # 用来正常显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 用来正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    return fig


# 画在canvas上，包括工具条
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# if __name__ == '__main__':
#     output()
