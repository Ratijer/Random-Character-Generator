from npcgen import NPCGen

n = NPCGen()

choice1 = input("Do you want to generate characters?   Y|N  ")
while(choice1 == "Y" or choice1 == "y"):
    choice2 = eval(input("How many characters do you want?  "))
    print()
    for x in range(choice2):
        print("\nCHARACTER", x + 1)
        n.executeNPCGen("CharPosTraits.txt", "CharNeuTraits.txt", "CharNegTraits.txt", "Alphabet.txt")
    choice1 = input("\nDo you want to generate characters?   Y|N  ")

if(choice1 == "N" or choice1 == "n"):
    print("Bye!")
else:
    print("That's not right. Bye anyways.")