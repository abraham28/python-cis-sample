import math
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox
from forms.client_form import ClientForm
from forms.client_form import ClientForm
from actions.api_client import api_client
from models.client_data import ClientData, Client
from .client_details import ClientDetailsWindow


class HomeLogic:
    def __init__(self, home_window):
        from .home import HomeWindow
        self.home_window: HomeWindow = home_window
        self.current_page = 1
        self.items_per_page = 5
        self.clients_data: list[Client] = []

    def on_add_client_clicked(self):
        client_form = ClientForm()
        client_form.on_success_add.connect(self.add_single_table_data)
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
            self.home_window.add_table_row(
                row, name_item, contact_number_item, client.user_id)

        self.update_pagination_buttons()

    def edit_client(self, client_id):
        client_to_edit = next(
            (client for client in self.clients_data if client.user_id == client_id), None)

        if client_to_edit is not None:
            client_form = ClientForm(client_to_edit)
            client_form.on_success_edit.connect(self.on_success_edit)
            client_form.exec()

    def on_success_edit(self, user_id: str, edited_client):
        print(f"edited_client: {edited_client}")
        solo_edited_client = Client(
            user_id=user_id, data=ClientData(**edited_client["data"]))

        for client in self.clients_data:
            if client.user_id == solo_edited_client.user_id:
                client.data = solo_edited_client.data
                break

        self.populate_table()

    def add_single_table_data(self, client):
        solo_client = Client(
            user_id=client["user_id"], data=ClientData(**client["data"]))

        self.clients_data.append(solo_client)
        self.populate_table()

    def delete_client(self, client_id):
        # Show confirmation dialog
        reply = QMessageBox.question(
            self.home_window,
            "Delete Client",
            "Are you sure you want to delete this client? This action cannot be reversed.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            # User confirmed deletion, proceed with the deletion
            if api_client.make_delete_client_request(client_id):
                print(f"Client {client_id} deleted successfully.")
                # After deleting, update the table

                client_index = next((index for index, client in enumerate(
                    self.clients_data) if client.user_id == client_id), None)
                if client_index is not None:
                    del self.clients_data[client_index]

                self.populate_table()
            else:
                print(f"Failed to delete client {client_id}.")
        else:
            # User chose not to delete
            print("Deletion canceled.")

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
