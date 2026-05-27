import os
import json

# Create recipes directory
os.makedirs("src/main/resources/data/lotsoffood/recipes", exist_ok=True)

recipes_count = 0

# Smelting recipes for meats and fish
smelting_recipes = [
    ("baconcru", "baconcuit", 0.35),
    ("chevalcru", "chevalcuit", 0.35),
    ("calamarcru", "calamarcuit", 0.35),
    ("colincru", "colincuit", 0.35),
    ("truitecrue", "truitecuite", 0.35),
    ("solecrue", "solecuite", 0.35),
    ("poissonorcru", "poissonorcuit", 0.35),
    ("barcru", "barcuit", 0.35),
]

for raw, cooked, exp in smelting_recipes:
    recipe = {
        "type": "minecraft:smelting",
        "ingredient": {"item": f"lotsoffood:{raw}"},
        "result": f"lotsoffood:{cooked}",
        "experience": exp,
        "cookingtime": 200
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{cooked}_from_smelting.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Smoking recipes (faster cooking)
for raw, cooked, exp in smelting_recipes:
    recipe = {
        "type": "minecraft:smoking",
        "ingredient": {"item": f"lotsoffood:{raw}"},
        "result": f"lotsoffood:{cooked}",
        "experience": exp,
        "cookingtime": 100
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{cooked}_from_smoking.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Campfire cooking
for raw, cooked, exp in smelting_recipes:
    recipe = {
        "type": "minecraft:campfire_cooking",
        "ingredient": {"item": f"lotsoffood:{raw}"},
        "result": f"lotsoffood:{cooked}",
        "experience": exp,
        "cookingtime": 600
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{cooked}_from_campfire.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Sandwiches
sandwiches = [
    ("sandfrom", [{"item": "lotsoffood:tranche"}, {"item": "lotsoffood:fromage"}, {"item": "lotsoffood:tranche"}]),
    ("sandjamb", [{"item": "lotsoffood:tranche"}, {"item": "minecraft:cooked_porkchop"}, {"item": "lotsoffood:tranche"}]),
    ("sandpoiss", [{"item": "lotsoffood:tranche"}, {"item": "minecraft:cooked_cod"}, {"item": "lotsoffood:tranche"}]),
    ("sandpoul", [{"item": "lotsoffood:tranche"}, {"item": "minecraft:cooked_chicken"}, {"item": "lotsoffood:tranche"}]),
    ("sandbacon", [{"item": "lotsoffood:tranche"}, {"item": "lotsoffood:baconcuit"}, {"item": "lotsoffood:tranche"}]),
    ("sandboeuf", [{"item": "lotsoffood:tranche"}, {"item": "minecraft:cooked_beef"}, {"item": "lotsoffood:tranche"}]),
]

for name, ingredients in sandwiches:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": ingredients,
        "result": {"item": f"lotsoffood:{name}"}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{name}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Bread slice from bread
recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [{"item": "minecraft:bread"}],
    "result": {"item": "lotsoffood:tranche", "count": 4}
}
with open("src/main/resources/data/lotsoffood/recipes/tranche.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Ice creams (need ice cream machine in full version, but for now simple recipes)
ice_creams = [
    ("glacechoco", "lotsoffood:chocolat"),
    ("glacevanille", "lotsoffood:vanille"),
    ("glacefraise", "lotsoffood:fraise"),
    ("glacebanane", "lotsoffood:banane"),
    ("glacecaramel", "lotsoffood:caramel"),
    ("glacecerise", "lotsoffood:cerise"),
    ("glacecoco", "lotsoffood:noixdecoco"),
    ("glaceraisin", "lotsoffood:raisin"),
    ("glacepomme", "minecraft:apple"),
    ("glacemelon", "minecraft:melon_slice"),
    ("glacechocoblanc", "lotsoffood:chocolatblanc"),
    ("glacecafe", "lotsoffood:grainscafe"),
]

for ice_cream, ingredient in ice_creams:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            {"item": ingredient},
            {"item": "minecraft:snowball"},
            {"item": "minecraft:sugar"}
        ],
        "result": {"item": f"lotsoffood:{ice_cream}"}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{ice_cream}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Juices
juices = [
    ("juspomme", "minecraft:apple"),
    ("jusmelon", "minecraft:melon_slice"),
    ("jusbanane", "lotsoffood:banane"),
    ("jusraisin", "lotsoffood:raisin"),
    ("juscarotte", "minecraft:carrot"),
    ("justomate", "lotsoffood:tomate"),
    ("juscactus", "minecraft:cactus"),
]

for juice, ingredient in juices:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            {"item": ingredient},
            {"item": ingredient},
            {"item": "lotsoffood:verre"}
        ],
        "result": {"item": f"lotsoffood:{juice}"}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{juice}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Coconut milk
recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        {"item": "lotsoffood:noixdecocoouverte"},
        {"item": "lotsoffood:verre"}
    ],
    "result": {"item": "lotsoffood:juscoco"}
}
with open("src/main/resources/data/lotsoffood/recipes/juscoco.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Hot drinks
recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        {"item": "lotsoffood:grainscafe"},
        {"item": "lotsoffood:mug"},
        {"item": "minecraft:water_bucket"}
    ],
    "result": {"item": "lotsoffood:cafe"}
}
with open("src/main/resources/data/lotsoffood/recipes/cafe.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        {"item": "lotsoffood:chocolat"},
        {"item": "lotsoffood:mug"},
        {"item": "minecraft:milk_bucket"}
    ],
    "result": {"item": "lotsoffood:chocochaud"}
}
with open("src/main/resources/data/lotsoffood/recipes/chocochaud.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Milkshakes
milkshakes = [
    ("milkshakechoco", "lotsoffood:chocolat"),
    ("milkshakefraise", "lotsoffood:fraise"),
    ("milkshakevanille", "lotsoffood:vanille"),
    ("milkshakecaramel", "lotsoffood:caramel"),
    ("milkshakechocoblanc", "lotsoffood:chocolatblanc"),
]

for milkshake, ingredient in milkshakes:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            {"item": ingredient},
            {"item": "minecraft:milk_bucket"},
            {"item": "minecraft:ice"},
            {"item": "lotsoffood:verre"}
        ],
        "result": {"item": f"lotsoffood:{milkshake}"}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{milkshake}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Pasta recipes
recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        {"item": "minecraft:wheat"},
        {"item": "minecraft:wheat"},
        {"item": "minecraft:egg"}
    ],
    "result": {"item": "lotsoffood:pates", "count": 2}
}
with open("src/main/resources/data/lotsoffood/recipes/pates.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Pasta with toppings
pasta_recipes = [
    ("patepoulet", "minecraft:cooked_chicken"),
    ("patepiment", "lotsoffood:piment"),
    ("patetomate", "lotsoffood:tomate"),
    ("patechampi", "minecraft:brown_mushroom"),
]

for pasta, topping in pasta_recipes:
    recipe = {
        "type": "minecraft:crafting_shapeless",
        "ingredients": [
            {"item": "lotsoffood:pates"},
            {"item": topping}
        ],
        "result": {"item": f"lotsoffood:{pasta}"}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{pasta}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Carbonara
recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        {"item": "lotsoffood:pates"},
        {"item": "lotsoffood:baconcuit"},
        {"item": "minecraft:egg"}
    ],
    "result": {"item": "lotsoffood:patecarbonara"}
}
with open("src/main/resources/data/lotsoffood/recipes/patecarbonara.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Popcorn
recipe = {
    "type": "minecraft:smelting",
    "ingredient": {"item": "lotsoffood:mais"},
    "result": "lotsoffood:popcorn",
    "experience": 0.1,
    "cookingtime": 100
}
with open("src/main/resources/data/lotsoffood/recipes/popcorn.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Hard boiled egg
recipe = {
    "type": "minecraft:smelting",
    "ingredient": {"item": "minecraft:egg"},
    "result": "lotsoffood:oeufdur",
    "experience": 0.1,
    "cookingtime": 200
}
with open("src/main/resources/data/lotsoffood/recipes/oeufdur.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Mashed potato
recipe = {
    "type": "minecraft:crafting_shapeless",
    "ingredients": [
        {"item": "minecraft:baked_potato"},
        {"item": "minecraft:baked_potato"},
        {"item": "minecraft:milk_bucket"}
    ],
    "result": {"item": "lotsoffood:puree"}
}
with open("src/main/resources/data/lotsoffood/recipes/puree.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Decorative blocks
blocks = [
    ("chocobloc", "lotsoffood:chocolat"),
    ("caram", "lotsoffood:caramel"),
    ("bricksucre", "minecraft:sugar"),
    ("cocobloc", "lotsoffood:noixdecoco"),
    ("alguebloc", "lotsoffood:algues"),
]

for block, ingredient in blocks:
    recipe = {
        "type": "minecraft:crafting_shaped",
        "pattern": ["XXX", "XXX", "XXX"],
        "key": {"X": {"item": ingredient}},
        "result": {"item": f"lotsoffood:{block}"}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{block}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Fences
fences = [
    ("chocofence", "lotsoffood:chocobloc"),
    ("caramfence", "lotsoffood:caram"),
    ("sugarfence", "lotsoffood:bricksucre"),
]

for fence, block in fences:
    recipe = {
        "type": "minecraft:crafting_shaped",
        "pattern": ["XSX", "XSX"],
        "key": {
            "X": {"item": block},
            "S": {"item": "minecraft:stick"}
        },
        "result": {"item": f"lotsoffood:{fence}", "count": 3}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{fence}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Stairs
stairs = [
    ("chocostairs", "lotsoffood:chocobloc"),
    ("caramstairs", "lotsoffood:caram"),
    ("sugarstairs", "lotsoffood:bricksucre"),
]

for stair, block in stairs:
    recipe = {
        "type": "minecraft:crafting_shaped",
        "pattern": ["X  ", "XX ", "XXX"],
        "key": {"X": {"item": block}},
        "result": {"item": f"lotsoffood:{stair}", "count": 4}
    }
    with open(f"src/main/resources/data/lotsoffood/recipes/{stair}.json", "w") as f:
        json.dump(recipe, f, indent=2)
    recipes_count += 1

# Glass and mug
recipe = {
    "type": "minecraft:crafting_shaped",
    "pattern": ["G G", " G "],
    "key": {"G": {"item": "minecraft:glass"}},
    "result": {"item": "lotsoffood:verre", "count": 3}
}
with open("src/main/resources/data/lotsoffood/recipes/verre.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

recipe = {
    "type": "minecraft:crafting_shaped",
    "pattern": ["C C", "C C", " C "],
    "key": {"C": {"item": "minecraft:clay_ball"}},
    "result": {"item": "lotsoffood:mug"}
}
with open("src/main/resources/data/lotsoffood/recipes/mug.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Chef hat
recipe = {
    "type": "minecraft:crafting_shaped",
    "pattern": ["WWW", "W W"],
    "key": {"W": {"item": "minecraft:white_wool"}},
    "result": {"item": "lotsoffood:chapeauchef"}
}
with open("src/main/resources/data/lotsoffood/recipes/chapeauchef.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

# Picnic basket
recipe = {
    "type": "minecraft:crafting_shaped",
    "pattern": ["S S", "P P", "PPP"],
    "key": {
        "S": {"item": "minecraft:stick"},
        "P": {"item": "minecraft:oak_planks"}
    },
    "result": {"item": "lotsoffood:panier"}
}
with open("src/main/resources/data/lotsoffood/recipes/panier.json", "w") as f:
    json.dump(recipe, f, indent=2)
recipes_count += 1

print(f"Generated {recipes_count} recipes!")
