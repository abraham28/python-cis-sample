from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget
from .home_logic import HomeLogic


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.home_logic = HomeLogic(self)
        self.init_ui()

    def init_ui(self):
        self.label_title = QLabel("Clients List", self)
        self.button_add = QPushButton("Add Client")
        self.button_add.clicked.connect(self.home_logic.on_add_client_clicked)

        self.table_clients = QTableWidget(self)
        self.table_clients.setColumnCount(5)
        self.table_clients.setHorizontalHeaderLabels(
            ["Name", "Contact Number", "", "", ""])

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.button_add)
        layout.addWidget(self.table_clients)

        self.button_next = QPushButton("Next Page")
        self.button_next.clicked.connect(self.home_logic.next_page)

        self.button_prev = QPushButton("Previous Page")
        self.button_prev.clicked.connect(self.home_logic.prev_page)

        layout.addWidget(self.button_next)
        layout.addWidget(self.button_prev)

        self.setLayout(layout)

        self.home_logic.initialize_clients_data()

    def add_table_row(self, row_number, item_name, item_contact_number):
        self.table_clients.setItem(row_number, 0, item_name)
        self.table_clients.setItem(
            row_number, 1, item_contact_number)

        view_button = QPushButton("View", self)
        view_button.clicked.connect(
            lambda _, r=row_number: self.home_logic.view_client(r))

        edit_button = QPushButton("Edit", self)
        edit_button.clicked.connect(
            lambda _, r=row_number: self.home_logic.edit_client(r))

        delete_button = QPushButton("Delete", self)
        delete_button.clicked.connect(
            lambda _, r=row_number: self.home_logic.delete_client(r))

        self.table_clients.setCellWidget(
            row_number, 2, view_button)
        self.table_clients.setCellWidget(
            row_number, 3, edit_button)
        self.table_clients.setCellWidget(
            row_number, 4, delete_button)

        self.table_clients.resizeColumnsToContents()
