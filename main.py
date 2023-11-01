from flask import Flask, render_template
from game_of_life import GameOfLife
app = Flask(__name__)

@app.route('/')
def index():
    game = GameOfLife(25,25)
    return render_template(
        'index.html',
        game=game

    )



@app.route('/live')
def live():
    current_game = GameOfLife()
    current_game.form_new_generation()
    return render_template(
        'live.html',
        current_game=current_game

    )

if __name__=='__main__':
    app.run(debug=True)
