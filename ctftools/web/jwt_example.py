import jwt

# 定义密钥
secret_key = '123456'

# 定义 payload
payload = {
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}

# 生成 JWT
encoded_jwt = jwt.encode(payload, secret_key, algorithm='HS256')

print(encoded_jwt)
print(jwt.decode(encoded_jwt, secret_key, algorithms=['HS256']))