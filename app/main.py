
import asyncio
from app.config import Log
from app.db import DBS

async def main():
    Log.info(" Server started")
    await asyncio.sleep(1)
    Log.info(" Databases initialized")
    await asyncio.sleep(1)
    Log.debug(f"DBS: {DBS}")
    await asyncio.sleep(1)
    Log.info(" Server stopped")

if __name__ == "__main__":
    asyncio.run(main())