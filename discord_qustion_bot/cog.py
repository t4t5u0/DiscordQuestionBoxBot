import csv
import io
import json
from typing import OrderedDict

import aiohttp
import discord
from discord.ext import commands


class QuestionBotCog(commands.Cog, name="QuestionBox"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        with open('./info.json', 'r') as f:
            self.json_load = json.load(f)
        self.channel_id: int = self.json_load['channel_id']

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # botには反応しない
        if message.author.bot:
            return
        # DM限定
        if str(message.channel.type) != 'private':
            return
        to_send_channel: discord.TextChannel = self.bot.get_channel(
            self.channel_id)
        if not to_send_channel:
            return await message.author.send('転送対象のテキストチャンネルが見つかりません。転送したいチャンネルで`/set`と送信してください。')
        text = message.content
        if text:
            with open('./store.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow([message.id, message.author, message.content])
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

    @commands.command(name='set')
    async def _set(self, ctx: commands.Context):
        "質問を転送するチャンネルを設定します"
        channel_id: int = ctx.channel.id
        self.channel_id = channel_id
        with open('./info.json', 'r+') as f:
            updated = json.load(f, object_pairs_hook=OrderedDict)
            updated['channel_id'] = channel_id
            json.dump(updated, f, indent=4, ensure_ascii=False)
        await ctx.send('メッセージを転送するチャンネルをこのチャンネルに変更しました')


def setup(bot: commands.Bot):
    return bot.add_cog(QuestionBotCog(bot))
