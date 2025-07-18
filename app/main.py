
import asyncio
from app.config import Log
from app.db import DBS

async def main():
    Log.info(" Server started")
    await asyncio.sleep(1)
    Log.info(f"DBS: {DBS}")
    Log.info(" Server stopped")

if __name__ == "__main__":
    asyncio.run(main())