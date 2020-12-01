class baseBuilding:
    def getActualCost(self):
        raise NotImplementedError("this method is not implemented")
    def getCost(self):
        return 10000000
    def tookTimeToConstruct(self):
        return "0.5 year"

class threeStoreBuilding(baseBuilding):
    def destroyBuilding(self):
        print("The building destroyed!")

class fourStoreBuilding(baseBuilding):
    baseCost1="100 $"
    def getHeight(self):
        print("5.2 meters")


theBuild4=fourStoreBuilding()

try:
    theBuild4.getActualCost()
    print("continue main program line")
except:
    print (f"Error happened {'msg'}")


print("continue outside of except block")



