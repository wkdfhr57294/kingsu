import discord  
client = discord.Client()
import os


@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("=========================================================================================")

@client.event
async def on_message(message):
    if message.content == "!온클":
        await message.channel.send("https://www.ebsoc.co.kr/")
    if message.content.startswith ("!청소"):
        i = (message.author.guild_permissions.administrator)

        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embedtitle=(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}사용권한 없음".format(message.author.mention))



access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
