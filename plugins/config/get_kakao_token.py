import requests

client_id = '69187781ebb1debfc8cc3cc8fb485d77'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'CM6YJPrzzQuHA1zUoFQWLwENm-QI5UGZEPXRRC_WW-m5lCT6Ee2oqAAAAAQKFxTuAAABljwnnfFSGUcvaFb1Eg'

token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type' : 'authorization_code',
    'client_id' : client_id,
    'redirect_uri' : redirect_uri,
    'code' : authorize_code
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)