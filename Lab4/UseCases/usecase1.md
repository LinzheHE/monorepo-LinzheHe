**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 1

<hr>

**Use Case**: Canvas Size

**Primary Actor**: User

**Goal in Context**: The user aims to set the canvas size to 600 pixels wide, 400 pixels high.

**Preconditions**: (1) The program must be running and in a responsive state. (2) The user is on the canvas setting screen.

**Trigger**: The user selects the option to set the canvas size.
  
**Scenario**: (1) The user selects the "Canvas size setting" option from the setting menu. (2) The system presents the user with options to set the width and height of the canvas. (3) The user specifies the canvas width as 600 pixels. (4) The use specifies the canvas height as 400 pixels. (5) The system updates the canvas to be 600 pixels wide, 400 pixels high, providing the user a drawable area of the size.
 
**Exceptions**: If the user enter an invalid number for the size (negative, non-numeric), an error message should display, and the user is prompted to enter a valid number.

**Priority**: Middle-priority. It is essential but not critical.

**When available**: Second release.

**Channel to actor**: The primary actor communicates through I/O devices. The user use a mouse to click the menu options. The system is responsible for maintaining focus of the window when the user clicks, and should respond within 1 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: (1) Determine whether the software should provide default canvas size for the user. (2) Determine whether changing canvas size while painting would affect existing content on it and how it would affect.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
