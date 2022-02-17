import datetime

import requests
from django.shortcuts import render

from .utils import get_response_from_server
from .params import (
    SDK_PASSWORD,
    SERVER_IP,
    SERVER_ERROR_RESPONSE,
    DATA_ERROR_RESPONSE
)


def index(request):
    server_url = 'https://' + SERVER_IP + ':8080/'
    setting_url = server_url + 'settings/'
    health_url = server_url + 'health'
    payload = {'password': SDK_PASSWORD}
    now = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    try:
        server_name = get_response_from_server(
            setting_url, params=payload
        ).get('name')
        cpu_usage = get_response_from_server(
            health_url, params=payload
        ).get('cpu_load')
    except requests.exceptions.RequestException:
        return render(
            request,
            'index.html',
            SERVER_ERROR_RESPONSE
        )
    if server_name is not None and cpu_usage is not None:
        response = {
            'server_name': server_name,
            'now': now,
            'cpu_usage': cpu_usage,
        }
        return render(
            request,
            'index.html',
            response
        )
    return render(
        request,
        'index.html',
        DATA_ERROR_RESPONSE
    )
