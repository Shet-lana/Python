import random

# Функции для генерации отдельных сюжетов

def shaman_queen_plot():
    characters = ["Иван-Царевич", "Шаманская Царица"]
    actions = [
        "{char1} отправился в дальние края, чтобы разгадать тайну бессмертия.",
        "{char1} нашел магический камень, способный исполнить одно желание.",
        "{char1} встретил мудреца, рассказавшего легенду о Шаманской Царице."
    ]
    char1 = random.choice(characters[:-1])
    action = random.choice(actions)
    plot = action.format(char1=char1)
    return f"Сюжет \"Шаманская Царица\": {plot}"

def golden_fish_plot():
    characters = ["Старик", "Рыбак", "Золотой Карп"]
    objects = ["Свободу", "Богатство", "Любовь"]
    events = [
        "{char1} поймал {obj}, пообещавший исполнить три желания.",
        "{char1} узнал о существовании магии золотой рыбки и захотел воспользоваться ею.",
        "{char1} мечтал обрести {obj}, но потерял шанс из-за жадности."
    ]
    char1 = random.choice(characters[:-1])
    obj = random.choice(objects)
    event = random.choice(events)
    plot = event.format(char1=char1, obj=obj)
    return f"Сюжет \"Золотая Рыбка\": {plot}"

def alenka_blossom_plot():
    characters = ["Девушка", "Принц", "Колдунья"]
    locations = ["Волшебный сад", "Таинственный лес", "Заколдованный замок"]
    stories = [
        "{char1} отправилась в путешествие, чтобы спасти любимого.",
        "{char1} нашла чудесный цветок, обладающий особыми свойствами.",
        "{char1} встретила колдунью, предложившую сделку."
    ]
    char1 = random.choice(characters[:-1])
    loc = random.choice(locations)
    story = random.choice(stories)
    plot = story.format(char1=char1)
    return f"Сюжет \"Аленький цветочек\": {plot}"

def turnip_plot():
    characters = ["Дед", "Бабка", "Внучка", "Жучка"]
    objects = ["Огромную Репку", "Маленькую Репку", "Чудесную Репку"]
    situations = [
        "{char1} посадил {obj}, выросшую настолько большой, что пришлось звать всех помогать.",
        "{char1} обнаружил удивительное свойство своей {obj}, дающей богатство.",
        "{char1} решил устроить праздник урожая благодаря своей уникальной {obj}."
    ]
    char1 = random.choice(characters[:-1])
    obj = random.choice(objects)
    sit = random.choice(situations)
    plot = sit.format(char1=char1, obj=obj)
    return f"Сюжет \"Репка\": {plot}"

# Генератор сюжета
def generate_random_plot():
    all_story_functions = [shaman_queen_plot, golden_fish_plot, alenka_blossom_plot, turnip_plot]
    selected_function = random.choice(all_story_functions)
    return selected_function()

# Основной блок запуска
if __name__ == "__main__":
    print(generate_random_plot())