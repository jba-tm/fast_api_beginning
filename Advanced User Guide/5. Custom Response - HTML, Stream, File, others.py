# Custom Response - HTML, Stream, File, others

# Use ORJSONResponse
# from fastapi import FastAPI
# from fastapi.responses import ORJSONResponse
#
# app = FastAPI()
#
#
# @app.get("/items/", response_class=ORJSONResponse)
# async def read_items():
#     return [{"item_id": "Foo"}]


# HTML Response
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
#
# app = FastAPI()
#
#
# @app.get("/items/", response_class=HTMLResponse)
# async def read_items():
#     html_content= """
#     <html>
#         <head>
#             <title>Some HTML in here</title>
#         </head>
#         <body>
#             <h1>Look ma! HTML!</h1>
#         </body>
#     </html>
#     """
#     return HTMLResponse(content=html_content, status_code=200)



# Default response class
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI(default_response_class=ORJSONResponse)


@app.get("/items/")
async def read_items():
    return [{"item_id": "Foo"}]