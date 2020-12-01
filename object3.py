class baseLaw:
    lawName="Basic Law"
    lawVersion="1.0.0.2"
    def __init__(self):
        print("Basic Law Initialized")
    def __del__(self):
        print("Basic Law Deleted From Memory")
    def tellSomething(self):
        print("Version "+self.lawVersion)
        print("What do you want to know?")

class baseLaw2(baseLaw):
    newVar="new Version"    
    def __init__(self):
        print("Basic Law2 Initialized")
        super().__init__()

bo=baseLaw2()
bo.tellSomething()

    
