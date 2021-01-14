import discord
import random
import re
import os
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()
set = 0
word = ("ばなな")
end = ("たべたい")
nu = 1
run = 0
stop = 0

@client.event
async def on_ready():
    print("れんとうぼっと（かり）")
    print('ろぐいんしたよー')

@client.event
async def on_message(message):

    global n,nu,word,end,set,run,stop

    if message.content.startswith("あたまのわるいひと") and client.user != message.author and set == 0:
        await message.channel.send('ばなな')

    if message.content.startswith("バナナでも食ってろ！") and client.user != message.author and set == 0:
        await message.channel.send('はーい')
        await client.logout()

    if message.content.startswith("ばなな") and client.user != message.author and set == 0:
        banana = ('ばなな\n''なんで\n''ないの', "たべたい", "おいしい","ほしい","えいごだと\nVANANA","ちょうだい")
        await message.channel.send(random.choice(banana))

    if message.content.startswith("連投設定") and client.user != message.author and set == 0:
        set = 5
        talk = ("でばんだねー","なにいえばいいー？","ぼくにまかせてー",)
        await message.channel.send(random.choice(talk))
        await message.channel.send('ことばをかいてー')
        await client.wait_for("message")
        await message.channel.send('わかったー')

    if set == 5 and client.user != message.author:
        word = message.content
        print(word)

    if set == 5 and message.content.startswith("わかったー"):
        set = 4

    if set == 4:
        set = 3
        await message.channel.send('おわりのことばかいてー')
        await client.wait_for("message")
        await message.channel.send('あいあいあさー')

    if set == 3 and client.user != message.author:
        end = message.content
        print(end)

    if set == 3 and message.content.startswith("あいあいあさー"):
        set = 2

    if set == 2:
        set = 1
        await message.channel.send('すうじかいてー')
        await client.wait_for("message")

    if set == 1 and client.user != message.author:
        n = re.sub("\\D", "", message.content)
        n1 = int(n)
        nu = n1
        print(nu)
        await message.channel.send('おっけー')
        text_a = "{}かいだねー"
        text_b = text_a.format(nu)
        await message.channel.send(text_b)
        set = 0

    if message.content.startswith("連投開始") and client.user != message.author:
        run = 1
        num = 0
        while num < nu:
            num += 1
            await message.channel.send(word)
        await message.channel.send(end)
        run = 0
        print("連投終了")
        if stop ==1:
            await message.channel.send('れんとうちゅーししたよー')
            print("れんとうちゅーししたよー")
            stop = 0

    if message.content.startswith("連投中止") and client.user != message.author and set == 0 and run == 1:
        nu = 0
        stop = 1


    if message.content.startswith("連投中止") and client.user != message.author and set == 0 and run == 0:
        await message.channel.send("れんとうしてないよー")


client.run(token)
