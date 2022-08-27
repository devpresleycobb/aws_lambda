# verify-jwt

This lambda verifies and returns the contents of the jwt passed in under the Authorization parameter. This expectacton for this lambda is that is will be used after a user makes a request to an apigateway endpoint. This gateway endpoint should have an Authorization header key that has a value of a jwt token. That token comes from aws cognito. We need this function to get the contents of that token so we make sure the person using the gateway can only update their records.

### Stack Name

verify-jwt