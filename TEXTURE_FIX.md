# Исправление путей к текстурам для Minecraft 1.20.1

## Проблема

В Minecraft 1.20.1 изменились пути к текстурам:
- Старый путь: `assets/modid/textures/items/` → Новый путь: `assets/modid/textures/item/`
- Старый путь: `assets/modid/textures/blocks/` → Новый путь: `assets/modid/textures/block/`

## Что было сделано

### 1. Переименованы папки с текстурами
```
src/main/resources/assets/lotsoffood/textures/items/ 
  → src/main/resources/assets/lotsoffood/textures/item/

src/main/resources/assets/lotsoffood/textures/blocks/ 
  → src/main/resources/assets/lotsoffood/textures/block/
```

### 2. Удалены ненужные папки
- `textures/models/` - не используется в Minecraft 1.20.1
- `textures/gui/` - не используется в текущей версии мода

### 3. Обновлены скрипты генерации моделей

Исправлены пути в следующих скриптах:
- `generate_advanced_blocks.py` - для fence, stairs, cakes
- `generate_crop_models.py` - для растений

Изменено:
```python
# Было:
"texture": f"lotsoffood:blocks/{texture_name}"

# Стало:
"texture": f"lotsoffood:block/{texture_name}"
```

### 4. Перегенерированы все модели блоков

Все модели теперь используют правильные пути:
- Модели предметов: `lotsoffood:item/название`
- Модели блоков: `lotsoffood:block/название`

## Структура текстур после исправления

```
src/main/resources/assets/lotsoffood/textures/
├── item/           (150+ текстур предметов)
│   ├── chocolat.png
│   ├── fromage.png
│   ├── pizza.png
│   └── ...
└── block/          (90+ текстур блоков)
    ├── chocobloc.png
    ├── caram.png
    ├── croptomate0.png
    ├── croptomate1.png
    └── ...
```

## Проверка

После исправления:
1. ✅ Сборка проекта успешна (`./gradlew build`)
2. ✅ Все модели используют правильные пути
3. ✅ Текстуры находятся в правильных папках

## Как проверить текстуры в игре

1. Соберите мод: `./gradlew build`
2. Запустите клиент: `./gradlew runClient`
3. В игре откройте креативный инвентарь (E)
4. Найдите вкладку "Lots of Food"
5. Проверьте, что все предметы и блоки имеют текстуры

Если текстуры отображаются правильно - всё работает! 🎉

## Возможные проблемы

### Розовые/чёрные кубики вместо текстур

**Причина**: Неправильные пути в моделях или отсутствующие текстуры

**Решение**:
1. Проверьте, что папки названы `item` и `block` (без 's' в конце)
2. Проверьте, что в моделях используются пути `lotsoffood:item/` и `lotsoffood:block/`
3. Перегенерируйте модели:
   ```bash
   python generate_advanced_blocks.py
   python generate_crop_models.py
   ```

### Текстуры не загружаются

**Причина**: Текстуры не скопированы из оригинального мода

**Решение**:
```bash
# Скопируйте текстуры из распакованного мода
Copy-Item -Recurse -Force "Lots of Food-unpacked/assets/pda/textures" "src/main/resources/assets/lotsoffood/textures"

# Переименуйте папки
Move-Item "src/main/resources/assets/lotsoffood/textures/items" "src/main/resources/assets/lotsoffood/textures/item" -Force
Move-Item "src/main/resources/assets/lotsoffood/textures/blocks" "src/main/resources/assets/lotsoffood/textures/block" -Force
```

## Итог

Все текстуры теперь находятся в правильных папках и используют правильные пути. Мод готов к запуску и тестированию в Minecraft 1.20.1!
