from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QLineEdit, QPushButton, QCheckBox, QFrame)
from PyQt6.QtCore import Qt
import sys

class PasswordApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Colors
        self.color_background_frame = "#2c3e50"
        self.color_background_ui = "#34495e"
        self.color_text = "#ecf0f1"
        
        self.setWindowTitle("Password Tool")
        self.setGeometry(100, 100, 800, 500)
        
        # Main widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Left Frame - Check Password
        self.frame_check = QFrame()
        self.frame_check.setStyleSheet(f"background-color: {self.color_background_frame};")
        self.frame_check.setFixedWidth(int(self.width() * 0.55))
        main_layout.addWidget(self.frame_check)
        
        self.setup_check_frame()
        
        # Right Frame - Generate Password
        self.frame_generate = QFrame()
        self.frame_generate.setStyleSheet(f"background-color: {self.color_background_frame};")
        main_layout.addWidget(self.frame_generate)
        
        self.setup_generate_frame()
        
    def setup_check_frame(self):
        layout = QVBoxLayout(self.frame_check)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        
        # Title
        title = QLabel("Check Password")
        title.setStyleSheet(f"color: white; font: bold 14px Arial;")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(20)
        
        # Password input
        self.pass_input = QLineEdit()
        self.pass_input.setStyleSheet(f"""
            background-color: {self.color_background_ui};
            color: {self.color_text};
            padding: 8px;
            border: 1px solid #7f8c8d;
            border-radius: 4px;
        """)
        layout.addWidget(self.pass_input)
        
        # Check button
        self.btn_check = QPushButton("Check your pass")
        self.btn_check.setStyleSheet(f"""
            QPushButton {{
                background-color: #3498db;
                color: white;
                padding: 8px;
                border: none;
                border-radius: 4px;
                font: bold 12px Arial;
            }}
            QPushButton:hover {{
                background-color: #2980b9;
            }}
        """)
        # self.btn_check.clicked.connect(self.check_password)
        layout.addWidget(self.btn_check)
        layout.addSpacing(10)
        
        # Result label
        self.result_label = QLabel("")
        self.result_label.setStyleSheet(f"color: {self.color_text}; font: 12px Arial;")
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.result_label)
        
    def setup_generate_frame(self):
        layout = QVBoxLayout(self.frame_generate)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(10)
        
        # Title
        title = QLabel("Generate Password")
        title.setStyleSheet(f"color: white; font: bold 14px Arial;")
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addSpacing(20)
        
        # Checkboxes
        self.checkboxes = {
            'spec_symbol': QCheckBox("Include special characters"),
            'digits': QCheckBox("Include digits"),
            'up_case': QCheckBox("Include upper case")
        }
        
        for checkbox in self.checkboxes.values():
            checkbox.setStyleSheet(f"""
                QCheckBox {{
                    color: {self.color_text};
                    font: 12px Arial;
                }}
                QCheckBox::indicator {{
                    width: 16px;
                    height: 16px;
                }}
                QCheckBox::indicator:checked {{
                    background-color: #3498db;
                }}
            """)
            layout.addWidget(checkbox, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # Generate button
        self.btn_generate = QPushButton("Generate pass")
        self.btn_generate.setStyleSheet(f"""
            QPushButton {{
                background-color: #3498db;
                color: white;
                padding: 8px;
                border: none;
                border-radius: 4px;
                font: bold 12px Arial;
            }}
            QPushButton:hover {{
                background-color: #2980b9;
            }}
        """)
        # self.btn_generate.clicked.connect(self.gen_pass)
        layout.addWidget(self.btn_generate)
        layout.addSpacing(10)
        
        # Generated password
        self.pass_generated = QLineEdit()
        self.pass_generated.setReadOnly(True)
        self.pass_generated.setStyleSheet(f"""
            background-color: {self.color_background_ui};
            color: {self.color_text};
            padding: 8px;
            border: 1px solid #7f8c8d;
            border-radius: 4px;
        """)
        layout.addWidget(self.pass_generated)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordApp()
    window.show()
    sys.exit(app.exec())