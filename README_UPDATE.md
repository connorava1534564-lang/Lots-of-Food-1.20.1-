# Lots of Food - Forge 1.20.1 Update

## Обзор проекта

Это обновленная версия мода "Lots of Food" для Minecraft Forge 1.20.1. Мод был полностью переписан с использованием современного API Forge.

## Структура проекта

```
lotsoffood/
├── src/
│   └── main/
│       ├── java/
│       │   └── pda/
│       │       └── lotsoffood/
│       │           ├── LotsOfFood.java          # Главный класс мода
│       │           └── init/
│       │               ├── ModItems.java        # Регистрация предметов
│       │               ├── ModBlocks.java       # Регистрация блоков
│       │               └── ModCreativeTabs.java # Креативные вкладки
│       └── resources/
│           ├── META-INF/
│           │   └── mods.toml                    # Метаданные мода
│           ├── pack.mcmeta                      # Метаданные ресурспака
│           └── assets/
│               └── lotsoffood/
│                   ├── lang/
│                   │   └── en_us.json           # Переводы
│                   ├── models/
│                   │   ├── item/                # Модели предметов
│                   │   └── block/               # Модели блоков
│                   ├── blockstates/             # Состояния блоков
│                   └── textures/
│                       ├── item/                # Текстуры предметов
│                       └── block/               # Текстуры блоков
├── build.gradle                                 # Конфигурация Gradle
└── gradle.properties                            # Свойства проекта
```

## Основные изменения для Forge 1.20.1

### 1. Регистрация через DeferredRegister

**Старый способ (1.12.2):**
```java
@SubscribeEvent
public void registerItems(RegistryEvent.Register<Item> event) {
    event.getRegistry().register(new Item());
}
```

**Новый способ (1.20.1):**
```java
public class ModItems {
    public static final DeferredRegister<Item> ITEMS = 
        DeferredRegister.create(ForgeRegistries.ITEMS, MOD_ID);
    
    public static final RegistryObject<Item> CHOCOLATE = ITEMS.register("chocolat",
            () -> new Item(new Item.Properties().food(Foods.CHOCOLATE)));
    
    public static void register(IEventBus eventBus) {
        ITEMS.register(eventBus);
    }
}
```

### 2. Креативные вкладки (Creative Tabs)

**Старый способ:**
```java
public static CreativeTabs TAB = new CreativeTabs("lotsoffood") {
    @Override
    public ItemStack createIcon() {
        return new ItemStack(PIZZA);
    }
};
```

**Новый способ:**
```java
public static final RegistryObject<CreativeModeTab> TAB = CREATIVE_MODE_TABS.register("lotsoffood_tab",
    () -> CreativeModeTab.builder()
        .icon(() -> new ItemStack(ModItems.PIZZA.get()))
        .title(Component.translatable("itemGroup.lotsoffood.main"))
        .displayItems((parameters, output) -> {
            output.accept(ModItems.CHOCOLATE.get());
            // ... добавить все предметы
        })
        .build());
```

### 3. Свойства еды (Food Properties)

**Старый способ:**
```java
new ItemFood(2, 0.3f, false);
```

**Новый способ:**
```java
new Item(new Item.Properties().food(
    new FoodProperties.Builder()
        .nutrition(2)
        .saturationMod(0.3f)
        .build()
));
```

### 4. Языковые файлы

**Старый формат (.lang):**
```
item.chocolat.name=Chocolate
```

**Новый формат (.json):**
```json
{
  "item.lotsoffood.chocolat": "Chocolate"
}
```

### 5. Модели и текстуры

- Модели остаются в формате JSON
- Текстуры должны быть в формате PNG
- Путь к текстурам: `assets/lotsoffood/textures/item/` или `block/`

## Инструкции по сборке

### Требования

- Java 17 или выше
- Gradle (включен в проект через wrapper)

### Шаги сборки

1. **Настройка проекта:**
```bash
./gradlew setupDecompWorkspace
```

2. **Сборка мода:**
```bash
./gradlew build
```

Готовый JAR-файл будет в `build/libs/`

3. **Запуск клиента для тестирования:**
```bash
./gradlew runClient
```

4. **Запуск сервера для тестирования:**
```bash
./gradlew runServer
```

## Что уже реализовано

✅ Основная структура мода
✅ Регистрация предметов через DeferredRegister
✅ Регистрация блоков через DeferredRegister
✅ Креативная вкладка
✅ Базовые свойства еды
✅ Модели предметов и блоков
✅ Языковые файлы (en_us.json)
✅ Текстуры (скопированы из старого мода)

## Что нужно добавить

### Приоритет 1 (Основное)
- [ ] Добавить все остальные предметы из старого мода (100+ предметов)
- [ ] Добавить все блоки (заборы, лестницы, торты)
- [ ] Реализовать растения (crops) с ростом
- [ ] Добавить рецепты крафта

### Приоритет 2 (Дополнительно)
- [ ] Машина для мороженого (TileEntity + GUI)
- [ ] Корзина для пикника (Container + GUI)
- [ ] Генерация мира (кокосовые пальмы, кофейные деревья)
- [ ] Специальные эффекты еды (Fortune Cookie, алкоголь)
- [ ] Броня (Chef Hat)

### Приоритет 3 (Полировка)
- [ ] Добавить все языковые файлы (fr_fr, de_de, ru_ru и т.д.)
- [ ] Оптимизация текстур
- [ ] Добавить звуки
- [ ] Документация

## Примеры кода для расширения

### Добавление нового предмета

```java
// В ModItems.java
public static final RegistryObject<Item> NEW_FOOD = ITEMS.register("new_food",
    () -> new Item(new Item.Properties().food(
        new FoodProperties.Builder()
            .nutrition(4)
            .saturationMod(0.5f)
            .build()
    )));
```

### Добавление нового блока

```java
// В ModBlocks.java
public static final RegistryObject<Block> NEW_BLOCK = registerBlock("new_block",
    () -> new Block(BlockBehaviour.Properties.copy(Blocks.STONE)
        .strength(2.0f)
        .sound(SoundType.STONE)));
```

### Добавление рецепта крафта

Создайте файл `src/main/resources/data/lotsoffood/recipes/chocolate.json`:

```json
{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "CCC",
    "CCC",
    "CCC"
  ],
  "key": {
    "C": {
      "item": "minecraft:cocoa_beans"
    }
  },
  "result": {
    "item": "lotsoffood:chocolat",
    "count": 1
  }
}
```

## Отладка

### Проблемы с текстурами

Если текстуры не загружаются:
1. Проверьте путь: `assets/lotsoffood/textures/item/название.png`
2. Проверьте модель: `assets/lotsoffood/models/item/название.json`
3. Убедитесь, что имя файла совпадает с registry name

### Проблемы с регистрацией

Если предметы не появляются:
1. Проверьте, что `ModItems.register(eventBus)` вызывается в конструкторе мода
2. Проверьте логи на ошибки регистрации
3. Убедитесь, что MOD_ID совпадает везде

## Полезные ссылки

- [Forge Documentation](https://docs.minecraftforge.net/)
- [Forge Community Wiki](https://forge.gemwire.uk/wiki/Main_Page)
- [Minecraft Wiki - Data Pack](https://minecraft.wiki/w/Data_pack)
- [Parchment Mappings](https://parchmentmc.org/)

## Лицензия

Оригинальный мод создан pifou92000. Обновление для 1.20.1 выполнено сообществом.

## Контакты

Для вопросов и предложений создавайте Issue на GitHub.
