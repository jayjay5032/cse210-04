from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
    
    def get_score_factor(self, score, artifact):
        if artifact == '*':
            return score + 1
        if artifact == 'o':
            return score - 1 

    