from flask import Flask, render_template, jsonify
from models import db, Player
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
    # Add one player if none exists
    if not Player.query.first():
        db.session.add(Player())
        db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def toggle_inventory():
    player = Player.query.first()
    inventory = {
        'Plant Fiber': player.fiber,
        'Sticks': player.sticks,
        'Stones': player.stones,
        'Rope': player.rope,
        'Wooden Handles': player.wooden_handles
    }
    return jsonify(inventory)

@app.route('/crafting')
def toggle_crafting_menu():
    player = Player.query.first()
    crafting_options = [
        {
            'name': 'Craft Rope',
            'cost': {'Plant Fiber': 10},
            'available': player.fiber >= 10},
        {
            'name': 'Craft Wooden Handle',
            'cost': {'Sticks': 4, 'Rope': 2},
            'available': player.sticks >= 4 and player.rope >= 2
        }
    ]
    return jsonify(crafting_options)



@app.route('/collect_fiber', methods=['POST'])
def collect_fiber():
    player = Player.query.first()

    if random.random() < 0.9:
        player.fiber += 1
        db.session.commit()
        return jsonify({'message': f'You found +1 Plant Fiber! Inventory: Plant Fiber {player.fiber}'})
    else:
        return jsonify({'message': 'You searched but found no Plant Fiber...'})


@app.route('/collect_stick', methods=['POST'])
def collect_stick():
    player = Player.query.first()

    if random.random() < 0.7:
        player.sticks += 1
        db.session.commit()
        return jsonify({'message': f'You got +1 Stick! Inventory: Sticks {player.sticks}'})
    else:
        return jsonify({'message': 'You searched but found no Sticks...'})


@app.route('/collect_stone', methods=['POST'])
def collect_stone():
    player = Player.query.first()

    if random.random() < 0.5:
        player.stones += 1
        db.session.commit()
        return jsonify({'message': f'You got +1 Stone! Inventory: Stones {player.stones}'})
    else:
        return jsonify({'message': 'You searched but found no Stones...'})


@app.route('/craft_rope', methods=['POST'])
def craft_rope():
    player = Player.query.first()

    if player.fiber >= 10:
        player.fiber -= 10
        player.rope += 1
        db.session.commit()
        return jsonify({'message': f'You got +1 Rope! Inventory: Rope {player.rope}'})
    else:
        return jsonify({'message': f"You don't have enough resources to craft a Rope. You have {player.fiber} Plant Fiber"})


@app.route('/craft_wooden_handle', methods=['POST'])
def craft_wooden_handle():
    player = Player.query.first()

    if player.sticks >= 4 and player.rope >= 2:
        player.sticks -= 4
        player.rope -= 2
        player.wooden_handles += 1
        db.session.commit()
        return jsonify({'message': f'You got +1 Wooden Handle! Inventory: Wooden Handles - {player.wooden_handles}'})
    else:
        return jsonify({'message': f"You don't have enough resources to craft a Wooden Handle. You have {player.sticks} Sticks, {player.rope} Rope"})




if __name__ == '__main__':
  app.run(debug=True)