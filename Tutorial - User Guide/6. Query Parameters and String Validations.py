# Query Parameters and String Validations

# from typing import Optional
#
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: Optional[str] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Additional validation
# from typing import Optional
#
# from fastapi import FastAPI, Query  # ///////////
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Add more validations
# from typing import Optional
#
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50)):  # ///////////
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Add regular expressions
# from typing import Optional
#
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(
#         q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Default values
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: str = Query("fixedquery", min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Make it required
# When we don't need to declare
# more validations or metadata, we can make the q query
# parameter required just by not declaring a default value, like:
#
#
# q: str
# instead of:
#
#
# q: Optional[str] = None
# But we are now declaring it with Query, for example like:
#
#
# q: Optional[str] = Query(None, min_length=3)
# So, when you need to declare a value as required while using Query, you can use ... as the first argument:
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: str = Query(..., min_length=3)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Query parameter list / multiple values
# from typing import List, Optional


# Query parameter list / multiple values with defaults
# from typing import List
#
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
#
# async def read_items(q: List[str] = Query(["foo", "bar"])):
#
#     query_items = {"q": q}
#     return query_items


# Using list
# You can also use list directly instead of List[str]:
#
#
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(q: list = Query([])):
#     query_items = {"q": q}
#     return query_items


# Declare more metadata
# from typing import Optional
#
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(
#     q: Optional[str] = Query(
#         None,
#         title="Query string",
#         description="Query string for the items to search in the database that have a good match",
#         min_length=3,
#     )
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Alias parameters
# from typing import Optional
#
# from fastapi import FastAPI, Query
#
# app = FastAPI()
#
#
# @app.get("/items/")
#
# async def read_items(q: Optional[str] = Query(None, alias="item-query")):
#
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# Deprecating parameters
from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Optional[str] = Query(
        None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",

        deprecated=True,

    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
