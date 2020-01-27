from csvExport import *
from guiTest import *
from Brothers import *
from calExport import *


def main():
     # *****DIALOG STARTUP*****#
     import sys
     app = QtWidgets.QApplication(sys.argv)
     Dialog = QtWidgets.QDialog()
     ui = Ui_Dialog()
     ui.setupUi(Dialog)
     Dialog.show()
     csv = csvExp()
     brothers1 = brothers()
     csv.fileStart()  # Start .csv file for members entered into gui dialog
     brothers1.intake()
     calendar = cal()


     sys.exit(app.exec_())


main()
