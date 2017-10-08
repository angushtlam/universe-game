from flask import Flask, jsonify, request
# from mongoengine import connect

from game import controller as game_controller

# connect('mongodb://alphonce:ubcsebetteryouandme1967@ds113835.mlab.com:13835/universe-game')

app = Flask(__name__)
game = game_controller.Game()


@app.route('/')
def landing():
    return 'Hello!'


@app.route('/api/get_current_game')
def api_get_current_game():
    return jsonify({'status': game.get_game_status()})


@app.route('/api/start_new_game')
def api_start_new_game():
    game.start_new_game()
    return jsonify({'status': game.get_game_status()})


@app.route('/api/submit_update', methods=['POST'])
def api_submit_update():
    content = request.get_json()
    name = content.get('name', None)
    new_page = content.get('page', None)

    if name is None or new_page is None:
        return jsonify({'error': 'missing name or page'})

    game.update_player(name, new_page)

    return jsonify({'status': game.get_game_status()})
