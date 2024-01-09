
from pydantic import BaseModel
from typing import List, Union


class ClientData(BaseModel):
    full_name: str  # text
    contact_number: str  # text
    favorite_colors: Union[List[str], str]  # checkbox
    gender: str  # radio "M" or "F"
    dependents_count: int  # number of dependends
    income_range: str  # range
    birthday: str  # date
    notes: str  # textarea
    zip_code: str  # text
    region: str  # dropdown
    province: str  # dropdown
    municipality_city: str  # dropdown
    town_district: str  # dropdown
    barangay: str  # dropdown
    subdivision_village_zone: str  # text
    street_name: str  # text
    lot_block_phase_house_building_no: str  # text
    building_tower_name: str  # text
    unit_room_floor_building_no: str  # text
