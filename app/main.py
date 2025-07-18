
import asyncio
from app.config import Log, config

async def main():
    Log.info("Hello, world!")
    Log.info(f"Config: {config}")
    await asyncio.sleep(1)
    Log.error("Something went wrong!")
    await asyncio.sleep(1)
    Log.debug("This is a debug message")
    await asyncio.sleep(1)
    Log.warning("This is a warning message")
    await asyncio.sleep(1)
    Log.critical("This is a critical message")
    await asyncio.sleep(1)
    Log.info("This is an info message")
    await asyncio.sleep(1)
    Log.info("This is another info message")
    await asyncio.sleep(1)
    Log.info("This is the last info message")

if __name__ == "__main__":
    asyncio.run(main())