import os
import json

print("=== Проверка текстур и моделей ===\n")

# Проверка текстур предметов
item_textures = set()
for file in os.listdir("src/main/resources/assets/lotsoffood/textures/item"):
    if file.endswith(".png"):
        item_textures.add(file.replace(".png", ""))

print(f"Найдено текстур предметов: {len(item_textures)}")

# Проверка моделей предметов
item_models = set()
missing_textures = []
for file in os.listdir("src/main/resources/assets/lotsoffood/models/item"):
    if file.endswith(".json"):
        model_name = file.replace(".json", "")
        item_models.add(model_name)
        
        # Проверяем, есть ли текстура для этой модели
        if model_name not in item_textures:
            missing_textures.append(model_name)

print(f"Найдено моделей предметов: {len(item_models)}")

if missing_textures:
    print(f"\n⚠️ Отсутствуют текстуры для {len(missing_textures)} предметов:")
    for name in sorted(missing_textures)[:20]:  # Показываем первые 20
        print(f"  - {name}")
    if len(missing_textures) > 20:
        print(f"  ... и ещё {len(missing_textures) - 20}")
else:
    print("✅ Все модели предметов имеют текстуры!")

# Проверка текстур блоков
block_textures = set()
for file in os.listdir("src/main/resources/assets/lotsoffood/textures/block"):
    if file.endswith(".png"):
        block_textures.add(file.replace(".png", ""))

print(f"\nНайдено текстур блоков: {len(block_textures)}")

# Проверка моделей блоков
block_models = set()
missing_block_textures = []
for file in os.listdir("src/main/resources/assets/lotsoffood/models/block"):
    if file.endswith(".json"):
        model_name = file.replace(".json", "")
        block_models.add(model_name)
        
        # Читаем модель и проверяем текстуры
        with open(f"src/main/resources/assets/lotsoffood/models/block/{file}", "r") as f:
            try:
                model_data = json.load(f)
                if "textures" in model_data:
                    for tex_key, tex_path in model_data["textures"].items():
                        if tex_path.startswith("lotsoffood:block/"):
                            tex_name = tex_path.replace("lotsoffood:block/", "")
                            if tex_name not in block_textures:
                                missing_block_textures.append(f"{model_name} -> {tex_name}")
            except:
                pass

print(f"Найдено моделей блоков: {len(block_models)}")

if missing_block_textures:
    print(f"\n⚠️ Отсутствуют текстуры для {len(missing_block_textures)} блоков:")
    for name in sorted(set(missing_block_textures))[:20]:
        print(f"  - {name}")
    if len(missing_block_textures) > 20:
        print(f"  ... и ещё {len(missing_block_textures) - 20}")
else:
    print("✅ Все модели блоков имеют текстуры!")

print("\n=== Проверка завершена ===")
