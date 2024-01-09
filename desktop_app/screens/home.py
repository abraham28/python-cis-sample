from typing import List
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, \
    QDialog
from forms.client_form import ClientForm

from forms.client_form import ClientForm
from actions.api_client import api_client
from models.client_data import ClientData, Client


class HomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label_title = QLabel("Clients List", self)

        self.button_add = QPushButton("Add Client")
        self.button_add.clicked.connect(self.on_add_client_clicked)

        self.table_clients = QTableWidget(self)
        self.table_clients.setColumnCount(5)
        self.table_clients.setHorizontalHeaderLabels(
            ["Name", "Contact Number", "", "", ""])

        self.populate_table()

        layout = QVBoxLayout()
        layout.addWidget(self.label_title)
        layout.addWidget(self.button_add)
        layout.addWidget(self.table_clients)

        self.setLayout(layout)

    def on_add_client_clicked(self):
        client_form = ClientForm(self.add_single_table_data)
        # client_form.on_success_add.connect()
        client_form.exec()

    def add_single_table_data(self, client):
        row_position = self.table_clients.rowCount()
        self.table_clients.insertRow(row_position)
        solo_client = Client(
            user_id=client["user_id"], data=ClientData(**client["data"]))

        name_item = QTableWidgetItem(solo_client.data.full_name)
        contact_number_item = QTableWidgetItem(solo_client.data.contact_number)

        self.table_clients.setItem(row_position, 0, name_item)
        self.table_clients.setItem(row_position, 1, contact_number_item)

        view_button = QPushButton("View", self)
        view_button.clicked.connect(
            lambda _, r=row_position: self.view_client(r))

        edit_button = QPushButton("Edit", self)
        edit_button.clicked.connect(
            lambda _, r=row_position: self.edit_client(r))

        delete_button = QPushButton("Delete", self)
        delete_button.clicked.connect(
            lambda _, r=row_position: self.delete_client(r))

        self.table_clients.setCellWidget(row_position, 2, view_button)
        self.table_clients.setCellWidget(row_position, 3, edit_button)
        self.table_clients.setCellWidget(row_position, 4, delete_button)

        self.table_clients.resizeColumnsToContents()
        self.table_clients.scrollToItem(
            self.table_clients.item(row_position, 0))

    def populate_table(self):
        all_clients_response = api_client.make_get_all_clients_request()
        if not all_clients_response.status_code // 100 == 2:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText(
                "please make sure you are connected to the redis-server")
            msg_box.exec()
        else:
            all_clients_response_json = all_clients_response.json()
            clients_data = [Client(user_id=client["user_id"], data=ClientData(
                **client["data"])) for client in all_clients_response_json["clients"]]
        self.table_clients.setRowCount(len(clients_data))

        for row, client in enumerate(clients_data):
            name_item = QTableWidgetItem(client.data.full_name)
            contact_number_item = QTableWidgetItem(
                client.data.contact_number)

            self.table_clients.setItem(row, 0, name_item)
            self.table_clients.setItem(row, 1, contact_number_item)

            # Add view, edit, delete buttons
            view_button = QPushButton("View", self)
            view_button.clicked.connect(lambda _, r=row: self.view_client(r))

            edit_button = QPushButton("Edit", self)
            edit_button.clicked.connect(lambda _, r=row: self.edit_client(r))

            delete_button = QPushButton("Delete", self)
            delete_button.clicked.connect(
                lambda _, r=row: self.delete_client(r))

            # Set buttons in the last three columns
            self.table_clients.setCellWidget(row, 2, view_button)
            self.table_clients.setCellWidget(row, 3, edit_button)
            self.table_clients.setCellWidget(row, 4, delete_button)

        # Adjust the column widths
        self.table_clients.resizeColumnsToContents()

    def view_client(self, row):
        # Implement view functionality here
        print(f"Viewing client at row {row}")

    def edit_client(self, row):
        # Implement edit functionality here
        print(f"Editing client at row {row}")

    def delete_client(self, row):
        # Implement delete functionality here
        print(f"Deleting client at row {row}")
        # After deleting, update the table
        self.populate_table()
