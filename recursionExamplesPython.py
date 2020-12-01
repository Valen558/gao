def stringReverse(str):
     if(len(str)==1):
             return str
     return str[len(str)-1]+stringReverse(str[0:len(str)-1])

