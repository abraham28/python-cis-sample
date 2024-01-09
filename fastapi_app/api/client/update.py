from fastapi import APIRouter, HTTPException
from redis_utils.redis_connection import get_redis_connection, close_redis_connection
from .models import ClientData
import json

router = APIRouter()


@router.put("/clients/{client_id}/update")
async def update_client(client_id: str, updated_data: ClientData):
    redis = get_redis_connection()

    # Check if the user exists
    if not await redis.exists(f"user:{client_id}"):
        raise HTTPException(status_code=404, detail="Client not found")

    # Convert favorite_colors to a JSON string
    updated_data.favorite_colors = json.dumps(updated_data.favorite_colors)

    # Update information for the specified user
    hash_key = f"user:{client_id}"
    await redis.hmset(hash_key, updated_data.model_dump())

    # Convert favorite_colors back to a list for response
    updated_data.favorite_colors = json.loads(updated_data.favorite_colors)

    await close_redis_connection()
    return {"message": f"Client with ID {client_id} updated successfully", "data": updated_data.model_dump()}
