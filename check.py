# import statements
import PIL
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

font_fname = '/fonts/Arial/arial.ttf' # Прописываем путь к основеому шрифту
font_fname_bold = '/fonts/Arial/arialbd.ttf' # Прописываем путь к жирному шрифту
font_size = 100 # Устанавливаем размер шрифта

font = ImageFont.truetype(font_fname, font_size) # Устанавливаем стиль для обычного текста

# bolded font
font_bold = ImageFont.truetype(font_fname_bold, font_size) # Устанавливаем стиль для жирного текста

with Image.open("3.jpg") as picture:
    draw = ImageDraw.Draw(picture)
    TL=font.getlength("Hello") + font.getlength(" world")
    print(TL)

    draw.text(xy=(10, 10), text="helo world", font=font)
    draw.text(xy=(10 + TL, 10), text="Катя", font=font_bold, fill =(255, 0, 0))
picture.show()