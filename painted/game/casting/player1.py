import constants
from game.casting.actor1 import Actor1
from game.shared.point import Point


class Player1(Actor1):
    """
    A person who plays the game.
    
    The responsibility of Player1 is to move itself and color the tiles.

    Attributes:
        _segments(list): a list of a player1
        _position: position of Player1
    """
    def __init__(self):
        # Constructs Player1
        super().__init__()
        self._segments = []
        self.x = int(constants.CELL_SIZE*2)
        self.y = int(constants.MAX_Y / 2)
        self._position = Point(self.x, self.y)
        self.set_text("8")
        self.set_color(constants.RED)

    def set_position(self, position):
        """Updates the position of Player1
        Args:
            position(point): a position of Player1
        """
        self._position = position


    def turn_head(self, velocity):
        # head(segments[0]) gets new velocity
        self._segments[0].set_velocity(velocity)
    
