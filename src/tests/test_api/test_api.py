import pytest
from httpx import AsyncClient

from mainapi import app


@pytest.mark.anyio
async def test_root():
    body = {
      "sheet_url" :"https://docs.google.com/spreadsheets/d/1A77-RWx7x8PK2uDm_1XlXyCy2ID9-9lhwix8wPDd5X0/pubhtml?gid=0"
                   "&amp;single=true"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/ASSIGNMENT/api/v1/download-contracts-csv-mode", json=body)
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}