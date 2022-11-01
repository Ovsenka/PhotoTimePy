from dataclasses_ import CurrentTime
from time import strftime
from exceptions import SaveImgError


def get_time() -> CurrentTime:
    return CurrentTime(hour=strftime("%H"),
                       minute=strftime("%M"),
                       second=strftime("%S"))

from PIL import Image, ImageDraw, ImageFont
def create_img(time: CurrentTime) -> None:
    time_str = f"{time.hour}:{time.minute}"
    try:
        print("[INFO] Create image...")
        img = Image.new(mode="RGB", size=(400, 300))
        img_draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fonts/Roboto-Condensed/RobotoCondensed-Bold.ttf", size=128)
        img_draw.text((49, 80), time_str, font=font, fill=(255, 255, 255))
        print("[OK] time.JPEG has created!")
        print("[INFO] Saving image...")
        img.save("Temp/time", 'jpeg')
        print("[OK] ]time.JPEG saved!")
    except:
        raise SaveImgError("create_img error!")
    
    