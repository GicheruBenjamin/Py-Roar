
# app/db/sql/migration.py
from .migration_ddl import DDL_STATEMENTS
from pip._internal.network import session

async def migrate(session)->bool:
    """
    Migrate the database using the DDL_STATEMENTS
    """
    pass