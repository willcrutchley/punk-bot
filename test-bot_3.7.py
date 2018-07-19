import asyncio, discord, os, pickle
from prettytable import PrettyTable
TOKEN = 'NDY4ODM1NDAxODE0MTE0MzA0.DjAHiA.Y-6dmYg3pTb52vYfwwRg1ifXWFc'

client = discord.Client()

directory = os.path.dirname(os.path.abspath(__file__))

@client.event
async def on_message(message):
    sender = message.author
    avatar_url = sender.avatar_url

    async def binfo():
        title = 'The current commands for the Boundless section are:'
        helpDistances = "b!distances - display distances inbetween planets on a server"
        helpPortals = "b!portals - display portal requirements"
        helpUniverse = "b!universe - display a map of the universe, and the punk stargates"
        description = "**1.- **`" + helpDistances + "`\n**2.- **`" + helpPortals + "`\n**3.- **`" + helpUniverse + "`\n**4.- **`b!help - show this message`\n**5.- **`!help - list all of the help sections`"
        embed = discord.Embed(description = description, colour = 0xBECCE0)
        embed.set_author(name = title, icon_url = avatar_url)
        embed.set_footer(text="Enter a number to execute that command.")
        await client.send_message(message.channel, embed = embed)
        response = await client.wait_for_message(author = sender, timeout = 60)
        response = int(response.content)
        lines = int(description.count("\n") + 1)
        if int(response) <= int(lines):
            if response == 1:
                await bdistances()
            elif response == 2:
                await bportals()
            elif response == 3:
                await buniverse()
            elif response == 4:
                await binfo()
            elif response == 5:
                await info()
            else:
                pass
        else:
            title = "Error!"
            description = "There is no command corresponding to that number."
            embed = discord.Embed(description = description, colour = 0xDC5A46)
            embed.set_author(name = title, icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)

    async def info():
        title = 'The different help sections are:'
        description = "**1.- **`b!help - help for the Boundless section of the bot`"
        embed = discord.Embed(description = description, colour = 0xBECCE0)
        embed.set_author(name = title, icon_url = avatar_url)
        embed.set_footer(text="Enter a number to execute that command.")
        await client.send_message(message.channel, embed = embed)
        lines = int(description.count("\n") + 1)
        response = await client.wait_for_message(author = sender, timeout = 60)
        response = int(response.content)
        if response <= lines:
            if response == 1:
                await binfo()
        else:
            title = "Error!"
            description = "There is no command corresponding to that number."
            embed = discord.Embed(description = description, colour = 0xDC5A46)
            embed.set_author(name = title, icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)

    async def brecipes():
        args = message.content.split(" ")
        try:
            outputItem = args[1]
            outputItem = outputItem.upper()

            with open ("outputs", "rb") as fp:
                outputs = pickle.load(fp)
            with open ("jsonData", "rb") as jd:
                data = pickle.load(jd)
            if outputItem in outputs:
                index = outputs.index(outputItem)

                inputs = data["recipes"][index]["inputs"]

                n = 0
                inputItems = []
                inputQuantities = []
                skills = []
                while True:
                    try:
                        inputItems.append(inputs[n]["inputItem"])
                        inputQuantities.append(inputs[n]["inputQuantity"])
                        n += 1
                    except:
                        skills.append(data["recipes"][index]["prerequisites"])
                        machine = data["recipes"][index]["machine"]
                        hand = data["recipes"][index]["canHandCraft"]
                        duration = data["recipes"][index]["duration"]
                        power = data["recipes"][index]["powerRequired"]
                        spark = data["recipes"][index]["spark"]
                        wear = data["recipes"][index]["wear"]
                        output = data["recipes"][index]["outputItem"]
                        outputNum = data["recipes"][index]["outputQuantity"]
                        break
                out = PrettyTable(["Outputs:", "Normal", "Bulk", "Mass"])
                out.add_row([output, outputNum[0], outputNum[1], outputNum[2]])
                
                table = PrettyTable(["Requires:", "Normal", "Bulk", "Mass"])
                table.align["Requires:"] = "l"
                for item in inputItems:
                    nor = inputQuantities[inputItems.index(item)][0]
                    bul = inputQuantities[inputItems.index(item)][1]
                    mas = inputQuantities[inputItems.index(item)][2]
        
                    table.add_row([item, nor, bul, mas])
                table.add_row(["Spark", spark[0], spark[1], spark[2]])
                table.add_row(["Power", power, power, power])
                table.add_row(["Time", str(duration[0]) + 's', str(duration[1]) + 's', str(duration[2]) + 's'])

                embed = discord.Embed(description = "`" + out.get_string() + "`" + "\n" + "`" + table.get_string() + "`", colour = 0xAE86C4)
                embed.set_author(name = "Recipe for " + output, icon_url = avatar_url)
                embed.set_footer(text = str(skills[0]) + "\n" + machine)

                await client.send_message(message.channel, embed = embed)
                
            else:
                title = "Error!"
                description = "There is no recipe for that item"
                embed = discord.Embed(description = description, colour = 0xDC5A46)
                embed.set_author(name = str(title), icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
        
        except:
            title = "Incorrect usage!"
            description = "The correct usage is `b!recipe outputItem`"
            embed = discord.Embed(description = description, colour = 0xDC5A46)
            embed.set_author(name = title, icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)
        

    async def bdistance(server):
            title = "Here are the distances between planets on Boundless' " + server + " server:"
            embed = discord.Embed(colour = 0xAE86C4)
            if server == "live":
                id_server = "469227663803023370/"
            elif server == "testing":
                id_server = "469227666512281605/"
            else:
                id_server = "469227665296195586/"
            embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/"+ id_server +"distances_" + server + ".png")
            embed.set_author(name = title, icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)

    async def bdistances():
        args = message.content.split(" ")
        try:
            if args[1] == "live":
                await bdistance("live")
                return
            elif args[1] == "testing":
                await bdistance("testing")
                return
            elif args[1] == "staging":
                await bdistance("staging")
                return
            else:
                title = "Error!"
                description = "These distances haven't been uploaded yet, or that Boundless server doesn't exist."
                embed = discord.Embed(description = description, colour = 0xDC5A46)
                embed.set_author(name = title, icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
                return
            return
        except:
            description = "**1.- **`live`**\n2.- **`testing`**\n3.- **`staging`"
            embed = discord.Embed(description = description, colour = 0xBECCE0)
            embed.set_author(name = "Select a server:", icon_url = avatar_url)
            embed.set_footer(text="Enter a number to select that server.")
            await client.send_message(message.channel, embed = embed)
            response = await client.wait_for_message(author = sender, timeout = 60)
            response = int(response.content)
            lines = int(description.count("\n") + 1)
            if int(response) <= int(lines):
                if response == 1:
                    await bdistance("live")
                elif response == 2:
                    await bdistance("testing")
                elif response == 3:
                    await bdistance("staging")
            else:
                title = "Error!"
                description = "There is no server corresponding to that number."
                embed = discord.Embed(description = description, colour = 0xDC5A46)
                embed.set_author(name = title, icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
            

    async def bportals():
        title = "Here are the portal requirements in Boundless:"
        embed = discord.Embed(colour = 0xA0A0A)
        embed.set_author(name = title, icon_url = avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227668311900170/portalTables.png")
        await client.send_message(message.channel, embed = embed)

    async def buniverse():
        embed = discord.Embed(colour = 0xE2B660)
        embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227664369254411/Cuttlepunk_Stargates.jpg")
        embed.set_author(name = "Here is a map of the live universe in Boundless:", icon_url = avatar_url)
        await client.send_message(message.channel, embed = embed)

    async def createrole():
        await client.send_message(message.channel, sender)
        args = message.content.split(" ")
        arg1 = str(args[1])
        role = await client.create_role(sender.server, name = arg1)

        title = "Assign this role a colour? If yes, enter a hex colour code. If no, reply 'N'."
        embed = discord.Embed(colour = 0xA0A0A)
        embed.set_author(name = title, icon_url = avatar_url)
        
        await client.send_message(message.channel, embed = embed)
        response = await client.wait_for_message(author = message.author, timeout = 60)
        response = str(response.content)
        if response.startswith("#"):
            response = response.replace("#", "")
            colour = discord.Colour(int(response, 16))
        elif response.lower().startswith("0x"):
            colour = discord.Colour(int(response, 16))
        elif response.lower() == "n":
            colour = role.colour
        else:
            try:
                colour = discord.Colour(int(response, 16))
            except:
                colour = role.colour
                description = "Invalid response. The default colour will be used."
                embed = discord.Embed(description = description, colour = 0xDC5A46)
                embed.set_author(name = "Error!", icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
        await client.edit_role(sender.server, role, colour = colour, name=arg1)

        title = "Make this role mentionable? Y/n?"
        embed = discord.Embed(colour = 0xA0A0A)
        embed.set_author(name = title, icon_url = avatar_url)
        await client.send_message(message.channel, embed = embed)
        response = await client.wait_for_message(author = message.author, timeout = 60)
        response = str(response.content)
        if response.lower() == 'n':
            mentionable = False
            await client.edit_role(sender.server, role, mentionable = mentionable, colour = colour, name=arg1)
        elif response.lower() == 'y':
            mentionable = True
            await client.edit_role(sender.server, role, mentionable = mentionable, colour = colour, name=arg1)
        else:
            description = "Invalid response. The default option will be used."
            embed = discord.Embed(description = description, colour = 0xDC5A46)
            embed.set_author(name = "Error!", icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)

        title = "List players with this role seperately? Y/n?"
        embed = discord.Embed(title = title, colour = 0xA0A0A)
        embed.set_author(name = title, icon_url = avatar_url)
        await client.send_message(message.channel, embed = embed)
        response = await client.wait_for_message(author = message.author, timeout = 60)
        response = str(response.content)
        if response.lower() == 'n':
            pass
        elif response.lower() == 'y':
            await client.edit_role(sender.server, role, hoist = True, mentionable = mentionable, colour = colour, name=arg1)
        else:
            description = "Invalid response. The default setting will be used."
            embed = discord.Embed(description = description, colour = 0xDC5A46)
            embed.set_author(name = "Error!", icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)
    
    if message.author == client.user:
        return

    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

    if message.content.lower().startswith('!help') or message.content.lower().startswith('!info'):
        await info()

    if message.content.lower().startswith("b!recipe"):
        await brecipes()

    if message.content.lower().startswith('b!help') or message.content.lower().startswith('b!info'):
        await binfo()

    if message.content.lower().startswith('b!distance'):
        await bdistances()

    if message.content.lower().startswith('b!portal'):
        await bportals()

    if message.content.lower().startswith('b!universe'):
        await buniverse()

    if message.content.lower().startswith("!createrole") and str(message.author) == "willcrutchley#1331":
        await createrole()
            
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
