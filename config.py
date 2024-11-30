import os
from dotenv import load_dotenv
from datetime import datetime
# Load environment variables
load_dotenv()

# Reddit API accounts
ACCOUNTS = [
    {
        'CLIENT_ID': os.getenv('CLIENT_ID'),
        'SECRET_TOKEN': os.getenv('SECRET_TOKEN'),
        'USERNAME': os.getenv('USERNAME'),
        'PASSWORD': os.getenv('PASSWORD'),
    },
    {
        'CLIENT_ID': os.getenv('CLIENT_ID_2'),
        'SECRET_TOKEN': os.getenv('SECRET_TOKEN_2'),
        'USERNAME': os.getenv('USERNAME_2'),
        'PASSWORD': os.getenv('PASSWORD_2'),
    },
]

# Subreddits and tags
SUBREDDITS = [
    "python", "webdev", "MachineLearning", "datascience", "artificial",
    "programming", "devops", "physics", "math", "science",
    "learnprogramming", "gaming", "pcgaming", "books", "movies",
]
TAGS = ['hot', 
        'top', 
        # 'rising', 
        # 'controversial', 
        # 'new',
        ]
# Parameters
LIMIT = 100  # Posts per request
NUM_ITER = 10  # Iterations per subreddit
RUN_DIR = datetime.now().strftime('run_%Y_%m_%d_%H_%M_%S')
os.makedirs(f'posts/{RUN_DIR}', exist_ok=True)  # Ensure output folder exists
