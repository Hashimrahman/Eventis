from app.db.database import get_user_collection

async def get_all_users():
    user_collection = get_user_collection()
    cursor = user_collection.find({})
    users = []
    async for user in cursor:
        user["id"] = str(user["_id"])
        user["full_name"] = user.pop("name")
        user.pop("_id", None)
        user.pop("reset_token", None)
        user.pop("reset_token_expiry", None)
        user.pop("verification_token", None)
        users.append(user)
    
    return users