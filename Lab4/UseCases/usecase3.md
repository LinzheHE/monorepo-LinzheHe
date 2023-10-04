**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Clear Canvas and Fill with Last Selected Color.

**Primary Actor**: User

**Goal in Context**: When the user press the space key, the canvas should be cleared and filled with the last selected color.

**Preconditions**: (1) The program must be running and in a responsive state. (2) The user is on the canvas drawing screen.

**Trigger**: The user presses the space key.
  
**Scenario**: (1) The user is on the drawing screen. (2) The user selects a drawing color by pressing the number keys 1-8. (3) The user presses the space key. (4) The system detects the space key press, then clears the canvas and fills it with the last selected color.
 
**Exceptions**: (1) The user may press the space key accidentally. The system could prompt for confiramtion or provide an undo option. (2) If the canvas is empty, or no color has been selected, pressing the space key may not have visible effect.

**Priority**: Middle to low. Some users may not need this feature.

**When available**: second release or later.

**Channel to actor**: The user use a keyboard to input the space key.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Consider providing a confirmation dialog to prevent accidental press.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
