
import asyncio
from app.config import Log

async def main():
    Log.info("App is running")
    await asyncio.sleep(1)
    Log.info("App is sleeping")

if __name__ == "__main__":
    asyncio.run(main())