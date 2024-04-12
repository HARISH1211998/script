from pymongo import MongoClient
import boto3

def test_mongodb_connection(uri, sns_arn):
    try:
        # Attempt to connect to the MongoDB database
        client = MongoClient(uri)
        # Check if the connection was successful by trying to list the database names
        db_names = client.list_database_names()
        # If listing database names was successful, print 'connected'
        print("Connected")
    except Exception as e:
        # If an exception occurred during connection, print 'not connected' along with the error message
        print("Not connected:", e)
        # Send alert via SNS
        sns_client = boto3.client('sns', region_name='ap-southeast-1')  # Specify your region
        sns_client.publish(
            TopicArn=sns_arn,
            Message="MongoDB connection failed: {}".format(str(e))
        )

# Your MongoDB URI
uri = "......"

# SNS ARN for sending alerts
sns_arn = "...."

# Call the function to test the connection
test_mongodb_connection(uri, sns_arn)
