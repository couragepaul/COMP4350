import boto3
import time
from boto3.dynamodb.conditions import Key,Attr

class Dynamo:
    # http://boto3.readthedocs.org/en/latest/reference/services/dynamodb.html
    # http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html#Tools.DynamoDBLocal.DownloadingAndRunning

    def __init__(self, stub=False):
        # If you don't feel like setting environment variables for boto3 on your machine,
        # you can hard code them here for testing.

        # boto3.setup_default_session(
        # aws_access_key_id = XXXXX,
        # aws_secret_access_key = YYYYY
        # )

        try:
            if stub:
                self.dynamodb = boto3.resource(
                    'dynamodb',
                    endpoint_url='http://localhost:8000' # change if required
                )
            else :
                self.dynamodb = boto3.resource(
                    'dynamodb',
                    region_name='us-west-2',
                    endpoint_url="https://dynamodb.us-west-2.amazonaws.com"
                )
        except:
            if stub:
                print('DB Connection Error: Unable to connect to local database. Check if database is running locally '
                      'and ensure port number is correct.')
            else:
                print('DB Connection Error: Unable to connect to AWS Hosted DynamoDB server. Check if access '
                      'credentials are properly configured.')
            raise

    def send_message(self, message):
        table = self.dynamodb.Table('se2_message')

        response = table.put_item(Item=message)
        print(response)

    def get_message_by_recipient(self, recipient):
        table = self.dynamodb.Table('se2_message')

        response = table.query(KeyConditionExpression=Key('recipient').eq(recipient))
        return response['Items']

    def get_message_by_id(self, message_id):
        table = self.dynamodb.Table('se2_message')
        msgID = int(message_id)

        response = table.scan(FilterExpression=Attr('message_id').eq(msgID))

        print(response['Items'])
        return response['Items']

    def update_message(self, message):
        table = self.dynamodb.Table('se2_message')
        response = table.put_item(Item=message)
        print(response)

    # message_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # sent_by = models.CharField(max_length=50)
    # sent_to = models.CharField(max_length=50)
    # urgency = models.IntegerField()
    # has_read = models.BooleanField()


