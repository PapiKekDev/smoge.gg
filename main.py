import discord

token = 'MTExNTIzNTA0ODIwODIyMDE2MA.GERz_n.znFGIq48D7v4gtxSo_CRp7TKTPZom5NGV14AbM'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('https://twitter.com/'):
        temp = message.content
        final = temp.replace('https://twitter.com/','https://fxtwitter.com/')
        await message.channel.send(final)
        await message.delete()

client.run(token)