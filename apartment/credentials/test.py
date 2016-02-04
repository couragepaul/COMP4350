import boto3

aws_access_key_id = "AKIAIGLM2CBBY5EOMXYQ"
aws_secret_access_key = "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"

session = boto3.setup_default_session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="https://dynamodb.us-west-2.amazonaws.com")

table = dynamodb.Table("Message")

# Above is setup to communicate with DB, will refactor.

message_id = 1000
timestamp = 100000

# http://boto3.readthedocs.org/en/latest/reference/services/dynamodb.html #

response = table.put_item(Item={
    'message_id': message_id,
    'timestamp': timestamp,
    'content': "testData"
})

    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sent_by = models.CharField(max_length=50)
    sent_to = models.CharField(max_length=50)
    urgency = models.IntegerField()
    has_read = models.BooleanField()

print(response)
