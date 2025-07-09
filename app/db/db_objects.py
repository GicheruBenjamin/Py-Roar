
# app/db/db_objects.py
from dataclasses import dataclass
from enum import Enum

class Role(Enum):
    USER = "user"
    LEADER = "leader"
    ADMIN = "admin"

@dataclass
class User:
    id: int
    user_id: str
    username: str
    role : Role
    email: str
    password: str
    is_active: bool
    created_at: str
    updated_at: str

@dataclass
class Message:
    id: int
    msg_id: str
    title : str
    content: str
    creator_id: str
    created_at: str
    updated_at: str

@dataclass
class Usermessages:
    id: int
    user_id: str
    message_id: str
    created_at: str
    updated_at: str

@dataclass
class Tag:
    id: int
    tagname: str
    creator_id: str
    created_at: str
    updated_at: str

@dataclass
class Usertags:
    id: int
    user_id: str
    tag_id: str
    created_at: str

@dataclass
class Messagetags:
    id: int
    message_id: str
    tag_id: str
    created_at: str

@dataclass
class Comment:
    id: int
    comment_id: str
    content: str
    creator_id: str
    msg_id: str
    created_at: str

@dataclass
class Usercomments:
    id: int
    user_id: str
    comment_id: str
    created_at: str

@dataclass
class Mesaagecomments:
    id: int
    message_id: str
    comment_id: str
    created_at: str

class DTOS(Enum):
    user = user
    message = Message
    usermessages = Usermessages
    tag = Tag
    usertags = Usertags
    messagetags = Messagetags
    comment = Comment
    usercomments = Usercomments
    messagecomments = Mesaagecomments

