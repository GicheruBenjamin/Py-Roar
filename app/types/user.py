
from datetime import datetime

class User:
    def __init__(self, id:str, username:str, email:str , password:str , is_active:bool , created_at:str, updated_at:str):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.is_active = is_active
        self.created_at = created_at    
        self.updated_at = updated_at