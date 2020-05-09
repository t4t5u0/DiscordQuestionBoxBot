import io
import aiohttp
import json

import discord

json_open = open('./info.json', 'r')
json_load = json.load(json_open)

client = discord.Client()

# to_send_channel = client.get_channel(json_load['channel_id'])

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
    to_send_channel = client.get_channel(json_load['channel_id'])    
    print(f'message:{message}')
    text = message.content
    if len(text):
        await to_send_channel.send(text)
    for image in message.attachments:
        image_url = image.url
        image_name = image.filename
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as resp:
                if resp.status != 200:
                    return await to_send_channel.send('画像を取得できませんでした')
                data = io.BytesIO(await resp.read())
                await to_send_channel.send(file=discord.File(data, image_name))

client.run(json_load['token'])
