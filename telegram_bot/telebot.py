import telepot

class TeleBot:
    def __init__(self, token):
        self.token = token
        self.mc = "1352182483"
    
    def send(self, msg):
        bot = telepot.Bot(self.token)
        bot.sendMessage(self.mc, msg)