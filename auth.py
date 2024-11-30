import requests

def authenticate(account):
    try:
        client_auth = requests.auth.HTTPBasicAuth(account['CLIENT_ID'], account['SECRET_TOKEN'])
        auth_data = {'grant_type': 'password', 'username': account['USERNAME'], 'password': account['PASSWORD']}
        headers = {'User-Agent': 'myBot/0.0.1'}
        auth_res = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=auth_data, headers=headers)

        if auth_res.status_code == 200:
            token = f"bearer {auth_res.json().get('access_token')}"
            headers['Authorization'] = token
            return headers
        else:
            raise Exception(f"Authentication failed! Status: {auth_res.status_code}, Message: {auth_res.text}")
    except Exception as e:
        print(f"Authentication error: {e}")
        return None
