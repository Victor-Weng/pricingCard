tempptrnidentifyNL = 'ur mom hahaha \u2342 mm'

if(not (tempptrnidentifyNL).isascii()):

    print(tempptrnidentifyNL)

    print("ascii identified, tempptrnidentifyNL SHOULD BE CLEARED")
    tempptrnidentifyNL = ("this is a pattern dump for single-use and un-identifiable characters")
else:
    print("the message was fine")

print(tempptrnidentifyNL)