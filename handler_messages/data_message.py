import enum
from dataclasses import dataclass, field
from typing import Any


class MessageType(enum.Enum):
    TELEGRAM = enum.auto()
    MATTERMOST = enum.auto()
    SLACK = enum.auto()


@dataclass
class JsonMessage:
    message_type: MessageType
    payload: dict[str, Any]


@dataclass
class ParsedMessage:
    """There is no need to describe anything here."""

    source: MessageType
    data: dict[str, Any] = field(default_factory=dict)
