# import secrets
# from datetime import datetime, timedelta

# from bson import ObjectId

# from app.core.security import create_access_token
# from app.db.database import get_user_collection
# from app.models.user_model import UserModel
# from app.schemas.auth_schema import ResetPasswordRequest
# from app.utils.email import send_reset_password_email, send_verification_email
# from app.utils.password import hash_password, verify_password

# # from app.utils.mail import


# def register_user(data):
#     is_admin= False
#     users = get_user_collection()
#     if users.find_one({"email": data.email}):
#         raise Exception("User already exists")
#     if len(data.password.strip()) < 6:
#         raise Exception("Password Should contain atleast 6 charecters")
#     if data.password != data.confirm_password:
#         raise Exception("Password Does Not match")
#     if data.role == "admin":
#         is_admin = True

#     hashed_pwd = hash_password(data.password)
#     verification_token = secrets.token_urlsafe(32)

#     user = {
#         "name": data.full_name,
#         "email": data.email,
#         "hashed_password": hashed_pwd,
#         "phone": data.phone,
#         "role": data.role,
#         "email_verified": False,
#         "is_active": True,
#         "verification_token": verification_token,
#         "is_admin": is_admin,
#     }
#     users.insert_one(user)
#     send_verification_email(data.email, verification_token)
#     return {"msg": "User registered successfully"}


# def authenticate_user(email: str, password: str):
#     users = get_user_collection()
#     user = users.find_one({"email": email})
#     if not user or not verify_password(password, user["hashed_password"]):
#         return None

#     token = create_access_token({"sub": str(user["_id"])})
#     return {"access_token": token, "token_type": "bearer"}


# def email_verification(token: str):
#     users = get_user_collection()
#     user = users.find_one({"verification_token": token})

#     if not user:
#         raise Exception({"Invalid or Expired Code"})

#     users.update_one(
#         {"_id": user["_id"]},
#         {"$set": {"email_verified": True}, "$unset": {"verification_token": ""}},
#     )

#     return {"Message": "Email Verified Succesfully"}


# def initiate_password_reset(email: str):
#     users = get_user_collection()
#     user = users.find_one({"email": email})
#     if not user:
#         raise Exception("User Not Found")

#     reset_token = secrets.token_urlsafe(32)
#     expiry = datetime.utcnow() + timedelta(minutes=30)

#     users.update_one(
#         {"_id": user["_id"]},
#         {"$set": {"reset_token": reset_token, "reset_token_expiry": expiry}},
#     )

#     reset_link = f"http://localhost:8000/api/v1/auth/reset-password?token={reset_token}"
#     message = f"Click the link to reset your password: {reset_link}"

#     send_reset_password_email(email, reset_token)

#     return {"msg": "Password reset email sent"}


# def reset_password(data: ResetPasswordRequest):

#     users = get_user_collection()
#     user = users.find_one({"reset_token": data.token})
#     if not user:
#         raise Exception("Invalid or expired token")

#     if datetime.utcnow() > user["reset_token_expiry"]:
#         raise Exception("Token has expired")

#     if data.new_password != data.confirm_password:
#         raise Exception("Password do not match")

#     if len(data.new_password.strip()) < 6:
#         raise Exception("Password should be at least 6 characters")

#     hashed_pwd = hash_password(data.new_password)

#     users.update_one(
#         {"_id": user["_id"]},
#         {
#             "$set": {"hashed_password": hashed_pwd},
#             "$unset": {"reset_token": "", "reset_token_expiry": ""},
#         },
#     )

#     return {"msg": "Password has been reset successfully"}


import secrets
from datetime import datetime, timedelta

from bson import ObjectId

from app.core.security import create_access_token
from app.db.database import get_user_collection
from app.models.user_model import UserModel
from app.schemas.auth_schema import ResetPasswordRequest
from app.utils.email import send_reset_password_email, send_verification_email
from app.utils.password import hash_password, verify_password


async def register_user(data):
    is_admin = False
    users = await get_user_collection()
    if await users.find_one({"email": data.email}):
        raise Exception("User already exists")
    if len(data.password.strip()) < 6:
        raise Exception("Password Should contain at least 6 characters")
    if data.password != data.confirm_password:
        raise Exception("Password Does Not match")
    if data.role == "admin":
        is_admin = True

    hashed_pwd = hash_password(data.password)
    verification_token = secrets.token_urlsafe(32)

    user = {
        "name": data.full_name,
        "email": data.email,
        "hashed_password": hashed_pwd,
        "phone": data.phone,
        "role": data.role,
        "email_verified": False,
        "is_active": True,
        "verification_token": verification_token,
        "is_admin": is_admin,
    }
    await users.insert_one(user)
    send_verification_email(data.email, verification_token)
    return {"msg": "User registered successfully"}


async def authenticate_user(email: str, password: str):
    users = get_user_collection()
    user = await users.find_one({"email": email})
    if not user or not verify_password(password, user["hashed_password"]):
        return None

    token = create_access_token({"sub": str(user["_id"])})
    return {"access_token": token, "token_type": "bearer"}


async def email_verification(token: str):
    users = await get_user_collection()
    user = await users.find_one({"verification_token": token})

    if not user:
        raise Exception({"Invalid or Expired Code"})

    await users.update_one(
        {"_id": user["_id"]},
        {"$set": {"email_verified": True}, "$unset": {"verification_token": ""}},
    )

    return {"Message": "Email Verified Successfully"}


async def initiate_password_reset(email: str):
    users = await get_user_collection()
    user = await users.find_one({"email": email})
    if not user:
        raise Exception("User Not Found")

    reset_token = secrets.token_urlsafe(32)
    expiry = datetime.utcnow() + timedelta(minutes=30)

    await users.update_one(
        {"_id": user["_id"]},
        {"$set": {"reset_token": reset_token, "reset_token_expiry": expiry}},
    )

    reset_link = f"http://localhost:8000/api/v1/auth/reset-password?token={reset_token}"
    message = f"Click the link to reset your password: {reset_link}"

    send_reset_password_email(email, reset_token)

    return {"msg": "Password reset email sent"}


async def reset_password(data: ResetPasswordRequest):
    users = await get_user_collection()
    user = await users.find_one({"reset_token": data.token})
    if not user:
        raise Exception("Invalid or expired token")

    if datetime.utcnow() > user["reset_token_expiry"]:
        raise Exception("Token has expired")

    if data.new_password != data.confirm_password:
        raise Exception("Passwords do not match")

    if len(data.new_password.strip()) < 6:
        raise Exception("Password should be at least 6 characters")

    hashed_pwd = hash_password(data.new_password)

    await users.update_one(
        {"_id": user["_id"]},
        {
            "$set": {"hashed_password": hashed_pwd},
            "$unset": {"reset_token": "", "reset_token_expiry": ""},
        },
    )

    return {"msg": "Password has been reset successfully"}
