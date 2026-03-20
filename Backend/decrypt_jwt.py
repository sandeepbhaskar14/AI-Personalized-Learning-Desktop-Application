import jwt
import datetime

# Sample encoded JWT (from the previous example)
encoded_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMTIzIiwidXNlcm5hbWUiOiJqb2huX2RvZSIsImV4cCI6MTc0NjQzNTE0Mn0.jvz4SVEKQnih1N6Bn3MEer5mE95SO3FrutMIYulGUtk'  # Replace with your actual token

# Secret key for signing and verification
secret_key = '1234'  # Replace with your actual secret key

try:
    # Decode the JWT and verify the signature
    decoded_payload = jwt.decode(encoded_token, secret_key, algorithms=['HS256'])
    print(decoded_payload)  # Print the decoded payload
except jwt.ExpiredSignatureError:
    print("Token has expired")
except jwt.InvalidTokenError:
    print("Invalid token")