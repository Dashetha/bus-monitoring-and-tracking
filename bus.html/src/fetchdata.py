import boto3

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# Reference the table
table = dynamodb.Table('DriverDetails')

# Fetch an item using Primary Key
response = table.get_item(Key={'Name': 'Suresh'})

# Print the item
print(response.get('Item'))
