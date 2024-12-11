from flask import Flask, request
import json

app = Flask(__name__)

# Endpoint do webhook
@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    # Pega os dados que o Telegram manda
    data = request.json

    # Aqui, você pode adicionar a lógica para responder às mensagens
    print(f"Mensagem recebida: {json.dumps(data)}")

    # Retorna um "ok" para o Telegram
    return "ok", 200

if __name__ == '__main__':
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
