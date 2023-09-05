import math
import re
from collections import Counter #Used to compare the similarity of two word lists

emptyarray = []

patterns = [
                "maxine caulfield from life is strange"
            ]
InputPatterns = [
                'real chads use lua fr'
            ]

def counter_cosine_similarity(c1, c2):

    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    
    if(magA != 0 and magB != 0):
        return (dotprod / (magA * magB)) #returns a value between 0 and 1 that describes the similarity between the two word lists
    else:
        
        print("Cannot divide by 0") #This is likely caused by an existing pattern holding no value.
        return 100

tempstring = ' '.join(patterns)


emptyarray = tempstring.split()

counterJson = Counter(emptyarray) 


counterInput = Counter(InputPatterns)


print(counterJson)

print(counterInput)


print(counter_cosine_similarity(counterJson, counterInput))