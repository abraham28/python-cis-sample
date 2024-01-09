from PyQt6.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QFormLayout, QTextEdit, QRadioButton, QHBoxLayout, QCheckBox, QSpinBox, QDateEdit, QComboBox, QMessageBox
from actions.api_requests import make_post_request
from typing import List
from models.client_data import ClientData
import json


def load_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def populate_combobox(combobox: QComboBox, dataList: dict[str, str]
                      ):
    combobox.clear()
    for name, code in dataList.items():
        combobox.addItem(name, code)
    combobox.setCurrentIndex(-1)


def json_to_combobox_transform(json_data,  key: str, filter_key: str, filter_value: str):
    if (not filter_key or not filter_value):
        filtered_data = json_data
    else:
        filtered_data = [
            item for item in json_data if item.get(filter_key) == filter_value
        ]
    return {
        item["name"]: item[key] for item in filtered_data}


class ClientForm(QDialog):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):

        # Create Labels
        label_full_name = QLabel('Full Name:', self)
        label_contact_number = QLabel('Contact Number:', self)
        label_favorite_colors = QLabel('Favorite Colors:', self)
        label_gender = QLabel('Gender:', self)
        label_dependents_count = QLabel('Number of Dependents:', self)
        label_birthday = QLabel('Date of Birth:', self)
        label_notes = QLabel('Notes:', self)
        label_zip_code = QLabel('Zip Code:', self)
        label_region = QLabel('Region:', self)
        label_province = QLabel('Province:', self)
        label_municipality_city = QLabel('Municipality/City:', self)
        label_town_district = QLabel('Town/District:', self)
        label_barangay = QLabel('Barangay:', self)
        label_subdivision_village_zone = QLabel(
            'Subdivision/Village/Zone:', self)
        label_street_name = QLabel('Street Name:', self)
        label_lot_block_phase_house_building_no = QLabel(
            'Lot/Block/Phase/House/Building Number:', self)
        label_building_tower_name = QLabel('Building/Tower Name:', self)
        label_unit_room_floor_building_no = QLabel(
            'Unit/Room/Floor/Building Number:', self)

        # Create Fields
        self.edit_full_name = QLineEdit(self)
        self.edit_contact_number = QLineEdit(self)

        self.favorite_colors_checkbox_group = []

        colors = ["Red", "Blue", "Pink", "Yellow"]
        for color in colors:
            checkbox = QCheckBox(color, self)
            self.favorite_colors_checkbox_group.append(checkbox)

        self.radio_gender_male = QRadioButton('Male', self)
        self.radio_gender_female = QRadioButton('Female', self)
        self.spinbox_dependents_count = QSpinBox(self)
        self.edit_birthday = QDateEdit(self)

        regions_json = load_json_file('desktop_app/json_files/regions.json')
        self.combobox_region = QComboBox(self)
        populate_combobox(self.combobox_region,
                          json_to_combobox_transform(regions_json, "reg_code", "", ""))
        self.combobox_region.currentIndexChanged.connect(
            self.on_combobox_region_selected)

        self.combobox_province = QComboBox(self)
        self.combobox_province.currentIndexChanged.connect(
            self.on_combobox_province_selected)

        self.combobox_municipality_city = QComboBox(self)
        self.combobox_municipality_city.currentIndexChanged.connect(
            self.on_combobox_municipality_city_selected)

        self.combobox_barangay = QComboBox(self)

        self.edit_town_district = QLineEdit(self)
        self.edit_subdivision_village_zone = QLineEdit(self)
        self.edit_street_name = QLineEdit(self)
        self.edit_lot_block_phase_house_building_no = QLineEdit(self)
        self.edit_building_tower_name = QLineEdit(self)
        self.edit_unit_room_floor_building_no = QLineEdit(self)
        self.edit_zip_code = QLineEdit(self)

        self.edit_notes = QTextEdit(self)

        # Create a button
        button_submit = QPushButton('Submit', self)
        button_submit.clicked.connect(self.on_button_click)

        # Set up layout
        layout = QFormLayout()

        layout.addRow(label_full_name, self.edit_full_name)
        layout.addRow(label_contact_number, self.edit_contact_number)

        for checkbox in self.favorite_colors_checkbox_group:
            layout.addRow(label_favorite_colors, checkbox)

        # setup Gender Layout
        layout_gender_radios = QHBoxLayout()
        layout_gender_radios.addWidget(
            self.radio_gender_male)
        layout_gender_radios.addWidget(
            self.radio_gender_female)
        layout.addRow(label_gender, layout_gender_radios)

        layout.addRow(label_dependents_count, self.spinbox_dependents_count)
        layout.addRow(label_birthday, self.edit_birthday)
        layout.addRow(label_region, self.combobox_region)
        layout.addRow(label_province, self.combobox_province)
        layout.addRow(label_municipality_city, self.combobox_municipality_city)
        layout.addRow(label_barangay, self.combobox_barangay)
        layout.addRow(label_town_district, self.edit_town_district)
        layout.addRow(label_subdivision_village_zone,
                      self.edit_subdivision_village_zone)
        layout.addRow(label_street_name, self.edit_street_name)
        layout.addRow(label_lot_block_phase_house_building_no,
                      self.edit_lot_block_phase_house_building_no)
        layout.addRow(label_building_tower_name, self.edit_building_tower_name)
        layout.addRow(label_unit_room_floor_building_no,
                      self.edit_unit_room_floor_building_no)
        layout.addRow(label_zip_code, self.edit_zip_code)
        layout.addRow(label_notes, self.edit_notes)

        layout.addRow(button_submit)

        self.setLayout(layout)

    def on_combobox_region_selected(self):
        selected_value = self.combobox_region.currentData()
        if not selected_value:
            return
        provinces_json = load_json_file(
            'desktop_app/json_files/provinces.json')
        populate_combobox(self.combobox_province,
                          json_to_combobox_transform(provinces_json, "prov_code", "reg_code", selected_value))

    def on_combobox_province_selected(self):
        selected_value = self.combobox_province.currentData()
        if not selected_value:
            return
        city_mun_json = load_json_file(
            'desktop_app/json_files/city-mun.json')
        populate_combobox(self.combobox_municipality_city,
                          json_to_combobox_transform(city_mun_json, "mun_code", "prov_code", selected_value))

    def on_combobox_municipality_city_selected(self):
        selected_value = self.combobox_municipality_city.currentData()
        if not selected_value:
            return
        barangays_json = load_json_file(
            'desktop_app/json_files/barangays.json')
        populate_combobox(self.combobox_barangay,
                          json_to_combobox_transform(barangays_json, "name", "mun_code", selected_value))

    def on_button_click(self):
        full_name = self.edit_full_name.text()
        contact_number = self.edit_contact_number.text()

        favorite_colors: List[str] = [checkbox.text(
        ) for checkbox in self.favorite_colors_checkbox_group if checkbox.isChecked()]

        if self.radio_gender_male.isChecked():
            gender: str = "Male"
        elif self.radio_gender_female.isChecked():
            gender: str = "Female"
        else:
            gender = None

        if not gender:
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Gender is required")
            msg_box.exec()
            return

        dependents_count = self.spinbox_dependents_count.value()
        birthday = self.edit_birthday.text()
        notes = self.edit_notes.toPlainText()
        zip_code = self.edit_zip_code.text()
        region = self.combobox_region.currentText()
        province = self.combobox_province.currentText()
        municipality_city = self.combobox_municipality_city.currentText()
        barangay = self.combobox_barangay.currentText()
        town_district = self.edit_town_district.text()
        subdivision_village_zone = self.edit_subdivision_village_zone.text()
        street_name = self.edit_street_name.text()
        lot_block_phase_house_building_no = self.edit_lot_block_phase_house_building_no.text()
        building_tower_name = self.edit_building_tower_name.text()
        unit_room_floor_building_no = self.edit_unit_room_floor_building_no.text()

        api_url = "http://localhost:8000/clients/create"

        data = ClientData(
            full_name,
            contact_number,
            favorite_colors,
            gender,
            dependents_count,
            birthday,
            notes,
            zip_code,
            region,
            province,
            municipality_city,
            barangay,
            town_district,
            subdivision_village_zone,
            street_name,
            lot_block_phase_house_building_no,
            building_tower_name,
            unit_room_floor_building_no)

        success = make_post_request(api_url, data)

        if success:
            # Process the successful response
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Client is created successfully")
            msg_box.exec()
            self.close()

        else:
            # Handle the error
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Error occurred.")
            msg_box.exec()
