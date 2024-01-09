import requests
import json


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_post_request(self, endpoint, payloadDict):
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        payload_json = json.dumps(payloadDict)
        response = requests.post(url, data=payload_json, headers=headers)
        return response

    def make_get_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        return response

    def make_put_request(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        payload_json = json.dumps(payload)
        response = requests.put(url, data=payload_json, headers=headers)
        return response

    def make_delete_request(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.delete(url)
        return response

    def make_create_client_request(self, payload: object):
        # Convert ClientData object to a dictionary
        payload_dict = vars(payload)
        response = self.make_post_request("clients/create", payload_dict)
        # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
            return True
        else:
            return False

    def make_delete_all_clients_request(self):
        # Convert ClientData object to a dictionary
        response = self.make_delete_request("clients/delete-all")
        # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
            return True
        else:
            return False

    def make_delete_client_request(self, client_id):
        # Convert ClientData object to a dictionary
        response = self.make_delete_request(f"clients/{client_id}/delete")
        # Check if the request was successful (status code 2xx)
        if response.status_code // 100 == 2:
            return True
        else:
            return False

    def make_get_all_clients_request(self):
        response = self.make_get_request("clients")
        return response

    def make_get_client_request(self, client_id):
        response = self.make_get_request(f"clients/{client_id}")
        return response

    def make_update_client_request(self, client_id, payload: object):
        payload_dict = vars(payload)
        response = self.make_put_request(
            f"clients/{client_id}/update", payload_dict)
        return response


# Change the base_url as needed
api_client = ApiClient(base_url='http://localhost:8000')
