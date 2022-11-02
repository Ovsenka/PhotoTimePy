from dataclasses import dataclass
from pathlib import PurePath


@dataclass
class ColorSettings:
    '''
    Color Format: color = (R,G,B)
    '''
    BLACK: tuple[int, int, int] = (0,0,0)
    WHITE: tuple[int, int, int] = (255,255,255)

@dataclass
class TextSettings:
    # Font from file
    FONT: str = str(PurePath("Fonts", "Roboto-Condensed", "RobotoCondensed-Bold.ttf"))
    # Size text
    SIZE: int = 128                 
    # Text position
    POS: tuple[int, int] = (49, 80)

IMG_SIZE = (400, 300)

colors = ColorSettings()
text = TextSettings()






