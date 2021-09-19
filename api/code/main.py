from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    return {"message": "Hello World"}

@api.get("/hoti")
async def hotReload():
    return {"message": "Hello Hot-Reload"}
