from fastapi import APIRouter, HTTPException
from redis_utils.redis_connection import get_redis_connection, close_redis_connection
import uuid
from .models import ClientData
import json

router = APIRouter()


@router.post("/clients/create")
async def create_client(client_data: ClientData):

    redis = get_redis_connection()

    # Generate a UUID for the new user
    user_id = str(uuid.uuid4())

    # Convert favorite_colors to a JSON string
    client_data.favorite_colors = json.dumps(client_data.favorite_colors)

    # Create a hash with the user information
    hash_key = f"user:{user_id}"
    await redis.hmset(hash_key, client_data.model_dump())

    # Convert favorite_colors back to a list for response
    client_data.favorite_colors = json.loads(client_data.favorite_colors)

    await close_redis_connection()
    return {"message": "Client created successfully", "user_id": user_id, "data": client_data.model_dump()}
