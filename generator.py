#generator that uses yield

def wordGenerator():
    n=-1
    allWords=['tea','table','go','speak','swim','jump','Earth','fly','plane','study','girl','boy','student']
    
    while(True):
        n+=1
        if(n<len(allWords)):
            yield allWords[n]
        else:
            raise StopIteration()

wordGeneratorInstance=wordGenerator()
next(wordGeneratorInstance)
next(wordGeneratorInstance)
