from fastapi import Request, status
from fastapi.responses import JSONResponse

from taskmaster.main import app, exception_handler


@app.get('/')
def sx(): ...


def test_index_should_suggest_docs(client):
    res = client.get('/')

    assert res.status_code == status.HTTP_200_OK
    assert 'Visit Swagger documentation' in res.text


def test_exception_handler():
    req = Request({'type': 'http', 'scheme': 'http', 'method': 'GET'})
    exc = Exception('Test exception')

    res = exception_handler(req, exc)
    assert res.status_code == status.HTTP_500_INTERNAL_SERVER_ERROR
    assert res.body == JSONResponse({'detail': 'Internal Server Error'}).body
