import io
import json
import csv

import aiohttp
import discord

json_open = open('./info.json', 'r')
json_load = json.load(json_open)

client = discord.Client()

@client.event
async def on_ready():
    # print('ログインしました')
    # print('-'*40)
    pass

# DMにメッセージが送信されたら、テキストや画像を取得して
# channel に send する
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if str(message.channel.type) != 'private':
        return
    to_send_channel = client.get_channel(json_load['channel_id'])    
    # print(f'message:{message}')
    text = message.content
    if len(text):
        with open('./store.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([message.id ,message.author ,message.content])
        await to_send_channel.send(text)
    # 受信したファイルを取得する
    for file_ in message.attachments:
        file_url = file_.url
        file_name = file_.filename
        async with aiohttp.ClientSession() as session:
            async with session.get(file_url) as resp:
                if resp.status != 200:
                    return await to_send_channel.send('ファイルを取得できませんでした')
                data = io.BytesIO(await resp.read())
                # 送信部分
                await to_send_channel.send(file=discord.File(data, file_name))

client.run(json_load['token'])
