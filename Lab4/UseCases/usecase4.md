**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Draw with Left-Click and Drag

**Primary Actor**: User

**Goal in Context**: When the user left-clicking the mouse and dragging, a pixel will change wherever the mouse is located.

**Preconditions**: (1) The program must be running and in a responsive state. (2) The user is on the canvas drawing screen.

**Trigger**: The user presses the left mouse and drags the mouse while holding the button down.
  
**Scenario**: (1) The user is on the drawing screen. (2) The user positions the mouse cursor on the canvas where they want to start drawing. (3) The user presses the left mouse button and holds it down. (4) The user drags the mouse. (5) The system changes the color of the pixels under the mouse cursor. (6) The user releases the left mouse button, the drawing action stops.
 
**Exceptions**: (1) If the user does not select a color before drawing, prompt the user to select a color. (2) If the user drag to a place out of the canvas, end drawing at the border of the canvas.

**Priority**: High. It is a core feature for painting.

**When available**: First release.

**Channel to actor**: The primary actor communicates through I/O devices. The user use a mouse to click and drad. The system is responsible for maintaining focus of the window when the user clicks and drags.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: Ensure the drawing action is smooth.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
