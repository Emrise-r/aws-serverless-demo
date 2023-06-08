#!/usr/bin/env python3

import http.server
import urllib.parse
import http.client

import requests
from dotenv import dotenv_values
from urllib.parse import urlparse, parse_qs
from requests.auth import HTTPBasicAuth

properties = dotenv_values()

PORT = int(properties.get('server.port'))
client_id = properties.get('aws.client_id')
client_secret = properties.get('aws.client_secret')
cognito_url = properties.get('aws.cognito_url')
scope = properties.get('aws.auth.scope')


class MyHttpRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        print(path)
        try:
            match path:
                case path if path.startswith('/auth'):
                    self.process_auth()
                case path if path.startswith('/code?'):
                    self.process_exchange()
                case _:
                    print('operator not support')
        except Exception as e:
            print('Exception args: {}'.format(', '.join(e.args)))

    def process_auth(self):
        resource_url = cognito_url + '/login?'
        query_components = parse_qs(urlparse(self.path).query)
        scopes = query_components.get('scope')
        if scopes:
            scope = ' '.join(scopes)
        params = {'client_id': client_id,
                  'response_type': 'code',
                  'scope': scope,
                  'redirect_uri': 'http://localhost:8000/code'}
        uri = resource_url + urllib.parse.urlencode(params)
        print('cognito uri:', uri)
        self.send_response(301)
        self.send_header('Location', uri)
        self.end_headers()

    def process_exchange(self):
        resource_url = cognito_url + '/oauth2/token'
        auth = HTTPBasicAuth(client_id, client_secret)
        query_components = parse_qs(urlparse(self.path).query)
        code = str(query_components.get('code')[0])
        payload = {'grant_type': 'authorization_code',
                   'code': code,
                   'redirect_uri': 'http://localhost:8000/code'}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(resource_url, auth=auth, data=payload, headers=headers, timeout=10)
        print(response)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response.content)


Handler = MyHttpRequestHandler

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
