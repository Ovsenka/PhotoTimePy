import vk_api
from PIL import Image, ImageDraw, ImageFont
import time
from config import LOGIN, PASSWORD

def main():
    session = vk_api.VkApi(LOGIN, PASSWORD)
    session.auth()

    vk = session.get_api()

    # Create jpg
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    text = hour + ":" + minute

    img = Image.new('RGBA', (500, 500), 'white')
    draw = ImageDraw.Draw(img) 
    font = ImageFont.truetype("arial.ttf", size=128) # Font

    draw.text((100, 160), text, font=font, fill=(0, 0, 0))
    filename = "time_" + hour + "_" + minute + ".png"
    print("Saving " + filename)
    img.save("Temp/" + filename)

if __name__ == "__main__":
    main()

