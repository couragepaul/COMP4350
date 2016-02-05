import boto3


class Dynamo:
    # http://boto3.readthedocs.org/en/latest/reference/services/dynamodb.html
    __aws_access_key_id = 'AKIAIGLM2CBBY5EOMXYQ'
    __aws_secret_access_key = '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'
    __message_id = 1000

    def __init__(self):
        boto3.setup_default_session(
            aws_access_key_id = self.__aws_access_key_id,
            aws_secret_access_key = self.__aws_secret_access_key
        )

        self.dynamodb = boto3.resource(
            'dynamodb',
            region_name='us-west-2',
            endpoint_url="https://dynamodb.us-west-2.amazonaws.com"
        )

    def send_message(self, message):
        table = self.dynamodb.Table('Message')
        message['message_id'] = self.__message_id
        self.__message_id += 1
        response = table.put_item(Item=message)
        print(response)

    def get_message_by_recipient(self, recipient):
        table = self.dynamodb.Table('Message')

        response = table.query(recipient=recipient)
        print(response)

    # message_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')
    # sent_by = models.CharField(max_length=50)
    # sent_to = models.CharField(max_length=50)
    # urgency = models.IntegerField()
    # has_read = models.BooleanField()


