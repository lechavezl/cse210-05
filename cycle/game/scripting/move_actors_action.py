from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):
    """The responsibility of MoveActorsAction is to move all the actors in the screen.
    """

# Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        """Move all the actors.

        Arg:
            cast: the given value.
            script: the given value.
        """

# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()