# QuestionBoxBot

質問箱風のDiscord Botです

## DEMO

![1857374d031d0808bbefd12628f2ba1a.png (642×394)](https://i.gyazo.com/1857374d031d0808bbefd12628f2ba1a.png)

![cb4d8b8ee6ae9c07791be2a387687be0.png (375×249)](https://i.gyazo.com/cb4d8b8ee6ae9c07791be2a387687be0.png)

## Features
BotにDMを送ると、匿名化して特定のチャンネルにメッセージを転送してくれます。
これにより、Discord内で質問をすることに対する心理的安全性を確保する目的があります。
要するに、質問をすることのハードルを下げることが目的です。
質問が公開されることで、同じ質問をする人を減らせる。回答できる人が増える。
情報共有になる。など、メリットがたくさんあります。

DM質問問題を解決できたらと思います。


## required
- Python 3.9
## Usage
GCPなどでVMインスタンスを立てます。
info.json にBotトークンと転送したいチャンネルIDを書き込みます。
チャンネルIDは、後で`/set`コマンドを用いて実装する場合は適当な数字で大丈夫です。

```bash
$ git clone https://github.com/t4t5u0/DiscordQuestionBoxBot.git
$ cd question_bot
$ pip install -r requirements.txt
$ vim info.json
$ nohup python main.py &
```
してください。環境によっては`python3` や `pip3` を指定しなければいけないことがあります。
