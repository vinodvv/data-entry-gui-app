import sys
import csv
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox


def write_to_csv(text):
    """
    Append the entered text to a new row in the CSV file.
    Args text: (str): The text to be written to the CSV file.
    """
    csv_file = 'data.csv'
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([text])


class DataEntryApp(QWidget):
    def __init__(self):
        """
        Initialize the DataEntryApp window, setting up the user interface components.
        """
        super().__init__()

        # Set up the user interface
        self.setWindowTitle("Data Entry Tool")
        self.setGeometry(150, 150, 300, 150)

        self.layout = QVBoxLayout()

        # Text input field
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Enter text here")
        self.text_input.returnPressed.connect(self.submit_text)  # Connect Enter key to submit
        self.layout.addWidget(self.text_input)

        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.clicked.connect(self.submit_text)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def submit_text(self):
        """
        Handle the submission of text entered by the user.
        This method fetches the text from the input field and, if the text is not empty,
        writes it to a CSV file. If the text is empty, it shows a warning message.
        """
        text = self.text_input.text()

        if text:
            write_to_csv(text)
            QMessageBox.information(self, "Success", "Text has been add to CSV.")
            self.text_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter some text.")


if __name__ == "__main__":
    """
    The main entry point for the application.
    This block creates an instance of QApplication, instantiates the DataEntryApp,
    shows the main window, and starts the application's event loop.
    """
    app = QApplication(sys.argv)
    window = DataEntryApp()
    window.show()
    sys.exit(app.exec())
