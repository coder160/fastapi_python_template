from typing import Union

import uvicorn as SERVER
from fastapi import FastAPI as APP

_app = APP()
_server = SERVER


@_app.get("/")
def read_root():
    return {"Hello": "World"}

@_app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    _server.run(_app, host="localhost", port=8080)
