import constants
from game.shared.color import Color
from game.shared.point import Point


class Actor3:
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor1 is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Actor1."""
        self._text = ""
        self._font_size = constants.FONT_SIZE
        self._color = constants.BACKGROUND_COLOR
        self._position = Point(0, 0)
        self._velocity = Point(0,0)
    

    def get_color(self):
        """Gets the actor3's color as a tuple of three ints (r, g, b).
        
        Returns:
            Color: The actor3's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the actor3's font size.
        
        Returns:
            Point: The actor3's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the actor3's position in 2d space.
        
        Returns:
            Point: The actor3's position in 2d space.
        """
        return self._position
    
    def get_text(self):
        """Gets the actor3's textual representation.
        
        Returns:
            string: The actor3's textual representation.
        """
        return self._text
    
    def set_color(self, color):
        """Updates the color to the given one.
        
        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position
    
    def set_font_size(self, font_size):
        """Updates the font size to the given one.
        
        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size
    
    def set_text(self, text):
        """Updates the text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text
