from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class Role(Enum):
    USER = "user"
    LEADER = "leader"
    ADMIN = "admin"

@dataclass
class User:
    id: int                          # PK auto increment
    user_uuid: str                   # business-level uuid string (optional)
    username: str
    role: Role
    email: str
    password: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

@dataclass
class Message:
    id: int
    message_uuid: str
    title: str
    content: str
    creator_id: int                  # FK → User.id
    is_published: bool
    created_at: datetime
    updated_at: datetime

@dataclass
class UserMessage:
    id: int
    user_id: int                     # FK → User.id
    message_id: int                  # FK → Message.id
    created_at: datetime
    updated_at: datetime

@dataclass
class Tag:
    id: int
    name: str
    creator_id: int                  # FK → User.id
    description: str
    created_at: datetime
    updated_at: datetime

@dataclass
class UserTag:
    id: int
    user_id: int
    tag_id: int
    created_at: datetime

@dataclass
class MessageTag:
    id: int
    message_id: int
    tag_id: int
    created_at: datetime

@dataclass
class Comment:
    id: int
    comment_uuid: str
    content: str
    creator_id: int                  # FK → User.id
    message_id: int                  # FK → Message.id
    created_at: datetime
    updated_at: datetime

@dataclass
class UserComment:
    id: int
    user_id: int
    comment_id: int
    created_at: datetime

@dataclass
class MessageComment:
    id: int
    message_id: int
    comment_id: int
    created_at: datetime
