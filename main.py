import tweepy
import os
import schedule
import time
import random
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "YourKey")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "YourKey")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "YourKey")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET", "YourKey")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "YourKey")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "YourGeminiKey")

# Initialize Tweepy client
client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True
)

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate tweets using Gemini
def generate_tweet():
    # Taking 4 sample prompts for demo purpose , this can be scaled depending on the use-case
    prompts = [
        "Write a creative and engaging tweet about the latest trends in technology. Keep it under 50-280 characters.",
        "Compose a casual tweet about the importance of holidays. Keep it under 50-280 characters.",
        "Write a humorous tweet on modern AI uses. Keep it under 50-280 characters.",
        "Generate a thoughtful tweet on stress management. Keep it under 50-280 characters."
    ]
    prompt = random.choice(prompts)
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    tweet = response.text.strip()
    
    return tweet[:280]  # Enforce Twitter's 280 character limit

# Function to post tweets
def post_tweet():
    tweet_text = generate_tweet()
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Tweet posted: {tweet_text}")
    except Exception as e:
        print(f"Error posting tweet: {e}")

# Schedule the tweet posting every 30 secs just for demo
schedule.every(30).seconds.do(post_tweet)

print("Tweet bot started. Posting a tweet every 30 seconds for demo ...")

while True:
    schedule.run_pending()
    time.sleep(1)
