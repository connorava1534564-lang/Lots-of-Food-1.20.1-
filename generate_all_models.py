#!/usr/bin/env python3
"""
Complete script to generate all item models for Lots of Food mod
"""

import os
import json

# Complete list of all items from ModItems.java
items = [
    # Basic Foods
    "chocolat", "caramel", "fromage", "fraise", "banane", "raisin", "cerise",
    "tomate", "piment", "mais", "vanille", "noixdecoco",
    
    # Meats
    "baconcru", "baconcuit", "chevalcru", "chevalcuit", "calamarcru", "calamarcuit",
    
    # Fish
    "colincru", "colincuit", "truitecrue", "truitecuite", "solecrue", "solecuite",
    "poissonorcru", "poissonorcuit", "barcru", "barcuit",
    
    # Prepared Foods
    "tranche", "sandfrom", "sandjamb", "sandpoiss", "sandpoul", "sandbacon", "sandboeuf",
    
    # Soups
    "fishsoup", "citrouilsoup", "cactusoup", "soupelegumes", "soupepoulet", "ragoutalgues", "pho",
    
    # Pasta
    "pates", "patepoulet", "patepiment", "patetomate", "patechampi", "patecarbonara",
    
    # Desserts
    "crepe", "crepecaram", "crepechoco", "crepefrom", "crepesucre",
    "cupcake", "cupcakechoco", "cupcakefraise",
    "donutchoco", "donutfraise", "donutglace", "donutraisin",
    "tartetatin", "blackforest", "painchoco", "pommedamour", "bananasplit", "saladefruits",
    "marshmallow", "marshmallowstick", "marshmallowstickcooked",
    "fortunecookie", "cookiechocoblanc", "papillote",
    
    # Cakes
    "gateauchoco", "gateaucarotte", "gateaufraise", "cheesecake",
    
    # Ice Creams
    "glacechoco", "glacevanille", "glacefraise", "glacebanane", "glacecaramel",
    "glacecerise", "glacecoco", "glaceraisin", "glacepomme", "glacemelon",
    "glacechocoblanc", "glacecafe",
    
    # Special Foods
    "steakfrites", "fishandchips", "steaktartare", "chili", "chorizo", "brochette",
    "takoyaki", "popcorn", "oeufdur", "puree", "porcaramel", "biscuitchien",
    "gateaufaim", "zombiepure", "algues", "chocolatblanc", "chocopim", "pizza", "sushi",
    
    # Juices
    "juspomme", "jusmelon", "jusbanane", "jusraisin", "juscarotte", "justomate",
    "juscactus", "juscoco",
    
    # Hot Drinks
    "cafe", "chocochaud", "thevert", "thenoir", "theblanc",
    
    # Milkshakes
    "milkshakechoco", "milkshakefraise", "milkshakevanille", "milkshakecaramel",
    "milkshakechocoblanc",
    
    # Alcoholic
    "vin", "cidre", "rhum", "vodka",
    
    # Ingredients
    "grainscafe", "seaufromage", "noixdecocoouverte",
    
    # Seeds
    "seedpiment", "seedtomate",
    
    # Utility
    "verre", "mug", "panier"
]

# Blocks that need item models
blocks = [
    "chocobloc", "caram", "bricksucre", "cocobloc"
]

# Create directory if it doesn't exist
model_dir = "src/main/resources/assets/lotsoffood/models/item"
os.makedirs(model_dir, exist_ok=True)

# Generate item models
for item in items:
    model = {
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": f"lotsoffood:item/{item}"
        }
    }
    
    filepath = os.path.join(model_dir, f"{item}.json")
    with open(filepath, 'w') as f:
        json.dump(model, f, indent=2)

print(f"Generated {len(items)} item models!")

# Generate block item models
for block in blocks:
    model = {
        "parent": f"lotsoffood:block/{block}"
    }
    
    filepath = os.path.join(model_dir, f"{block}.json")
    with open(filepath, 'w') as f:
        json.dump(model, f, indent=2)

print(f"Generated {len(blocks)} block item models!")
print(f"Total: {len(items) + len(blocks)} models created!")
