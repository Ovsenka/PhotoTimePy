from dataclasses_ import CurrentTime
from time import strftime
from exceptions import SaveImgError
from pathlib import PurePath
from PIL import Image, ImageDraw, ImageFont


def get_time() -> CurrentTime:
    return CurrentTime(hour=strftime("%H"),
                       minute=strftime("%M"),
                       second=strftime("%S"))

def create_img(time: CurrentTime) -> None:
    time_str = f"{time.hour}:{time.minute}"
    path_to_font = str(PurePath("Fonts", "Roboto-Condensed", "RobotoCondensed-Bold.ttf"))
    try:
        
        print("[INFO] Create image...")
        img = Image.new(mode="RGB", size=(400, 300))
        img_draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(path_to_font, size=128)
        img_draw.text((49, 80), time_str, font=font, fill=(255, 255, 255))
        print("[OK] time.JPEG has created!")
        print("[INFO] Saving image...")
        img.save("Temp/time", 'jpeg')
        print("[OK] time.JPEG saved!")
    except:
        raise SaveImgError("create_img error!")
    
    