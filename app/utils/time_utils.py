import datetime
from dataclasses import dataclass
from typing import Union

@dataclass
class Datetimeutils:
    """
    Utility class to convert datetime objects to/from different string formats,
    timestamps, and human-readable strings.
    """

    DEFAULT_FORMAT: str = "%Y-%m-%d %H:%M:%S"        # e.g., 2025-07-09 17:30:00
    HUMAN_FORMAT: str = "%d %b %Y %H:%M"             # e.g., 09 Jul 2025 17:30

    @staticmethod
    def from_datetime_to_str(dt: datetime.datetime) -> str:
        """Parse datetime to string using DEFAULT_FORMAT"""
        return dt.strftime(Datetimeutils.DEFAULT_FORMAT)

    @staticmethod
    def from_str_to_datetime(dt: str) -> datetime.datetime:
        """Parse string (DEFAULT_FORMAT) to datetime"""
        return datetime.datetime.strptime(dt, Datetimeutils.DEFAULT_FORMAT)

    @staticmethod
    def from_datetime_to_iso(dt: datetime.datetime) -> str:
        """Parse datetime to ISO 8601 string"""
        return dt.isoformat()

    @staticmethod
    def from_iso_to_datetime(dt: str) -> datetime.datetime:
        """Parse ISO 8601 string to datetime"""
        return datetime.datetime.fromisoformat(dt)

    @staticmethod
    def from_datetime_to_timestamp(dt: datetime.datetime) -> int:
        """Parse datetime to Unix timestamp (seconds since epoch)"""
        return int(dt.timestamp())

    @staticmethod
    def from_timestamp_to_datetime(ts: Union[int, float]) -> datetime.datetime:
        """Parse Unix timestamp to datetime"""
        return datetime.datetime.fromtimestamp(ts)

    @staticmethod
    def from_datetime_to_human(dt: datetime.datetime) -> str:
        """Parse datetime to human-readable string"""
        return dt.strftime(Datetimeutils.HUMAN_FORMAT)

    @staticmethod
    def from_human_to_datetime(dt: str) -> datetime.datetime:
        """Parse human-readable string to datetime"""
        return datetime.datetime.strptime(dt, Datetimeutils.HUMAN_FORMAT)
