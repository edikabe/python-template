"""Input ports module defining the application interfaces."""

from abc import ABC, abstractmethod
from typing import Any


class ProcessDataUseCase(ABC):
    """Interface for processing data use cases."""

    @abstractmethod
    def process_data(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Process the input data.

        Args:
            data: Input data to process

        Returns:
            Processed data
        """
        pass
