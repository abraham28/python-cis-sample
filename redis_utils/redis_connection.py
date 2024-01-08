import redis.asyncio as aioredis

redis_connection = None

def get_redis_connection():
    global redis_connection
    if redis_connection is None:
        redis_connection = aioredis.Redis(host='localhost', port=6379, decode_responses=True)
        
    return redis_connection

async def close_redis_connection():
    global redis_connection
    if redis_connection is not None:
        await redis_connection.aclose()
        redis_connection = None
