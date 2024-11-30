from config import ACCOUNTS, SUBREDDITS, TAGS, LIMIT, NUM_ITER, RUN_DIR
from auth import authenticate
from fetcher import fetch_posts

if __name__ == "__main__":
    current_account_index = 0
    while current_account_index < len(ACCOUNTS):
        headers = authenticate(ACCOUNTS[current_account_index])
        if headers:
            try:
                fetch_posts(headers, SUBREDDITS, TAGS, NUM_ITER, LIMIT, RUN_DIR)
                break  # Exit loop if fetch_posts completes successfully
            except Exception as e:
                print(f"Error during fetching: {e}")
                current_account_index += 1  # Switch to the next account
        else:
            current_account_index += 1  # Switch to the next account

    if current_account_index == len(ACCOUNTS):
        print("All accounts failed.")
