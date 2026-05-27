import os
import json
import shutil

print("=== Исправление моделей блоков ===\n")

# 1. Исправляем модель кокосового блока
cocobloc_model = {
    "parent": "minecraft:block/cube_column",
    "textures": {
        "end": "lotsoffood:block/cocobloc_topbottom1",
        "side": "lotsoffood:block/cocobloc_side"
    }
}
with open("src/main/resources/assets/lotsoffood/models/block/cocobloc.json", "w") as f:
    json.dump(cocobloc_model, f, indent=2)
print("✅ Исправлена модель cocobloc")

# 2. Копируем текстуры блоков в папку item для BlockItem
blocks_needing_item_textures = [
    "bricksucre",
    "caram",
    "chocobloc",
    "cocobloc_side"  # Для кокоса используем боковую текстуру
]

for block_name in blocks_needing_item_textures:
    src = f"src/main/resources/assets/lotsoffood/textures/block/{block_name}.png"
    # Для кокоса переименовываем
    if block_name == "cocobloc_side":
        dst = "src/main/resources/assets/lotsoffood/textures/item/cocobloc.png"
    else:
        dst = f"src/main/resources/assets/lotsoffood/textures/item/{block_name}.png"
    
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"✅ Скопирована текстура: {block_name}")
    else:
        print(f"⚠️ Текстура не найдена: {src}")

print("\n=== Исправление завершено ===")
