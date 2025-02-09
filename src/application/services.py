"""Application services implementing the use cases."""

from typing import Any

from application.ports.input_port import ProcessDataUseCase
from application.ports.output_port import DataRepository
from domain.models import Data


class DataProcessor(ProcessDataUseCase):
    """Service for processing data."""

    def __init__(self, repository: DataRepository) -> None:
        """
        Initialize the service.

        Args:
            repository: Repository for data persistence
        """
        self._repository = repository

    def process_data(self, data: dict[str, Any]) -> dict[str, Any]:
        """
        Process the input data and store it.

        Args:
            data: Input data to process

        Returns:
            Processed data
        """
        processed_data = Data(
            id=data.get("id", ""),
            content=data.get("content", ""),
            metadata=data.get("metadata"),
        )

        self._repository.save(processed_data)
        return {"message": "Data processed successfully", "id": processed_data.id}
