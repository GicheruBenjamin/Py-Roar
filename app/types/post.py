

class Post:
    def __init__(self, id:int, title:str, body:str , creator:str , created_at:str, updated_at:str):
        self.id = id
        self.title = title
        self.body = body
        self.creator = creator
        self.created_at = created_at    
        self.updated_at = updated_at