import asyncio
import discord


app = discord.Client()

# 1-6에서 생성된 토큰을 이곳에 입력해주세요.
token = "NjEwMDAyMjgzNjI2ODg5MjE2.XU-7LQ.EFjqPvIVIN9LRCRF-AqIbHzVhrI"


# 봇이 구동되었을 때 동작되는 코드입니다.
@app.event
async def on_ready():
    print("Logged in as ")  # 화면에 봇의 아이디, 닉네임이 출력됩니다.
    print(app.user.name)
    print(app.user.id)
    print("===========")
    # 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
    # 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
    activity = discord.Game(name="Macbook12\'")
    await app.change_presence(status=discord.Status.idle, activity=activity)


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@app.event
async def on_message(message):
    if message.author.bot:  # 만약 메시지를 보낸사람이 봇일 경우에는
        return None  # 동작하지 않고 무시합니다.

    id = message.author.id  # id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel  # channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!커맨드'):  # 만약 해당 메시지가 '!커맨드' 로 시작하는 경우에는
        await channel.send('답변')  # 봇은 해당 채널에 '답변' 라고 말합니다.
    else:  # 위의 if에 해당되지 않는 경우
        # 메시지를 보낸사람을 호출하며 말한 메시지 내용을 그대로 출력해줍니다.
        msg = "<@"+str(id)+">님이 \""+message.content+"\"라고 말하였습니다."
        await channel.send(msg)

app.run(token)
