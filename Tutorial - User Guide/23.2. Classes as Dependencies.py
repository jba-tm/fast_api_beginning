# Classes as Dependencies

# A dict from the previous example

# from typing import Optional
#
# from fastapi import Depends, FastAPI
#
# app = FastAPI()
#
#
# async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}
#
#
# @app.get("/items/")
# async def read_items(commons: dict = Depends(common_parameters)):
#     return commons
#
#
# @app.get("/users/")
# async def read_users(commons: dict = Depends(common_parameters)):
#     return commons


# What makes a dependency
# Up to now you have seen dependencies declared as functions.
#
# But that's not the only way to declare dependencies (although it would probably be the more common).
#
# The key factor is that a dependency should be a "callable".
#
# A "callable" in Python is anything that Python can "call" like a function.
#
# So, if you have an object something (that might not be a function) and you can "call" it (execute it) like:
#
#
# something()
# or
#
#
# something(some_argument, some_keyword_argument="foo")


# Classes as dependencies
from typing import Optional

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends(CommonQueryParams)):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response
