# Path Parameters and Numeric Validations
from typing import Optional

from fastapi import FastAPI, Path, Query


app = FastAPI()


# Import Path
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(..., title="The ID of the item to get"),
#     q: Optional[str] = Query(None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# Declare metadata
# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: int = Path(..., title="The ID of the item to get"),
#     q: Optional[str] = Query(None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# Order the parameters as you need
# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: int = Path(..., title="The ID of the item to get")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# Number validations: greater than or equal
@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
