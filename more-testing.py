import json, pickle
from prettytable import PrettyTable

n = 0
outputs = []

choice = input("Generate new list? Y/n")
if choice.lower() == 'y':
    with open("recipes.json", "r") as infile:
        data = json.load(infile)
    with open("strings.json", "r") as names:
        strings = json.load(names)
    while True:
        try:
            outputs.append(data["recipes"][n]["outputItem"])
            n += 1
        except:
            break
    with open('outputs', 'wb') as fp:
        pickle.dump(outputs, fp)
    with open('jsonData', 'wb') as jd:
        pickle.dump(data, jd)
    with open('strings', 'wb') as st:
        pickle.dump(strings, st)
    keys = []
    vals = []
    for key in strings:
        keys.append(key)
        vals.append(strings[key])
    with open('keys', 'wb') as ky:
        pickle.dump(keys, ky)
    with open('vals', 'wb') as vl:
        pickle.dump(vals, vl)
elif choice.lower() == 'n':
    with open ('outputs', 'rb') as fp:
        outputs = pickle.load(fp)
    with open ('jsonData', 'rb') as jd:
        data = pickle.load(jd)
    with open ('strings', 'rb') as st:
        strings = pickle.load(st)
    with open ('keys', 'rb') as ky:
        keys = pickle.load(ky)
    with open ('vals', 'rb') as vl:
        vals = pickle.load(vl)
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
        skill = data["recipes"][index]["prerequisites"]
        skill = skill[0].replace(" ", "_")
        skillName = vals[keys.index("GUI_SKILLS_" + skill.upper() + "_TITLE")]
        machine = data["recipes"][index]["machine"]
        machine = machine.replace("_", "")
        machineName = vals[keys.index("ITEM_TYPE_MACHINE_" + machine.upper() + "_BASE")]
        hand = data["recipes"][index]["canHandCraft"]
        duration = data["recipes"][index]["duration"]
        power = data["recipes"][index]["powerRequired"]
        spark = data["recipes"][index]["spark"]
        wear = data["recipes"][index]["wear"]
        output = data["recipes"][index]["outputItem"]
        outputName = vals[keys.index("ITEM_TYPE_" + output.upper())]
        outputNum = data["recipes"][index]["outputQuantity"]
        break
out = PrettyTable(["Outputs:", "Normal", "Bulk", "Mass"])
out.add_row([outputName, outputNum[0], outputNum[1], outputNum[2]])

table = PrettyTable(["Requires:", "Normal", "Bulk", "Mass"])
table.align["Requires:"] = "l"

for item in inputItems:
    nor = inputQuantities[inputItems.index(item)][0]
    bul = inputQuantities[inputItems.index(item)][1]
    mas = inputQuantities[inputItems.index(item)][2]
    if "ITEM_TYPE_" + item.upper() in keys:
        name = vals[keys.index("ITEM_TYPE_" + item.upper())]
        table.add_row([name, nor, bul, mas])
    else:
        table.add_row([item, nor, bul, mas])
        
spark_nor = spark[0]
spark_bul = spark[1]
spark_mas = spark[2]

table.add_row(["Spark", spark_nor, spark_bul, spark_mas])
table.add_row(["Power", power, power, power])
table.add_row(["Time", str(duration[0]) + 's', str(duration[1]) + 's', str(duration[2]) + 's'])

print("Recipe for " + outputName)
print(out.get_string())
print(table.get_string())
print(str(skillName))
print(str(machineName))


'''
print(skills)
print(machine)
print(hand)
print(duration)
print(power)

print(wear)
'''
