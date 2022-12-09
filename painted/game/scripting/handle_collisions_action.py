import constants
from game.casting.actor1 import Actor1
from game.casting.actor2 import Actor2
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the players collide
    with the tiles. A player who collide with more than a half of the total tile(COLUMNS*(ROES-1)/2)
    wins the game

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
        _player1_score: score for player1
        _player2_score: score for player2
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._player1_score = 0
        self._player2_score = 0

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)

    
    def _handle_segment_collision(self, cast):
        """When a player collides with a tile, it changes the color of the tile
           (player1 color is red, and player2 color is blue). 
           It also calculate the score for each players, and sets is_game_over flag
           if a player gets more than a half of tiles.  
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1s")
        player2 = cast.get_first_actor("player2s")

        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        tiles = cast.get_actors("tiles")
    
        self._player1_score = 0
        self._player2_score = 0
        for tile in tiles:

            # tile gets player1's color    
            if player1.get_position().equals(tile.get_position()): 
                tile.set_color(player1.get_color())

            # tile gets player2's color
            if player2.get_position().equals(tile.get_position()):
                tile.set_color(player2.get_color())

            # tile gets its original color when player1 and 2 collide with a tile at the same time
            if player1.get_position().equals(tile.get_position()) \
                and player2.get_position().equals(tile.get_position()):
                tile.set_color(constants.BACKGROUND_COLOR)

            # score setting
            if tile.get_color() == player1.get_color():
                self._player1_score += 1

            if tile.get_color() == player2.get_color():
                self._player2_score += 1  

        score1.set_text(f"Player1: {self._player1_score}") 
        score2.set_text(f"Player2: {self._player2_score}") 

        # end of the game setting
        if (self._player1_score > constants.COLUMNS*(constants.ROWS-1)/2) or\
            (self._player2_score > constants.COLUMNS*(constants.ROWS-1)/2):
            self._is_game_over = True
      
        
    def _handle_game_over(self, cast):
        """Shows the winner when a player reaches more than a half of tiles.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            # game over message handling
            message = Actor1()
            if self._player1_score == 286:        
                message.set_text("Player1 wins!")
            if self._player2_score == 286:
                message.set_text("Player2 wins!")    
            message.set_position(position)
            message.set_color(constants.WHITE)
            cast.add_actor("messages", message)