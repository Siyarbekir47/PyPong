# PyPong - Turtle Ping Pong Game

PyPong is a simple implementation of the classic Ping Pong game, created using Python's Turtle module. Players can control two paddles and try to score points by getting the ball past their opponent's paddle. The game features collision detection with the paddles, walls, and keeps track of the score until one player wins.

## Features

- Player 1 (left paddle) uses the 'w' and 's' keys for movement.
- Player 2 (right paddle) uses the arrow keys (Up and Down) for movement.
- The ball moves automatically and bounces off walls and paddles.
- The game ends when a player scores 3 points.

## Gameplay

- The ball starts in the middle of the screen and moves in a random direction.
- Players must move their paddles to prevent the ball from getting past them.
- When the ball hits the paddle, it bounces back.
- If the ball goes out of bounds (past a paddle), the opposing player scores a point.
- The first player to reach 3 points wins, and the game ends.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pypong.git
2. Navigate into the project directory:



```bash
cd pypong
```
Run the game:

```bash
python main.py
```
Make sure you have Python 3 installed.


# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments
Thanks to the Python Turtle module for providing a simple way to create graphics and animations in Python.