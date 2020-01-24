class Calc:
    def calcShifts(self,num):
        if num >= 3.0:
            return 4

        elif num < 3.0 and num >= 2.5:
            return 5

        elif num < 2.5:
            return 6
        else:
            return 6
