import boto3
from messaging.message import Message
from bulletin.bulletin import Bulletin
from bulletin.comment import Comment
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

    @staticmethod
    def send_bulletin(bulletin):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin')

        response = table.put_item(Item=bulletin)
        return response

    @staticmethod
    def send_comment(comment):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin_comment')

        response = table.put_item(Item=comment)
        return response

    @staticmethod
    def get_bulletin_by_reference(reference):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin')

        split_ref = reference.split(':')
        response = table.get_item(Key={'sender': split_ref[0], 'timestamp': int(split_ref[1])})

        bulletin = Bulletin(response['Item'])
        return bulletin

    @staticmethod
    def get_bulletins():
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin')

        response = table.scan()
        bulletins = list()

        for item in response['Items']:
            bulletins.append(Bulletin(item))

        return bulletins

    @staticmethod
    def get_comments(bulletin):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_bulletin_comment')

        response = table.query(KeyConditionExpression=Key('bulletin_reference').eq(bulletin.get_reference()))
        comments = list()

        for item in response['Items']:
            comments.append(Comment(item))

        return comments

    @staticmethod
    def get_message(message):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_message')

        response = table.get_item(Key={'recipient': message['recipient'], 'timestamp': message['timestamp']})
        return Message(response['Item'])

    @staticmethod
    def update_message(message):
        Dynamo.initialize()
        table = Dynamo.dynamodb.Table('se2_message')

        response = table.update_item(Key={'recipient': message.recipient, 'timestamp': message.timestamp})
        print(response)


