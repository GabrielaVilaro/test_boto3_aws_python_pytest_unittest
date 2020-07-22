import unittest

import boto3


class DynamoDBConsult(unittest.TestCase):

    def setUp(self):
        self.session = boto3.Session(profile_name="uala-mex-debit-test", region_name="us-east-1")
        self.resource = self.session.resource('dynamodb')
        self.table = self.resource.Table('testUsers')
        self.key = {'UserId': '014'}

    def test_get_item_print_response(self):
        result = self.table.get_item(Key={'UserId': '014'})
        print(result)


class QueryDynamoDB(unittest.TestCase):

    def setUp(self):
        self.session = boto3.Session(profile_name="uala-arg-prepaid-prod", region_name="us-east-1")
        self.client = self.session.client('dynamodb')

    def test_query_dynamoDB(self):
        response = self.client.query(
            TableName='testUsers',
            KeyConditionExpression='UserId = :UserId',
            ExpressionAttributeValues={':UserId': {'S': '014'}}
        )

        print(response)
