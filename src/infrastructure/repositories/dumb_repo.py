from application.ports.output_port import DataRepository
from domain.models import Data


class DumbRepo(DataRepository):
    """Dumb repository implementation."""

    def __init__(self) -> None:
        """Initialize the Dumb repository."""
        self.data = {}

    def save(self, data: Data) -> None:
        """Save data to the Dumb repository."""
        self.data[data.id] = data

    def get(self, id: str) -> Data | None:
        """Retrieve data from the Dumb repository."""
        return self.data.get(id)
