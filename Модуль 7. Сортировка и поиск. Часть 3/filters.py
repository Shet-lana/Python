from PIL import Image

image = Image.open('example.jpg')


def enhance_cold_colors(image):
    # Копируем исходное изображение
    enhanced_image = image.copy()

    # Получаем размеры изображения
    width, height = image.size

    # Проходим по каждому пикселю изображения
    for x in range(width):
        for y in range(height):
            # Получаем значения RGB текущего пикселя
            r, g, b = image.getpixel((x, y))

            # Увеличиваем синий и зелёный каналы, уменьшаем красный канал
            new_r = max(r - 30, 0)
            new_g = min(g + 20, 255)
            new_b = min(b + 40, 255)

            # Устанавливаем новый цвет пикселя
            enhanced_image.putpixel((x, y), (new_r, new_g, new_b))

    return enhanced_image

# Применение фильтра для усиления холодных цветов
cold_enhanced_image = enhance_cold_colors(image)
cold_enhanced_image.save("output_cold.jpg")


def enhance_warm_colors(image):
    # Копируем исходное изображение
    enhanced_image = image.copy()

    # Получаем размеры изображения
    width, height = image.size

    # Проходим по каждому пикселю изображения
    for x in range(width):
        for y in range(height):
            # Получаем значения RGB текущего пикселя
            r, g, b = image.getpixel((x, y))

            # Увеличиваем красный и жёлтый каналы, уменьшаем синий и зелёный каналы
            new_r = min(r + 50, 255)
            new_g = max(g - 10, 0)
            new_b = max(b - 30, 0)

            # Устанавливаем новый цвет пикселя
            enhanced_image.putpixel((x, y), (new_r, new_g, new_b))

    return enhanced_image

# Применение фильтра для усиления тёплых цветов
warm_enhanced_image = enhance_warm_colors(image)
warm_enhanced_image.save("output_warm.jpg")

