# Security - First Steps

# Create 24.2. Security - First Steps.py

# from fastapi import Depends, FastAPI
# from fastapi.security import OAuth2PasswordBearer
#
# app = FastAPI()
#
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
#
#
# @app.get("/items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token": token}


# FastAPI's OAuth2PasswordBearer
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
