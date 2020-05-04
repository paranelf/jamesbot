import discord
import requests
import asyncio
from json import loads


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("RainbowSix Siege")
    await client.change_presence(status=discord.Status.online, activity=game)
    channel = client.get_channel()
    twitch = input(1)
    if input(1) is None
       await channel.send('트위치아이디를 입력해주세요.')
    text = input(3)
    server = input(4)

    a = 0
    while True:
        headers = {'Client-ID': '3hc6pf8pdxq22xvtxe0d79kr3d9mk1'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch,
                                headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(text)
                a = 1
        except:
            a = 0
        await asyncio.sleep(2)


@client.event
async def on_message(message):
    if message.content.startswith("잘가"):
        await message.channel.send("안녕히계세요 ㅠㅠ")
    if message.content.startswith("하이"):
        await message.channel.send("안녕하세요!!")
    if message.content.startswith("태양만세!!"):
        await message.channel.send("\\\[T]/")
    elif message.content.startswith("트위치설정"):
        await message.channel.send("알림을 받을 스트리머의 트위치 아이디를 입력하세요.")
        msg = await client.wait_for('msg', timeout=15.0, check=None)



        if msg is None:
           await message.channel.send("15초내로 입력해주세요. 다시시도:트위치설정")
           return
        else:
            await message.channel.send("알림에 사용할 별명을 입력해주세요.")
            msg2 = await client.wait_for(msg2, timeout=15.0, check=None)


            if msg2 is None:
               await message.channel.send("15초내로 입력해주세요. 다시시도:트위치설정")
               return
            else:
                await message.channel.send("알림에 사용할 문장을 입력해주세요.")
                msg3 = await client.wait_for(input(3), timeout=15.0, check=None)


                if msg3 is None:
                   await message.channel.send("15초내로 입력해주세요. 다시시도:트위치설정")
                   return
                else:
                    await message.channel.send("알림을 보낼 채널아이디를 입력해주세요.")
                    msg4 = await client.wait_for(input(4), timeout=15.0, check=None)


                    if msg4 is None:
                       await message.channel.send("15초내로 입력해주세요. 다시시도:트위치설정")
                       return
                    else:
                        await message.channel.send("설정이 완료되었습니다.")



client.run("NzA2NzM5MTU2ODE0MTM1MzA3.Xq-oqQ.wceIW9rAdTyUKqoQn5ieoxnerbU")