#!/bin/bash

# URL to check
URL="....."

# Send SNS notification function
send_notification() {
    # AWS region
    REGION="ap-southeast-1"
    # AWS SNS topic ARN
    TOPIC_ARN="........"
    # SNS message
    MESSAGE="URL $URL returned status code $1"
    
    # Publish message to SNS topic
    aws sns publish --region $REGION --topic-arn $TOPIC_ARN --message "$MESSAGE"
}

# Check URL status
HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

# Check if status code is not equal to 200
if [ $HTTP_STATUS -ne 200 ]; then
    echo "URL $URL returned status code $HTTP_STATUS. Sending notification..."
    send_notification $HTTP_STATUS
else
    echo "URL $URL is reachable with status code 200."
fi
