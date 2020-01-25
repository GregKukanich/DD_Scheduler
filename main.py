from guiTest import *
from csvExport import *

def main():
       #*****DIALOG STARTUP*****#
       import sys
       app = QtWidgets.QApplication(sys.argv)
       Dialog = QtWidgets.QDialog()
       ui = Ui_Dialog()
       ui.setupUi(Dialog)
       Dialog.show()
       sys.exit(app.exec_())

       csv = csvExp()
       csv.fileStart()



main()
