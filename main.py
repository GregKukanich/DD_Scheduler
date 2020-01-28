from Calculations import *
from calExport import *
from guiTest import *


def main():
     # *****DIALOG STARTUP*****#
     import sys
     app = QtWidgets.QApplication(sys.argv)
     Dialog = QtWidgets.QDialog()
     brothers1 = brothers()
     ui = Ui_Dialog()
     ui.setupUi(Dialog)
     Dialog.show()
     csv = csvExp()
     csv.fileStart()  # Start .csv file for members entered into gui dialog

     calendar = cal()
     calc = Calc()
     calc.calcSched()
     sys.exit(app.exec_())


main()
