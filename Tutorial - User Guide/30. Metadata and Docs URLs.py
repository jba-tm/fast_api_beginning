# Metadata and Docs URLs

# Title, description, and version
from fastapi import FastAPI

# app = FastAPI(
#     title="My Super Project",
#     description="This is a very fancy project, with auto docs for the API and everything",
#     version="2.5.0",
# )
#
#
# @app.get("/items/")
# async def read_items():
#     return [{"name": "Foo"}]


# Metadata for tags
# from fastapi import FastAPI
#
# tags_metadata = [
#     {
#         "name": "users",
#         "description": "Operations with users. The **login** logic is also here.",
#     },
#     {
#         "name": "items",
#         "description": "Manage items. So _fancy_ they have their own docs.",
#         "externalDocs": {
#             "description": "Items external docs",
#             "url": "https://fastapi.tiangolo.com/",
#         },
#     },
# ]
#
# app = FastAPI(openapi_tags=tags_metadata)
#
#
# @app.get("/users/", tags=["users"])
# async def get_users():
#     return [{"name": "Harry"}, {"name": "Ron"}]
#
#
# @app.get("/items/", tags=["items"])
# async def get_items():
#     return [{"name": "wand"}, {"name": "flying broom"}]



# OpenAPI URL
# from fastapi import FastAPI
#
# app = FastAPI(openapi_url="/api/v1/openapi.json")
#
#
# @app.get("/items/")
# async def read_items():
#     return [{"name": "Foo"}]


# Docs URLs
from fastapi import FastAPI

app = FastAPI(docs_url="/documentation", redoc_url=None)


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]