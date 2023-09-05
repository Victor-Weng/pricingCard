'''
Instagram bot for the account "influence.ai." This program will call to EdgeGPT (based on Bing AI)
to generate prompts based on the keys in keys.json, generate the caption, hashtags, and new key terms.

Everything needed: 

Posting file: postmain.py
Image generation file: imagen.py
>Caption (and hashtag) generation file: capgen.py
Keyword score tracking file: keys.py

'''
import asyncio
import json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

def get_prompt(FINAL_CAPTION):
    '''
    Returns the prompt that is sent to EdgeGPT
    '''
    cleancap = FINAL_CAPTION.replace("\n", "")
    PROMPT = f"I need you to generate 3 things for me: An instagram caption, a rating from \"1/10\" to \"10/10\", and relevant hashtags for an instagram post\
    I will need these as a response under a specific format that I will give you.\
    1. I need you to change the wording, add a call to action, and expand upon very generally, etc. this provided caption {cleancap}. Make sure to not change it so much that \
    it becomes incorrect or lose it's initial meaning. When making your new caption, keep everything very general and do not make too many extra assumptions. \
    For example, if the caption was \" This is embarrassing 😭 \", throw in a CALL TO ACTION like \what would you do if this happened to you? \"\
    Notice how we made no assumptions about the context behind this while still providing new content. \
    DO NOT end the caption with an emoji, it is absolutely important that you NEVER USE EMOJIS AND NEVER SKIP LINES. \"What's the most amazing fact you know? 🤔\n\n\n\"Here is more information:\" is INCORRECT and should be: \"What's the most amazing fact you know? Here is more information:\".\
    NEVER EVER SKIP A LINE. DO NOT EVER SKIP A LINE IN THE CAPTION, GENERATE IT ALL IN ONE LINE. Remember your caption as GENERATED_CAPTION\
    2. Considering the caption, I want you to estimate a rating from \"1/10\" to \"10/10\" for how relatable the content is with \"1/10\" being not relatable at all and \"10/10\" being extremely relatable. \
    It doesn't have to be very precise, just any guess is ok. However, if the given caption and the tone of the text is very negative, sad, or grieving, I want you to give a rating of \"NA/10\". Rememeber this as GENERATED_RATING. \
    3. Considering the caption, I want you to provide 10 to 15 hashtags relating to the post with hashtags of multiple words being combined without spaces. Ex. #funnymemes #viralmemes. \
    Since the caption you will have is very general, I want you to mostly stick with hashtags that are general and you can't go wrong with such as:\
    #viralmemes #dailyfacts #instagramreels #funnyclips #relatablememes and others. However, you can try to add some unique ones like #embarrassingmoments #embarrassing for the example above. \
    Rememeber this as GENERATED_HASHTAGS. \
    I want you to give your response under this format:\
    \"caption\" : \"GENERATED_CAPTION\", \"rating\" : \"GENERATED_RATING\", \"hashtag\" : \"GENERATED_HASHTAGS\" \
    An example response could be: \
    \"caption\" : \"That was so embarrassing 😬😭 What would you do if this happened to you?\", \"rating\" : \"8/10\", \"hashtag\" : \" #viralmemes #dailyfacts #instagramreels #funnyclips #relatablememes #embarrassingmoments #embarrassing #funnymemes\""

    return PROMPT

async def gen(prmpt):
    '''
    Method to return 
    '''
    cookies = json.loads(open(r"C:\Users\Victo\OneDrive\Desktop\pythonCode\bing_cookies_.json", encoding="utf-8").read())
    bot = await Chatbot.create(cookies=cookies)
    # Passing cookies is "optional", as explained above
    response = await bot.ask(prompt=prmpt,
                       conversation_style=ConversationStyle.creative,
                       simplify_response=True)
    await bot.close()

    cutout = ((response["text"]).split("\""))[0]
    to_send = response["text"].replace(cutout,"")

    return "{" + to_send + "}" #converts string to dictionary

# JSON RETURNS:
#   {
#       "text": str,
#       "author": str,
#       "sources": list[dict],
#       "sources_text": str,
#       "suggestions": list[str],
#       "messages_left": int
#   }

def get_capgen(FINAL_CAPTION):
    '''
    Function to run to return everything in the file
    '''

    results = asyncio.run(gen(get_prompt(FINAL_CAPTION)))
    print(results)
    return results
