import os

from PIL import Image, ImageDraw, ImageFont
import random

from PIL.ImageEnhance import Color


def initials_image(name):
    # Ad soyadı böl ve baş harfleri al
    name_split = name.split(' ')
    first_name = name_split[0]
    last_name = name_split[1]

    first_letter = first_name[0].upper()
    second_letter = last_name[0].upper()

    # Görsel boyutları
    img_width = 500
    img_height = 500

    # Arkaplan rengi
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    bg_color = (r, g, b)

    # Yazı font boyutu
    font_size = img_width // 2

    # Yazıyı ortalamak için koordinatlar
    x = img_width // 2
    y = img_height // 2

    # Görsel oluştur
    img = Image.new('RGB', (img_width, img_height), color=bg_color)

    # Yazıyı ortaya yerleştir
    draw = ImageDraw.Draw(img)

    # Arkaplan rengi
    r, g, b = random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)
    bg_color = (r, g, b)

    # Ortalama arkaplan rengini hesapla
    avg_bg = (r + g + b) // 3

    # Eğer açık renkse siyah, koyu renkse beyaz yazı rengi olarak belirle
    if avg_bg > 127:
        text_color = 'DimGray'
    else:
        text_color = 'white'

    # Yazı rengini belirlenen renkte çiz

    text = first_letter + second_letter
    draw.text((x, y), text, fill=text_color,
              font=ImageFont.truetype("arial.ttf", size=font_size),
              anchor="mm")

    # Görsel kaydet
    media_dir = os.path.join(os.getcwd(), 'media')
    image_path = os.path.join(media_dir, 'profil_picture.png')

    if not os.path.exists(media_dir):
        os.mkdir(media_dir)

    img.save(image_path)

    return image_path
