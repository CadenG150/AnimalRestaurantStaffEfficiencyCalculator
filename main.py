from costTrees import *

def editData():
    try:
        dataFile = open("data.txt", "r")
        splitData = dataFile.read().splitlines()
        dataFile.close()
    except:
        print("No data created")
        return
    for b, y in enumerate(splitData):
        print(str(b+1) + ": " + names[b] + ": " + y)
    print("Which would you like to edit?")
    numToEdit = int(input("Enter a number: "))
    numToEdit -= 1
    print("What new value would you like to input?")
    newValue = input("Enter here: ")
    splitData[numToEdit] = newValue
    with open('data.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(splitData))

def createData():
    myFile = open("data.txt", "w")
    myFile.close()
    print("Staff")
    print("-----")
    print("Enter in how much it costs to buy the next level of each staff")
    peopleCosts = []
    for i in names:
        individualCost = input(i + ": ")
        peopleCosts.append(individualCost)
    with open('data.txt', mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(peopleCosts))
def calculate():
    dataFile = open("data.txt", "r")
    splitData = list(map(int, dataFile.read().splitlines()))
    dataFile.close()
    codPerStarDictionary = {}
    for e, j in enumerate(splitData):
        codPerStarDictionary[names[e]] = (j / listOfTrees[e][j])
    codPerStarDictionarySorted = dict(sorted(codPerStarDictionary.items(), key=lambda item: item[1]))
    print(codPerStarDictionarySorted)

print("Animal Restaurant Calculator :)")
print("Option 1: Edit Data")
print("Option 2: Create Data")
print("Option 3: Calculate")
choice = input("Please input a number: ")
if choice == "1":
    editData()
elif choice == "2":
    createData()
elif choice == "3":
    calculate()
else:
    print("Please try again.")