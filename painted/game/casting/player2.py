import constants
from game.casting.actor2 import Actor2
from game.shared.point import Point


class Player2(Actor2):
    """
    An opponent of Player1
    
    The responsibility of Player2 is to move itself and color the tile.

    Attributes:
        _segments(list): a list of a player2
        _position(point): a position of player2
    """
    def __init__(self):
        # Constructs Player2
        super().__init__()
        self._segments = []
        self.x = int(constants.MAX_X - constants.CELL_SIZE*2)
        self.y = int(constants.MAX_Y / 2)
        self.set_text("#")
        self.set_color(constants.BLUE)
        self._position = Point(self.x, self.y)

    def set_position(self, position):
        """Updates a position of player2
        Args:
            position(point): a position of player2
        """
        self._position = position

    def turn_head(self, velocity):
        # head(segments[0]) gets new velocity
        self._segments[0].set_velocity(velocity)
    
