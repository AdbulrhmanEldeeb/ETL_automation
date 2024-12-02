import os
import requests
import pandas as pd
from tqdm import tqdm
from processor import df_from_response

def fetch_posts(headers, subreddits, tags, num_iter, limit, run_dir):
    os.makedirs(f'posts/{run_dir}', exist_ok=True)  # Ensure directory exists
    all_dataframes = []  # Collect data for all iterations
    
    for tag in tags:
        for sub in tqdm(subreddits, desc=f"Fetching {tag} posts"):
            print(f"Fetching posts for r/{sub} with tag '{tag}'")
            params = {'limit': limit}
            data = []

            for _ in range(num_iter):
                try:
                    res = requests.get(f"https://oauth.reddit.com/r/{sub}/{tag}",
                                       headers=headers, params=params)
                    if res.status_code != 200:
                        print(f"Request failed for r/{sub}/{tag}: {res.status_code}")
                        break
                    
                    new_df = df_from_response(res)
                    if new_df.empty:
                        print(f"No more data to fetch for r/{sub}/{tag}.")
                        break
                    
                    data.append(new_df)
                    params['after'] = res.json()['data'].get('after')  # Pagination
                    if not params['after']:
                        break
                except Exception as e:
                    print(f"Error during fetching posts: {e}")
                    break

            # Save individual subreddit-tag data
            if data:
                combined_data = pd.concat(data, ignore_index=True)
                output_path = os.path.join('posts', run_dir, f"{sub}_{tag}.csv")
                combined_data.to_csv(output_path, index=False)
                print(f"Saved posts for r/{sub}/{tag} to {output_path}")
                all_dataframes.append(combined_data)

    # Combine all data into a single CSV
    if all_dataframes:
        merged_data = pd.concat(all_dataframes, ignore_index=True)
        merged_path = os.path.join('posts', run_dir, 'merge','merged.csv')
        merged_data.to_csv(merged_path, index=False)
        print(f"Merged CSVs saved to {merged_path}")
    else:
        print("No data collected. Skipping merging step.")
