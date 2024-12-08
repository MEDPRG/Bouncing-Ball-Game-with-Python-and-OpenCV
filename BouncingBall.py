import cv2 as cv
import numpy as np
import random

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_NAME = "Bouncing Ball"

# Ball settings
BALL_RADIUS = 10
BALL_SPEED = .5

# Racket settings
RACKET_WIDTH = 100
RACKET_HEIGHT = 10
RACKET_SPEED = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Ball:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.dx = random.choice([-1, 1]) * BALL_SPEED
        self.dy = random.choice([-1, 1]) * BALL_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce(self, racket_x):
        if self.x <= BALL_RADIUS or self.x >= WINDOW_WIDTH - BALL_RADIUS:
            self.dx = -self.dx
        if self.y <= BALL_RADIUS:
            self.dy = -self.dy
        if WINDOW_HEIGHT - BALL_RADIUS <= self.y <= WINDOW_HEIGHT and \
                racket_x <= self.x <= racket_x + RACKET_WIDTH:
            self.dy = -self.dy

    def draw(self, frame):
        cv.circle(frame, (int(self.x), int(self.y)), BALL_RADIUS, WHITE, -1)


class Racket:
    def __init__(self):
        self.x = (WINDOW_WIDTH - RACKET_WIDTH) // 2
        self.y = WINDOW_HEIGHT - RACKET_HEIGHT

    def right_move(self):
        self.x = min(self.x + RACKET_SPEED, WINDOW_WIDTH - RACKET_WIDTH)

    def left_move(self):
        self.x = max(0, self.x - RACKET_SPEED)

    def draw(self, frame):
        cv.rectangle(frame, (self.x, self.y), (self.x + RACKET_WIDTH, WINDOW_HEIGHT), WHITE, -1)


def main():
    cv.namedWindow(WINDOW_NAME)
    ball = Ball()
    racket = Racket()
    start = False
    while True:
        frame = np.zeros((WINDOW_HEIGHT, WINDOW_WIDTH, 3), dtype=np.uint8)
        if start:
            ball.move()
            ball.bounce(racket.x)
        else:
            cv.putText(frame, "PRESS  SPACE", (WINDOW_WIDTH//2-115, WINDOW_HEIGHT//2), cv.FONT_HERSHEY_DUPLEX, 1, WHITE, 3)

        ball.draw(frame)
        racket.draw(frame)

        cv.imshow(WINDOW_NAME, frame)

        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('a'):
            racket.left_move()
        elif key == ord('d'):
            racket.right_move() 
        elif key == ord(' ') and not start:
            start = True

        if ball.y >= WINDOW_HEIGHT:
            print("Game Over!")
            start = False
            ball = Ball()

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
