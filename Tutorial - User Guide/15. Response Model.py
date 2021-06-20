# Response Model

# You can declare the model used for the response with the parameter response_model in any of the path operations:
#
# @app.get()
# @app.post()
# @app.put()
# @app.delete()
# etc.

# from typing import List, Optional
#
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []
#
#
# @app.post("/items/", response_model=Item)  # //////////////
# async def create_item(item: Item):
#     return item

# Note
#
# Notice that response_model is a parameter of the "decorator" method (get, post, etc).
# Not of your path operation function, like all the parameters and body.
#
# It receives the same type you would declare for a Pydantic model attribute, so, it can be a Pydantic model,
# but it can also be, e.g. a list of Pydantic models, like List[Item].
#
# FastAPI will use this response_model to:
#
# Convert the output data to its type declaration.
# Validate the data.
# Add a JSON Schema for the response, in the OpenAPI path operation.
# Will be used by the automatic documentation systems.
# But most importantly:
#
# Will limit the output data to that of the model. We'll see how that's important below.
# Technical Details
#
# The response model is declared in this parameter instead of as a function return type annotation,
# because the path function may not actually return that response model but rather return a dict,
# database object or some other model, and then use the response_model to perform the field limiting and serialization.

# from typing import Optional
#
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr
#
# app = FastAPI()
#
#
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Optional[str] = None
#
#
# # Don't do this in production!
# @app.post("/user/", response_model=UserIn)
# async def create_user(user: UserIn):
#     return user

# Now, whenever a browser is creating a user with a password, the API will return the same password in the response.
#
# In this case, it might not be a problem, because the user himself is sending the password.
#
# But if we use the same model for another path operation, we could be sending our user's passwords to every client.
#
# Danger
#
# Never store the plain password of a user or send it in a response.


# Add an output model

# We can instead create an input model with the plaintext password and an output model without it:

# from typing import Optional
#
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr
#
# app = FastAPI()
#
#
#
# class UserIn(BaseModel):
#
#     username: str
#
#     password: str
#
#     email: EmailStr
#     full_name: Optional[str] = None
#
#
#
# class UserOut(BaseModel):
#
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None
#
#
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user


# Response Model encoding parameters
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str

    description: Optional[str] = None

    price: float

    tax: float = 10.5

    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
