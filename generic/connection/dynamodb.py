import unittest
from generic.connection.session import Session


class DynamoDBConsult(unittest.TestCase):

    def setUp(self):
        self.session = Session()

    def test_get_item_print_response(self):
        """En este ejercicio se ejemplifica cómo realizar una consulta a una tabla de Dynamo, utilizando
        la librería boto3."""
        result = self.session.table.get_item(Key=self.session.key)
        print(result)
        assert result['ResponseMetadata']['HTTPStatusCode'] == 200


class QueryDynamoDB(unittest.TestCase):

    def setUp(self):
        self.session = Session()

    def test_query_dynamoDB(self):
        """En este ejercicio se ejemplifica cómo ejecutar una query con boto3, utilizando client y query"""

        response = self.session.client.query(
            TableName='testUsers',
            KeyConditionExpression='UserId = :UserId',
            ExpressionAttributeValues={':UserId': {'S': '014'}}
        )
        print(response)
        assert response['Count'] == 0
        assert response['ResponseMetadata']['HTTPStatusCode'] == 200