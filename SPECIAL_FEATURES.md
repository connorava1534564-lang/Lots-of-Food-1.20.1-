# Специальные функции мода Lots of Food

## ✨ Добавленные специальные предметы

### 1. 🌶️ Перец (Pepper) - `PepperItem`
**Файл:** `src/main/java/pda/lotsoffood/item/PepperItem.java`

**Эффект:** При употреблении даёт эффект огнестойкости на 30 секунд (600 тиков)

**Использование:**
```java
entity.addEffect(new MobEffectInstance(MobEffects.FIRE_RESISTANCE, 600, 0));
```

---

### 2. 🥠 Печенье с предсказанием (Fortune Cookie) - `FortuneCookieItem`
**Файл:** `src/main/java/pda/lotsoffood/item/FortuneCookieItem.java`

**Эффект:** При употреблении показывает случайное предсказание в чате

**Предсказания:** 10 уникальных сообщений на 3 языках (en, ru, fr)

**Примеры предсказаний:**
- "Ваш код скомпилируется с первого раза!"
- "Приключение уже за углом!"
- "Удача найдёт вас сегодня."

**Локализация:**
- `fortune.lotsoffood.1` до `fortune.lotsoffood.10`

---

### 3. 🎂 Торт голода (Hunger Cake) - `HungerCakeItem`
**Файл:** `src/main/java/pda/lotsoffood/item/HungerCakeItem.java`

**Эффект:** Полностью восстанавливает голод и насыщение

**Использование:**
```java
player.getFoodData().setFoodLevel(20);
player.getFoodData().setSaturation(20.0F);
```

**Питательность:** 20 единиц голода + 20 насыщения (максимум)

---

### 4. 🍵 Чай (Tea) - `TeaItem`
**Файл:** `src/main/java/pda/lotsoffood/item/TeaItem.java`

**Типы чая:**

#### Зелёный чай (Green Tea)
- **Эффект:** Регенерация I на 10 секунд
- **Код:** `MobEffects.REGENERATION, 200, 0`

#### Чёрный чай (Black Tea)
- **Эффект:** Скорость I на 30 секунд
- **Код:** `MobEffects.MOVEMENT_SPEED, 600, 0`

#### Белый чай (White Tea)
- **Эффект:** Удача I на 60 секунд
- **Код:** `MobEffects.LUCK, 1200, 0`

---

### 5. 🍷 Алкогольные напитки - `AlcoholItem`
**Файл:** `src/main/java/pda/lotsoffood/item/AlcoholItem.java`

**Эффект:** Тошнота + замедление (эффект опьянения)

**Типы напитков:**

#### Вино (Wine)
- **Длительность:** 15 секунд (300 тиков)
- **Сила:** Уровень 0
- **Эффекты:** Тошнота I (15с) + Замедление I (7.5с)

#### Сидр (Cider)
- **Длительность:** 10 секунд (200 тиков)
- **Сила:** Уровень 0
- **Эффекты:** Тошнота I (10с) + Замедление I (5с)

#### Ром (Rum)
- **Длительность:** 30 секунд (600 тиков)
- **Сила:** Уровень 1
- **Эффекты:** Тошнота II (30с) + Замедление I (15с)

#### Водка (Vodka)
- **Длительность:** 40 секунд (800 тиков)
- **Сила:** Уровень 2
- **Эффекты:** Тошнота III (40с) + Замедление I (20с)

---

## 📋 Обновлённые регистрации в ModItems.java

### Импорты
```java
import pda.lotsoffood.item.PepperItem;
import pda.lotsoffood.item.FortuneCookieItem;
import pda.lotsoffood.item.HungerCakeItem;
import pda.lotsoffood.item.TeaItem;
import pda.lotsoffood.item.AlcoholItem;
```

### Регистрации
```java
// Перец с эффектом огнестойкости
public static final RegistryObject<Item> PEPPER = ITEMS.register("piment",
    () -> new PepperItem(new Item.Properties().food(Foods.PEPPER)));

// Печенье с предсказанием
public static final RegistryObject<Item> FORTUNE_COOKIE = ITEMS.register("fortunecookie",
    () -> new FortuneCookieItem(new Item.Properties().food(Foods.COOKIE)));

// Торт голода
public static final RegistryObject<Item> HUNGER_CAKE = ITEMS.register("gateaufaim",
    () -> new HungerCakeItem(new Item.Properties().food(Foods.SPECIAL_CAKE)));

// Чаи с эффектами
public static final RegistryObject<Item> GREEN_TEA = ITEMS.register("thevert",
    () -> new TeaItem(new Item.Properties().stacksTo(16).food(Foods.TEA), TeaItem.TeaType.GREEN));

public static final RegistryObject<Item> BLACK_TEA = ITEMS.register("thenoir",
    () -> new TeaItem(new Item.Properties().stacksTo(16).food(Foods.TEA), TeaItem.TeaType.BLACK));

public static final RegistryObject<Item> WHITE_TEA = ITEMS.register("theblanc",
    () -> new TeaItem(new Item.Properties().stacksTo(16).food(Foods.TEA), TeaItem.TeaType.WHITE));

// Алкогольные напитки
public static final RegistryObject<Item> WINE = ITEMS.register("vin",
    () -> new AlcoholItem(new Item.Properties().stacksTo(16), 300, 0));

public static final RegistryObject<Item> CIDER = ITEMS.register("cidre",
    () -> new AlcoholItem(new Item.Properties().stacksTo(16), 200, 0));

public static final RegistryObject<Item> RUM = ITEMS.register("rhum",
    () -> new AlcoholItem(new Item.Properties().stacksTo(16), 600, 1));

public static final RegistryObject<Item> VODKA = ITEMS.register("vodka",
    () -> new AlcoholItem(new Item.Properties().stacksTo(16), 800, 2));
```

---

## 🎮 Как протестировать

### 1. Перец
```
/give @p lotsoffood:piment
```
Съешьте перец → получите огнестойкость на 30 секунд

### 2. Печенье с предсказанием
```
/give @p lotsoffood:fortunecookie
```
Съешьте печенье → увидите предсказание в чате

### 3. Торт голода
```
/give @p lotsoffood:gateaufaim
```
Съешьте торт → голод полностью восстановится

### 4. Чаи
```
/give @p lotsoffood:thevert    # Зелёный - регенерация
/give @p lotsoffood:thenoir    # Чёрный - скорость
/give @p lotsoffood:theblanc   # Белый - удача
```

### 5. Алкоголь
```
/give @p lotsoffood:vin        # Вино - слабое опьянение
/give @p lotsoffood:cidre      # Сидр - очень слабое
/give @p lotsoffood:rhum       # Ром - сильное опьянение
/give @p lotsoffood:vodka      # Водка - очень сильное
```

---

## 📊 Сравнение с оригинальным модом

### ✅ Портировано
- ✅ PepperItem (ItemPiment) - эффект огнестойкости
- ✅ FortuneCookieItem (ItemFortuneCookie) - предсказания
- ✅ HungerCakeItem (ItemGateauFaim) - полное восстановление голода
- ✅ TeaItem (ItemThe) - эффекты от чая
- ✅ AlcoholItem (ItemAlcool) - эффекты опьянения
- ✅ ChefHatItem (ItemChapeauChef) - шапка повара (броня)
- ✅ ModSeedItem (ItemPDASeed) - семена для растений

### ⬜ Не портировано (опционально)
- ⬜ ItemPanier - корзина для пикника с GUI
- ⬜ ItemNoixDeCoco - кокос как снаряд (EntityNoixDeCoco)
- ⬜ ItemPapillote - конфеты с разными текстурами
- ⬜ ItemPoissonOr - золотая рыба с особыми свойствами
- ⬜ TileEntityMachineGlaces - машина мороженого с GUI
- ⬜ TileEntityAssiette - тарелка с рендером
- ⬜ WorldGen классы - генерация мира

---

## 🔧 Технические детали

### Структура классов
```
src/main/java/pda/lotsoffood/item/
├── ChefHatItem.java          # Броня (шапка повара)
├── ModSeedItem.java           # Семена для растений
├── PepperItem.java            # Перец с эффектом
├── FortuneCookieItem.java     # Печенье с предсказаниями
├── HungerCakeItem.java        # Торт голода
├── TeaItem.java               # Чай с эффектами
└── AlcoholItem.java           # Алкогольные напитки
```

### Используемые эффекты
- `MobEffects.FIRE_RESISTANCE` - огнестойкость
- `MobEffects.REGENERATION` - регенерация
- `MobEffects.MOVEMENT_SPEED` - скорость
- `MobEffects.LUCK` - удача
- `MobEffects.CONFUSION` - тошнота (опьянение)
- `MobEffects.MOVEMENT_SLOWDOWN` - замедление

### Локализация
Все специальные сообщения переведены на 3 языка:
- 🇬🇧 English (en_us.json)
- 🇷🇺 Русский (ru_ru.json)
- 🇫🇷 Français (fr_fr.json)

---

## 📝 Заметки для разработчиков

### Добавление новых предсказаний
1. Добавьте ключ в массив `FORTUNES` в `FortuneCookieItem.java`
2. Добавьте переводы в 3 языковых файла

### Изменение эффектов
Параметры эффектов:
- **duration** - длительность в тиках (20 тиков = 1 секунда)
- **amplifier** - сила эффекта (0 = уровень I, 1 = уровень II, и т.д.)

### Балансировка
Текущие значения подобраны для баланса:
- Перец: 30 секунд огнестойкости (достаточно для лавы)
- Чаи: слабые эффекты, но доступные
- Алкоголь: негативные эффекты, усиливаются с крепостью

---

## ✅ Статус сборки

```bash
./gradlew build
```

**Результат:** BUILD SUCCESSFUL in 13s

Все новые классы успешно скомпилированы и интегрированы в мод!

---

**Дата обновления:** 2 марта 2026  
**Версия мода:** 1.20.1-1.0.0  
**Forge версия:** 47.3.0+
