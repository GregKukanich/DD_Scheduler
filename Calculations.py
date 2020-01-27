class Calc:
     def calcShifts(self, num):
          if num >= 3.0 and num <= 4.0:
               return 4

          elif num < 3.0 and num >= 2.5:
               return 5

          elif num < 2.5:
               return 6
          else:
               return "ERROR"

     def calcGrade(self,stringGrade):
          if stringGrade == 'Freshman':
               return 1
          elif stringGrade == 'Sophomore':
               return 2
          elif stringGrade == 'Junior':
               return 3
          elif stringGrade == 'Senior':
               return 4
          elif stringGrade == '5th Year':
               return 5
          elif stringGrade == 'Old':
               return 6

     def calcDays(self, num):
          if num >= 4 and num <= 6:
               return "Thrs"
          elif num == 3:
               return "Thrs or Fri"
          elif num == 2:
               return 'Fri or Sat'
          elif num == 1:
               return 'Fri or Sat'
          else:
               return "ERROR"

     #def calcSched(self):
          #