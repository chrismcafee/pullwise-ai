from abc import ABC, abstractmethod
from typing import Any

from pullwise.config.settings import Settings

class BaseAdapterFactory(ABC):
    """
    Base class for all adapter factories.
    Subclasses must implement from_settings() or from_env().
    """

    @classmethod
    @abstractmethod
    def from_settings(cls, settings: Settings) -> Any:
        """Create adapter instance using app settings (e.g. loaded config)."""
        raise NotImplementedError

    @classmethod
    def from_env(cls) -> Any:
        """Fallback method to construct adapter from environment variables."""
        raise NotImplementedError
