from flask import Flask, request
import json
import requests

app = Flask(__name__)

# Token do seu bot
TOKEN = 'seu_token_aqui'
URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# Endpoint do webhook
@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    data = request.json
    chat_id = data['message']['chat']['id']
    text = data['message']['text']

    # Enviar uma resposta automática
    message = "Você disse: " + text
    requests.post(URL, data={'chat_id': chat_id, 'text': message})

    return 'ok', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
