from functools import partial

def printer(a,b,c,d):
    print (f"Received: {a} {b} {c} {d}")

printerV1=partial(printer,10,20,30,40)

printerV1()
#Received: 10 20 30 40

printerV1(9,4,5)
#error

printerV2=partial(printer,a='a value',d='d value')
printerV2(15,20)
#TypeError: printer() got multiple values for argument 'a'

printerV2(b=15,c=20)
#Received: a value 15 20 d value
