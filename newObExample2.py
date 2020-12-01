class temperatureConverter:
    def __init__(self,temp=25):
        self.temp=temp
    
    def convertToFar(self):
        #the formula may be incorrect
        return self.temp*1.38


class emptyClass:
    pass

newTempMeter=temperatureConverter()
