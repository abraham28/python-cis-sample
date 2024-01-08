from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.client import router as client_router

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    # Adjust as needed for your application's security requirements
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(client_router, tags=["client"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
