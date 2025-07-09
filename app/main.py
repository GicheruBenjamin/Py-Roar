

from app.config import config,Log
from app.utils import Datetimeutils
import asyncio
from datetime import datetime

async def main():
    Log.info("Server started ")
    now = datetime.now()
    Log.info(f"Current time in UTC: {now}")
    Log.info(f"Current time in local: {Datetimeutils.from_datetime_to_human(now)}")
    Log.info("Server stopped ")

if __name__ == '__main__':
    asyncio.run(main())