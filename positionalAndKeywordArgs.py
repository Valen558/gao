def someFunc(a,b,c,*,salary,name):
     print(f"Your salary is {salary}")
     print(f"Your name is {name}")
     print(f"a,b,c={a,b,c}")

someFunc(1,2,3,salary=100,name='Tom')
#TypeError: someFunc() takes 3 positional arguments but 4 positional arguments (and 1 #keyword-only argument) were given

someFunc(1,2,3,salary=100,name='Tom')
#ok



#unlimited arg number

def argsUnlimited(*args):
    print(str(args[0])+' '+str(args[1])+' '+str(args[2]))


#format string

"My name is {}, my age is {}".format('Valentin',35)


def newSuperFunc(*args,**kargs):
    print(*args)
    print(*kargs)
    print("{}".format(args))
    print("{}".format(kargs))
