import requests
import pandas as pd
from tqdm import tqdm
from processor import df_from_response

def fetch_posts(headers, subreddits, tags, num_iter, limit, run_dir):
    for tag in tags:
        for sub in tqdm(subreddits):
            print(f"Fetching posts for r/{sub} with tag '{tag}'")
            params = {'limit': limit}
            data = pd.DataFrame()
            for _ in range(num_iter):
                res = requests.get(f"https://oauth.reddit.com/r/{sub}/{tag}",
                                   headers=headers, params=params)
                if res.status_code != 200:
                    print(f"Request failed for r/{sub}/{tag}: {res.status_code}")
                    raise Exception("Switching account due to request failure.")
                
                new_df = df_from_response(res)
                if new_df.empty:
                    print(f"No more data to fetch for r/{sub}/{tag}.")
                    break

                data = pd.concat([data, new_df], ignore_index=True)
                params['after'] = res.json()['data'].get('after')  # Pagination
                if not params['after']:
                    break

            # Save to CSV
            output_path = f'posts/{run_dir}/{sub}_{tag}.csv'
            data.to_csv(output_path, index=False)
            print(f"Saved posts for r/{sub}/{tag} to {output_path}")
