import uvicorn
from fastapi.logger import logger
async def app(scope, receive, send):
    ...

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, log_level="info")