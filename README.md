# cs1821-python-game
This Repo contains the code for the CS1821 Python Games Project, a 2D Osmos clone built in Python using the ``` simpleguitk ``` library.

## Project Requirements
The requirements of the project are shown below.

### 2.1 User interface
- The program displays a welcome screen when it starts.
- When the player runs out of lives, the welcome screen reappears and all the game sprites are cleared.
- While the welcome screen is being displayed the game mechanism is stopped (a pause feature).
- When the welcome screen is clicked, the lives and the score are reset.
- The program displays on the canvas an appropriate text for both the lives and the score.

### 2.2 Vectors
- The program must use the ``` Vector ``` class (developed during lectures and lab sessions) to position each sprite on the canvas.
- Some of the game sprites are subject to a velocity vector and move accordingly on the canvas.

### 2.3 Game Initialisation
- Initially, the canvas should be populated with a (relatively large) number of non-overlapping motes with random characteristics like the position and size; recall that some of the characteristics such as the overall colour should change while the game is played.
- The motes should be represented using sprites.
- The player has a limited number of lives (three is a good number). Lives are lost via collisions as described below.
- There is a realtime score mechanism. The score should be based on the number of motes absorbed by the player.

### 2.4 Movement
- The player can control using the keyboard exactly one of the motes, clearly identified by its colour and/or texture.
- Pressing any of the directional keys on your keyboard should result in a corresponding movement of the mote; maintaining the keys pressed (or pressing the space bar) should enable the player mote to travel faster, while losing mass.
- Make sure you fully address the movement of the player mote when several keys are pressed at the same time.
- The motes are not able to move outside of the screen. If a mote that is not controlled by the player hits the edge of the screen, it should bounce back as discussed in the lectures.
- The motes attract each other (depending on their sizes) when they are sufficiently close. This should act like gravity, where the player may escape a mote but will need to use more mass to do so.

### 2.5 Player sprite
- Depending on its kind, each mote should be depicted (and animated) using an appropriately selected sprite sheet. Scale the images to match the size of the mote;
The sprite animation depends on the control (e.g., a character can be moving to the left or to the right, and the animation should reflect this).

### 2.6 Collisions
- The effect of a collision between any two motes should be that the larger mote slowly absorbs the smaller one. If the player’s mote is absorbed, a life is lost. - - If the player’s mote absorbs a mote, their score is increased.
- Collisions between motes are handled using the techniques described in the lectures.
- For collision purposes, the motes can be approximated using circles.

### 2.7 Object-oriented approach
- The program follows an object-oriented approach.
- The sprite controlled by the player should be wrapped inside a ``` Player ``` class.
- Other game sprites should be wrapped inside appropriate classes.
- The collisions between the sprite controlled by the player and other sprites should be wrapped inside an ``` Interaction ``` class.
- The main aspects of the game (state variables, or constants for canvas dimensions, images, etc.) should be wrapped inside a ``` Game ``` class. This class can also encapsulate the game loop.

## Additional features
40% of the credit for the project is based on the implementation of additional features. A list of suggestions is given below. The amount of credit to be granted will be determined by the module staff based on the perceived effort invested into implementing these features.

- Animated backgrounds or other interesting animation effects (absorptions, etc).
- Two-player cooperative or competitive game.
- Some of the non-player motes move with acceleration.
- Power-ups adding features such as short-term protection against absorption, extra lives, increased/decreased gravitational pull, etc.
- Other pick-features such as enabling wrapping at the screen edges, speeding up or slowing down game play, shrinking all motes on screen, etc.
- Multiplayer modes.
- Static on-screen features such as walls.
- A game world larger than the screen. The view should track the player as they move.
- Other nontrivial features that enhance the gaming experience.
