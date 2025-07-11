
from app.config import Log
from app.db import Databases
import asyncio

async def main():
    Log.info("Server started ")
    Log.info("Databases initialized")
    Log.info(f"Databases: {Databases}")so
    Log.info("Server stopped ")

if __name__ == '__main__':
    asyncio.run(main())