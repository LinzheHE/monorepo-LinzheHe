**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: *use-case-title*

**Primary Actor**: Change Drawing Color.

**Goal in Context**: Changing the drawing color when the user press a number key 1-8. Each key corresponds to a specific color.

**Preconditions**: (1) The program must be running and in a responsive state. (2) The user is on the canvas drawing screen.

**Trigger**: The user presses one of the number key 1-8.
  
**Scenario**: (1) The user is on the drawing screen. (2) The user presses one of the number keys 1-8. (3) The system sets the color: 1=black, 2=while, 3=red, 4=green, 5=blue, 6=yellow, 7=magenta, 8=cyan. (4) The user proceeds to draw with the chosen color.
 
**Exceptions**: If the user presses an invalid key, the system should provide feedback indicating the selection is invalid.

**Priority**: Medium. The user could use a default color, but allowing set colors could enhance user experience.

**When available**: Second release.

**Channel to actor**: The primary actor communicates through I/O devices. The user use a keyboard to set the color. The system should respond within 1 second of any keyboard event.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: (1) Ensure the mapping of number keys and colors is documented clearly to the user. (2) Consider providing feedback when user press the keys, such as changing the pen color to let user know the current color. (2) Define the default color.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
