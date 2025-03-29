from app import create_app, db
from app.models import Hero, Power, HeroPower
import random

def seed_database():
    app = create_app()
    with app.app_context():
        print("🌱 Seeding database...")
        
        print("Deleting existing data...")
        HeroPower.query.delete()
        Hero.query.delete()
        Power.query.delete()
        
        print("Creating heroes...")
        heroes_data = [
            {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
            {"name": "Doreen Green", "super_name": "Squirrel Girl"},
            {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
            {"name": "Janet Van Dyne", "super_name": "The Wasp"},
            {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
            {"name": "Carol Danvers", "super_name": "Captain Marvel"},
            {"name": "Jean Grey", "super_name": "Dark Phoenix"},
            {"name": "Ororo Munroe", "super_name": "Storm"},
            {"name": "Kitty Pryde", "super_name": "Shadowcat"},
            {"name": "Elektra Natchios", "super_name": "Elektra"}
        ]
        
        heroes = []
        for hero_info in heroes_data:
            hero = Hero(name=hero_info["name"], super_name=hero_info["super_name"])
            heroes.append(hero)
        
        db.session.add_all(heroes)
        
        print("Creating powers...")
        powers_data = [
            {
                "name": "super strength",
                "description": "gives the wielder super-human strengths"
            },
            {
                "name": "flight",
                "description": "gives the wielder the ability to fly through the skies at supersonic speed"
            },
            {
                "name": "super human senses",
                "description": "allows the wielder to use her senses at a super-human level"
            },
            {
                "name": "elasticity",
                "description": "can stretch the human body to extreme lengths"
            }
        ]
        
        powers = []
        for power_info in powers_data:
            power = Power(name=power_info["name"], description=power_info["description"])
            powers.append(power)
        
        db.session.add_all(powers)
        db.session.commit()
        
        print("Creating hero powers...")
        strengths = ["Strong", "Weak", "Average"]
        
        for hero in heroes:
            for _ in range(random.randint(1, 3)):
                power = random.choice(powers)
                strength = random.choice(strengths)
                
                hero_power = HeroPower(hero=hero, power=power, strength=strength)
                db.session.add(hero_power)
        
        db.session.commit()
        print("✅ Done seeding!")

if __name__ == "__main__":
    seed_database()