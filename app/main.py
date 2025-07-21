
import asyncio
from app.config import Log

async def main():
    Log.info(" Server started")
    await asyncio.sleep(1)
    Log.info(" Server stopped")

if __name__ == "__main__":
    asyncio.run(main())