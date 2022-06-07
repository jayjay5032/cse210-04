# Design for Greed

Our design will largely be a mimic of the preparation “RobotFindsKitten (Rfk)”. In RobotFindsKitten (Rfk), the artifact inherits the attributes from the actor to reduce repeating codes. Our design changes the additional attributes of the artifact. Instead of set and get messages, we replace them with the score factor to determent the score change when the player touches a gem or rock. Corresponded changes to meet the game specification were done in the code as well. The following snippet of design shows the inherited relationship between actor and artifact:


## Object: Actor

Responsibility: A visible, moveable thing that participates in the game. The responsibility of Actor is to keep track of its appearance, position, and velocity in 2D space.

Attributes:
_text (string): The text to display
_font_size (int): The font size to use.
_color (Color): The color of the text.
_position (Point): The screen coordinates.
_velocity (Point): The speed and direction.


Behavior:
get_color, get_font_size, get_position, get_text, get_velocity, move_next, set_color, set_position, set_font_size, set_text, set_velocity 

```
class: Actor

Attributes:
_text (string): The text to display
_font_size (int): The font size to use.
_color (Color): The color of the text.
_position (Point): The screen coordinates.
_velocity (Point): The speed and direction.

Functions
get_color(): _color
get_font_size(): _font_size
get_position(): _position
get_text(): _text
get_velocity(): _velocity
move_next(): Moves the actor to its next position
set_color(): Updates the color
set_position(): Updates the position
set_font_size(): Updates the font size
set_text(): Updates the text
set_velocity(): Updates the velocity
```

## Object: Artifact

Responsibility: An item of cultural or historical interest. The responsibility of an Artifact is to determent the score change when the player touches a gem or rock.
Attributes:
super().__init__(): inherit all attributes and functions from Actor

Behavior:
get_score_factor 

```
class: Artifact

Attributes:
super().__init__(): inherit all attributes and functions from Actor

Functions
get_score_factor(): determent the score change when the player touches a gem or rock
```