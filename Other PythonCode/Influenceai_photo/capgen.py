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
import keytrack

# Ratio from 0% - 100% that sets how much the EdgeGPT model experiments with new key terms
inno_ratio = 60

def get_prompt(innovation_ratio, keys, last_prompt):
    '''
    Returns the prompt that is sent to EdgeGPT
    '''
    PROMPT = f"TEMPERATURE SETTING: 100. I need you to generate 4 things for me. 1. A one-sentence prompt for AI generative art, 2. unique key terms \
    3. a caption for an instagram post of that art, 4. 10 to 20 relevant, trending, engaging, hashtags. I will need a response under \
    a very specific format and will provide a detailed overview of all the requirements. \
    Part 1: Generate me one-sentence prompt to create a captivating and unique image when input into StableDiffusion. \
    When thinking of a prompt, I advise you to search online and consult resources that describe how to formulate good prompts \
    Furthermore, the order that you will see the upcoming keys \
    DOES NOT MATTER AT ALL, you should look at the WEIGHTS indicated by \" weight \" to understand that the higher weights corresponds to better key terms. \
    Your last prompt was {last_prompt}, make sure your NEW ONE IS DIFFERENT, UNIQUE, AND INNOVATIVE. Remember this as GENERATED_PROMPT\
    Part 2: I want you to create the prompt with a few key terms in mind. When picking these key terms, I want you to reference \
    a provided list of Key Terms and their Weights under the format of \"Key Term\" : \" Weight \" where the higher \
    Weight count means a more successful and benficial Key Term. Remember, you MUST ADD YOUR OWN key terms. Use about {innovation_ratio}% new key words. Key words should be ONE single word. \
    Remember ALL the keys used (old and new) as KEYS_USED with each separated by a comma. Ex. Red, Cat, Astronaut\
    Part 3: Generate an ENGAGING Instagram caption with the first sentence being a CALL TO ACTION. Example caption for \
    an AI generated photo of a cool futuristic house: \" Tag three friends you would stay here with 👀 \" You \
    should add 1 to 2 more sentences below this, DO NOT mention StableDiffusion or AI. Remember this as GENERATED_CAPTION\
    Part 4: Generate 10 to 20 RELEVANT, ENGAGING, and POPULAR hashtags to increase engagement for the given post. \
    HASHTAGS SHOULD NOT BE SEPARATED by dashes, but rather, have no spaces between words. Ex. #conceptart Remember this as GENERATED_HASHTAGS\
    This next part is EXTREMELY IMPORTANT for you to follow PERFECTLY and relates to the formatting of your response to me: \
    When giving your response, you will respond PERFECTLY with the following format by substituting your 4 responses where it applies\
    \"prompt\" : \"GENERATED_PROMPT\", \"key\" : [\"KEYS_USED\"], \"caption\" : \"GENERATED_CAPTION\", \"hashtag\" : \"GENERATED_HASHTAGS\" \
    An example response could be: \
    \"prompt\" : \"Astronaut cat on the moon in the style of DaVinci\", \"key\" : [\"astronaut\", \"cat\", \"moon\", \"davinci\"], \
    \"caption\" : \"What would you do if you saw this at your local pet store? \", \"hashtag\" : \"#illustrations #cat #kitty \
    #catsoninstagram #DaVinci #DaVinciArt #characterdesign #cutecat #cutecats #astronautca\" This example is just for demonstration, the prompt is not very good as it is short and undetailed. \
    KEEP YOUR PROMPT SHORTER THAN 150 CHARACTERS. \
    Here is the list of Key Terms to base your generation upon : {keys}"

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

def get_capgen():
    '''
    Function to run to return everything in the file
    '''

    # Open keys.json
    with open('keys.json', encoding='utf-8') as dt:
        data = json.load(dt)
        keys = str(keytrack.highest_weights(data))

    with open('prompt.json', 'r',encoding='utf-8') as pr:
        prompt_list = json.load(pr)
        last_prompt = prompt_list[0]

    results = asyncio.run(gen(get_prompt(inno_ratio, keys, last_prompt)))

    return results
