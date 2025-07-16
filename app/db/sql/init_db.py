
# app/db/sql/init_db.py

"""
This file is used to initialize the database
1. Create a db session/pool size= 1
2. Migrate the database i.e create tables their columns and indexes
3. Add default data
4. Close that session/pool
5. Create a new session/pool size= 100 for the app to use
"""

async def init_db(db_url: str)->bool:
    pass