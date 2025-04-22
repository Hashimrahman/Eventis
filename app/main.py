from fastapi import FastAPI

from app.api.v1 import routes_auth

app = FastAPI()

app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["Auth"])


@app.get("/")
def root():
    return {"msg": "Event Management API"}
