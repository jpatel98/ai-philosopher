from requests_oauthlib import OAuth1Session
import requests
import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="You are AI Socrates. Please write a philosophical tweet as if you're AI Socrates. Please write unique tweets, do not repeat yourself\n\n",
  temperature=0.7,
  max_tokens=250,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

tweet = response.choices[0].text

# Twitter Keys
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

payload = {"text": tweet}

# Make the request to twitter
oauth = OAuth1Session(
    client_key = consumer_key,
    client_secret= consumer_secret,
    resource_owner_key= access_token,
    resource_owner_secret= access_token_secret,
)

# Making the request to tweet
response = oauth.post(
    "https://api.twitter.com/2/tweets",
    json=payload,
)
# throw an error if tweet creation was not success.
if response.status_code != 201:
    raise Exception(
        "Request returned an error: {} {}".format(response.status_code, response.text)
    )
print("Tweet success")