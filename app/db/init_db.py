
# app/db/init_db.py
'''
This is the init_db file
Used to use config to setup the database
Plan 
=> 1. connect to the database and create a single connection
=> 2. setup by creating tables and columns
=> 3. add default data
=> 4. close the connection to allow a db_session to be created
=> 5. provide a db session that allows a lot of operations
=> 6. Have a backwards compatibility for the db_session to be closed if needed
'''
import sqlite3

async def conn_sqlite_db(db_url):
    """
    Used to create a single connection to the database
    """
    pass

async def provide_db_session(conn):
    """
    Used to provide a db session
    For te repos to use
    """
    pass


async def close_db_session(session):
    """
    Used to close the db session
    """
    pass


