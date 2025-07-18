# app/db/sql/db_objects.py

from dataclasses import dataclass
from enum import Enum
from typing import Optional


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
    is_deleted: bool
    created_at: str
    updated_at: str


@dataclass
class Message:
    id: int
    message_uuid: str
    title: str
    content: str
    slug: Optional[str]
    creator_uuid: str
    updated_by: Optional[str]
    is_published: bool
    is_deleted: bool
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
    slug: Optional[str]
    creator_uuid: str
    updated_by: Optional[str]
    description: Optional[str]
    is_deleted: bool
    created_at: str
    updated_at: str


@dataclass
class UserTag:
    id: int
    user_uuid: str
    tag_uuid: str
    created_by: Optional[str]
    notes: Optional[str]
    weight: int
    created_at: str
    updated_at: str


@dataclass
class MessageTag:
    id: int
    message_uuid: str
    tag_uuid: str
    created_by: Optional[str]
    notes: Optional[str]
    weight: int
    created_at: str
    updated_at: str


@dataclass
class Comment:
    id: int
    comment_uuid: str
    content: str
    creator_uuid: str
    updated_by: Optional[str]
    message_uuid: str
    is_deleted: bool
    created_at: str
    updated_at: str


@dataclass
class MessageComment:
    id: int
    message_uuid: str
    comment_uuid: str
    created_at: str
    updated_at: str
