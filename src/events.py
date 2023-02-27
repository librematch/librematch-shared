"""Events for internal messaging."""

from enum import Enum, auto


class EventBaseEnum(Enum):
    """Defines the AoE2 specific events in our messaging system."""


class Age2Events(EventBaseEnum):
    """Defines the AoE2 specific events in our messaging system."""

    PROFILE_UPDATED = auto()
    MATCH_UPDATED = auto()
    MATCH_FINISHED = auto()
    PLAYER_JOINED_LOBBY = auto()
    NEW_ONGOING_MATCH_DISCOVERED = auto()
