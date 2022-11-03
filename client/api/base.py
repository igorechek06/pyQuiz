from typing import Any

import requests
from PyQt5.QtWidgets import QMessageBox


def response(response: requests.Response) -> Any:
    status = response.status_code

    if 200 <= status <= 299:
        return response.json()
    elif 400 <= status <= 499:
        raise requests.HTTPError(status, response.json()["message"])
    else:
        raise requests.HTTPError(status, "Неизвестная ошибка")
