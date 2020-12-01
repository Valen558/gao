def functionGenerator(starsNumber):
    def smallerDude():
        global starsNumber
        starsNumber+=1
        return "Hi!"*starsNumber
    return smallerDude


newWelcomer=functionGenerator(2)
newWelcomer()
newWelcomer()
