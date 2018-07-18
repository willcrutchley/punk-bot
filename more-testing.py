import json, pickle

with open("recipes.json", "r") as infile:
    data = json.load(infile)

n = 0
outputs = []

choice = input("Generate new list? Y/n")
if choice.lower() == 'y':
    while True:
        try:
            outputs.append(data["recipes"][n]["outputItem"])
            print(data["recipes"][n]["outputItem"]) 
            n += 1
        except:
            break
    with open('outputs', 'wb') as fp:
        pickle.dump(outputs, fp)
elif choice.lower() == 'n':
    with open ('outputs', 'rb') as fp:
        outputs = pickle.load(fp)
else:
    print("Invalid response")
    exit
desired = input("What item?")
desired = desired.upper()
if desired in outputs:
    index = outputs.index(desired)
else:
    print("Invalid output item")
    exit

inputs = data["recipes"][index]["inputs"]

n = 0
inputItems = []
inputQuantities = []
while True:
    try:
        inputItems.append(inputs[n]["inputItem"])
        inputQuantities.append(inputs[n]["inputQuantity"])
        n += 1
    except:
        break

for item in inputItems:
    print(item)
    print(inputQuantities[inputItems.index(item)])

