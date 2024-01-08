from fastapi import APIRouter, HTTPException
from redis_utils.redis_connection import get_redis_connection, close_redis_connection
from .create import ClientData

router = APIRouter()

@router.put("/clients/{client_id}/update")
async def update_client(client_id: str, updated_data: ClientData):
    # Logic to update client information by client_id
    # Example: Update client information in the Redis hash

    redis = get_redis_connection()

    # Check if the user exists
    if not await redis.exists(f"user:{client_id}"):
        raise HTTPException(status_code=404, detail="Client not found")

    # Update information for the specified user
    hash_key = f"user:{client_id}"
    await redis.hmset(hash_key, updated_data.model_dump())

    await close_redis_connection()
    return {"message": f"Client with ID {client_id} updated successfully", "data": updated_data.model_dump()}
