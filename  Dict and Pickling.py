#Programmer: Brandon Hodgdon
#Project: Inter Planetary Weights Using Dictionaries and Pickling
#Class: CIT-117/ Python 2
#Date: 8MAR2025

# Imports pickle module
import pickle

# Validates weight input
def Val_Input(sPrompt):
   fNum = 0
   while fNum <= 0 :
      try:
         fNum = float(input(sPrompt))
         if fNum <= 0:
             print("Weight must be a positive number.")
      except ValueError:
         print("Input must a numeric value")
   return fNum


def main():
    # Dictionary of different planets weight factors
    dictPlanetWeightFactors = {
            "Mercury" :0.38,
            "Venus"   :0.91,
            "Moon"    :0.165,
            "Mars"    :0.38,
            "Jupiter" :2.34,
            "Saturn"  :0.93,
            "Uranus"  :0.92,
            "Neptune" :1.12,
            "Pluto"   :0.066
        }

    dictPlanetHistory = {}
    #Try/except for EOF(End of File) and FileNotFoundErrors and opens file if there.
    eof = False
    try:
        input_file = open("bhPlanetaryWeights.db", 'rb')
        while not eof:
            try:
                dictPlanetHistory = pickle.load(input_file)
            except EOFError:
                eof = True
        input_file.close()
    except FileNotFoundError:
        pass

    #If file is found/user would like to see history, outputs history to screen
    if input("Would you like to see the history? y/n: ").lower() == "y":
        for name, dictWeights in dictPlanetHistory.items():
            print(f"{name}, here are your weights on our Solar System's planets.")
            for planet, weight in dictWeights.items():
                print(f"Weight on {planet + ":":10s} {weight:10,.2f}")

    while True:
        # Ask user for name and checks dictPlanetHistory to see if name in file
        sName = input("What is your name (enter key to quit): ").title()
        if not sName: break #Lines 60-65 are not pretty but they work
        while sName in dictPlanetHistory:
            print(f"{sName} is already in history file. Enter an unique name.")
            sName = input("What is your name (enter key to quit): ").title()
            if not sName: break
        if not sName: break
        fWeight = Val_Input("What is your weight: ") #Function that validates weight
        dictPersonWeights = {}
        print(f"{sName + ","} here are your weights on our Solar System's planets")
        #Loop that calculates weight and outputs to screen
        for planet, factor in dictPlanetWeightFactors.items():
            fCalculatedWeight = fWeight * factor
            dictPersonWeights[planet] = fCalculatedWeight
            print(f"Weight on {planet + ":":10s}{fCalculatedWeight:10,.2f}")
        dictPlanetHistory[sName] = dictPersonWeights
    #Dumps above output into pickle file for next session
    with open("bhPlanetaryWeights.db", "wb") as file:
        pickle.dump(dictPlanetHistory, file)

main()