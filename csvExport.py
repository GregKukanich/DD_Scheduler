import csv
from Calculations import *

class csvExp:
     def fileStart(self):
          # field names
          fields = ['Name', 'GPA', 'Year', 'Num Shifts', 'Days']
          filename = "Brothers.csv"
          with open(filename, 'w') as csvfile:
               # creating a csv writer object
               csvwriter = csv.writer(csvfile)

               # writing the fields
               csvwriter.writerow(fields)

     def fileFill(self,name,gpa,grade):
          filename = "Brothers.csv"
          #####Calling function to calc shifts######
          numShifts = Calc()
          e1 = name
          e2 = gpa
          e3 = grade
          e4 = numShifts.calcShifts(float(gpa))
          e5 = numShifts.calcDays(float(grade))

          rows = [[e1, e2, e3, e4, e5]]
          # writing to csv file
          with open(filename, 'a') as csvfile:
               # creating a csv writer object
               csvwriter = csv.writer(csvfile)
               # writing the data rows
               csvwriter.writerows(rows)
