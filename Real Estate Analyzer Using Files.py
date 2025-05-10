#Programmer: Brandon Hodgdon
#Project: Real Estate Analyzer Using Files
#Date: 20MAR2025
#Class: Python Python Programming 2

import csv

#function that opens file with reader and puts into a list
def getDataInput(sFilePath) -> list:
    with open(sFilePath, "r") as file:
        reader = csv.reader(file)
        next(reader)
        lstRecords = []
        for record in reader:
            lstRecords.append(record)
        return lstRecords

#Function that takes in a list and returns the medium
def getMedian(list) -> float:
    fRemainder = len(list) % 2
    fHalfway = len(list) // 2
    if fRemainder == 0:
        lstmedian = (list[fHalfway] + list[fHalfway -1]) / 2
    else:
        lstmedian = list[fHalfway]
    return lstmedian

def main():
    sFilePath = "RealEstateData.csv"
    lstRecords = getDataInput(sFilePath)

# Defining list
    lstPropertyTypes = []
    lstPrices = []

# Defining dict's
    dictPropertyType = {}
    dictCities = {}
    dictZipCode = {}

# Loop that pulls the specific part required for each index from each record
    for row in lstRecords:
        sCity = row[1]
        sPropertyType = row[7]
        fPrice = float(row[8])
        sZip = row[2]

# These if statements will check if they are in the respective lst/dict and if not they will be added.

        if sPropertyType not in lstPropertyTypes:
            lstPropertyTypes.append(sPropertyType)

        if sPropertyType in dictPropertyType:
            dictPropertyType[sPropertyType] += fPrice
        else:
            dictPropertyType[sPropertyType] = fPrice

        if sCity in dictCities:
            dictCities[sCity] += fPrice
        else:
            dictCities[sCity] = fPrice

        if sZip in dictZipCode:
            dictZipCode[sZip] += fPrice
        else:
            dictZipCode[sZip] = fPrice

        lstPrices.append(fPrice)

    lstPrices.sort()

#Output for each piece of information
    print(f"\n\033[1;4mFile Name:       {sFilePath}\033[0m")
    print(f"Minimum {lstPrices[0]:27,.2f}")
    print(f"Maximum {lstPrices[-1]:27,.2f}")
    print(f"Sum {sum(lstPrices):31,.2f}")
    print(f"Average {sum(lstPrices)/len(lstPrices):27,.2f}")
    print(f"Median {getMedian(lstPrices):28,.2f} ")

    print("\n\033[1mSummary by Property Type: \033[0m")
    for propertyType, fTotal in dictPropertyType.items():
        print(f"{propertyType:20s}{fTotal:15,.2f}")

    print("\n\033[1mSummary by City: \033[0m")
    for sCity, fTotal in dictCities.items():
        print(f"{sCity.title():20s}{fTotal:15,.2f}")

    print("\n\033[1mSummary by Zip: \033[0m")
    for sZip, fTotal in dictZipCode.items():
        print(f"{sZip:20s}{fTotal:15,.2f}")

main()