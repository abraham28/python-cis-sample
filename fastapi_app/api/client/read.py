from fastapi import APIRouter, HTTPException
from redis_utils.redis_connection import get_redis_connection, close_redis_connection

router = APIRouter()

@router.get("/clients")
async def read_all_clients(cursor: int, count: int):
    # Logic to retrieve information for all clients
    # Example: Fetch all client information from the Redis hashes
    
    redis = get_redis_connection()
    
    # Retrieve all keys matching the pattern "user:*"
    scannedUsers = await redis.scan(cursor, "user:*", count)
    nextCursor = scannedUsers[0]
    user_keys = scannedUsers[1]

    # Fetch information for each user
    clients = []
    for key in user_keys:
        client_data = await redis.hgetall(key)
        clients.append({ "user_id": key.split(":")[1],"data": client_data})

    await close_redis_connection()
    return {"message": "Read all clients", "nextCursor": nextCursor, "clients": clients}

@router.get("/clients/{client_id}")
async def read_client(client_id: str):
    # Logic to retrieve client information by client_id
    # Example: Fetch client information from the Redis hash
    
    redis = get_redis_connection()
    
    # Check if the user exists
    if not await redis.exists(f"user:{client_id}"):
        raise HTTPException(status_code=404, detail="Client not found")

    # Fetch information for the specified user
    client_data = await redis.hgetall(f"user:{client_id}")
    await close_redis_connection()
    return {"message": f"Read client with ID {client_id}", "data": client_data}
