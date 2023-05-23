import random
import string
from PyQt5 import QtCore, QtGui, QtWidgets

class PasswordGeneratorApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 300, 200)

        self.length_label = QtWidgets.QLabel("Password Length:", self)
        self.length_label.setGeometry(QtCore.QRect(20, 20, 120, 30))

        self.length_entry = QtWidgets.QSpinBox(self)
        self.length_entry.setGeometry(QtCore.QRect(150, 20, 70, 30))
        self.length_entry.setMinimum(3)

        self.generate_button = QtWidgets.QPushButton("Generate Password", self)
        self.generate_button.setGeometry(QtCore.QRect(20, 70, 200, 30))
        self.generate_button.clicked.connect(self.generate_and_store_password)

        self.generated_password_label = QtWidgets.QLabel("Generated password:", self)
        self.generated_password_label.setGeometry(QtCore.QRect(20, 120, 250, 30))

    def generate_password(self, length):
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length - 2))
        password += random.choice(string.ascii_uppercase)  # Capitalize a random letter
        password += random.choice(string.digits + string.punctuation)  # Add a number or punctuation at the end
        return password

    def generate_and_store_password(self):
        length = self.length_entry.value()
        password = self.generate_password(length)
        self.generated_password_label.setText("Generated password: " + password)
        self.store_password(password)

    def store_password(self, password):
        with open('passwords.txt', 'a') as file:
            file.write(password + '\n')

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = PasswordGeneratorApp()
    window.show()
    app.exec_()
