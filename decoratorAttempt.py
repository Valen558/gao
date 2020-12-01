#decorators P3 attempt

'''this is an attempt to make 
my own decorator in Python3
''' 

def controlFunction(controlledFunction):
    def returnFunction(a):
        print("I am return function "+a)
        controlledFunction(a)
        return 10
    def returnFunction2(a):
        print("I am return function 2"+a)
        controlledFunction(a)
        return 10
    return returnFunction2    


@controlFunction
def welcomerFunction(name):
    print (f"Who are you {name}?!?")


welcomerFunction('Tom')
