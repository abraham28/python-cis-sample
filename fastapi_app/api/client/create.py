from fastapi import APIRouter
from pydantic import BaseModel
from redis_utils.redis_connection import get_redis_connection, close_redis_connection
import uuid

router = APIRouter()


class ClientData(BaseModel):
    first_name: str
    last_name: str
    address: str
    contact_number: str



@router.post("/clients/create")
async def create_client(client_data: ClientData):
    # Logic to create a new client
    # Example: Save client_data to the Redis hash

    redis = get_redis_connection()
    
    # Generate a UUID for the new user
    user_id = str(uuid.uuid4())

    # Create a hash with the user information
    hash_key = f"user:{user_id}"
    await redis.hmset(hash_key, client_data.model_dump())

    await close_redis_connection()
    return {"message": "Client created successfully", "user_id": user_id, "data": client_data.model_dump()}
