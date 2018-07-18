import asyncio, discord, os, pickle
TOKEN = 'NDY4ODM1NDAxODE0MTE0MzA0.DjAHiA.Y-6dmYg3pTb52vYfwwRg1ifXWFc'

client = discord.Client()

directory = os.path.dirname(os.path.abspath(__file__))

@client.event
async def on_message(message):
    sender = message.author
    avatar_url = sender.avatar_url
    if message.author == client.user:
        return

    if message.content.startswith('!help'):
        title = 'The different help sections are:'
        description = "`b!help - help for the Boundless section of the bot`"
        embed = discord.Embed(description = description, colour = 0xBECCE0)
        embed.set_author(name = title, icon_url = avatar_url)
        await client.send_message(message.channel, embed = embed)

    if message.content.startswith("b!recipe"):
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
                while True:
                    try:
                        inputItems.append(inputs[n]["inputItem"])
                        inputQuantities.append(inputs[n]["inputQuantity"])
                        n += 1
                    except:
                        break
                for item in inputItems:
                    await client.send_message(message.channel, item)
                    await client.send_message(message.channel, inputQuantities[inputItems.index(item)])
            else:
                title = "Error!"
                description = "There is no recipe for that item"
                embed = discord.Embed(description = description, colour = 0xDC5A46)
                embed.set_author(name = title, icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
    
        except:
            title = "Error!"
            description = "The correct usage is `b!recipe outputItem`"
            embed = discord.Embed(description = description, colour = 0xDC5A46)
            embed.set_author(name = title, icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)
    
    if message.content.startswith('b!help'):
        title = 'The current commands for the Boundless section are:'
        helpDistances = "b!distances - display distances inbetween planets on a server"
        helpPortals = "\nb!portals - display portal requirements"
        helpUniverse = "\nb!universe - display a map of the universe, and the punk stargates"
        args = message.content.split(" ")
        try:
            if args[1].lower() == "distances":
                description = "`" + helpDistances + "`"
            elif args[1].lower() == "portals":
                description = "`" + helpPortals + "`"
            elif args[1].lower() == "universe":
                description = "`" + helpUniverse + "`"
        except:
            description = "`" + helpDistances + helpPortals + helpUniverse + "\nb!help - show this message or display help on a specific 'b!'command \n!help - list all of the help sections`"
        embed = discord.Embed(description = description, colour = 0xBECCE0)
        embed.set_author(name = title, icon_url = avatar_url)
        await client.send_message(message.channel, embed = embed)
        '''
        title = 'The different help sections are:'
        description = "`b!help - help for the Boundless section of the bot`"
        embed = discord.Embed(description = description, colour = 0xBECCE0)
        embed.set_author(name = title, icon_url = avatar_url)
        description = "`b!help - help for the Boundless section of the bot`"
        await client.send_message(message.channel, embed = embed)
        '''

    if message.content.startswith('b!distances'):
        args = message.content.split(" ")
        try:
            if args[1] == "live":
                title = "Here are the distances between planets on Boundless' live server:"
                embed = discord.Embed(colour = 0xAE86C4)
                embed.set_author(name = title, icon_url = avatar_url)
                embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227663803023370/distances_live.png")
                await client.send_message(message.channel, embed = embed)
            elif args[1] == "testing":
                title = "Here are the distances between planets on Boundless' testing server:"
                embed = discord.Embed(colour = 0xAE86C4)
                embed.set_author(name = title, icon_url = avatar_url)
                embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227666512281605/distances_testing.png")
                await client.send_message(message.channel, embed = embed)
            elif args[1] == "staging":
                title = "Here are the distances between planets on Boundless' staging server:"
                embed = discord.Embed(colour = 0xAE86C4)
                embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227665296195586/distances_staging.png")
                embed.set_author(name = title, icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
            else:
                title = "Error!"
                description = "These distances haven't been uploaded yet, or that Boundless server doesn't exist."
                embed = discord.Embed(description = description, colour = 0xDC5A46)
                embed.set_author(name = title, icon_url = avatar_url)
                await client.send_message(message.channel, embed = embed)
        except:
            description = "`b!distances serverName`"
            embed = discord.Embed(description = description, colour = 0xBECCE0)
            embed.set_author(name = "The correct usage is:", icon_url = avatar_url)
            await client.send_message(message.channel, embed = embed)
    if message.content.startswith('b!portals'):
        title = "Here are the portal requirements in Boundless:"
        embed = discord.Embed(colour = 0xA0A0A)
        embed.set_author(name = title, icon_url = avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227668311900170/portalTables.png")
        await client.send_message(message.channel, embed = embed)

    if message.content.startswith('b!universe'):
        embed = discord.Embed(colour = 0xE2B660)
        embed.set_image(url="https://cdn.discordapp.com/attachments/469227496018149406/469227664369254411/Cuttlepunk_Stargates.jpg")
        embed.set_author(name = "Here is a map of the live universe in Boundless:", icon_url = avatar_url)
        await client.send_message(message.channel, embed = embed)

    if message.content.startswith("!createrole") and str(message.author) == "willcrutchley#1331":
        await client.send_message(message.channel, sender)
        args = message.content.split(" ")
        arg1 = str(args[1])
        role = await client.create_role(sender.server, name = arg1)

        # ---------- #

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

        # ---------- #

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

        # ---------- #

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
            
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
