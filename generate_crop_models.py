import os
import json

# Create directories
os.makedirs("src/main/resources/assets/lotsoffood/models/block", exist_ok=True)
os.makedirs("src/main/resources/assets/lotsoffood/blockstates", exist_ok=True)

# Crops with 5 stages (0-4)
crops_5_stages = [
    ("croppiment", 5),
    ("cropcafe", 5),
    ("cropvanille", 5),
    ("cropvigne", 5),
    ("fraisier", 5)
]

# Crops with 6 stages (0-5)
crops_6_stages = [
    ("croptomate", 6)
]

# Corn with 5 stages (0-4)
crops_corn = [
    ("cropmaisbottom", 5)
]

def create_crop_models(crop_name, max_stage):
    # Create blockstate
    blockstate = {"variants": {}}
    for age in range(max_stage):
        blockstate["variants"][f"age={age}"] = {"model": f"lotsoffood:block/{crop_name}{age}"}
    # Add remaining ages pointing to last stage
    for age in range(max_stage, 8):
        blockstate["variants"][f"age={age}"] = {"model": f"lotsoffood:block/{crop_name}{max_stage-1}"}
    
    with open(f"src/main/resources/assets/lotsoffood/blockstates/{crop_name}.json", "w") as f:
        json.dump(blockstate, f, indent=2)
    
    # Create models for each stage
    for stage in range(max_stage):
        crop_model = {
            "parent": "minecraft:block/crop",
            "textures": {
                "crop": f"lotsoffood:block/{crop_name}{stage}"
            }
        }
        with open(f"src/main/resources/assets/lotsoffood/models/block/{crop_name}{stage}.json", "w") as f:
            json.dump(crop_model, f, indent=2)
    
    print(f"Created crop models and blockstate for {crop_name} ({max_stage} stages)")

# Generate all crops
for crop_name, stages in crops_5_stages:
    create_crop_models(crop_name, stages)

for crop_name, stages in crops_6_stages:
    create_crop_models(crop_name, stages)

for crop_name, stages in crops_corn:
    create_crop_models(crop_name, stages)

print("\nAll crop models and blockstates generated!")
