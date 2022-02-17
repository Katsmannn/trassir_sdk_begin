import json

import urllib3
import requests


def get_response_from_server(url, params):
    '''
    Get info from server.

    url - TRASSIR server URL,
    params - query parameters (ex: {'password': '1234'}).

    '''
    urllib3.disable_warnings()
    json_response = json.loads(
        requests.get(
            url, params, verify=False
        ).content.decode().split('/*\n\n')[0])
    return json_response
