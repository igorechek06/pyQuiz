from typing import Any
from urllib.parse import quote, urlencode

import httpx


def encode(value: dict[str, Any]) -> str:
    return urlencode(
        dict(filter(lambda i: i[1] is not None, value.items())),
        quote_via=quote,
    )


def response(response: httpx.Response) -> Any:
    status = response.status_code

    if 200 <= status <= 299:
        return response.json()
    elif 400 <= status <= 499:
        raise AssertionError(response.json()["detail"])
    else:
        raise AssertionError("Неизвестная ошибка")
