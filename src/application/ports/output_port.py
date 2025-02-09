"""Output ports module defining the repository interfaces."""

from abc import ABC, abstractmethod

from domain.models import Data


class DataRepository(ABC):
    """Interface for data persistence."""

    @abstractmethod
    def save(self, data: Data) -> None:
        """
        Save data to the repository.

        Args:
            data: Data to save
        """
        pass

    @abstractmethod
    def get(self, id: str) -> Data | None:
        """
        Retrieve data from the repository.

        Args:
            id: ID of the data to retrieve

        Returns:
            Retrieved data or None if not found
        """
        pass
