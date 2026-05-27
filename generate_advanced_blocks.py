import os
import json

# Create directories if they don't exist
os.makedirs("src/main/resources/assets/lotsoffood/models/block", exist_ok=True)
os.makedirs("src/main/resources/assets/lotsoffood/blockstates", exist_ok=True)

# Fence blocks
fences = [
    ("chocofence", "chocobloc"),
    ("caramfence", "caram"),
    ("sugarfence", "bricksucre")
]

for fence_name, texture_name in fences:
    # Fence post model
    fence_post = {
        "parent": "minecraft:block/fence_post",
        "textures": {
            "texture": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{fence_name}_post.json", "w") as f:
        json.dump(fence_post, f, indent=2)
    
    # Fence side model
    fence_side = {
        "parent": "minecraft:block/fence_side",
        "textures": {
            "texture": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{fence_name}_side.json", "w") as f:
        json.dump(fence_side, f, indent=2)
    
    # Fence inventory model
    fence_inventory = {
        "parent": "minecraft:block/fence_inventory",
        "textures": {
            "texture": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{fence_name}_inventory.json", "w") as f:
        json.dump(fence_inventory, f, indent=2)
    
    # Fence blockstate
    fence_blockstate = {
        "multipart": [
            {"apply": {"model": f"lotsoffood:block/{fence_name}_post"}},
            {"when": {"north": "true"}, "apply": {"model": f"lotsoffood:block/{fence_name}_side", "uvlock": True}},
            {"when": {"east": "true"}, "apply": {"model": f"lotsoffood:block/{fence_name}_side", "y": 90, "uvlock": True}},
            {"when": {"south": "true"}, "apply": {"model": f"lotsoffood:block/{fence_name}_side", "y": 180, "uvlock": True}},
            {"when": {"west": "true"}, "apply": {"model": f"lotsoffood:block/{fence_name}_side", "y": 270, "uvlock": True}}
        ]
    }
    with open(f"src/main/resources/assets/lotsoffood/blockstates/{fence_name}.json", "w") as f:
        json.dump(fence_blockstate, f, indent=2)
    
    print(f"Created fence models and blockstate for {fence_name}")

# Stairs blocks
stairs = [
    ("chocostairs", "chocobloc"),
    ("caramstairs", "caram"),
    ("sugarstairs", "bricksucre")
]

for stair_name, texture_name in stairs:
    # Stairs model
    stairs_model = {
        "parent": "minecraft:block/stairs",
        "textures": {
            "bottom": f"lotsoffood:block/{texture_name}",
            "top": f"lotsoffood:block/{texture_name}",
            "side": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{stair_name}.json", "w") as f:
        json.dump(stairs_model, f, indent=2)
    
    # Stairs inner model
    stairs_inner = {
        "parent": "minecraft:block/inner_stairs",
        "textures": {
            "bottom": f"lotsoffood:block/{texture_name}",
            "top": f"lotsoffood:block/{texture_name}",
            "side": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{stair_name}_inner.json", "w") as f:
        json.dump(stairs_inner, f, indent=2)
    
    # Stairs outer model
    stairs_outer = {
        "parent": "minecraft:block/outer_stairs",
        "textures": {
            "bottom": f"lotsoffood:block/{texture_name}",
            "top": f"lotsoffood:block/{texture_name}",
            "side": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{stair_name}_outer.json", "w") as f:
        json.dump(stairs_outer, f, indent=2)
    
    # Stairs blockstate
    stairs_blockstate = {
        "variants": {
            "facing=east,half=bottom,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "y": 270, "uvlock": True},
            "facing=east,half=bottom,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner"},
            "facing=east,half=bottom,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "y": 270, "uvlock": True},
            "facing=east,half=bottom,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer"},
            "facing=east,half=bottom,shape=straight": {"model": f"lotsoffood:block/{stair_name}"},
            "facing=east,half=top,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "uvlock": True},
            "facing=east,half=top,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "y": 90, "uvlock": True},
            "facing=east,half=top,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "uvlock": True},
            "facing=east,half=top,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "y": 90, "uvlock": True},
            "facing=east,half=top,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "x": 180, "uvlock": True},
            "facing=north,half=bottom,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "y": 180, "uvlock": True},
            "facing=north,half=bottom,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "y": 270, "uvlock": True},
            "facing=north,half=bottom,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "y": 180, "uvlock": True},
            "facing=north,half=bottom,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "y": 270, "uvlock": True},
            "facing=north,half=bottom,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "y": 270, "uvlock": True},
            "facing=north,half=top,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "y": 270, "uvlock": True},
            "facing=north,half=top,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "uvlock": True},
            "facing=north,half=top,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "y": 270, "uvlock": True},
            "facing=north,half=top,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "uvlock": True},
            "facing=north,half=top,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "x": 180, "y": 270, "uvlock": True},
            "facing=south,half=bottom,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner"},
            "facing=south,half=bottom,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "y": 90, "uvlock": True},
            "facing=south,half=bottom,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer"},
            "facing=south,half=bottom,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "y": 90, "uvlock": True},
            "facing=south,half=bottom,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "y": 90, "uvlock": True},
            "facing=south,half=top,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "y": 90, "uvlock": True},
            "facing=south,half=top,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "y": 180, "uvlock": True},
            "facing=south,half=top,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "y": 90, "uvlock": True},
            "facing=south,half=top,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "y": 180, "uvlock": True},
            "facing=south,half=top,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "x": 180, "y": 90, "uvlock": True},
            "facing=west,half=bottom,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "y": 90, "uvlock": True},
            "facing=west,half=bottom,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "y": 180, "uvlock": True},
            "facing=west,half=bottom,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "y": 90, "uvlock": True},
            "facing=west,half=bottom,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "y": 180, "uvlock": True},
            "facing=west,half=bottom,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "y": 180, "uvlock": True},
            "facing=west,half=top,shape=inner_left": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "y": 180, "uvlock": True},
            "facing=west,half=top,shape=inner_right": {"model": f"lotsoffood:block/{stair_name}_inner", "x": 180, "y": 270, "uvlock": True},
            "facing=west,half=top,shape=outer_left": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "y": 180, "uvlock": True},
            "facing=west,half=top,shape=outer_right": {"model": f"lotsoffood:block/{stair_name}_outer", "x": 180, "y": 270, "uvlock": True},
            "facing=west,half=top,shape=straight": {"model": f"lotsoffood:block/{stair_name}", "x": 180, "y": 180, "uvlock": True}
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/blockstates/{stair_name}.json", "w") as f:
        json.dump(stairs_blockstate, f, indent=2)
    
    print(f"Created stairs models and blockstate for {stair_name}")

# Simple blocks
simple_blocks = [
    ("alguebloc", "alguebloc0"),
    ("assiettebloc", "assiettebloc_up")
]

for block_name, texture_name in simple_blocks:
    block_model = {
        "parent": "minecraft:block/cube_all",
        "textures": {
            "all": f"lotsoffood:block/{texture_name}"
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/models/block/{block_name}.json", "w") as f:
        json.dump(block_model, f, indent=2)
    
    blockstate = {
        "variants": {
            "": {"model": f"lotsoffood:block/{block_name}"}
        }
    }
    with open(f"src/main/resources/assets/lotsoffood/blockstates/{block_name}.json", "w") as f:
        json.dump(blockstate, f, indent=2)
    
    print(f"Created simple block model and blockstate for {block_name}")

# Cake blocks
cakes = [
    ("gateauchocoblock", "gateauchocoblock"),
    ("gateaucarotteblock", "gateaucarotteblock"),
    ("gateaufraiseblock", "gateaufraiseblock"),
    ("cheesecakeblock", "cheesecakeblock"),
    ("tartetatinblock", "tartetatinblock"),
    ("blackforestblock", "blackforestblock")
]

for cake_name, texture_base in cakes:
    # Create blockstate with all bite states
    cake_blockstate = {"variants": {}}
    for bites in range(7):
        cake_blockstate["variants"][f"bites={bites}"] = {"model": f"lotsoffood:block/{cake_name}_slice{bites}"}
    
    with open(f"src/main/resources/assets/lotsoffood/blockstates/{cake_name}.json", "w") as f:
        json.dump(cake_blockstate, f, indent=2)
    
    # Create models for each bite state
    for bites in range(7):
        cake_model = {
            "parent": "minecraft:block/cake_slice" + str(bites) if bites > 0 else "minecraft:block/cake",
            "textures": {
                "particle": f"lotsoffood:block/{texture_base}_side",
                "bottom": f"lotsoffood:block/{texture_base}_bottom",
                "top": f"lotsoffood:block/{texture_base}_top",
                "side": f"lotsoffood:block/{texture_base}_side",
                "inside": f"lotsoffood:block/{texture_base}_inner"
            }
        }
        with open(f"src/main/resources/assets/lotsoffood/models/block/{cake_name}_slice{bites}.json", "w") as f:
            json.dump(cake_model, f, indent=2)
    
    print(f"Created cake models and blockstate for {cake_name}")

print("\nAll advanced block models and blockstates generated!")
