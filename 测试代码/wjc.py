dict1 = {"5+2": "7", "3*1": 4, "5*2": 10}
for key, value in dict1.items():
    print(eval(key))
    if str(eval(key)) != value:
        dict1[key] = False
    else:
        dict1[key] = True

print(dict1)
