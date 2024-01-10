import math
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from forms.client_form import ClientForm
from forms.client_form import ClientForm
from actions.api_client import api_client
from models.client_data import ClientData, Client


class HomeLogic:
    def __init__(self, home_window):
        from .home import HomeWindow
        self.home_window: HomeWindow = home_window
        self.current_page = 1
        self.items_per_page = 5
        self.clients_data: list[Client] = []

    def on_add_client_clicked(self):
        client_form = ClientForm(self.add_single_table_data)
        client_form.exec()

    def add_single_table_data(self, client):
        solo_client = Client(
            user_id=client["user_id"], data=ClientData(**client["data"]))

        self.clients_data.append(solo_client)
        self.populate_table()

    def initialize_clients_data(self):
        all_clients_response = api_client.make_get_all_clients_request()

        if not all_clients_response.status_code // 100 == 2:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText(
                "Please make sure you are connected to the redis-server")
            msg_box.exec()
            return
        else:
            all_clients_response_json = all_clients_response.json()
            self.clients_data = [Client(user_id=client["user_id"], data=ClientData(
                **client["data"])) for client in all_clients_response_json["clients"]]
            self.populate_table()

    def populate_table(self):
        start_index = (self.current_page - 1) * self.items_per_page
        end_index = start_index + self.items_per_page

        self.home_window.table_clients.clearContents()
        self.home_window.table_clients.setRowCount(self.items_per_page)

        for row, client in enumerate(self.clients_data[start_index:end_index]):
            name_item = QTableWidgetItem(client.data.full_name)
            contact_number_item = QTableWidgetItem(client.data.contact_number)
            self.home_window.add_table_row(row, name_item, contact_number_item)

        self.update_pagination_buttons()

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

    def next_page(self):
        self.current_page += 1
        self.populate_table()
        self.update_pagination_buttons()

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.populate_table()
            self.update_pagination_buttons()

    def update_pagination_buttons(self):
        total_pages = math.ceil(len(self.clients_data) / self.items_per_page)

        self.home_window.button_next.setEnabled(
            self.current_page < total_pages)
        self.home_window.button_prev.setEnabled(self.current_page > 1)
