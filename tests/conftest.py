"""Test configuration and fixtures."""

from collections.abc import Generator

import pytest

from application.ports.output_port import DataRepository
from domain.models import Data


class MockRepository(DataRepository):
    """Mock repository for testing."""

    def __init__(self) -> None:
        """Initialize the mock repository."""
        self.data = {}

    def save(self, data: Data) -> None:
        """Mock save operation."""
        self.data[data.id] = data

    def get(self, id: str) -> Data:
        """Mock get operation."""
        return self.data.get(id)


@pytest.fixture
def mock_repository() -> Generator[MockRepository]:
    """Provide a mock repository for tests."""
    yield MockRepository()
