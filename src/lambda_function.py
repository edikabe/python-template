"""Main Lambda handler module."""

from typing import Any

from application.services import DataProcessor
from infrastructure.repositories.dumb_repo import DumbRepo

repository = DumbRepo()
processor = DataProcessor(repository)


def handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    """
    Lambda handler function.

    Args:
        event: AWS Lambda event
        context: AWS Lambda context

    Returns:
        Dict containing the response
    """

    try:
        result = processor.process_data(event)
        return {"statusCode": 200, "body": result}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
