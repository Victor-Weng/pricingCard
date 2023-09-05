'''
Instagram bot for the account "dreamhomes.ai." This program will manage the keys in keys.json
with mathematical models such as a logarithmic decay of weights over-time for key terms
and addding in new key terms that are generated in capgen.py. The 

Everything needed: 

Posting file: postmain.py
Image generation file: imagen.py
Caption (and hashtag) generation file: capgen.py
>Keyword score tracking file: keytrack.py

'''
import json
from collections import OrderedDict # used to keep json files in the same order

with open('keys.json', "r", encoding='utf-8') as dt:
    data = json.load(dt, object_pairs_hook=OrderedDict) # list

with open('posts.json', "r", encoding='utf-8') as pt:
    posts = json.load(pt, object_pairs_hook=OrderedDict)

def highest_weights(keys):
    '''
    function that returns the top 10 highest weights so that the EdgeGPT prompt is not overwhelming
    '''
    top10pairs = []
    top10weights = [0]

    for keyvaluepair in keys:
        if ((keyvaluepair["weight"] > min(top10weights))and len(top10pairs) == 10):

            smallest_index = top10weights.index(min(top10weights))

            top10weights[smallest_index] = keyvaluepair["weight"]
            top10pairs[smallest_index] = (keyvaluepair)

        elif (keyvaluepair["weight"] > min(top10weights)):
            top10weights.append(keyvaluepair["weight"])
            top10pairs.append(keyvaluepair)

        else:
            pass
    return top10pairs

def update_weights(data, posts, results, bot):
    '''
    you first get a list of medias based on user id, then update a json file based on that.
    Iterate it into the json file, alongside the keys used. Then update based on how much
    the Like Count has changed
    '''
    
    # bot is taken from postmain.py

    postlist = bot.user_medias_gql(user_id = "52446113800", amount = 25)

    # lists for both keys and posts that stores all the keys that we have to check against new keys all at once
    key_list = [] 
    post_list = []
    
    weight_dif=0

    # decay all old values by 5%

    for pair in data:
        pair["weight"] = round(((pair["weight"])*0.95), 2)

    for media in postlist: # media from instagraphi

        # get values from one post "media"

        media_pk = (media.dict())["pk"]
        view = (media.dict())["view_count"]
        like = (media.dict())["like_count"]
        comment = (media.dict())["comment_count"]

        for post in posts:  # posts from posts.json

            if post["media_pk"] == media_pk:

                # compute changes in views, likes, and comments.
                view_dif = view - post["view_count"]
                like_dif = like - post["like_count"]
                comment_dif = comment - post["comment_count"]

                # update posts json file with new views and comments etc.

                post["view_count"] = view_dif
                post["like_count"] = like_dif
                post["comment_count"] = comment_dif

                # how much the weighting should change for associated keywords
                # Ratio of successful reel was 56000 : 3000 : 78 which is used to roughly based on the weight calc

                weight_dif = round((view_dif/(20*40) + like_dif/(40) + comment_dif), 2)

                post_list.append(media_pk)

            else:
                pass

            with open('posts.json', "w", encoding='utf-8') as pt:
                json.dump(posts, pt, indent=4)
                
            # iterate through the keys in data to see if they match with the ones in the post

            for key in post["keys"]: # for each individual key in the list from posts.json

                # if the key exists

                for pair in data:  # for all the pairs {"key":,"weight:"} in keys.json      
                    
                    if key == pair["key"]:
                        
                        pair["weight"] = pair["weight"] + weight_dif

                        key_list.append(key) # append to a list to check new keys against later

                        # if key is 0.5 or smaller after weight_dif, delete it

                    else:
                        pass

                    if pair["weight"] <= 0.5:
                            
                            data.remove({"key":pair["key"], "weight":pair["weight"]})

                    else:
                        pass

                    with open('keys.json', "w", encoding='utf-8') as dt:
                        json.dump(data,dt, indent=4)

                if key not in key_list:
                    # if it is a new key, append the key value to the json file

                        data.append({"key":key, "weight":1.0}) # set new weight to 1
                else:
                    pass
                    
                    # decay formula: y = (weight)(0.95), decays weights by 10%

                    # UPDATE all key weights in loop with new value
             
        if media_pk not in post_list:

            posts.append({"media_pk": media_pk,
                        "keys": results["key"],
                        "view_count": view,
                        "like_count": like,
                        "comment_count": comment})
        else:
            pass
        

    print("key and posts updating successful")
