from fastapi import APIRouter, HTTPException
from redis_utils.redis_connection import get_redis_connection, close_redis_connection

router = APIRouter()


@router.delete("/clients/{client_id}/delete")
async def delete_client(client_id: str):
    # Logic to delete client information by client_id
    # Example: Delete client information from the Redis hash

    redis = get_redis_connection()

    # Check if the user exists
    if not await redis.exists(f"user:{client_id}"):
        raise HTTPException(status_code=404, detail="Client not found")

    # Delete information for the specified user
    await redis.delete(f"user:{client_id}")

    await close_redis_connection()
    return {"message": f"Client with ID {client_id} deleted successfully"}


@router.delete("/clients/delete-all")
async def delete_all_clients():
    redis = get_redis_connection()

    # Get all user keys
    user_keys = await redis.keys("user:*")

    # Delete each user key
    for key in user_keys:
        await redis.delete(key)

    await close_redis_connection()
    return {"message": "All clients deleted successfully"}
