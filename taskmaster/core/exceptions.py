from http import HTTPStatus
from typing import Any, Optional
from typing import Dict as _Dict

from fastapi import HTTPException

Dict = _Dict[str, str]


class NotFoundException(HTTPException):
    message = HTTPStatus.NOT_FOUND.phrase

    def __init__(self, detail: Any = message, headers: Optional[Dict] = None) -> None:
        super().__init__(HTTPStatus.NOT_FOUND, detail, headers)
