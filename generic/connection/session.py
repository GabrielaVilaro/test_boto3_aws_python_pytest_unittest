import boto3


class Session:
    def __init__(self):
        self.session = boto3.Session(profile_name="mex-debit-test", region_name="us-east-1")
        self.resource = self.session.resource('dynamodb')
        self.client = self.session.client('dynamodb')
        self.table = self.resource.Table('testUsers')
        self.key = {'UserId': '014'}

        self.TableName = 'testUsers',
        self.KeyConditionExpression = 'UserId = :UserId',
        self.ExpressionAttributeValues = {':UserId': {'S': '014'}}
