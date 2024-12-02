import requests

def authenticate(account):
    """
    Authenticate with the Reddit API and obtain an access token.

    Args:
        account (dict): A dictionary containing the Reddit account credentials:
                        - CLIENT_ID: The client ID for the app.
                        - SECRET_TOKEN: The secret token for the app.
                        - USERNAME: The Reddit username.
                        - PASSWORD: The Reddit account password.

    Returns:
        dict: A headers dictionary containing the 'Authorization' token and 'User-Agent' 
              for making authenticated API requests if successful.
        None: If authentication fails.

    Raises:
        Exception: If the authentication request fails or returns a non-200 status code.
    """
    try:
        # Prepare the HTTP basic authentication using the client ID and secret token
        client_auth = requests.auth.HTTPBasicAuth(account['CLIENT_ID'], account['SECRET_TOKEN'])
        
        # Prepare the authentication data
        auth_data = {
            'grant_type': 'password',  # OAuth2 grant type for password-based authentication
            'username': account['USERNAME'],  # Reddit username
            'password': account['PASSWORD']   # Reddit password
        }
        
        # Set headers with a user-agent for the API request
        headers = {'User-Agent': 'myBot/0.0.1'}
        
        # Send POST request to the Reddit API access token endpoint
        auth_res = requests.post('https://www.reddit.com/api/v1/access_token', 
                                 auth=client_auth, data=auth_data, headers=headers)
        
        # Check if the authentication request was successful
        if auth_res.status_code == 200:
            # Extract the access token and update headers with the Authorization token
            token = f"bearer {auth_res.json().get('access_token')}"
            headers['Authorization'] = token
            return headers
        else:
            # Raise an exception if the authentication failed
            raise Exception(f"Authentication failed! Status: {auth_res.status_code}, Message: {auth_res.text}")
    
    except Exception as e:
        # Log and return None if an error occurs during authentication
        print(f"Authentication error: {e}")
        return None
