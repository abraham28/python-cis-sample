from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton

from models.client_data import Client


class ClientDetailsWindow(QDialog):
    def __init__(self, client: Client):
        super().__init__()

        self.setWindowTitle("Client Details")
        self.setGeometry(100, 100, 400, 300)

        self.init_ui(client)

    def init_ui(self, client: Client):
        layout = QVBoxLayout()

        label_name = QLabel(f"Full Name: {client.data.full_name}")
        label_contact = QLabel(f"Contact Number: {client.data.contact_number}")

        # Add more labels for other client details as needed

        button_close = QPushButton("Close")
        button_close.clicked.connect(self.close)

        layout.addWidget(label_name)
        layout.addWidget(label_contact)

        # Add more labels to the layout

        layout.addWidget(button_close)

        self.setLayout(layout)
