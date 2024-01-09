from typing import List


class ClientData:
    def __init__(self, full_name: str, contact_number: str, favorite_colors: List[str], gender: str,
                 dependents_count: int, birthday: str, notes: str,
                 zip_code: str, region: str, province: str, municipality_city: str,
                 town_district: str, barangay: str, subdivision_village_zone: str,
                 street_name: str, lot_block_phase_house_building_no: str,
                 building_tower_name: str, unit_room_floor_building_no: str):
        self.full_name = full_name
        self.contact_number = contact_number
        self.favorite_colors = favorite_colors
        self.gender = gender
        self.dependents_count = dependents_count
        self.birthday = birthday
        self.notes = notes
        self.zip_code = zip_code
        self.region = region
        self.province = province
        self.municipality_city = municipality_city
        self.town_district = town_district
        self.barangay = barangay
        self.subdivision_village_zone = subdivision_village_zone
        self.street_name = street_name
        self.lot_block_phase_house_building_no = lot_block_phase_house_building_no
        self.building_tower_name = building_tower_name
        self.unit_room_floor_building_no = unit_room_floor_building_no
