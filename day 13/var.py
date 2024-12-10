# args - reads multiple date,  store the tuple, use * to define args
# def sum(*args):
#    b= 0
#    for i in args:
#       b +=i
#    print(b)

# sum(5,10, 50, 8, 50,90,8)

# kwargs (keyword argments) use ** to define kwargs
# def person(**a):
#    for a,b in a.items():
#       print(a, b)
#    # print(kwargs)

# person(name = "dia",age = "18",address="ktm", number = "9874563210")

# combination
def person(*args,**kwargs):
   print(args)
   print(kwargs)

person("ram","18","ktm","ram",age = 20,address = "ktm")