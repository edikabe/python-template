"""Tests for the DataProcessor service."""

from typing import Any

from application.services import DataProcessor


def test_process_data(mock_repository: Any) -> None:
    """Test data processing."""
    processor = DataProcessor(mock_repository)

    input_data: dict[str, Any] = {
        "id": "test-id",
        "content": "test content",
        "metadata": {"key": "value"},
    }

    result = processor.process_data(input_data)

    assert result["id"] == "test-id"
    assert result["message"] == "Data processed successfully"

    stored_data = mock_repository.get("test-id")
    assert stored_data is not None
    assert stored_data.id == "test-id"
    assert stored_data.content == "test content"
    assert stored_data.metadata == {"key": "value"}
