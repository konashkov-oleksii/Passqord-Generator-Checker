from PyQt6 import QtCore, QtGui, QtWidgets
import re
import random
import string

class Ui_PasswordGenerator(object):
    def setupUi(self, PasswordGenerator):
        PasswordGenerator.setObjectName("PasswordGenerator")
        PasswordGenerator.setFixedSize(700, 300)
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
        self.labelCheckResult.setFixedWidth(300)
        self.labelCheckResult.setWordWrap(True)

        self.contentLayout.addLayout(self.checkerLayout)

        # Generator Layout
        self.generatorLayout = QtWidgets.QVBoxLayout()

        self.checkDigits = QtWidgets.QCheckBox("Digits")
        self.checkDigits.setChecked(True)
        self.checkSpecialSymbols = QtWidgets.QCheckBox("Special Symbols")
        self.checkSpecialSymbols.setChecked(True)
        self.checkUpperCase = QtWidgets.QCheckBox("Upper Case")
        self.checkUpperCase.setChecked(True)

        self.generatorLayout.addWidget(self.checkDigits)
        self.generatorLayout.addWidget(self.checkSpecialSymbols)
        self.generatorLayout.addWidget(self.checkUpperCase)

        self.btnGenerate = QtWidgets.QPushButton("Generate")
        self.btnGenerate.setStyleSheet("background-color: #34495e;")
        self.generatorLayout.addWidget(self.btnGenerate)

        self.generatedPassword = QtWidgets.QLineEdit()
        self.generatedPassword.setPlaceholderText("Generated password will appear here...")
        self.generatedPassword.setReadOnly(True)
        self.generatorLayout.addWidget(self.generatedPassword)

        self.contentLayout.addLayout(self.generatorLayout)

        self.layout.addLayout(self.contentLayout)

        PasswordGenerator.setCentralWidget(self.centralwidget)

        self.retranslateUi(PasswordGenerator)
        self.connectSignals()

    def retranslateUi(self, PasswordGenerator):
        _translate = QtCore.QCoreApplication.translate
        PasswordGenerator.setWindowTitle(_translate("PasswordGenerator", "Password Generator/Checker"))
    
    def connectSignals(self):
        self.btnCheck.clicked.connect(self.checkHandler)
        self.btnGenerate.clicked.connect(self.generateHandler)

    def checkHandler(self):
        password = self.inputPassword.text().strip()
        if not password:
            self.labelCheckResult.setText("Result: Please enter a password.")
            self.labelCheckResult.setStyleSheet("color: #ecf0f1;")
            return

        strength = self.check_password(password)
        if strength >= 5:
            self.labelCheckResult.setText("Result: Strong password!")
            self.labelCheckResult.setStyleSheet("color: green;")
        elif strength >= 3:
            self.labelCheckResult.setText("Result: Medium strength password.")
            self.labelCheckResult.setStyleSheet("color: yellow;")
        else:
            self.labelCheckResult.setText("Result: Weak password!")
            self.labelCheckResult.setStyleSheet("color: red;")

    def check_password(self, password):
        strong_index = 0
        password_length = len(password)

        with open('password_list.txt', 'r') as txt:
            pass_list = [line.strip().lower() for line in txt.readlines()]

        if password.strip().lower() in pass_list:
            return 0

        if password_length >= 12:
            strong_index += 2
        elif password_length >= 8:
            strong_index += 1

        if re.search(r'[a-z]', password):
            strong_index += 1
        if re.search(r'[A-Z]', password):
            strong_index += 1
        if re.search(r'\d', password):
            strong_index += 1
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            strong_index += 1

        return strong_index
    
    def generateHandler(self):
        checkbox_include_special = self.checkSpecialSymbols.isChecked()
        checkbox_include_digits = self.checkDigits.isChecked()
        checkbox_include_uppercase = self.checkUpperCase.isChecked()
        self.generatedPassword.setText(self.generate_password(12, include_special = checkbox_include_special, include_digits = checkbox_include_digits, include_upper = checkbox_include_uppercase))
    def generate_password(self,length, include_special, include_digits, include_upper):
        characters = string.ascii_lowercase
        if include_special:
            characters += string.punctuation
        if include_digits:
            characters += string.digits
        if include_upper:
            characters += string.ascii_uppercase
        return ''.join(random.choice(characters) for _ in range(length))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PasswordGenerator = QtWidgets.QMainWindow()
    ui = Ui_PasswordGenerator()
    ui.setupUi(PasswordGenerator)
    PasswordGenerator.show()
    sys.exit(app.exec())
    print()
