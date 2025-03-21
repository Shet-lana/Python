from colorama import init, Fore, Style
import random

init()

QUEST_GOALS = [
    'Найти потерянный артефакт',
    'Убить босса',
    'Спасти заложника',
    'Доставить письмо',
    'Разведать территорию',
]

QUEST_REWARDS = [
    ('Золото', 0),
    ('Оружие', 'Меч'),
    ('Броня', 'Легкая броня'),
    ('Зелье', 'Зелье здоровья'),
    ('Опыт', 0)
]

LOCATIONS = [
    'Темный лес',
    'Заброшенный замок',
    'Подземелье',
    'Горная деревня',
    'Пустыня'
]

NPCS = {
    'Старик': {'класс': 'Жрец', 'раса': 'Человек'},
    'Воин': {'класс': 'Боец', 'раса': 'Орк'},
    'Маг': {'класс': 'Чародей', 'раса': 'Эльф'},
    'Торговец': {'класс': 'Купец', 'раса': 'Гном'},
}


def generate_quest():
    goal = random.choice(QUEST_GOALS)
    reward_type, reward_value = random.choice(QUEST_REWARDS)
    location = random.choice(LOCATIONS)
    npc_name = random.choice(list(NPCS.keys()))
    npc_details = NPCS[npc_name]

    if reward_type == 'Опыт':
        reward_value = random.randint(100, 500)
    elif reward_type == 'Золото':
        reward_value = random.randint(50, 200)

    quest = (
        goal,
        (reward_type, reward_value),
        location,
        (npc_name, npc_details['класс'], npc_details['раса'])
    )

    return quest


def generate_unique_quests(count):
    unique_quests = set()

    while len(unique_quests) < count:
        quest = generate_quest()
        unique_quests.add(quest)

    return unique_quests


def print_quests_to_file(quests, filename="quests.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("=== Сгенерированные квесты ===\n")

        for i, quest in enumerate(quests, start=1):
            goal, reward, location, npc = quest

            reward_type, reward_value = reward
            npc_name, npc_class, npc_race = npc

            file.write(f"Квест №{i}\n")
            file.write(f"Цель: {goal}\n")
            file.write(f"Нагада: {reward_type} ({reward_value})\n")
            file.write(f"Локация: {location}\n")
            file.write(f"NPC: {npc_name} ({npc_class}, {npc_race})\n\n")


quest_count = int(input('Сколько квестов надо сгенерировать? '))

quests = generate_unique_quests(quest_count)
print_quests_to_file(quests)