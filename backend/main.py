from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    route_1
)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins     = origins,
    allow_credentials = True,
    allow_methods     = ['*'],
    allow_headers     = ['*']
)

app.include_router(route_1.router, prefix = "/v1/howathon/repo-rangers/route-1")
