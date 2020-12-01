class myIteratorClass:
    n=1
    def __iter__(self):
        return self
    def __next__(self):
        self.n+=1
        print(str(self.n))
        return self.n 

iterObj=myIteratorClass()
iterator=iter(iterObj)
next(iterObj)
next(iterObj)
next(iterObj)