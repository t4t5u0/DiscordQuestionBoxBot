# question_box

Python3 質問箱風 Discord Botです

# DEMO

# Features
BotにDMを送ると特定のチャンネルに匿名化してメッセージを送信してくれます
これにより、質問に対する心理的安全性を確保する目的があります。
質問が公開になることで、同じ質問をする人を減らせる。回答できる人が増える。
情報共有になるなど、メリットがたくさんあります。

# Requirments
依存パッケージは

- discord.py
- discord
- aiohttp

# Installattion
```bash
$ pip install -r requirements.txt
```
で取得してください。環境によっては`pip3`を指定しなければいけないことがあります。

# Usage
GCPなどで、VMインスタンスを立てます
info.json にBotトークンとチャンネルIDを書き込みます

```bash
$ git clone https://github.com/t4t5u0/question_box.git
$ cd question_bot
$ vim info.json
$ nohup python main.py &
```
してください。環境によっては`python3` を指定しなければいけないことがあります。
