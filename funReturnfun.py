def bigFun(welcomeMessage,counter=0):
    counter+=1
    print (counter)
    return lambda name:welcomeMessage+' '+name

getWorker=bigFun('Hello Mister ')
getWorker('Tom')
