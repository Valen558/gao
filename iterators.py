class wordGiver:
    pointer=-1
    allWords=['tea','table','go','speak','swim','jump','Earth','fly','plane','study','girl','boy','student']
    def __iter__(self):
        return self
    def __next__(self):
        self.pointer+=1
        if(self.pointer>=len(self.allWords)):
            raise StopIteration()
            return 'Error'
        return self.allWords[self.pointer]
    def restartWordGiver(self):
        self.pointer=-1    
    

obWordGiver=wordGiver()
iteratorWordGiver=iter(obWordGiver)
next(iteratorWordGiver)
