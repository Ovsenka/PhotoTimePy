from PIL import Image, ImageDraw, ImageFont
import time
# from config import path_to_save

def create_time_pic(path_to_save=None):
    # ---------------------------------------------------------
    # Func that create picture with time text for profile photo
    # ---------------------------------------------------------
    
    # generate time text
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    text = hour + ":" + minute
    # create image
    img = Image.new('RGBA', (500, 500), 'white')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", size=128) # Font
    draw.text((100, 160), text, font=font, fill=(0, 0, 0))
    
    filename = "time_" + hour + "_" + minute + ".png"
    print("Saving " + filename)
    try:
        if path_to_save != None:
            img.save(path_to_save + filename)
        else:
            img.save("./Temp/" + filename)
        print("TimeImage succesfully saved!")
    except Exception as x:
        print("TimeImage is not saved!")
        print(x)
    pass

