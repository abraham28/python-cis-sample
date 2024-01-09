from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, \
    QDialog

from forms.client_form import ClientForm


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

        # Set a default window size
        self.setGeometry(100, 100, 800, 600)

    def on_add_client_clicked(self):
        client_form = ClientForm()
        result = client_form.exec()

        if result == QDialog.accepted:
            self.populate_table()

    def populate_table(self):
        # This is just a sample data, you should replace it with your actual client data
        clients_data = [
            {"name": "John Doe", "contact_number": "1234567890"},
            {"name": "Jane Doe", "contact_number": "9876543210"}
        ]

        self.table_clients.setRowCount(len(clients_data))

        for row, client in enumerate(clients_data):
            name_item = QTableWidgetItem(client["name"])
            contact_number_item = QTableWidgetItem(client["contact_number"])

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

        # Set the window size based on the contents of the table
        self.resize(self.table_clients.horizontalHeader().length() + 20, 600)

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
