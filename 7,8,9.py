# Прописать в консоли pip install pillow для работы модулей
# импортируем модули
from PIL import Image # Работа с фото
from PIL import ImageFont # Работа со шрифтами
from PIL import ImageDraw # Создание новых фото
from PIL import ImageFilter #  Работа с фильтрами
from PIL.ExifTags import TAGS # Работа с exif тэгами


def watermarkPict(input_image_path, output_image_path, watermark_image_path, positionX, positionY): # Наложение водяного знака
    base_image = Image.open(input_image_path) # Открываем исходное фото в переменной
    watermark = Image.open(watermark_image_path) # Открываем водяной знак в переменной
    width, height = base_image.size # Читаем размеры исходника в переменную
    transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0)) # Создаём новое фото с размерами исходника
    transparent.paste(base_image, (0, 0)) # Накладываем на него исходник
    transparent.paste(watermark, (positionX, positionY), mask=watermark) # Накладываем водяной знак на новое фото
    transparent.show() # Отображаем получившийся файл
    transparent.save(output_image_path) # Сохраняем получившийся файл

def PictShowing(path): # Выводим фото на экран
    picture = Image.open(path) # Открываем фото в переменной
    picture.show() # Выводим фото на экран

def PictPrintInfo(path): # Печать информации о фото
    picture = Image.open(path)  # Открываем фото в переменной
    print(picture.filename)  # Отображаем путь к фото в коноли
    print(picture.format) # Выводим информацию о формате фото
    print(picture.size) # Выводим информацию о размере фото
    print(picture.mode) # Выводим информацию о цветовой схеме фото
    print(type(picture))
    exifdata = picture.getexif() # Выводим информацию о дате, устройстве захвата и т.д.
    for tagid in exifdata: # Парсим exif данные
        tagname = TAGS.get(tagid, tagid)
        value = exifdata.get(tagid)
        print(f"{tagname:25}: {value}")
    print(picture.__dict__)

def PictTransp(path): # Отзеркаливание фото
    picture = Image.open(path)  # Открываем фото в переменной
    picture = picture.reduce(3)  # уменьшаем фото в 3 раза
    picture.show()  # Выводим фото на экран
    picture = Image.open(path)  # Открываем фото в переменной
    picture = picture.transpose(0) # Зеркалим фото по горизонтали
    picture.show()
    picture = Image.open(path)  # Открываем фото в переменной
    picture = picture.transpose(5) # Зеркалим фото по вертикали
    picture.show()

def PictFilterRGB(path): # Наложить фильтр (альтернативный способ)
    picture = Image.open(path) # Открываем фото в переменной
    r, g, b = picture.split() # Раскладываем фото на цветовые каналы
    picture = Image.merge(mode="RGB", bands=(r, b, g)) # Собираем цветовые каналы в другой очередности
    picture.show() # Выводим фото на экран
    picture.save("redacted.jpg")  # Сохраняем фото

def PictSharp(): # Наложить фильтр
    # Накладываем фильтр повышения резкости из библиотки на 5 фотографий
    number=1
    while number < 6:
        path=str(number) + str(".JPG") # Собираем имя  входного фото из порядкогого номера и формата
        picture = Image.open(path) # Открываем фото в переменной
        picture = picture.filter(ImageFilter.SHARPEN) # Накладываем фильтр повышения резкости
        picture.show()# Выводим фото на экран
        picture.save(str("Redacted/NEW___") + str(number) + str(".JPG")) # Собираем новый путь и новое имя полученного файла и сохраняем его.
        number = number + 1 # Идём в следующий цикл.

def PictCrop(path, x1, y1, x2, y2): # Обрезка фото 8.1
    picture = Image.open(path)  # Открываем фото в переменной
    print(picture.size)
    picture = picture.crop((x1, y1, x2, y2))
    picture.show()
    picture.save("Открытка ОБРЕЗАНО.png")

CelebsPath = {"новый год": "6.JPEG", "день рождения": "7.JPG", "23 февраля": "8.JPG", "8 марта": "9.JPG"}
CelebsText = {"новый год": "Новым годом, ", "день рождения": "Днём рождения, ", "23 февраля": "23-им февраля, ", "8 марта": "8-ым марта, "}
CelebsCoordX = {"новый год": 350, "день рождения": 620, "23 февраля": 200, "8 марта": 220}
CelebsCoordY = {"новый год": 500, "день рождения": 900, "23 февраля": 500, "8 марта": 165}

def  Congrats(celeb, conname):
    path = CelebsPath.get(celeb)
    print(path)
    ConText = CelebsText.get(celeb) # Текст поздравления
    print(ConText)
    CelebCoordX = CelebsCoordX.get(celeb)
    print(CelebCoordX)
    CelebCoordY = CelebsCoordY.get(celeb)
    print(CelebCoordY)
    print(conname)
    font_fname = '/fonts/Arial/arial.ttf'  # Прописываем путь к основеому шрифту
    font_fname_bold = '/fonts/Arial/arialbd.ttf'  # Прописываем путь к жирному шрифту
    font_size = 70  # Устанавливаем размер шрифта
    font = ImageFont.truetype(font_fname, font_size)  # Устанавливаем стиль для обычного текста
    font_bold = ImageFont.truetype(font_fname_bold, font_size)  # Устанавливаем стиль для жирного текста
    with Image.open(path) as picture:
        draw = ImageDraw.Draw(picture)
        draw.text(xy=(CelebCoordX, CelebCoordY), text="Поздравляю с ", font=font, fill=(0, 255, 0))
        TL = font.getlength("Поздравляю с ")
        draw.text(xy=(CelebCoordX + TL, CelebCoordY), text=ConText + " ", font=font, fill=(0, 0, 255))
        TL = TL + font.getlength(ConText)
        draw.text(xy=(CelebCoordX + TL, CelebCoordY), text=conname, font=font_bold, fill=(255, 0, 0))
    picture.show()

MyLabs = input("Номер лабы: ")
if MyLabs == "7.1":
    PictShowing("first.jpg") # 7.1 Отобразить любое изображение
    PictPrintInfo("first.jpg") # 7.1 Отобразить информацию о фото
if MyLabs == "7.2":
    PictTransp("first.jpg") # 7.2 Отзеркаливание изображения
if MyLabs == "7.3":
    PictFilterRGB("first.jpg") # 7.3 Наложить фильтр (альтернативный способ)
    PictSharp() # 7.3 Наложить фильтр (альтернативный способ)
if MyLabs == "7.4":
    watermarkPict("1.jpg", "11s.png", "yastreb.ico", 3008, 2200) # 7.4 Накладываем водяной знак на фото:
    # Очерёдность:исходник/выходной файл/файл с водяным знаком/позиция
if MyLabs == "8.1":
    PictCrop("открытка.png", 239, 37, 1280, 853) # 8.1 Обреззка фото
if MyLabs == "8.2" or MyLabs == "8.3":
    Congrats(input("Назовите праздник"), input("Имя получателя"))
