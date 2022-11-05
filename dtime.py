from dataclasses_ import CurrentTime
from time import strftime
from exceptions import SaveImgError
from PIL import Image, ImageDraw, ImageFont
from settings import colors, IMG_SIZE, text


def get_time() -> CurrentTime:
    return CurrentTime(hour=strftime("%H"),
                       minute=strftime("%M"),
                       second=strftime("%S"))

def create_img(time: CurrentTime) -> None:
    time_str = f"{time.hour}:{time.minute}"
    try:
        img = Image.new(mode="RGB", size=IMG_SIZE)
        img_draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(text.FONT, size=text.SIZE)
        img_draw.text(text.POS, time_str, font=font, fill=colors.WHITE)
        img.save("Temp/time", 'jpeg')
        print("[OK] time.JPEG saved! ({})".format(time_str))
    except:
        raise SaveImgError()
    
    