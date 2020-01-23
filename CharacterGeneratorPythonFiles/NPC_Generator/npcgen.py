from random import Random

class NPCGen:   
    def __init__(self):       
        self.__pos = []
        self.__neu = []
        self.__neg = []
        self.__letters = []
        self.__height = ["Short", "Medium", "Tall"]
        self.__skinColor = ["Light, pale white", "White fair", "Medium, white to light brown", "Olive, moderate brown", "Brown, dark brown", "Very dark brown to black"]
        self.__hairColor = ["Brown", "Blond", "Black", "Auburn", "Red", "Other"]
        self.__faceShape = ["Oval", "Triangle", "Diamond", "Upside down triangle", "Rectangle", "Square", "Round", "Heart", "Oblong"]
        self.__sex = ["Female", "Male"]
        self.__bodyType = ["Skinny", "Muscular", "Overweight"]
        self.__eyeColor = ["Brown", "Hazel", "Blue", "Green", "Gray", "Amber"]
       
    #List of traits from a file are put into an array
    def __traitsToArray(self, text1, text2, text3, text4):
        fileLen = 0

        #Store positive traits
        file = open(text1, "r")
        fileLen = sum(1 for line in open(text1)) - 1
        for i in range(fileLen):
            self.__pos.append(file.readline().rstrip())       
        file.close()

        #Store neutral traits
        file = open(text2, "r")
        fileLen = sum(1 for line in open(text2)) - 1
        for i in range(fileLen):
            self.__neu.append(file.readline().rstrip())       
        file.close()

        #Store negative traits
        file = open(text3, "r")
        fileLen = sum(1 for line in open(text3)) - 1
        for i in range(fileLen):
            self.__neg.append(file.readline().rstrip())       
        file.close()

        #Store letter for initials 
        file = open(text4, "r")
        fileLen = sum(1 for line in open(text4)) - 1
        for i in range(fileLen):
            self.__letters.append(file.readline().rstrip())       
        file.close()

    #Generate one trait
    def __randomizeTraits(self, traitName, array):
        #traitName is a string
        r = Random()
        print(traitName, end = " ")
        chance = r.randint(0, len(array) - 1)
        print(array[chance])

    #Generate multiple traits
    def __randomizeMultiTraits(self, traitName, array, num):
        #Num is the number of traits that will be generated
        r = Random()
        print(traitName, end = " ")
        for x in range(num):
            chance = r.randint(0, len(array) - 1)
            if x == 0:
                print(array[chance], end = ", ")
            else:
                print(array[chance])

    #Random traits from the array are chosen
    #FIX: There is a chance where a trait repeats 
    def __generateTraits(self):
        r = Random()        
        #~~Name~~
        print("~~Name~~")
        self.__randomizeMultiTraits("Initials:", self.__letters, 2)      
        #~~Appearance~~
        print("~~Appearance~~")
        #Sex
        self.__randomizeTraits("Sex:", self.__sex)
        #Height
        self.__randomizeTraits("Height:", self.__height)
        #Skin Color
        self.__randomizeTraits("Skin Color:", self.__skinColor)
        #Body Type
        self.__randomizeTraits("Body Type:", self.__bodyType)
        #Face Shape
        self.__randomizeTraits("Face Shape:", self.__faceShape)
        #Hair Color
        self.__randomizeTraits("Hair Color:", self.__hairColor)
        #Eye Color
        self.__randomizeTraits("Eye Color:", self.__eyeColor)
               
        #~~Personality~~
        print("~~Personality Traits~~")
        #Positive
        self.__randomizeMultiTraits("Positive Traits:", self.__pos, 2)
        #Neutral
        self.__randomizeMultiTraits("Neutral Traits:", self.__neu, 2)
        #Negative
        self.__randomizeMultiTraits("Negative Traits:", self.__neg, 2)

    #Text1 = positive traits, text2 = neutral traits, text3 = negative traits, text4 = Initials
    def executeNPCGen(self, text1, text2, text3, text4):
        self.__traitsToArray(text1, text2, text3, text4)
        self.__generateTraits()