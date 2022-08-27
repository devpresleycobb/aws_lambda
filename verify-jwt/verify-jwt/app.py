import jwt

def lambda_handler(event, context):

    if event['Authorization']:
        return jwt.decode(event['Authorization'], options={"verify_signature": False})
        
