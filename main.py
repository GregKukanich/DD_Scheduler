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
     csv.fileStart()  # Start .csv file for members entered into gui dialog
     G = brothers("Greg",3.3,"Junior",5)
     calendar = cal()
     calendar.createCal(G.name)#init calendar file
     sys.exit(app.exec_())


main()
