from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # Agar bisa diakses dari frontend

# Database Item Gacha
GACHA_POOL = [
    {"name": "Armor Fish", "rarity": "Mitos", "color": "gray", "weight": 60},
    {"name": "Sharp One", "rarity": "Mitos Rare", "color": "gray", "weight": 50},
    {"name": "Hammer Head Shark", "rarity": "Mitos Epic", "color": "blue", "weight": 25},
    {"name": "Primodial Octopus", "rarity": "Mitos Legendary", "color": "blue", "weight": 25},
    {"name": "Nutcracker Ray", "rarity": "Mitos Mythical", "color": "purple", "weight": 5},
    {"name": "Sikrit Bebas Pilih", "rarity": "Secret", "color": "gold", "weight": 1}
]

@app.route('/api/pull')
def pull_gacha():
    # Logika RNG berdasarkan bobot (weight)
    items = [item for item in GACHA_POOL]
    weights = [item['weight'] for item in GACHA_POOL]
    
    # Acak 1 item
    result = random.choices(items, weights=weights, k=1)[0]
    
    return jsonify({
        "status": "success",
        "result": result
    })



# Ini penting untuk Vercel
if __name__ == '__main__':
    app.run()