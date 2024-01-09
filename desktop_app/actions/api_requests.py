import requests
import json


def make_post_request(api_url, payload: object):
    # Convert ClientData object to a dictionary
    payload_dict = vars(payload)

    # Convert the payload dictionary to JSON
    payload_json = json.dumps(payload_dict)

    # Specify the 'Content-Type' header as 'application/json'
    headers = {'Content-Type': 'application/json'}

    # Make the POST request using the 'data' parameter
    response_API = requests.post(
        api_url, data=payload_json, headers=headers)

    # Check if the request was successful (status code 2xx)
    if response_API.status_code // 100 == 2:
        return True
    else:
        # Raise an exception or handle the error as needed
        return False
