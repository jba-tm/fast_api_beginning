# Header Parameters

# from typing import Optional
#
# from fastapi import FastAPI, Header
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(user_agent: Optional[str] = Header(None)):
#     return {"User-Agent": user_agent}


# Automatic conversion
# from typing import Optional
#
# from fastapi import FastAPI, Header
#
# app = FastAPI()
#
#
# @app.get("/items/")
# async def read_items(
#
#     strange_header: Optional[str] = Header(None, convert_underscores=False)
#
# ):
#     return {"strange_header": strange_header}


# Duplicate headers
from typing import List, Optional

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(x_token: Optional[List[str]] = Header(None)):
    return {"X-Token values": x_token}

