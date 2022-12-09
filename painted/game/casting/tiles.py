import constants
from game.casting.actor3 import Actor3
from game.shared.point import Point

class Tiles(Actor3):
    """ Sits on the entire game board to be colored by players """

    def __init__(self,x,y):
        super().__init__()

        # initial setting of tiles   
        self.set_color(constants.BACKGROUND_COLOR)
        self.set_position(Point(x,y))
        self.set_text("@")

    def move_next(self):
        pass
