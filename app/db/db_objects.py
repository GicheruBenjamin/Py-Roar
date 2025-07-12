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
    user_uuid: str
    username: str
    role: Role
    email: str
    password: str
    is_active: bool
    created_at: str
    updated_at: str

@dataclass
class Message:
    id: int
    message_uuid: str
    title: str
    content: str
    creator_uuid: str
    is_published: bool
    created_at: str
    updated_at: str

@dataclass
class UserMessage:
    id: int
    user_uuid: str
    message_uuid: str
    created_at: str
    updated_at: str

@dataclass
class Tag:
    id: int
    tag_uuid: str
    name: str
    creator_uuid: str
    description: str
    created_at: str
    updated_at: str

@dataclass
class UserTag:
    id: int
    user_uuid: str
    tag_uuid: str
    created_at: str
    updated_at: str

@dataclass
class MessageTag:
    id: int
    message_uuid: str
    tag_uuid: str
    created_at: str
    updated_at: str

@dataclass
class Comment:
    id: int
    comment_uuid: str
    content: str
    creator_uuid: str
    message_uuid: str
    created_at: str
    updated_at: str

@dataclass
class MessageComment:
    id: int
    message_uuid: str
    comment_uuid: str
    created_at: str
    updated_at: str
