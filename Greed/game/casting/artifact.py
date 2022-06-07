from game.casting.actor import Actor


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

    