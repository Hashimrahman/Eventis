# from fastapi import APIRouter, HTTPException

# from app.schemas.auth_schema import (
#     ForgotPasswordRequest,
#     LoginRequest,
#     RegisterRequest,
#     ResetPasswordRequest,
#     TokenResponse,
# )
# from app.services.auth_service import (
#     authenticate_user,
#     email_verification,
#     initiate_password_reset,
#     register_user,
#     reset_password,
# )

# router = APIRouter()


# @router.post("/register")
# def register(data: RegisterRequest):
#     try:
#         return register_user(data)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# @router.post("/login", response_model=TokenResponse)
# def login(data: LoginRequest):
#     auth_data = authenticate_user(data.email, data.password)
#     if not auth_data:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return auth_data


# @router.get("/verify-email")
# def verify_email(token: str):
#     try:
#         return email_verification(token)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# @router.post("/forgot-password")
# def forgot_password(data: ForgotPasswordRequest):
#     try:
#         return initiate_password_reset(data.email)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))


# @router.post("/reset-password")
# def reset_password_endpoint(data: ResetPasswordRequest):
#     try:
#         return reset_password(data)
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# @router.get("/test-cicd")
# def test_cicd():
#     return {"msg" : "CICD Final Setup checking"}


from fastapi import APIRouter, HTTPException

from app.schemas.auth_schema import (
    ForgotPasswordRequest,
    LoginRequest,
    RegisterRequest,
    ResetPasswordRequest,
    TokenResponse,
)
from app.services.auth_service import (
    authenticate_user,
    email_verification,
    initiate_password_reset,
    register_user,
    reset_password,
)

router = APIRouter()


@router.post("/register")
async def register(data: RegisterRequest):
    try:
        return await register_user(data)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest):
    auth_data = await authenticate_user(data.email, data.password)  
    if not auth_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return auth_data


@router.get("/verify-email")
async def verify_email(token: str):
    try:
        return await email_verification(token)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/forgot-password")
async def forgot_password(data: ForgotPasswordRequest):
    try:
        return await initiate_password_reset(data.email)  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/reset-password")
async def reset_password_endpoint(data: ResetPasswordRequest):
    try:
        return await reset_password(data) 
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/test-cicd")
async def test_cicd():
    return {"msg": "CICD Final Setup checking 2"}
