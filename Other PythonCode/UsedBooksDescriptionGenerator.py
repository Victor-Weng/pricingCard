import pandas as pd

df = pd.read_csv(r"C:\Users\Victo\OneDrive\Desktop\pythonCode\Used Books\Used Books.xlsx - Sheet1.csv",encoding='UTF-8') #read used books
CND1 = df["Condition"].tolist()
TITL = df["Book Name"].tolist()
NUM = df["ISBN-13"].tolist()
WGT = df["Weight (g)"].tolist()
DMN = df["Dimensions"].tolist()
PGS = df["Pages"].tolist()
CND2 = df["Condition"].tolist()

for i in range (38):

    if (CND1[i] == "Perfect"):
        CND2[i] = "Brand new."
    elif (CND1[i] == "Lightly Used"):
        CND2[i] = "Slight cosmetic imperfections with no page markings."

    print(f"Ad title: {TITL[i]} in {CND1[i]} condition\n")
    print("Ad description:\n")
    print(f"Selling {TITL[i]} in {CND1[i]} condition!\n")

    print("Textbook Details:\n")

    if(not pd.isnull(TITL[i])):
        print(f"Title: {TITL[i]}")
    if(not pd.isnull(NUM[i])):
        print(f"ISBN-13: {NUM[i]}")
    if(not pd.isnull(WGT[i])):
        print(f"Item Weight (g): {WGT[i]}")
    if(not pd.isnull(DMN[i])):
        print(f"Item Dimensions (cm): {DMN[i]}")
    if(not pd.isnull(PGS[i])):
        print(f"Pages: {PGS[i]}")
    if(not pd.isnull(CND2[i])):
        print(f"Condition: {CND2[i]}")

    
    print("Price:")
    print("The price is open to negotiation. Feel free to present your offer. If you buy together with another one of our books, you can receive a 20%% discount on both items!\n")

    print("Location: Toronto, Canada\n")

    print("If this textbook meets your requirements or if you have any inquiries, kindly send me a message. We can arrange a convenient meet-up to proceed with the transaction.\n")
    print("_________________________________________________________________________________________________________________________________________________\n")
