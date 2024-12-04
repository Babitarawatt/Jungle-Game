Welcome to **Jungle Game**, a thrilling text-based adventure where every choice you make decides your fate. Will you survive the jungle or meet your doom? Play to find out!
About the Game : In this game, you find yourself lost in a jungle. You must navigate through various paths by making key decisions. Choose wisely to avoid traps and uncover the path to victory.
Gameplay Instructions
  1. Launch the game in Python.
  2. Follow the on-screen prompts to make your choices:
     - Choose 1 (Left) or 2 (Right) to start.
     - Subsequent choices will branch into new scenarios.
  3. Your objective: Make decisions that lead you to WIN and avoid paths that result in GAME OVER

Game Flow 
Initial Choice:
 - Press 1 (Go Left):
 - Press 3 (Left): Game Over.
 - Press 4 (Right): Game Over.

Press 2 (Go Right):
 - Press 1 (Left): Fall into a well (Game Over).
 - Press 2 (Right): You encounter another choice:
 - Type "HELP" →  You WIN!
 - Type "NO HELP" → GAME OVER.

How to Play the Game 
 1. Ensure Python 3.x is installed on your system.
 2. Save the following code to a file named `jungle_game.py`:

    python
    print("Jungle game")
    a = int(input("I am lost, ........ you have 2 directions. Press 1 for left or 2 for right: "))
    if a == 1:
        print("You are going left")
        z = int(input("Rasta ....... press 3 for left and 4 for right: "))
        if z == 3:
            print("Press 3 for game over")
        elif z == 4:
            print("Press 4 for game over")
    elif a == 2:
        print("You are going right")
        y = int(input("Raasta............. press 1 for left and 2 for right: "))
        if y == 1:
            print("Press 1 for falling into the well")
        elif y == 2:
            print("There are again two turns: left / right")
            x = input("Raasta.............. HELP / NO HELP: ")
            if x == "HELP":
                print("WIN")
            elif x == "NO HELP":
                print("GAME OVER")
 3. Open a terminal or command prompt.
 4. Run the game using:
       -bash python jungle_game.py

 Features 
  - Simple decision-based gameplay.
  - Multiple endings based on your choices.
  - Replayable to explore different paths and outcomes.

 Tips for Winning 
  - Think carefully about your choices.
  - Sometimes asking for HELP can save you from danger.
 
 Replay and Enjoy 
 Keep playing to uncover all possible paths. Have fun exploring the Jungle Game!







   











