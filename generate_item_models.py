#!/usr/bin/env python3
"""
Script to generate item model JSON files for Lots of Food mod
"""

import os
import json

# List of all items that need models
items = [
    "chocolat", "caramel", "fromage", "fraise", "banane", "raisin", "cerise",
    "tomate", "piment", "mais", "vanille", "noixdecoco", "pizza", "sushi",
    "gateauchoco", "gateaucarotte", "gateaufraise", "cheesecake",
    "glacechoco", "glacevanille", "glacefraise", "glacebanane",
    "juspomme", "jusmelon", "cafe", "verre", "mug"
]

# List of blocks that need item models
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
    print(f"Created {filepath}")

# Generate block item models
for block in blocks:
    model = {
        "parent": f"lotsoffood:block/{block}"
    }
    
    filepath = os.path.join(model_dir, f"{block}.json")
    with open(filepath, 'w') as f:
        json.dump(model, f, indent=2)
    print(f"Created {filepath}")

print(f"\nGenerated {len(items) + len(blocks)} item models!")
