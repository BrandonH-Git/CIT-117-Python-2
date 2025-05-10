#Programmer: Brandon Hodgdon
#Project: Numerology
#Class: Python 2
#Date: 17APR2025

from Numerology import Numerology


def main():

    while True:
        sName = input("Enter Name: ")
        if not sName:
            continue

        sDOB = input("Enter birthday: ")
        if sDOB[2] == "-" or sDOB[2] == "/" and sDOB[5] == "-" or sDOB[5] == "/" and len(sDOB) == 10:
            break

    myNumObject = Numerology(sName, sDOB)
    print(myNumObject)

main()
