import re

text = '<:catcry:590165957318672424> \u1213 ur mom lololol hahaha  https://media.discordapp.net/attachments/763957300507181077/995258438345044038/test.gif'

def clean_out(inputstring):

    inputstring = re.sub(r"(?:@|http?://|https?://|www)\S+", "", inputstring) #clean out links, mentions
    inputstring = re.sub(r"<.+?>","", inputstring)
    inputstring = re.sub(r"[^\w]"," ",inputstring)
    inputlist = (inputstring.split()) #turns the input string into a list

    print(type(inputlist))
    
    for i in range(len(inputlist)): #iterate through input list
        if(inputlist[i] == r"\\\\"): #if a character detected within the list is a backslash (used two backslashes to escape the backslash)
            print("backslash")
            for k in range(i, len(inputlist)): #loop through all the characters following the backslash until a space is reached
                while(inputlist[k] != " "):
                    inputlist[k] = "" #replace with nothing
                break #exit out of the loop

    if len(inputlist) == 0: #INCASE ALL THAT WAS SENT WAS NOTHING, THIS IS WHAT WILL BE SAVED INTO THE PATTERNS SO THAT IT DOESNT RUIN THE counter_cosine_similarity function and divide by zero
        return "no input, sadly"

    return inputlist

print(clean_out(text))