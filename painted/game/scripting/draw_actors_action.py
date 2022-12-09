from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        player1 = cast.get_first_actor("player1s")
        player2 = cast.get_first_actor("player2s")
        tiles = cast.get_actors("tiles")
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actor(player1)
        self._video_service.draw_actor(player2)
        self._video_service.draw_actors(tiles)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2, "right")
        self._video_service.draw_actors(messages, "center")
        self._video_service.flush_buffer()