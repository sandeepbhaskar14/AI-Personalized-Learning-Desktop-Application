import jwt
import datetime

# Sample payload (user information)
payload = {
    'user_id': '123',
    'username': 'john_doe',
    'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)  # Token expiration time
}

# Secret key for signing and verification
secret_key = '1234'  # Replace with your actual secret key

# Encode the JWT
encoded_token = jwt.encode(payload, secret_key, algorithm='HS256')

print(encoded_token)