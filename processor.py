import pandas as pd
from datetime import datetime

def df_from_response(res):
    """
    Converts a Reddit API response into a pandas DataFrame.

    Args:
        res (Response): The response object from a Reddit API request.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted post data or an empty DataFrame
                      in case of an error or unexpected structure.
    """
    try:
        # Parse the JSON from the response
        response_json = res.json()

        # Check if 'data' exists in the response JSON
        if 'data' not in response_json:
            print(f"Unexpected response structure: {response_json}")
            return pd.DataFrame()  # Return an empty DataFrame if structure is invalid
        
        # Initialize a list to store post data
        posts = []

        # Iterate through each post in the 'children' of the response data
        for post in response_json['data'].get('children', []):
            post_data = post['data']
            
            # Extract relevant fields and append them to the posts list
            posts.append({
                'subreddit': post_data.get('subreddit'),
                'title': post_data.get('title'),
                'selftext': post_data.get('selftext'),
                'author': post_data.get('author'),
                'id': post_data.get('id'),
                'permalink': f"https://reddit.com{post_data.get('permalink')}",
                'url': post_data.get('url'),
                'created_utc': datetime.utcfromtimestamp(
                    post_data.get('created_utc')
                ).strftime('%Y-%m-%d %H:%M:%S'),
                'score': post_data.get('score'),
                'upvote_ratio': post_data.get('upvote_ratio'),
                'ups': post_data.get('ups'),
                'downs': post_data.get('downs'),
                'num_comments': post_data.get('num_comments'),
                'total_awards_received': post_data.get('total_awards_received'),
                'gilded': post_data.get('gilded'),
                'is_video': post_data.get('is_video'),
                'is_original_content': post_data.get('is_original_content'),
                'is_self': post_data.get('is_self'),
                'over_18': post_data.get('over_18'),
                'spoiler': post_data.get('spoiler'),
                'link_flair_text': post_data.get('link_flair_text'),
                'thumbnail': post_data.get('thumbnail'),
                'name': post_data.get('name'),  # Required for pagination
            })
        
        # Convert the posts list into a pandas DataFrame
        return pd.DataFrame(posts)

    except Exception as e:
        # Log and return an empty DataFrame in case of errors
        print(f"Error processing response: {e}")
        return pd.DataFrame()
