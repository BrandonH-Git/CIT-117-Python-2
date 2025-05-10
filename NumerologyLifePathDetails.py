#Programmer: Brandon Hodgdon
#Project: Numerology_inheritance
#Class: Python 2
#Date: 26APR2025


class Numerology:   # Define the Class and intilaize everything so it is ready to go
    def __init__(self, sName, sDOB):

        self.__Name = sName
        self.__Birthdate = sDOB

#Replaces "-" and "/" with nothing, adds all numbers and puts it into the ReduceNumber module
        self.__LifePath = 0
        for char in self.__Birthdate.replace("-", "").replace("/", ""):
            self.__LifePath += int(char)
        self.__LifePath = self.__ReduceNumber(self.__LifePath)

#Gets the Birth day and puts it into the reduce number module.
        self.__Birthday = 0
        iBirthdayDay = int(self.__Birthdate[3:5])
        self.__Birthday = self.__ReduceNumber(iBirthdayDay)

#Replaces "-" and "/" with nothing, adds the Month and Day then puts it through the ReduceNumber module
        self.__iAttitude = 0
        for char in self.__Birthdate.replace("-", "").replace("/", "")[:4]:
            self.__iAttitude += int(char)
        self.__iAttitude = self.__ReduceNumber(self.__iAttitude)

#Dictionary of Letter with corresponding number
        self.dictChar = {"A": 1, "J": 1, "S": 1,
                         "B": 2, "K": 2, "T": 2,
                         "C": 3, "L": 3, "U": 3,
                         "D": 4, "M": 4, "V": 4,
                         "E": 5, "N": 5, "W": 5,
                         "F": 6, "O": 6, "X": 6,
                         "G": 7, "P": 7, "Y": 7,
                         "H": 8, "Q": 8, "Z": 8,
                         "I": 9, "R": 9}

#These next 3 calculations check the sName against the self.dictChar
# to get the correct output for needed calculations
        self.__Soul = 0
        self.__Personality = 0

        for sLetter in self.__Name.upper():
            if sLetter in "AEIOU":
                self.__Soul += self.dictChar.get(sLetter, 0)
            else:
                self.__Personality += self.dictChar.get(sLetter, 0)

        self.__Soul = self.__ReduceNumber(self.__Soul)

        self.__Personality = self.__ReduceNumber(self.__Personality)

        self.__Power = 0
        self.__Power = self.__ReduceNumber(self.__Soul + self.__Personality)

    def __ReduceNumber(self, iNumber):
        while (len(str(iNumber)) > 1):
            iNumber = (iNumber % 10) + (iNumber // 10)
        return iNumber

#These modules are getters to get the correct calculated value for each calculation
    @property
    def getName(self):
        return self.__Name
    @property
    def getBirthdate(self):
        return self.__Birthdate
    @property
    def getLifePath(self):
        return self.__LifePath
    @property
    def getBirthday(self):  # 6
        return self.__Birthday
    @property
    def getAttitude(self):
        return self.__iAttitude
    @property
    def getSoul(self):
        return self.__Soul
    @property
    def getPersonality(self):
        return self.__Personality
    @property
    def getPower(self):
        return self.__Power

#This module automatically does this at the end of the built class so it will
#return the output without needing to call it
    def __str__(self):
        return f'''Client Name: {self.getName}
Client DOB: {self.getBirthdate}
Life Path: {self.getLifePath}
Attitude: {self.getAttitude}
Birthday: {self.getBirthday}
Personality: {self.getPersonality}
Power: {self.getPower}
Soul: {self.getSoul}'''

# Subclass that inherits parent class
class NumerologyExtended(Numerology):
    def __init__(self, sName, sDOB):
        Numerology.__init__(self, sName, sDOB)

#
        self.__lifePathDescriptions = {

            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"}

#Property to get Life Path description and function that searches dict and returns description
    @property
    def __getLifePathDescription(self):
        return self.__lifePathDescriptions.get(self._Numerology__LifePath)

#Output with some formatting to look better that is automatically done when subclass is executed
    def __str__(self): return \
        (f"{Numerology.__str__(self)}\
        \n{"\n\033[4mLife Path Description\033[0m"}\n"
         f"{self.__getLifePathDescription}")
