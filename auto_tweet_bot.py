import random, time, tweepy, openai


api_key = "your api key"
api_secret = "your api secret key"

access_token = "your access token"
access_secret = "your access secret"

openai.api_key = "your openai api key"

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)

#Replace The Hashtag and Text with your Desired Hashtag and Texts

prompts = [
        {
            "hashtag": " #flutter #flutterframework #appdevelopment",
            "text": "ask a question for #flutterdeveloper"
        },

        {
            "hashtag": " #android #kotlin #bestapps",
            "text": "ask a question for #androiddeveloper"
        },

        {
            "hashtag": " #web #website #webdeveloper ",
            "text": "ask a question for #webdeveloper"
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
final_text = response_text + hashtag
print(final_text)

api = tweepy.API(auth, wait_on_rate_limit=True)

error = 1

while (error == 1):
        try:
            error = 0
            api.update_status(final_text)
        except:
            error = 1


        



