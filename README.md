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

open browser type `http://localhost:8000/auth?scope=https://407zzg11c6.execute-api.us-east-1.amazonaws.com/default/query lambda-app/read`

scope:

long scope

```agsl
https://407zzg11c6.execute-api.us-east-1.amazonaws.com/default/auth
https://407zzg11c6.execute-api.us-east-1.amazonaws.com/default/query
https://407zzg11c6.execute-api.us-east-1.amazonaws.com/default/read
https://407zzg11c6.execute-api.us-east-1.amazonaws.com/default/write
```

short scope

```agsl
lambda-app/auth
lambda-app/query
lambda-app/read
lambda-app/write
```
