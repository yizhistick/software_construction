import random


class Operation:
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
        elif grade == 5:
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
                                                                                                                ' ')
                else:
                    if o1 == '-':
                        if first < second:
                            first, second = second, first
                    r = '(' + str(first).ljust(2, ' ') + o1 + str(second).ljust(2, ' ') + ')' + o2 + str(third).ljust(2,
                                                                                                                      ' ')
            Exercises.append(r)
        return Exercises

    def Correct(self,ercises_dict:dict):
        return list