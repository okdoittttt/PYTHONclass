import telegram

class Telegram:

    # Telegram API
    chat_token = "5412707226:AAH0GcrnT16aKknamkQW7j0ntXi76l9cREY"
    chat = telegram.Bot(token = chat_token)
    updates = chat.getUpdates()
    # for u in updates:
    #     print(u.message['chat']['id'])

    def sendMessege(self):
        # bot = telegram.Bot(self.chat_token)
        # text = '등록되지 않은 사람이 인식되었습니다.'
        # bot.sendMessage(chat_id = "5526673347", text=text)
        print("sendMesege call")

    def sendImg(self, img):
        # bot = telegram.Bot(self.chat_token)
        # bot.send_photo(chat_id = '5526673347', photo=open(img, 'rb'))
        print("sendImg call")
    def send(self, q):
        while True:
            name = q.get()
            if name == 'Unknown':
                self.sendMessege()
                self.sendImg('Unknown.jpg')