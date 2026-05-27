#!/usr/bin/env python3
"""
Script to generate block model and blockstate JSON files
"""

import os
import json

blocks = [
    "chocobloc", "caram", "bricksucre", "cocobloc"
]

# Create directories
model_dir = "src/main/resources/assets/lotsoffood/models/block"
blockstate_dir = "src/main/resources/assets/lotsoffood/blockstates"
os.makedirs(model_dir, exist_ok=True)
os.makedirs(blockstate_dir, exist_ok=True)

for block in blocks:
    # Create block model
    model = {
        "parent": "minecraft:block/cube_all",
        "textures": {
            "all": f"lotsoffood:block/{block}"
        }
    }
    
    model_path = os.path.join(model_dir, f"{block}.json")
    with open(model_path, 'w') as f:
        json.dump(model, f, indent=2)
    print(f"Created {model_path}")
    
    # Create blockstate
    blockstate = {
        "variants": {
            "": {
                "model": f"lotsoffood:block/{block}"
            }
        }
    }
    
    blockstate_path = os.path.join(blockstate_dir, f"{block}.json")
    with open(blockstate_path, 'w') as f:
        json.dump(blockstate, f, indent=2)
    print(f"Created {blockstate_path}")

print(f"\nGenerated {len(blocks)} block models and blockstates!")
