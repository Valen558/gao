#super word attempt

class baseRoom:
    def getVersion(self):
        print("baseRoom")

class anotherRoom(baseRoom):
    def getVersion(self):
        print("anotherRoom")
    def checkThingsOut(self):
        super().getVersion()

class moreTopRoom(anotherRoom):
    def getVersion(self):
        print("anotherRoom")
    def checkThingsOut(self):
        super().getVersion()

obAR=moreTopRoom()
obAR.checkThingsOut()
