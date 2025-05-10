#Programmer: Brandon Hodgdon
#Project: Password Validator
#Class: Python Programming 2
#Date:21FEB2025

#Function that prompts for users input and gets initials
def Get_Name():
   sIntitial = sName = ""
   sName = input("Enter full name such as John Smith: ").title()
   sIntitial = sName[0] + sName[sName.find(" ")+1]
   return (sIntitial)

def Password_Check(sInitials):
    sPasswd = ""
    bIsVal = False
    #Sets all boolean values to false
    bLength = bPass = bInitials = bUpper = bLower = bDigit = bSpecial = bCount = False
    #while loop that checks for criteria and if True, turns the boolean switch from False to True otherwise displays message
    while not bIsVal:
        sPasswd = input("Enter new password: ")
        if len(sPasswd) in range(8, 13):
            bLength = True
        else:
            print("Password must be between 8 and 12 characters.")
        if sPasswd.lower().startswith("pass"):
            print("Password can't start with Pass")
        else:
            bPass = True
        if sInitials.lower() in sPasswd.lower():
            print("Password must not contain user initials")
        else:
            bInitials = True
# Makes a dict and the for loop goes through each character to see if it matches criteria, If True, turns boolean from False to True
        dictChar = {}
        for char in sPasswd:
            if char.isupper():
                bUpper = True
            elif char.islower():
                bLower = True
            elif char.isdigit():
                bDigit = True
            elif char in "!@#$%^":
                bSpecial = True
            iCount = sPasswd.lower().count(char.lower())
            if iCount > 1:
                dictChar[char.lower()] = iCount
# If any of above conditions are not met then these messages will display
        if not bUpper: print("Password must contain at least 1 uppercase letter.")
        if not bLower: print("Password must contain at least 1 lowercase letter.")
        if not bDigit: print("Password must contain at least 1 number.")
        if not bSpecial: print("Password must contain at least 1 of these special characters: ! @ # $ % ^ ")
        if dictChar:
            bCount = True
            print("These characters occur more than once:")
            #For loop to output the dictionary
            for key, value in dictChar.items():
                print(f"{key}: {value} times")
        #If all conditions are turned from False to True then password is good
        if bLength and bPass and bInitials and bUpper and bLower and bDigit and bSpecial and bCount:
            bIsVal = True
            print("Password is valid and OK to use")

#Main function that calls above functions
def main():
    sName_Initials = str(Get_Name())
    Password_Check(sName_Initials)

#Calling main
main()

