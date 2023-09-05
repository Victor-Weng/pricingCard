import json


import json

tempptrnidentify = ["DualityOfMan"]

v = 'D2' #Version of file
directory = 'C:/Users/victo/OneDrive/Desktop/pythonCode/PythonChatbot' + v + '/' #Directory where the general files are found
intentfilename = (directory + 'intents' + v + '.json')
tempresp = 'aaa'



with open (intentfilename) as json_file:
    data = json.load(json_file)

    print("before appending: \n")
    print(data)

    for value in data["intents"]: #iterate over the lists in data["intents"]
        print(tempptrnidentify)
        print(value["patterns"])
        print(value["responses"])
        if value["patterns"] == tempptrnidentify:

            value["responses"].append(tempresp) #lists are mutable so append it this way
            print("succesfully appended in results")
            break
        
        # for i,ptrn in enumerate(value): #iterate through each list
        #     if ptrn == tempptrnidentify: #if the pattern within the list is equal to the temporary pattern holding our similar one
        #         value[i+1] = value[i+1].append(tempresp) 
                
        #         #append the response value (which is i+1, or 1 position after the pattern) with our new responses
        #         break

tempptrnidentify = []

print("after appending: \n")
print(data)