


for i in range (books.length()){

    if (CND1[i] == "Perfect"){
        CND2[i] = "Brand new."
    }elif (CND1[i] == "Lightly Used"){
        CND2[i] = "Slight cosmetic imperfections with no page markings."
    }

    print(f"Ad title: {TITL[i]} in {CND1[i]} condition\n\n")
    print("Ad description:\n\n")
    print(f"Selling {TITL[i]} in {CND1[i]} condition!\n\n")

    print("Textbook Details:\n\n")

    if(TITL != "NA"){
        print(f"Title: {TITL[i]}\n")
    }
    if(NUM != "NA"){
        print(f"ISBN-13: {NUM[i]}\n")
    }
    if(WGT != "NA"){
        print(f"Item Weight (g): {WGT[i]}\n")
    }
    if(DMN != "NA"){
        print(f"Item Dimensions (cm): {DMN[i]}\n")
    }
    if(PGS != "NA"){
        print(f"Pages: {PGS[i]}\n")
    }
    if(CND2 != "NA"){
        print(f"Condition: {CND2[i]}\n")
    }
    
    print("Price:\n")
    print("The price is open to negotiation. Feel free to present your offer. If you buy together with another one of our books, you can receive a 20%% discount on both items!\n\n")

    print("Location: Toronto, Canada\n\n")

    print("If this textbook meets your requirements or if you have any inquiries, kindly send me a message. We can arrange a convenient meet-up to proceed with the transaction.\n\n")
    print("________________________________________________________________________________________________________________________________________________________________\n\n")
}



