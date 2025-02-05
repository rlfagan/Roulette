from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room
import random
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Store game state
players = {}
bets = {}
game_locked = False

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    """ Handles a player joining the game """
    player_id = data['player_id']
    players[player_id] = 100  # Starting chips
    join_room("roulette")
    emit("update_players", {"players": players}, broadcast=True)

@socketio.on('place_bet')
def handle_bet(data):
    """ Handles bet placement """
    global bets
    if game_locked:
        emit("error", {"message": "Betting is closed!"})
        return

    player_id = data['player_id']
    bet_amount = data['bet_amount']
    bet_number = data['bet_number']

    if player_id in players and players[player_id] >= bet_amount:
        players[player_id] -= bet_amount
        bets[player_id] = {"number": bet_number, "amount": bet_amount}
        emit("update_bets", {"bets": bets}, broadcast=True)
    else:
        emit("error", {"message": "Not enough chips!"})

@socketio.on('lock_bets')
def lock_bets():
    """ Locks betting and starts the spin """
    global game_locked
    game_locked = True
    emit("bets_locked", {}, broadcast=True)
    time.sleep(3)  # Simulate delay
    spin_wheel()

def spin_wheel():
    """ Spins the roulette wheel and announces the winner """
    winning_number = random.randint(0, 36)
    emit("spin_result", {"winning_number": winning_number}, broadcast=True)

    for player, bet in bets.items():
        if bet["number"] == winning_number:
            players[player] += bet["amount"] * 35  # 35x payout for a single-number bet

    emit("update_players", {"players": players}, broadcast=True)
    reset_game()

def reset_game():
    """ Resets the game for the next round """
    global bets, game_locked
    bets = {}
    game_locked = False

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
