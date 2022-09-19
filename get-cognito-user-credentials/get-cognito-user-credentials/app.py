import json
import boto3


def lambda_handler(event, context):
    token = event.get('id_token')
    account_id = event.get('account_id')
    identity_pool_id = event.get('identity_pool_id')
    user_pool_id = event.get('user_pool_id')
    client = boto3.client('cognito-identity')
    identity = client.get_id(
    AccountId=account_id,
    IdentityPoolId=identity_pool_id,
    Logins={
        f'cognito-idp.us-east-1.amazonaws.com/{user_pool_id}': token
    }
    )
    identity_id = identity['IdentityId']
    response = client.get_credentials_for_identity(
    IdentityId=identity_id,
    Logins={
        f'cognito-idp.us-east-1.amazonaws.com/{user_pool_id}': token
    }
    )
    access_key = response['Credentials']['AccessKeyId']
    secret_key = response['Credentials']['SecretKey']
    session_token = response['Credentials']['SessionToken']
    return {
        "statusCode": 200,
        "content-type": "application/json",
        "body": {
            "AccessKeyId": access_key,
            "SecretAccessKey": secret_key,
            "SessionToken": session_token
        }
    }
