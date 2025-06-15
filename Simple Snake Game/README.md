# 🐍 SnakeWithSparsh

A classic Snake game built using **Python** and **Pygame**. Eat the food, grow the snake, and avoid hitting the walls or yourself! Keep playing to beat your high score!

---

## 🎮 Game Features

* Classic snake gameplay with increasing length as you eat.
* Real-time keyboard controls (Arrow keys).
* Start screen and game over screen.
* Persistent **High Score** system (saved in a `highscore.txt` file).
* Smooth and responsive animation.

---

## 🛠️ Requirements

* Python 3.x
* Pygame

Install Pygame using pip:

```bash
pip install pygame
```

---

## ▶️ How to Run

1. Clone or download this repository.
2. Ensure `highscore.txt` exists in the same directory as the Python file.

   > Don't worry, it gets created automatically if not present.
3. Run the game using:

```bash
python snake_game.py
```

(Replace `snake_game.py` with your filename.)

---

## 🎮 Controls

| Key                 | Action                  |
| ------------------- | ----------------------- |
| SPACEBAR            | Start the game          |
| ↑ (UP)              | Move Up                 |
| ↓ (DOWN)            | Move Down               |
| ← (LEFT)            | Move Left               |
| → (RIGHT)           | Move Right              |
| ENTER               | Restart after Game Over |
| ESC or Close Button | Quit the game           |

---

## 🧠 Code Structure

* `Welcome()`: Display welcome screen.
* `Game_Loop()`: Main game logic loop.
* `text_screen()`: Utility to display text on the screen.
* `plot_snake()`: Renders the snake using a list of coordinates.

---

## 📁 Files

* `snake_game.py`: Main game script.
* `highscore.txt`: Stores the highest score ever achieved.

---

## ✨ Screenshots (Optional)

> *(Add images if you want to show the gameplay.)*

---

## 📌 To-Do / Future Improvements

* Add background music and sound effects.
* Add levels or increasing difficulty.
* Add obstacles for more challenge.
* Support for pause/resume feature.

---

## 📜 License
Free to use for learning and educational purposes. If you improve it, feel free to share or contribute!
