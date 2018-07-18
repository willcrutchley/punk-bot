import json, pickle

with open("recipes.json", "r") as infile:
    data = json.load(infile)

index = 0
outputs = []

choice = input("Generate new list? Y/n")
if choice.lower() == 'y':
    while True:
        try:
            outputs.append(data["recipes"][index]["outputItem"])
            print(data["recipes"][index]["outputItem"]) 
            index += 1
        except:
            break
    with open('outfile', 'wb') as fp:
        pickle.dump(outputs, fp)
elif choice.lower() == 'n':
    with open ('outfile', 'rb') as fp:
        outputs = pickle.load(fp)
desired = input("What item?")
desired = desired.upper()
if desired in outputs:
    index = outputs.index(desired)
else:
    print("Invalid output item")
