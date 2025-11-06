from flask import Flask, render_template, jsonify, request
from game import make_bot_move, check_winner

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/game')
def game():
    return render_template('index.html')

@app.route('/bot')
def bot():
    return render_template('bot.html')

@app.route('/bot-move', methods=['POST'])
def bot_move():
    data = request.get_json()
    board = data['board']
    bot_symbol = data['bot']
    player_symbol = 'O' if bot_symbol == 'X' else 'X'

    move = make_bot_move(board, bot_symbol)
    board[move] = bot_symbol

    winner = check_winner(board)
    return jsonify({'board': board, 'move': move, 'winner': winner})

if __name__ == '__main__':
    app.run(debug=True)
