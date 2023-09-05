from instagrapi import Client
import time
import random
bot = Client()

userid = "290694015"
password = "HowMuchWood7177893!"
accountSelection = ["Brightspace.ai","Dreamhomes.ai","Relatablerating","pun_plug","Influence.ai"]
hashtagSelection = [["coolfacts","unknownfacts","didyouknowfacts","knowledgeispower"],
                    ["dreamhomes","dreamhome","fantasyhomes","architecture"],
                    ["viralmemes","viralmemesdaily","foryourpage","dankmemes"],
                    ["puns","punsfordays","punstagram","badpuns","dadjokes"],
                    ["artdailydose","artdailypage","artdaily_viral","artdailycollective","artinstadaily"]
                    ]
count = 0 # amount of people to unfollow after

def login(account):
    bot.login(account,password) # STEP 1: LOGIN
    

def runFollow(hashtag):
    
    global count # amount of people to unfollow after
    # Get the 5 latest posts for a provided hashtag
    latestPosts = bot.hashtag_medias_top_v1(hashtag,5)

    # Iterate through the list of dictionaries of the 5 top posts
    for posts in latestPosts:
        
        # get the post id from the individual post
        postid = str((posts.dict())["id"])
        # get the list of accounts that liked the post (limited, so we do 20)
        postLikers = bot.media_likers(postid)
        # if the list is more than 20, shorten it down to 20.
        if len(postLikers) > 30:
            del postLikers[30:]

        # iterate through the list of likers of the post
        for index,liker in enumerate(postLikers):
            print(f"Following user{index+1}")
            time.sleep(random.uniform(0,1)+0.5) # wait a random amount between 0.5 and 1.5 seconds
            # 70% chance to follow
            if random.uniform(0,1) > 0.3:
                bot.user_follow(liker) # follow the user
                count += 1
            else:
                pass
            print("success") # print success
    return

def runUnfollow(user_id):
    global count
    print(f"from runUnfollow(): count is {count}")
    following = bot.user_following(user_id)
    for i,user in enumerate(reversed(following)): # start from the bottom of the following list
        if i+1 < count:
            time.sleep(random.uniform(0,1)+0.5) # wait a random amount between 0.5 and 1.5 seconds
            bot.user_unfollow(user)
        else:
            break


if __name__ == "__main__":
    for i,account in enumerate(accountSelection): # ITERATE THROUGH MY ACCOUNTS
        hashtag = random.choice(hashtagSelection[i]) # Pick a random hashtag from the list
        print(f"for account: {account}, we have picked the random hashtag {hashtag}")
        print(f"logging into {account}")
        login(account) # LOGIN
        print("login succesful, running follow")
        runFollow(hashtag) # Follow the accounts
        print("follow succesful, running unfollow")
        #runUnfollow(bot.user_id)
        print(f"done account {i+1}")
        count =0
    print("finished everything :)")

