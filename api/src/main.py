#!/usr/bin/env python3
from fastapi import FastAPI

api = FastAPI()


@api.get("/")
async def root():
    """Root Endpoint

    Returns:
        None
    """
    return {"message": "Hello World"}


@api.get("/hot-reload")
async def hotReload():
    """Hot reload test endpoint

    Returns:
        None
    """
    return {"message": "Hello Hot-Reload"}
