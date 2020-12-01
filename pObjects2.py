class baseAnimal:
    name="Basic Name"
    weight=1000
    def tellName(self):
        print("My Name is "+self.name)
    def __init__(self,name="noName"):
        self.name=name
        print(f"Creating new animal named {name}")
    def tellMore(self):
        print("My name is "+self.name)
        print("My weight is "+str(self.weight))

    def __del__(self):
        print ("This is garbage collection")

ob1=baseAnimal('Egor')
ob1.tellName()
ob1.tellMore()
