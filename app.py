from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.resize(420, 300)
        PasswordGenerator.setStyleSheet("background-color: #2c3e50; color: #ecf0f1;")

        self.centralwidget = QtWidgets.QWidget(PasswordGenerator)
        self.centralwidget.setObjectName("centralwidget")

        # Main layout
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.layout.setContentsMargins(20, 0, 20, 20)

        # Header layout (Aligned)
        self.headerLayout = QtWidgets.QHBoxLayout()

        self.checkerTitle = QtWidgets.QLabel("Checker")
        self.checkerTitle.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Weight.Bold))
        self.checkerTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.generatorTitle = QtWidgets.QLabel("Generator")
        self.generatorTitle.setFont(QtGui.QFont("Arial", 18, QtGui.QFont.Weight.Bold))
        self.generatorTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.headerLayout.addWidget(self.checkerTitle)
        self.headerLayout.addWidget(self.generatorTitle)

        self.layout.addLayout(self.headerLayout)

        # Content Layout
        self.contentLayout = QtWidgets.QHBoxLayout()

        # Checker section
        self.checkerLayout = QtWidgets.QVBoxLayout()
        self.inputPassword = QtWidgets.QLineEdit()
        self.inputPassword.setPlaceholderText("Enter password to check...")
        self.checkerLayout.addWidget(self.inputPassword)

        self.btnCheck = QtWidgets.QPushButton("Check")
        self.btnCheck.setStyleSheet("background-color: #34495e;")
        self.checkerLayout.addWidget(self.btnCheck)

        self.labelCheckResult = QtWidgets.QLabel("Result: ")
        self.checkerLayout.addWidget(self.labelCheckResult)

        self.contentLayout.addLayout(self.checkerLayout)

        # Generator Layout
        self.generatorLayout = QtWidgets.QVBoxLayout()

        self.checkDigits = QtWidgets.QCheckBox("Digits")
        self.checkSpecialSymbols = QtWidgets.QCheckBox("Special Symbols")
        self.checkUpperCase = QtWidgets.QCheckBox("Upper Case")

        self.generatorLayout.addWidget(self.checkDigits)
        self.generatorLayout.addWidget(self.checkSpecialSymbols)
        self.generatorLayout.addWidget(self.checkUpperCase)

        self.btnGenerate = QtWidgets.QPushButton("Generate")
        self.btnGenerate.setStyleSheet("background-color: #34495e;")
        self.generatorLayout.addWidget(self.btnGenerate)

        self.generatedPassword = QtWidgets.QLineEdit()
        self.generatedPassword.setPlaceholderText("Generated password will appear here...")
        self.generatorLayout.addWidget(self.generatedPassword)

        self.contentLayout.addLayout(self.generatorLayout)

        self.layout.addLayout(self.contentLayout)

        PasswordGenerator.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordGenerator)

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator/Checker"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec())
