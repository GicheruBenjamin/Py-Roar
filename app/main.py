
from app.config import Log
from app.db import SQLITE_DB_SESSION

async def main():
    Log.info("🚀 Starting app...")
    await SQLITE_DB_SESSION
    Log.info("🚀 App started successfully")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())