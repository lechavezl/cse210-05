import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, color, x_location, y_location):
        super().__init__()
        self._cycle_color = color
        self._cycle_x_location = x_location
        self._cycle_y_location = y_location
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        """Get the segments of the cycle
        Return:
            self._segments
        """
        return self._segments

    def move_next(self):
        """Move the cycle
        """
        # move all segments
        for segment in self._segments:
            segment.move_next()

        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Get the cycle's head
        """
        return self._segments[0]

    def grow_tail(self, number_of_segments, _cycle_color):
        """Create and makes the cycles tail grow.
        
        Arg:
            number_of_segments (int): The given value.
            _cycle_color: The given color.
        """
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._cycle_color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """make the cycle's head turn to other direction
        """
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Prepare the cycle's body"""
        x = int(self._cycle_x_location)
        y = int(self._cycle_y_location)

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = self._cycle_color if i == 0 else self._cycle_color
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)