# Ping Pong

A simple 2D Ping Pong game built with Python and Pygame.

## Description

Ping Pong is a 2D arcade game where the player controls a horizontal paddle and tries to keep a ball from reaching the bottom of the game area.

The ball moves continuously around the screen and bounces off the walls. When the ball hits the paddle, the player's score increases and a sound effect is played.

The background color also changes randomly when the player clicks the mouse or successfully hits the ball with the paddle.

The game ends when the ball reaches the bottom of the play area.

## Technologies

* Python
* Pygame

## Features

* Real-time paddle movement
* Ball movement and wall bouncing
* Paddle-ball collision detection
* Score tracking
* Random ball starting position
* Sound effect when the ball hits the paddle
* Random background color generation
* Game-over detection
* Space key restart system

## Project Preview

### Gameplay

![Gameplay](assets/preview/gameplay.png)

## How It Works

The game creates a `1200 × 900` Pygame window and initializes the ball, paddle, score, and background color.

### Ball Movement

The ball position is continuously updated using its horizontal and vertical speed:

```python
ball_x += ball_speed_x
ball_y += ball_speed_y
```

When the ball reaches the left or right boundaries, its horizontal direction is reversed.

When the ball reaches the top boundary, its vertical direction is reversed.

### Paddle Movement

The player controls the paddle using the Left and Right Arrow keys.

| Key         | Action            |
| ----------- | ----------------- |
| Left Arrow  | Move paddle left  |
| Right Arrow | Move paddle right |

The paddle is restricted to the visible horizontal game area.

### Collision Detection

The game creates rectangles for both the paddle and the ball:

```python
player_rect = player_img.get_rect(topleft=(player_x, player_Y))
ball_rect = player_ball.get_rect(topleft=(ball_x, ball_y))
```

When the rectangles collide, the ball changes its vertical direction and the score increases by `1`.

A sound effect is also played when the collision occurs.

### Score System

The score starts at `0`.

Every time the ball successfully hits the paddle:

```text
Score +1
```

The score is displayed in the top-left corner of the screen.

### Background Color

The game starts with a default background color.

When the player clicks the mouse, the program generates a new random RGB color.

The background color also changes when the ball hits the paddle.

### Game Over

When the ball reaches the bottom of the play area, the game enters the Game Over state.

The ball stops moving and the current score is displayed.

Pressing the Space key starts a new round and resets:

* Ball position
* Ball speed
* Paddle position
* Score
* Game-over state

## Challenges

Some of the main challenges in this project were:

* Implementing continuous ball movement
* Handling wall bouncing
* Detecting collisions between the ball and paddle
* Managing the game-over state
* Implementing the restart system
* Updating the score correctly
* Generating random background colors
* Working with Pygame images and sounds

## What I Learned

Through this project, I practiced:

* Creating a Pygame game loop
* Handling keyboard and mouse input
* Detecting collisions using rectangles
* Working with images and sounds
* Managing game states
* Updating object positions
* Working with random values
* Implementing a score system
* Creating a restart mechanism

## Status

Completed as a Python and Pygame practice project.

## Future Improvements

* Add multiple difficulty levels
* Increase ball speed as the score increases
* Add a start menu
* Add a pause system
* Improve the Game Over screen
* Add a high-score system
* Add more sound effects
* Add additional visual effects

## Requirements

* Python 3.x
* Pygame

## Installation

Install Pygame using:

```bash
pip install pygame
```

## How to Run

Run the game with:

```bash
python main.py
```

## Project Structure

```text
Ping_Pong/
│
├── assets/
│   └── preview/
│       └── gameplay.png
│
├── Ping-pongeffect.mp3
├── border.jpg
├── main.py
├── pingpong.png
├── tennis_ball.png
└── README.md
```
