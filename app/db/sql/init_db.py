# app/db/sql/init_db.py

"""
The plan for initializing a sqlite database.
- Create a a single connection db session using a url.
- Using that connection migrate the db i.e
create tables their columns, keys(primary and foreign), 
indexes , defaults and constraints.
- Use the same connection to seed i default data.
- Close that single connection db session.
- Open a multiple connection db session(100) using a url.
- Have a backward compatibility to close that multiple
connection session.
"""