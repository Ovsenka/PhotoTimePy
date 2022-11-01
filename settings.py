from dataclasses import dataclass


@dataclass
class Colors:
    BLACK: tuple[int, int, int] = (0,0,0)
    WHITE: tuple[int, int, int] = (255,255,255)
    
IMG_SIZE = (400, 300)

colors = Colors()






