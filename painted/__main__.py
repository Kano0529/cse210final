import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.player1 import Player1
from game.casting.player2 import Player2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.casting.tiles import Tiles


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player1s", Player1())
    cast.add_actor("player2s", Player2())
    cast.add_actor("score1", Score())
    score2 = Score()
    score2.set_position(Point(constants.MAX_X, 0))
    cast.add_actor("score2", score2)
    for x in range(0, constants.MAX_X, constants.CELL_SIZE):
        for y in range(constants.CELL_SIZE, constants.MAX_Y, constants.CELL_SIZE):
            cast.add_actor("tiles", Tiles(x, y))
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()