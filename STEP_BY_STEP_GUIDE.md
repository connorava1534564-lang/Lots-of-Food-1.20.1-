# Пошаговое руководство по сборке и запуску Lots of Food 1.20.1

## Шаг 1: Проверка требований

Убедитесь, что у вас установлено:
- **Java 17 или выше** (проверьте: `java -version`)
- **Git** (опционально, для клонирования)

## Шаг 2: Подготовка проекта

1. Откройте терминал в папке проекта
2. Проверьте структуру файлов:
```
lotsoffood/
├── src/
├── build.gradle
├── gradle.properties
├── gradlew (или gradlew.bat для Windows)
└── settings.gradle
```

## Шаг 3: Первая сборка (Setup)

### Windows (PowerShell/CMD):
```bash
.\gradlew setupDecompWorkspace
```

### Linux/Mac:
```bash
./gradlew setupDecompWorkspace
```

**Примечание:** Первая сборка может занять 10-30 минут, так как Gradle скачивает все зависимости и декомпилирует Minecraft.

## Шаг 4: Сборка мода

```bash
.\gradlew build
```

Если сборка успешна, вы увидите:
```
BUILD SUCCESSFUL in Xs
```

Готовый JAR-файл будет находиться в:
```
build/libs/lotsoffood-1.20.1-1.0.0.jar
```

## Шаг 5: Тестирование в dev-окружении

### Запуск клиента:
```bash
.\gradlew runClient
```

Это запустит Minecraft с вашим модом в режиме разработки.

### Запуск сервера:
```bash
.\gradlew runServer
```

## Шаг 6: Проверка мода в игре

1. Запустите клиент (`.\gradlew runClient`)
2. Дождитесь загрузки Minecraft
3. Создайте новый мир (Creative Mode)
4. Откройте инвентарь (E)
5. Найдите вкладку "Lots of Food"
6. Проверьте наличие предметов

## Возможные проблемы и решения

### Проблема 1: "Java version is too old"
**Решение:** Установите Java 17 или выше
```bash
# Проверить версию
java -version

# Скачать Java 17: https://adoptium.net/
```

### Проблема 2: "Could not resolve dependencies"
**Решение:** Проверьте интернет-соединение и повторите:
```bash
.\gradlew build --refresh-dependencies
```

### Проблема 3: "Task failed with an exception"
**Решение:** Очистите кэш и пересоберите:
```bash
.\gradlew clean
.\gradlew build
```

### Проблема 4: Текстуры не загружаются (розовые кубики)
**Решение:** 
1. Проверьте наличие текстур в `src/main/resources/assets/lotsoffood/textures/`
2. Убедитесь, что имена файлов совпадают с registry names
3. Пересоберите проект

### Проблема 5: Предметы не появляются в креативе
**Решение:**
1. Проверьте `ModCreativeTabs.java`
2. Убедитесь, что все предметы добавлены в `displayItems()`
3. Проверьте логи на ошибки регистрации

## Шаг 7: Установка мода в обычный Minecraft

1. Соберите мод: `.\gradlew build`
2. Найдите JAR в `build/libs/`
3. Установите Forge 1.20.1 (версия 47.3.0 или выше)
4. Скопируйте JAR в папку `mods/` вашего Minecraft
5. Запустите Minecraft с профилем Forge

## Шаг 8: Разработка и отладка

### Горячая перезагрузка (Hot Reload)
К сожалению, Forge не поддерживает полную горячую перезагрузку. После изменений:
1. Остановите клиент/сервер
2. Пересоберите: `.\gradlew build`
3. Запустите снова: `.\gradlew runClient`

### Просмотр логов
Логи находятся в:
- Dev-окружение: `run/logs/latest.log`
- Обычный Minecraft: `.minecraft/logs/latest.log`

### Отладка в IDE

#### IntelliJ IDEA:
1. Импортируйте проект как Gradle проект
2. Дождитесь индексации
3. Запустите задачу `runClient` из Gradle панели
4. Или создайте Run Configuration:
   - Main class: `net.minecraftforge.userdev.LaunchTesting`
   - Module: `lotsoffood.main`
   - Working directory: `$PROJECT_DIR$/run`

#### Eclipse:
1. Запустите: `.\gradlew eclipse`
2. Импортируйте проект в Eclipse
3. Запустите `GradleStart` для клиента

## Шаг 9: Добавление новых предметов

### Пример: Добавить новую еду

1. **Откройте `ModItems.java`**
2. **Добавьте регистрацию:**
```java
public static final RegistryObject<Item> MY_FOOD = ITEMS.register("my_food",
    () -> new Item(new Item.Properties().food(
        new FoodProperties.Builder()
            .nutrition(5)
            .saturationMod(0.6f)
            .build()
    )));
```

3. **Создайте модель** `src/main/resources/assets/lotsoffood/models/item/my_food.json`:
```json
{
  "parent": "minecraft:item/generated",
  "textures": {
    "layer0": "lotsoffood:item/my_food"
  }
}
```

4. **Добавьте текстуру** в `src/main/resources/assets/lotsoffood/textures/item/my_food.png`

5. **Добавьте перевод** в `src/main/resources/assets/lotsoffood/lang/en_us.json`:
```json
{
  "item.lotsoffood.my_food": "My Food"
}
```

6. **Добавьте в креативную вкладку** в `ModCreativeTabs.java`:
```java
output.accept(ModItems.MY_FOOD.get());
```

7. **Пересоберите и протестируйте:**
```bash
.\gradlew build
.\gradlew runClient
```

## Шаг 10: Создание рецептов

Создайте файл `src/main/resources/data/lotsoffood/recipes/my_food.json`:

```json
{
  "type": "minecraft:crafting_shaped",
  "pattern": [
    "WWW",
    "WBW",
    "WWW"
  ],
  "key": {
    "W": {
      "item": "minecraft:wheat"
    },
    "B": {
      "item": "minecraft:bread"
    }
  },
  "result": {
    "item": "lotsoffood:my_food",
    "count": 1
  }
}
```

## Полезные команды Gradle

```bash
# Очистка проекта
.\gradlew clean

# Сборка без тестов
.\gradlew build -x test

# Обновление зависимостей
.\gradlew build --refresh-dependencies

# Просмотр всех задач
.\gradlew tasks

# Генерация исходников Minecraft (для просмотра)
.\gradlew genIntellijRuns

# Запуск с дополнительной памятью
.\gradlew runClient -Dorg.gradle.jvmargs="-Xmx4G"
```

## Следующие шаги

После успешной сборки базового мода, вы можете:

1. ✅ Добавить больше предметов
2. ✅ Создать рецепты крафта
3. ⬜ Добавить растения (crops)
4. ⬜ Создать TileEntity (машина для мороженого)
5. ⬜ Добавить генерацию мира
6. ⬜ Реализовать специальные эффекты
7. ⬜ Добавить звуки
8. ⬜ Оптимизировать текстуры

## Дополнительные ресурсы

- [Forge Documentation](https://docs.minecraftforge.net/)
- [Forge Community Wiki](https://forge.gemwire.uk/wiki/Main_Page)
- [Minecraft Wiki](https://minecraft.wiki/)
- [Parchment Mappings](https://parchmentmc.org/)

## Поддержка

Если у вас возникли проблемы:
1. Проверьте логи в `run/logs/latest.log`
2. Убедитесь, что все файлы на месте
3. Попробуйте `.\gradlew clean build`
4. Создайте Issue на GitHub с описанием проблемы и логами

---

**Удачи в разработке! 🍕🍰🍦**
