'''
Instagram bot for the account "dreamhomes.ai." This program will call to the other functions to 
finalize the posting of images.

Everything needed: 

>Posting file: postmain.py
Image generation file: imagen.py
Caption (and hashtag) generation file: capgen.py
Keyword score tracking file: keytrack.py

'''
import os
import json
import ast
from fp.fp import FreeProxy
from PIL import Image
from instagrapi import Client
from collections import OrderedDict # used to keep json files in the same order
import capgen
import imagen
import keytrack

### LOGIN ###

bot = Client()
#proxy = FreeProxy(country_id=['CA'],anonym=True,elite=True,timeout=1.0,https=True).get()
#bot.set_proxy(proxy) # Use a proxy to login
bot.login("dreamhomes.ai", "HowMuchWood7177893!")

### OPEN JSON FILES ###

with open('keys.json', encoding='utf-8') as dt:
    data = json.load(dt, object_pairs_hook=OrderedDict) # list

with open('posts.json', encoding='utf-8') as pt:
    posts = json.load(pt, object_pairs_hook=OrderedDict)

### VARIABLES ###

res = capgen.get_capgen()
results = ast.literal_eval(res)
dump_list = []

CAP = results["caption"]
HASHTAG = results["hashtag"]
PROMPT = results["prompt"]

with open('prompt.json', 'w',encoding='utf-8') as pr:
        dump_list.append(PROMPT)
        json.dump(dump_list, pr, indent=4)

# Caption should be [0000] CAPTION + Follow @dreamhomes.ai for more. \n\n\n\n\n HASHTAGS

IMGLOCATIONS = imagen.generate_image(PROMPT)
# Photo generation number, kept track of in count.txt file.

# Counter currently not working
#GENUM = counternumber.readline()
#counternumber.write(str(int(counternumber.readline()) + 1))
#counternumber.close()
            
#IMGPATH = "C:\\Users\\Victo\\OneDrive\\Desktop\\pythonCode\\dreamhomes.ai\\imgs"

FINALCAP = f"Swipe to see the interior ➡️\n{CAP}\nFollow @dreamhomes.ai for daily fantasy homes 👀 \n \n{HASHTAG}"

### FUNCTIONS ###

def resize_post(photo):
    '''
    Resizes the photo to 1080 x 1080
    '''
    image = Image.open(photo)
    image = image.convert("RGB")
    new_image = image.resize((1080, 1080))
    new_image.save(photo)
def remove_photo(photo):
    '''
    delete the photo after uploading NOT IN USE
    '''
    os.remove(photo)

def upload_post(photo):
    '''
    upload the files 
    '''
    # Resize post to 1080 x 1080

    for image in photo:
        resize_post(image)

    # Upload post
    bot.album_upload(paths=photo,
                     caption=FINALCAP)
    
    for i,image in enumerate(photo):
         os.remove(image)
         print(f"photo{i} has been removed")
    
# Update keys and posts.json files

# Remove the photo
#remove_photo(photo)

# RUN COMMAND
if __name__ == "__main__":
    upload_post(IMGLOCATIONS)
    keytrack.update_weights(data, posts, results, bot)
