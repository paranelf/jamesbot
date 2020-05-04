import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("RainbowSix Siege")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("잘가"):
        await message.channel.send("안녕히계세요 ㅠㅠ")
    if message.content.startswith("하이"):
        await message.channel.send("안녕하세요!!")
    if message.content.startswith("태양만세!!"):
        await message.channel.send("\\\[T]/")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
