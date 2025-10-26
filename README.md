# Bouncing Ball Game with Python and OpenCV

This repository contains a Python script for a simple interactive game where a ball bounces around the screen and a racket controlled by the player prevents it from hitting the bottom edge. The game is built using OpenCV and NumPy.

## Features

- **Ball Physics**:

  - Simulates realistic ball movement and bouncing off walls and the racket.
  - The ball randomly chooses its initial direction at the start of each round.

- **Racket Movement**:

  - The player can move the racket left or right using keyboard controls (`A` and `D` keys).

- **Game State**:

  - Displays a start message ("PRESS SPACE") until the player starts the game.
  - Resets the ball when it hits the bottom of the screen, showing "Game Over" in the terminal.

- **Visualization**:
  - Clean, minimalistic visuals with a bouncing ball, a racket, and a black background.

## Requirements

To run the script, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (cv2)
- NumPy

Install the required packages using pip:

```bash
pip install opencv-python numpy
```

## Usage

1. **Run the Script**:

   - Execute the script to start the game:
     ```bash
     python bouncing_ball.py
     ```

2. **Game Controls**:

   - Press `SPACE` to start the game.
   - Use the `A` key to move the racket left.
   - Use the `D` key to move the racket right.
   - Press `Q` to quit the game.

3. **Objective**:
   - Keep the ball in play by bouncing it off the racket. The game resets when the ball hits the bottom of the screen.

## Example Gameplay

- **Start Screen**:
  Displays a message prompting the player to press `SPACE` to start the game.
  ![image](https://github.com/user-attachments/assets/47fd55bf-e722-421f-a73d-7df1d0dbe139)

- **Game in Action**:
  The ball bounces off walls, the racket, and the top of the screen. Prevent the ball from falling to the bottom!
  ![image](https://github.com/user-attachments/assets/63d2d240-29e6-4d81-89d0-c1ad9f5e9e8f)
  ![image](https://github.com/user-attachments/assets/7c30f733-467b-4ced-9517-9b437aab0ac6)

- **Game Over**:
  When the ball hits the bottom, the game resets, and the player can start a new round.
  ![image](https://github.com/user-attachments/assets/2376551a-a8c5-45ad-8c78-ab98d0a5133e)
  ![image](https://github.com/user-attachments/assets/47fd55bf-e722-421f-a73d-7df1d0dbe139)

## Input Data

No additional input data is required. The game environment is procedurally generated.

## Output

The game runs in a real-time OpenCV window:

- **Ball**: A white circle representing the moving ball.
- **Racket**: A white rectangle controlled by the player.
- **Game Messages**: Visual cues for starting the game.

---

## Author

**Mohammed EL Amine Hoceini**(https://github.com/MEDPRG)
