# Design for Greed

Our design will largely be a mimic of the preparation for this week. We will have 4 main parts under the names casting, directing, services, and shared. Casting will contain an actor file that will be passed into the artifact for the sake of reusing code. Actor will create the player character while artifact will create the items to be interacted with. The third file named cast will be used to keep track of everything. Directing will contain our director file. Services will house anything that will be to and from to the user, this includes one that reads the keyboard inputs and one that displays the current information. The final group, named shared, will house files called color and point. Color is used to create the color profile of both the actors and artifacts. Point is used to determine the starting position of the pieces. All of this will mostly be used from the given code for this week.

The following shows the part of code we would modify or add:
1. add artifact.move_next() in director.py to allow the gems(artifact) to move
2. 


### Object: display

Responsibility: determined the content to display on the screen

State:
Guess result in list, Life pic in list, Message to display

Behavior:
Content to display
```
class:display

Guess_result_in_list: list
Life_pic_in_list: list
Message_to_display: string

Content_to_display: list, string
```
