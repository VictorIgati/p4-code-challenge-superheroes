# Superheroes API

A Flask API for tracking heroes and their superpowers.

## Description

This API allows you to manage superheroes and their associated powers. You can:
- View all heroes and their powers
- View individual hero details
- View all available powers
- Update power descriptions
- Create associations between heroes and powers

## Setup Instructions

1. Clone this repository
```bash
git clone <repository-url>
cd superheroes.api
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup the database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

5. Seed the database
```bash
python -m app.seed
```

6. Run the server
```bash
flask run
```

## API Endpoints

### Heroes
- `GET /heroes`
  - Returns a list of all heroes
- `GET /heroes/:id`
  - Returns details of a specific hero and their powers

### Powers
- `GET /powers`
  - Returns a list of all powers
- `GET /powers/:id`
  - Returns details of a specific power
- `PATCH /powers/:id`
  - Updates a power's description

### Hero Powers
- `POST /hero_powers`
  - Creates a new association between a hero and a power

## Models

### Hero
- Attributes:
  - name
  - super_name
- Relationships:
  - Has many Powers through HeroPower

### Power
- Attributes:
  - name
  - description (must be present and at least 20 characters long)
- Relationships:
  - Has many Heroes through HeroPower

### HeroPower
- Attributes:
  - strength (must be one of: 'Strong', 'Weak', 'Average')
- Relationships:
  - Belongs to a Hero
  - Belongs to a Power

## Technologies Used
- Python
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite

## Author
VICTOR IGATI,
Senior backed engineer at Victor's class 