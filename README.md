# twitter-bot
# Twitter Bot with Gemini AI

This Twitter bot automatically generates and posts tweets using Google's Gemini AI (`gemini-1.5-pro-latest`).

## Features
- Uses `google-generativeai` to generate tweets.
- Posts tweets automatically using `tweepy`.
- Schedules tweets every 30 seconds with `schedule`.
- Loads API credentials from `.env` file.

## Requirements
- Python 3.8+
- Twitter Developer Account
- Google Gemini API access

## Installation
1. Clone the repository:
   ```bash
   https://github.com/vivekchoudhary05/twitter-bot.git
   cd twitter-bot
   ```
2. Create a `.env` file and add your credentials:
   ```ini
   TWITTER_API_KEY=your_api_key
   TWITTER_API_SECRET=your_api_secret
   TWITTER_ACCESS_TOKEN=your_access_token
   TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
   GEMINI_API_KEY=your_gemini_api_key
   ```
3. Requirements
   ```
   dotenv
   tweepy
   schedule
   google-generativeai
   tensorflow```
## Usage
Run the bot using:
```bash
python main.py
```
The bot will generate and post tweets every 30 seconds.

