import boto3
from messaging.message import Message
from boto3.dynamodb.conditions import Key,Attr


class Dynamo:
    # http://boto3.readthedocs.org/en/latest/reference/services/dynamodb.html
    # http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.DynamoDBLocal.html#Tools.DynamoDBLocal.DownloadingAndRunning

    dynamodb = None
    local = False

    @staticmethod
    def initialize():
        # If you don't feel like setting environment variables for boto3 on your machine,
        # you can hard code them here for testing.

        # boto3.setup_default_session(
        # aws_access_key_id = XXXXX,
        # aws_secret_access_key = YYYYY
        # )

        if Dynamo.dynamodb is None:
            try:
                if Dynamo.local:
                    Dynamo.dynamodb = boto3.resource(
                        'dynamodb',
                        endpoint_url='http://localhost:8000' # change if required
                    )
                else :
                    Dynamo.dynamodb = boto3.resource(
                        'dynamodb',
                        region_name='us-west-2',
                        endpoint_url="https://dynamodb.us-west-2.amazonaws.com"
                    )
            except:
                if Dynamo.local:
                    print('DB Connection Error: Unable to connect to local database. Check if database is '
                          'running locally and ensure port number is correct.')
                else:
                    print('DB Connection Error: Unable to connect to AWS Hosted DynamoDB server. Check if access '
                          'credentials are properly configured.')
                raise

        return Dynamo

    @staticmethod
    def send_message(message):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_message')

        response = table.put_item(Item=message)
        print(response)

    @staticmethod
    def get_messages_by_recipient(recipient):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_message')

        response = table.query(KeyConditionExpression=Key('recipient').eq(recipient))
        messages = list()

        for item in response['Items']:
            messages.append(Message(item))

        return messages

    # @staticmethod
    # def get_message(recipient, timestamp):


    @staticmethod
    def send_bulletin(bulletin):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin')

        response = table.put_item(Item=bulletin)
        print(response)

    @staticmethod
    def send_comment(comment):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_comment')

        response = table.put_item(Item=comment)
        print(response)

    @staticmethod
    def get_bulletins():
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin')

        response = table.scan()
        return response['Items']

    @staticmethod
    def get_comments(sender, timestamp):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_comment')

        response = table.scan(FilterExpression=Attr('sender').eq(sender) & Attr('timestamp').eq(timestamp))
        return response['Items']

    @staticmethod
    def update_message(message):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_message')
        response = table.update_item(Item=message)
        print(response)


