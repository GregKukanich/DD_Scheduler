# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from csvExport import *


class Ui_Dialog(object):
     # def reject(self):
     def setupUi(self, Dialog):
          Dialog.setObjectName("Dialog")
          Dialog.setEnabled(True)
          Dialog.resize(586, 268)
          Dialog.setMinimumSize(QtCore.QSize(586, 268))
          Dialog.setMaximumSize(QtCore.QSize(586, 268))
          Dialog.setSizeGripEnabled(False)
          Dialog.setModal(False)
          self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
          self.buttonBox.setGeometry(QtCore.QRect(20, 200, 271, 51))
          self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
          self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Ok)
          self.buttonBox.setCenterButtons(True)
          self.buttonBox.setObjectName("buttonBox")
          self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
          self.verticalLayoutWidget.setGeometry(QtCore.QRect(110, 60, 171, 141))
          self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
          self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
          self.verticalLayout.setContentsMargins(0, 0, 0, 0)
          self.verticalLayout.setObjectName("verticalLayout")
          self.nameInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
          self.nameInput.setObjectName("nameInput")
          self.verticalLayout.addWidget(self.nameInput)
          self.gpaInput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
          self.gpaInput.setObjectName("gpaInput")
          self.verticalLayout.addWidget(self.gpaInput)
          self.gradeInput = QtWidgets.QComboBox(self.verticalLayoutWidget)
          self.gradeInput.setEnabled(True)
          self.gradeInput.setEditable(False)
          self.gradeInput.setObjectName("gradeInput")
          self.gradeInput.addItem("")
          self.gradeInput.addItem("")
          self.gradeInput.addItem("")
          self.gradeInput.addItem("")
          self.gradeInput.addItem("")
          self.gradeInput.addItem("")
          self.verticalLayout.addWidget(self.gradeInput)
          self.label = QtWidgets.QLabel(Dialog)
          self.label.setGeometry(QtCore.QRect(20, 70, 81, 16))
          self.label.setObjectName("label")
          self.label_2 = QtWidgets.QLabel(Dialog)
          self.label_2.setGeometry(QtCore.QRect(20, 120, 81, 16))
          self.label_2.setObjectName("label_2")
          self.label_3 = QtWidgets.QLabel(Dialog)
          self.label_3.setGeometry(QtCore.QRect(20, 160, 81, 16))
          self.label_3.setObjectName("label_3")
          self.label_4 = QtWidgets.QLabel(Dialog)
          self.label_4.setGeometry(QtCore.QRect(320, 70, 261, 181))
          self.label_4.setText("")
          self.label_4.setPixmap(QtGui.QPixmap("444597675.jpg"))
          self.label_4.setObjectName("label_4")
          self.label_5 = QtWidgets.QLabel(Dialog)
          self.label_5.setGeometry(QtCore.QRect(100, 10, 391, 31))
          self.label_5.setObjectName("label_5")
          self.nameInput.setFocus()
          self.buttonBox.accepted.connect(self.accept)
          self.buttonBox.rejected.connect(Dialog.reject)
          self.retranslateUi(Dialog)

          QtCore.QMetaObject.connectSlotsByName(Dialog)

     #

     def accept(self):
          print("******************************************")
          csv = csvExp()
          csv.fileFill(self.nameInput.displayText(), self.gpaInput.displayText(), self.gradeInput.currentText())
          self.nameInput.clear()
          self.gradeInput.clear()
          self.gradeInput.addItems(["Freshman","Sophomore","Junior","Senior","5th Year","Old"])
          self.gpaInput.clear()
          self.nameInput.setFocus()

     def retranslateUi(self, Dialog):
          _translate = QtCore.QCoreApplication.translate
          Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
          self.buttonBox.setToolTip(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
          self.gradeInput.setItemText(0, _translate("Dialog", "Freshman"))
          self.gradeInput.setItemText(1, _translate("Dialog", "Sophomore"))
          self.gradeInput.setItemText(2, _translate("Dialog", "Junior"))
          self.gradeInput.setItemText(3, _translate("Dialog", "Senior"))
          self.gradeInput.setItemText(4, _translate("Dialog", "5th Year"))
          self.gradeInput.setItemText(5, _translate("Dialog", "Old"))
          self.label.setText(_translate("Dialog",
                                        "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name:</span></p></body></html>"))
          self.label_2.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">GPA:</span></p></body></html>"))
          self.label_3.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Year</span></p></body></html>"))
          self.label_5.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ΣΠ Designated Driver Scheduler</span></p></body></html>"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
