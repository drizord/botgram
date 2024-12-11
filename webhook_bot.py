from flask import Flask, request

app = Flask(__name__)

# Rota para receber o webhook
@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    data = request.json  # Pega os dados enviados pelo Telegram
    print(f"Mensagem recebida: {data}")  # Mostra a mensagem nos logs
    return "ok", 200  # Retorna um status de OK para o Telegram

if __name__ == '__main__':
import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)