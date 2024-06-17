from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get('/', include_in_schema=False, status_code=status.HTTP_200_OK)
def index():
    return HTMLResponse("Visit Swagger documentation at: <a href='/docs'>/docs</a>")
