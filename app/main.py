from fastapi import FastAPI

from app.api.v1 import routes_auth,routes_user

app = FastAPI()

app.include_router(routes_auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(routes_user.router)


@app.get("/")
def root():
    return {"msg": "Event Management API"}
