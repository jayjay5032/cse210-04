from game.casting.actor import Actor
import random
from game.shared.color import Color
from game.shared.point import Point

COLS = 60
GEM_OR_ROCK = ['*', 'o']
CELL_SIZE = 30
FONT_SIZE = 30

class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to determent the score change when the player touches a gem or rock.
    """
    def __init__(self):
        super().__init__()
    
    def get_score_factor(self, score, artifact):
        """
        determent the score change when the player touches a gem or rock
        """
        if artifact == '*':
            return score + 1
        if artifact == 'o':
            return score - 1
    
    @staticmethod
    def random_artifact():
        text = GEM_OR_ROCK[(random.randint(0, len(GEM_OR_ROCK) - 1))]

        x = random.randint(1, COLS - 1)
        y = 1
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        return artifact