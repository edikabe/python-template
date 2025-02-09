"""DynamoDB repository implementation."""

import boto3
from botocore.exceptions import ClientError

from application.ports.output_port import DataRepository
from domain.models import Data


class DynamoDBRepository(DataRepository):
    """DynamoDB implementation of the data repository."""

    def __init__(self) -> None:
        """Initialize the DynamoDB client."""
        self._dynamodb = boto3.resource("dynamodb")
        self._table = self._dynamodb.Table("data-table")

    def save(self, data: Data) -> None:
        """
        Save data to DynamoDB.

        Args:
            data: Data to save
        """
        try:
            item = {
                "id": data.id,
                "content": data.content,
                "metadata": data.metadata if data.metadata else {},
            }
            self._table.put_item(Item=item)
        except ClientError as e:
            raise Exception(f"Failed to save data: {str(e)}")

    def get(self, id: str) -> Data | None:
        """
        Retrieve data from DynamoDB.

        Args:
            id: ID of the data to retrieve

        Returns:
            Retrieved data or None if not found
        """
        try:
            response = self._table.get_item(Key={"id": id})
            item = response.get("Item")
            if item:
                return Data(
                    id=item["id"],
                    content=item["content"],
                    metadata=item.get("metadata"),
                )
            return None
        except ClientError as e:
            raise Exception(f"Failed to retrieve data: {str(e)}")
