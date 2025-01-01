from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from generator import generate_cards, generate_with_gemini
from games import get_game_data
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Suppress gPRC logging warnings
os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

@app.route("/", methods=["GET", "POST"])
def index():
    game_data_options = {
        1: "Krypteret",
        2: "Kortslutning",
        3: "Det burde man jo vide",
        4: "Logik",
        5: "Mime",
        6: "You laugh you lose"
    }
    game_names = [game_data_options[i] for i in game_data_options]

    if request.method == "POST":
        try:
            choice = int(request.form.get("game_choice"))
            num_cards = int(request.form.get("num_cards"))

            if not (1 <= choice <= len(game_data_options)):
                return render_template("index.html", error="Invalid game choice", game_names=game_names)
            if not (1 <= num_cards <= 20):
                return render_template("index.html", error="Please enter a number of cards between 1 and 20.", game_names=game_names)

            game_data = get_game_data(choice)
            if game_data:
                examples, game_name, game_description = game_data
                generated_cards = generate_cards(
                    num_cards, examples, game_name, game_description, generate_with_gemini
                )
                if generated_cards: #Check if cards were generated.
                    session['cards'] = generated_cards
                    session['game_name'] = game_name
                    session['current_card_index'] = 0
                    return redirect(url_for('game'))
                else:
                    return render_template("index.html", error="Could not generate cards.", game_names=game_names)
            else:
                 return render_template("index.html", error="Could not retrieve game data.", game_names=game_names)

        except ValueError:
            return render_template("index.html", error="Invalid input. Please enter numbers.", game_names=game_names)

    return render_template("index.html", game_names=game_names)

@app.route("/game")
def game():
    if 'cards' in session and session['cards']: #Check if cards exist in the session
        cards = session['cards']
        index = session.get('current_card_index',0) #Use get to avoid key error if not present.
        if 0 <= index < len(cards):
            card = cards[index]
            return render_template("game.html", card=card, game_name=session.get('game_name'))
        else:
            session.pop('cards', None)
            session.pop('current_card_index', None)
            return redirect(url_for('index')) #Redirect to the main page if no cards.
    return redirect(url_for('index')) #Redirect to the main page if no cards.


@app.route('/next_card')
def next_card():
    if 'cards' in session and 'current_card_index' in session:
        cards = session['cards']
        current_index = session['current_card_index']
        next_index = current_index + 1
        if next_index < len(cards):
            session['current_card_index'] = next_index
            return jsonify({'success': True})
        else:
            session.pop('cards', None)
            session.pop('current_card_index', None)
            return jsonify({'no_more_cards': True})
    return jsonify({'error': 'No cards available.'}), 400

if __name__ == "__main__":
    app.run(debug=True, port=8000)