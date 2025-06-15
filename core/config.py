"""Provides game config utilities."""

from dataclasses import dataclass, field
import json
from typing import Any

from core.npk.class_types import NPKReadOptions

@dataclass
class Config:
    """Represents a game config."""

    name: str = "Default"
    read_options: NPKReadOptions | None = None
    entry_signature_name_map: dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        """Post-initialization to ensure read_options is initialized."""
        if isinstance(self.read_options, dict):
            # Convert dict to NPKReadOptions if it is a dictionary
            self.read_options = NPKReadOptions(**self.read_options)

    @staticmethod
    def from_file(path: str) -> 'Config':
        """Creates a config from file."""
        with open(path, "r", encoding="utf-8") as config_file:
            data: dict[str, Any] = json.load(config_file)
            return Config(**data)
