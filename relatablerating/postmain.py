'''
Instagram bot for the account "relatablerating" This program will call to the other functions to 
finalize the posting of images.

Everything needed: 

>Posting file: postmain.py
Image generation file: imagen.py
Caption (and hashtag) generation file: capgen.py
Keyword score tracking file: keytrack.py

'''
import os
import json
from fp.fp import FreeProxy
from PIL import Image
from instagrapi import Client
from collections import OrderedDict # used to keep json files in the same order
import capgen
import ast

### LOGIN ###

bot = Client()
#proxy = FreeProxy(country_id=['CA'],anonym=True,elite=True,timeout=1.0,https=True).get()
#bot.set_proxy(proxy) # Use a proxy to login

### OPEN JSON FILES ###

with open('posts.json', "r", encoding='utf-8') as pt:
    posts = json.load(pt)

def uniquify(path):
    '''
    function to prevent images being overrided with new generated images (WILL COMMENT OUT TO SAVE STORAGE LATER)
    '''
    filename, extension = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = filename + '(' + str(counter) + ')' + extension
        counter += 1

    return path

# If album, don't download the last one
# save media id to json

post_list = []
post_options = {} # dict of post options
values = [] # temp value holder to sort by highest value
album_paths = [] # value used for album uploads
media_upload_type = "" # value set by download_photos() used by upload_photos() to figure out which upload method to use
FINAL_CAPTION = ""

def update_json_posts(new_post):
    global posts
    posts.append(new_post)
    if len(posts) < 50: # if the amount of posts stored in posts.json is smaller than 50
        pass
    else: 
        print("post length greater than 50")
        del posts[0] # delete oldest (first) post

    with open('posts.json', "w", encoding='utf-8') as pt:
        print("dumping into posts.json")
        #print(posts)
        json.dump(posts, pt, indent=4)


def download_photos():

    # Define global variables
    global post_list, post_options, values, album_paths, media_upload_type, FINAL_CAPTION, posts
    bot.login("relatablerating", "HowMuchWood7177893!")
    postlist = bot.user_medias_gql(user_id = "290694015", amount = 50) # taken from factsdailyy
    SAVE_PATH = r"c:/Users/Victo/OneDrive/Desktop/pythonCode/relatablerating/imgs"

    for media in postlist: # iterate through pun_bible's posts to find largest value
        media_pk = (media.dict())["pk"]
        view = (media.dict())["view_count"]
        like = (media.dict())["like_count"]
        comment = (media.dict())["comment_count"]
        media_type = (media.dict())["media_type"]
        product_type = (media.dict())["product_type"]
        caption_text = (media.dict())["caption_text"].replace("factsdailyy","relatablerating")
        post_value = round((view/(20*40) + like/(40) + comment), 2)
        values.append(post_value)

        post_options["media_pk"] = media_pk
        post_options["post_value"] = (post_value)
        post_options["caption_text"] = (caption_text)
        post_options["media_type"] = (media_type)
        post_options["product_type"] = (product_type)

        new_post = True

        for posted in posts: # iterate through posts.json
            
            #(f"postedmediapk:{posted['media_pk']}")
            #print(f"mediapk:{media_pk}")
            if posted["media_pk"] == media_pk: 
                new_post = False
            else:
                pass
                
        if new_post:
            post_list.append(post_options)    
        else:
            print("already posted, pass")
        post_options = {}

    #print("post_list:")
    #print(post_list)

    # Sort lists

    sorted_list = (sorted(post_list, key=lambda x: x["post_value"]))
    sorted_list.reverse()  # sort so that the highest post value is first

    #print(sorted_list)

    for option in sorted_list: # iterate through dictionaries in the list

        if (option)["media_type"] == 2 and (option)["product_type"] == "clips": # ignore reels
            print("reel/clip")
            media_upload_type = "Reel"
            FINAL_CAPTION = (option)["caption_text"]
            #bot.video_download((option)["media_pk"],SAVE_PATH)
            update_json_posts(option)
            return(bot.clip_download((option)["media_pk"],SAVE_PATH))
        elif (option)["media_type"] == 2 and (option)["product_type"] == "igtv": # ignore igtv
            pass
        elif (option)["media_type"] == 2 and (option)["product_type"] == "feed":
            # download video
            print("video in feed")
            media_upload_type = "Video"
            FINAL_CAPTION = (option)["caption_text"]
            bot.video_download((option)["media_pk"],SAVE_PATH)
            update_json_posts(option)
            return(bot.video_download((option)["media_pk"],SAVE_PATH))
            
        elif (option)["media_type"] == 1:
            pass

        elif (option)["media_type"] == 8:
            pass

        else:
            print("unknown media")
    
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

def upload_post(pathlocation):
    '''
    upload the files 
    '''

    res = capgen.get_capgen(FINAL_CAPTION)
    results = ast.literal_eval(res) #turn from string to dict
    cap = results["caption"]
    rating = results["rating"]
    hashtag = results["hashtag"]
    ALTEREDCAPTION = f"{cap}\nRelatable Rating:{rating}\nFollow @relatablerating for a daily dose of happiness 😊\n\n\n\n{hashtag}"
    
    
    #thumblocation = os.path.join(pathlocation, ".jpg")
    
    # check to see if reel duration is more than the allowed 90 seconds:

    if media_upload_type == "Reel":
        
        bot.clip_upload(path=pathlocation,
                        caption=ALTEREDCAPTION)
        
        print("upload successful")
    elif media_upload_type == "Video":
        print("uploading video")
        # Upload post
        bot.video_upload(path=pathlocation,
                         caption=ALTEREDCAPTION)
        print("upload successful")
    else:
        print("error occured, unknown media_upload_type")
    os.remove(pathlocation) 
    temp = str(pathlocation)
    print("video removed after")
    os.remove(temp+".jpg")
    print("photo removed after")
    
# Update keys and posts.json files

# Remove the photo
#remove_photo(photo)

# RUN COMMAND
if __name__ == "__main__":
    upload_post(download_photos())
