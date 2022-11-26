import random
import os
import tkinter
import tkinter.ttk
from docx.shared import Pt
from docx import Document

columnsNumber = 4


def main(rowsNumbers, grade):
    if grade < 3:
        operators = '+-'
        Max = 20
    elif grade <= 4:
        operators = '＋－×÷'
        Max = 100
    elif grade == 5:
        operators = '＋－×÷('
        Max = 100
    document = Document()
    table = document.add_table(rows=rowsNumbers, cols=columnsNumber)
    table.style.font.name = '微软雅黑'
    table.style.font.size = Pt(10)
    for row in range(rowsNumbers):
        for col in range(columnsNumber):
            first = random.randint(1, Max)
            second = random.randint(1, Max)
            operator = random.choice(operators)
            if operator != '(':  # 不是五年级
                if operator == '-' or '÷':
                    if first < second:
                        first, second = second, first
                r = str(first).ljust(2, ' ') + ' ' + operator + str(second).ljust(2, ' ') + '='

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
                                                                                                                ' ') + ')='
                else:
                    if o1 == '-':
                        if first < second:
                            first, second = second, first
                    r = '(' + str(first).ljust(2, ' ') + o1 + str(second).ljust(2, ' ') + ')' + o2 + str(third).ljust(2,
                                                                                                                      ' ') + '='

            cell = table.cell(row, col)
            cell.text = r

    document.save('小学生口算题.docx')
    os.startfile("小学生口算题.docx")


if __name__ == '__main__':
    app = tkinter.Tk()
    app.title('小学口算题生成器')
    app['width'] = 300
    app['height'] = 150
    lableNumber = tkinter.Label(app, text='Number:', justify=tkinter.RIGHT, width=50)
    lableNumber.place(x=10, y=40, width=50, height=20)
    comboNumber = tkinter.ttk.Combobox(app, values=(100, 200, 300, 400, 500), width=50)
    comboNumber.place(x=70, y=40, width=50, height=20)

    labelGrade = tkinter.Label(app, text='Grade:', justify=tkinter.RIGHT, width=50)
    labelGrade.place(x=130, y=40, width=50, height=20)
    comboGrade = tkinter.ttk.Combobox(app, values=(1, 2, 3, 4, 5,6), width=50)
    comboGrade.place(x=200, y=40, width=50, height=20)


    def generate():
        number = int(comboNumber.get())
        grade = int(comboGrade.get())
        rowsNumbers = int(number / 4)
        main(rowsNumbers, grade)


    buttonGenerate = tkinter.Button(app, text='Go', width=40, command=generate)
    buttonGenerate.place(x=130, y=90, width=40, height=30)

    app.mainloop()