#Programmer: Brandon Hodgdon
#Project: Numerology
#Class: Python 2
#Date: 17APR2025


# class Numerology:   # Define the Class and intilaize everything so it is ready to go
#     def __init__(self, sName, sDOB):
#
#         self.Name = sName
#         self.Birthdate = sDOB
#
# #Replaces "-" and "/" with nothing, adds all numbers and puts it into the ReduceNumber module
#         self.LifePath = 0
#         for char in self.Birthdate.replace("-", "").replace("/", ""):
#             self.LifePath += int(char)
#         self.LifePath = self.ReduceNumber(self.LifePath)
#
# #Gets the Birth day and puts it into the reduce number module.
#         self.Birthday = 0
#         iBirthdayDay = int(self.Birthdate[3:5])
#         self.Birthday = self.ReduceNumber(iBirthdayDay)
#
# #Replaces "-" and "/" with nothing, adds the Month and Day then puts it through the ReduceNumber module
#         self.iAttitude = 0
#         for char in self.Birthdate.replace("-", "").replace("/", "")[:4]:
#             self.iAttitude += int(char)
#         self.iAttitude = self.ReduceNumber(self.iAttitude)
#
# #Dictionary of Letter with corresponding number
#         self.dictChar = {"A": 1, "J": 1, "S": 1,
#                          "B": 2, "K": 2, "T": 2,
#                          "C": 3, "L": 3, "U": 3,
#                          "D": 4, "M": 4, "V": 4,
#                          "E": 5, "N": 5, "W": 5,
#                          "F": 6, "O": 6, "X": 6,
#                          "G": 7, "P": 7, "Y": 7,
#                          "H": 8, "Q": 8, "Z": 8,
#                          "I": 9, "R": 9}
#
# #These next 3 calculations check the sName against the self.dictChar
# # to get the correct output for needed calculations
#         self.Soul = 0
#         self.Personality = 0
#
#         for sLetter in self.Name.upper():
#             if sLetter in "AEIOU":
#                 self.Soul += self.dictChar.get(sLetter, 0)
#             else:
#                 self.Personality += self.dictChar.get(sLetter, 0)
#
#         self.Soul = self.ReduceNumber(self.Soul)
#
#         self.Personality = self.ReduceNumber(self.Personality)
#
#         self.Power = 0
#         self.Power = self.ReduceNumber(self.Soul + self.Personality)
#
#     def ReduceNumber(self, iNumber):
#         while (len(str(iNumber)) > 1):
#             iNumber = (iNumber % 10) + (iNumber // 10)
#         return iNumber
#
# #These modules are getters to get the correct calculated value for each calculation
#     def getName(self):
#         return self.Name
#
#     def getBirthdate(self):
#         return self.Birthdate
#
#     def getLifePath(self):
#         return self.LifePath
#
#     def getBirthday(self):  # 6
#         return self.Birthday
#
#     def getAttitude(self):
#         return self.iAttitude
#
#     def getSoul(self):
#         return self.Soul
#
#     def getPersonality(self):
#         return self.Personality
#
#     def getPower(self):
#         return self.Power
#
# #This module automatically does this at the end of the built class so it will
# #return the output without needing to call it
#     def __str__(self):
#         return f'''Client Name: {self.getName()}
# Client DOB: {self.getBirthdate()}
# Life Path: {self.getLifePath()}
# Attitude: {self.getAttitude()}
# Birthday: {self.getBirthday()}
# Personality: {self.getPersonality()}
# Power: {self.getPower()}
# Soul: {self.getSoul()}'''
#

class Numerology:  # Define the Class and intilaize everything so it is ready to go
    def __init__(self, sName, sDOB):

        self.__Name = sName
        self.__Birthdate = sDOB

        # Replaces "-" and "/" with nothing, adds all numbers and puts it into the ReduceNumber module
        self.__LifePath = 0
        for char in self.__Birthdate.replace("-", "").replace("/", ""):
            self.__LifePath += int(char)
        self.__LifePath = self.__ReduceNumber(self.__LifePath)

        # Gets the Birth day and puts it into the reduce number module.
        self.__Birthday = 0
        iBirthdayDay = int(self.__Birthdate[3:5])
        self.__Birthday = self.__ReduceNumber(iBirthdayDay)

        # Replaces "-" and "/" with nothing, adds the Month and Day then puts it through the ReduceNumber module
        self.__iAttitude = 0
        for char in self.__Birthdate.replace("-", "").replace("/", "")[:4]:
            self.__iAttitude += int(char)
        self.__iAttitude = self.__ReduceNumber(self.__iAttitude)

        # Dictionary of Letter with corresponding number
        self.dictChar = {"A": 1, "J": 1, "S": 1,
                         "B": 2, "K": 2, "T": 2,
                         "C": 3, "L": 3, "U": 3,
                         "D": 4, "M": 4, "V": 4,
                         "E": 5, "N": 5, "W": 5,
                         "F": 6, "O": 6, "X": 6,
                         "G": 7, "P": 7, "Y": 7,
                         "H": 8, "Q": 8, "Z": 8,
                         "I": 9, "R": 9}

        # These next 3 calculations check the sName against the self.dictChar
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

    # These modules are getters to get the correct calculated value for each calculation
    def getName(self):
        return self.__Name

    def getBirthdate(self):
        return self.__Birthdate

    def getLifePath(self):
        return self.__LifePath

    def getBirthday(self):  # 6
        return self.__Birthday

    def getAttitude(self):
        return self.__iAttitude

    def getSoul(self):
        return self.__Soul

    def getPersonality(self):
        return self.__Personality

    def getPower(self):
        return self.__Power

    # This module automatically does this at the end of the built class so it will
    # return the output without needing to call it
    def __str__(self):
        return f'''Client Name: {self.getName()}
Client DOB: {self.getBirthdate()}
Life Path: {self.getLifePath()}
Attitude: {self.getAttitude()}
Birthday: {self.getBirthday()}
Personality: {self.getPersonality()}
Power: {self.getPower()}
Soul: {self.getSoul()}'''
