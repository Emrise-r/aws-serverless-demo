# aws-serverless-demo
aws serverless basic

install package using pip or pipenv

with pip
```
pip install -r requirements.txt
```

with pipenv
```
pipenv install
```


server for get access_token

``/source/server``

change .env file

run 
```
python /source/server/simple_auth_server.py
```

open browser type `http://localhost:8000/auth?scope=lambda-app/read lambda-app/write openid`

scope:

```agsl
lambda-app/auth
lambda-app/query
lambda-app/read
lambda-app/write
openid
```
