import random
import time
import tweepy
import openai

api_key = "XV7Z33nD2nkPzhxntthfbr6If"
api_secret = "Fac1PxsZchfhKwIKEVV7oLHimMPIYP2JUfzSPFqCMhUQ2O8M05"

access_token = "1441576083640360968-gwkyQ7WE7Te2Tg0TapzQEP9iM9IQB0"
access_secret = "trWN2onaxKzQoZZIpqqjab1LNTI4JQl6R2bgokfJ7av4p"

openai.api_key = "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"


auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)

prompts = [
        {
            "hashtag": " #flutter",
            "text": "ask a question for #flutterdeveloper"
        },
    ]

choose_prompt = random.choice(prompts)
text = choose_prompt["text"]
hashtag = choose_prompt["hashtag"]


response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=text,
    max_tokens=64
)
response_text = response.choices[0].text
final_text = response_text+hashtag
print(final_text)



api = tweepy.API(auth, wait_on_rate_limit=True)

error = 1

while(error == 1):
    try:
        error = 0
        api.update_status(final_text)

    except:
        error = 1




