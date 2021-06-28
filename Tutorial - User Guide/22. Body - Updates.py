# Body - Updates


# Update replacing with PUT
# from typing import List, Optional
#
# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     tax: float = 10.5
#     tags: List[str] = []
#
#
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }
#
#
# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]
#
#
# @app.put("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     update_item_encoded = jsonable_encoder(item)
#     items[item_id] = update_item_encoded
#     return update_item_encoded


# Partial updates with PATCH
# PATCH is less commonly used and known than PUT.
#
# And many teams use only PUT, even for partial updates.
#
# You are free to use them however you want, FastAPI doesn't impose any restrictions.
#
# But this guide shows you, more or less, how they are intended to be used


# Using Pydantic's exclude_unset parameter
# from typing import List, Optional
#
# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: Optional[str] = None
#     description: Optional[str] = None
#     price: Optional[float] = None
#     tax: float = 10.5
#     tags: List[str] = []
#
#
# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }
#
#
# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]
#
#
# @app.patch("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     stored_item_data = items[item_id]
#     stored_item_model = Item(**stored_item_data)
#     update_data = item.dict(exclude_unset=True)
#     updated_item = stored_item_model.copy(update=update_data)
#     items[item_id] = jsonable_encoder(updated_item)
#     return updated_item


# Using Pydantic's update parameter
from typing import List, Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.patch("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
