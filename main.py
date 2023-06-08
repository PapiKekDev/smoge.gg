import discord

token = 'token here'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('https://twitter.com/'):
        temp = message.content
        link = temp.replace('https://twitter.com/','https://fxtwitter.com/')
        usor = message.author.name
        await message.channel.send("{}\n{}".format(usor, link))
        await message.delete()

client.run(token)
