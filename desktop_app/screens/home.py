from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from forms.client_form import ClientForm


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        label_title = QLabel(
            "Clients List", self)

        button_add = QPushButton("Add Client")
        button_add.clicked.connect(self.on_add_client_clicked)

        layout = QVBoxLayout()
        layout.addWidget(label_title)
        layout.addWidget(button_add)

        self.setLayout(layout)

    def on_add_client_clicked(self):
        client_form = ClientForm()
        client_form.show()
        client_form.exec()
