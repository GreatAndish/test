# Simple Jumping Game

A classic side-scrolling jumping game built with Python and Pygame. Jump over obstacles and see how high you can score!

## Description

This is a simple but fun jumping game where you control a black square that must jump over red obstacles moving from right to left. The game gets progressively challenging as you dodge more obstacles and rack up points.

## Features

- Simple one-button controls (spacebar to jump)
- Score tracking system
- Smooth physics with gravity and jump mechanics
- Random obstacle spacing for variety
- Game over detection with final score display

## Prerequisites

Before running the game, you need to have Python 3 and Pygame installed on your system.

### Installing Python

If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/)

### Installing Pygame

Install Pygame using pip:

```bash
pip install pygame
```

Or with pip3:

```bash
pip3 install pygame
```

## How to Run

1. Clone this repository or download the `jump_game.py` file
2. Navigate to the directory containing the game
3. Run the game with:

```bash
python jump_game.py
```

Or:

```bash
python3 jump_game.py
```

## How to Play

- Press **SPACEBAR** to jump
- Avoid the red obstacles
- Each obstacle you successfully pass increases your score by 1
- If you hit an obstacle, the game ends and displays your final score

## Game Controls

| Key | Action |
|-----|--------|
| SPACE | Jump |
| Close Window | Exit game |

## Game Mechanics

- **Player**: Black square (50x50 pixels)
- **Obstacles**: Red rectangles (40x60 pixels)
- **Jump Height**: Controlled by jump strength (-15) and gravity (0.8)
- **Obstacle Speed**: 6 pixels per frame
- **Frame Rate**: 60 FPS

## Known Issues

There is a minor physics bug where the player's velocity doesn't reset when landing on the ground. This doesn't affect gameplay significantly but may be fixed in future versions.

## Future Improvements

Potential enhancements for the game:
- Difficulty progression (obstacles speed up over time)
- High score tracking
- Sound effects and background music
- Different obstacle types
- Power-ups
- Pause functionality
- Restart option without closing the game

## License

This is a simple educational project. Feel free to use and modify as you wish.

## Contributing

Feel free to fork this project and submit pull requests with improvements!
