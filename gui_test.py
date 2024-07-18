from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QVBoxLayout, QWidget
import sys

class UserDialogApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Selection")

        # Create buttons for User1 and User2
        self.user1_button = QPushButton("User1", self)
        self.user2_button = QPushButton("User2", self)

        # Set layout
        layout = QVBoxLayout()
        layout.addWidget(self.user1_button)
        layout.addWidget(self.user2_button)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Connect the button click events to their respective functions
        self.user1_button.clicked.connect(lambda: self.show_message("User1"))
        self.user2_button.clicked.connect(lambda: self.show_message("User2"))

    def show_message(self, user):
        # Create the message box
        message_box = QMessageBox()
        message_box.setText(f"Hey {user}!")
        message_box.setWindowTitle(f"Greeting for {user}")

        # Resize the message box
        message_box.resize(1500, 1350)  # Adjust the width and height as needed

        # Display the message box
        message_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserDialogApp()
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec_())
