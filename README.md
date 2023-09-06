# 2048-Ai

## Images
File size is too large.
Click [here](https://rayyanshaik.com/images/2048-demo2.gif) to view the [gif](https://rayyanshaik.com/images/2048-demo2.gif)

## Running the Application (Mac only)
- Within this repository, under `\dist`, there is a `.app` file named: `2048 AI`. On a Mac computer, this file alone can be downloaded and run.
- Runtime Troubleshooting
    - Unverfied Developer: Right click application and then select "open". This should prompt you with an option to open the application anyways
    - Application not opening: During its first 1-2 times running, the application takes around 5-6 seconds to load. It may also require you to "open" the app a few times on its initial run

## Executing the code
- Dependencies Required:
    - PyQT5
    - Pygame 2.1 (or newer)
    - numpy
- File to run: `form.py`


## What is 2048 Game?
- 2048 is a popular web game, in which the player shifts numbered tiles across a 4x4 grid to create the number `2048`.
- Starts start with values of `2` or `4` and can be shifted `up`, `down`, `left`, or `right`. When two tiles collide, their values are combined into one new tile.
- After every "turn" or "move", a new tile is randomly placed in an empty tile slot.

## Project Content
- This project emulates the game of 2048 and applies Monte Carlo Simulations to have an AI, reach the 2048 (and potentially the 4096) tile. 

## Key Components
- **2048 Game Logic**
    - The mechanics of this game primarily consist of "spawning" tiles in random locations, shifting tiles in a direction depending on input, and merging tiles that collide.
    - The shifting/movement code on it's own was not very difficult, but when combined with the fact that tiles could merge mid-shift, was a challange to implement

- **GUI**
    - This program implements 2 seperate GUI features. A simple GUI run through PyQT5 is initially launched - from this panel, certain run-time variables can be adjusted. The 2048 simulation is run through pygame to draw the game in a neat and colorful manner.
    - The PyQT5 gui/panel was created with the applications QT-Creator and Qt-Designer. Using these apps, my design was compiled into the `form.ui` file, from which `form.py` was auto-generated. Additional changes have been made to `form.py` to account for inputs and pygame implementation.
    - The file `rounded_rect.py` allows rounded rectangles to be easily created in pygame (not natively supported). This file was not created by myself.

- **Monte Carlo Logic**
    - Since tiles can spawn in random locations, I found 2048 to be a difficult problem to tackle with convetional genetic algorithm approaches. The Monte Carlo approach seemed especially desirable at first due to its potential for larges samples and for its "consideration" of random decisions. This means that it becomes good at accounting for the random tile placement at the end of each move.
    - Given the current state of the board/all tiles, an adjustable number of simulations `N` are run for each possible move - `up`, `down`, `left`, `right`. So, each move runs `N` simulations until their simulation reaches an end state. Then, each moves' simulation scores are averaged, and the move with the highest score is selected as the next move to play.

## Fun
- **Themes**
    - To put my own spin on this game, I included an option for custom color combinatinos or "themes". Some themes included are: `Tokyo Night`, `Tortoise`, and `Dracula`.
