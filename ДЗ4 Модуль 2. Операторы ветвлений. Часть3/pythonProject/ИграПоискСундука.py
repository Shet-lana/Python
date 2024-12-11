has_key = False
has_map = False
has_chest = False

energy = 100  # Начальный запас энергии
day = 1  # День игры


def move_to_direction(direction):
    global energy, has_key, has_map, has_chest

    if direction == 'север':
        print('Вы отправились на север острова.')
        energy -= 30
        print(f'Текущий запас энергии: {energy}')
        if not has_key:
            print('Вы нашли ключ!')
            has_key = True
        else:
            print('Вы уже находили здесь ключ ранее.')
    elif direction == 'юг':
        print('Вы отправились на юг острова.')
        energy -= 25
        print(f'Текущий запас энергии: {energy}')
        if not has_map:
            print('Вы нашли карту!')
            has_map = True
        else:
            print('Вы уже находили здесь карту ранее.')
    elif direction == 'запад':
        print('Вы отправились на запад острова.')
        energy -= 15
        print(f'Текущий запас энергии: {energy}')
        print('Вы не нашли ничего интересного.')
    elif direction == 'восток':
        print('Вы отправились на восток острова.')
        energy -= 35
        print(f'Текущий запас энергии: {energy}')
        if has_key and has_map:
            print('Вы использовали ключ и карту, чтобы открыть сундук!')
            has_chest = True
        else:
            print('Вам нужен ключ и карта, чтобы открыть сундук.')
    else:
        print('Вы целый день думали куда пойти и впустую потратили энергию')
        energy -= 20


while energy > 0 and not has_chest:
    print(f'\nДень {day}')
    print(f'Энергия: {energy}')
    choice = input('Куда пойдёте? [север, юг, запад, восток] ').lower().strip()

    move_to_direction(choice)

    day += 1

if has_chest:
    print('\nПоздравляем! Вы нашли сундук и завершили приключение!')
else:
    print('\nВаши силы иссякли.')
    print('Вы проиграли, попробуйте ещё раз!')
