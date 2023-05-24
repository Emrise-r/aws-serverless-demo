import base64
import hashlib
import hmac
import sys

username = sys.argv[1]
client_id = sys.argv[2]
client_secret = sys.argv[3]
message = bytes(username + client_id, 'utf-8')
key = bytes(client_secret, 'utf-8')
secret_hash = base64.b64encode(hmac.new(key, message, digestmod=hashlib.sha256).digest()).decode()

print("SECRET HASH:", secret_hash)
