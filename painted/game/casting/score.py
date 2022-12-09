from game.casting.actor1 import Actor1

class Score(Actor1):
    """
    A record of points earned or lost. 
    
    The responsibility of Score is to keep track of the points the players earned by 
    changing the color of tiles.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0

    def move_next(self):
        pass    

    