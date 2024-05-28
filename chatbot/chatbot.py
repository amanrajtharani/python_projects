from flask import Flask,render_template,requests
from chatterbot import Chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = Chatbot("ChatterBot",storage_adapter="chatterBot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = requests.args.get('chat-input')
    return str(english_bot.get_response(userText))

if __name__=="__main__":
    app.run(debug=True)

