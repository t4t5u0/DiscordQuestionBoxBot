import json

import discord

json_open = open('./info.json', 'r')
json_load = json.load(json_open)

client = discord.Client()
@client.event
async def on_ready():
    print('ログインしました')
    print('-'*40)

# DMにメッセージが送信されたら、テキストや画像を取得して
# channel に send する
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if str(message.channel.type) != 'private':
        return
    text = message.content
    to_send_channel = client.get_channel(json_load['channel_id'])
    await to_send_channel.send(text)


client.run(json_load['token'])
