from flask import Blueprint, jsonify, request, make_response
from .models import db, Hero, Power, HeroPower

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Superheroes API",
        "available_endpoints": {
            "GET /heroes": "Get all heroes",
            "GET /heroes/<id>": "Get hero by ID",
            "GET /powers": "Get all powers",
            "GET /powers/<id>": "Get power by ID",
            "PATCH /powers/<id>": "Update power description",
            "POST /hero_powers": "Create hero power association"
        }
    })

@main.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name
    } for hero in heroes])

@main.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": [{
            "id": hp.power.id,
            "name": hp.power.name,
            "description": hp.power.description
        } for hp in hero.hero_powers]
    })

@main.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{
        "id": power.id,
        "name": power.name,
        "description": power.description
    } for power in powers])

@main.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    return jsonify({
        "id": power.id,
        "name": power.name,
        "description": power.description
    })

@main.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()
    try:
        if 'description' in data:
            power.description = data['description']
            db.session.commit()
            return jsonify({
                "id": power.id,
                "name": power.name,
                "description": power.description
            })
    except ValueError as e:
        return jsonify({"errors": ["validation errors"]}), 400

@main.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    try:
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])
        
        if not hero or not power:
            return jsonify({"error": "Hero or Power not found"}), 404

        hero_power = HeroPower(
            strength=data['strength'],
            hero=hero,
            power=power
        )
        db.session.add(hero_power)
        db.session.commit()
        
        return jsonify({
            "id": hero_power.id,
            "strength": hero_power.strength,
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            },
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            }
        })
    except ValueError:
        return jsonify({"errors": ["validation errors"]}), 400