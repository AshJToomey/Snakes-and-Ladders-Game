**Ashley’s Snakes and Ladders Game (Refactored)**

A Python-based visual Snakes and Ladders game using the Turtle graphics module. This version is fully interactive and features custom player icons, dice visuals, and a board with snakes and ladders—perfect for a fun two-player experience!

Features
	•	Graphical board with a 5x5 grid
	•	Player avatars (cow and bull)
	•	Visual dice rolls (images of dice faces)
	•	Snakes and ladders logic
	•	Win detection and automatic game restart
	•	Smooth turtle graphics animation

Gameplay
	•	Two players: Cow and Bull
	•	Players take turns rolling the dice (press Enter)
	•	Land on ladders to climb up or snakes to slide down
	•	First to reach square 25 wins the game!

Setup

Requirements
	•	Python 3.x
	•	turtle module (usually included with Python)

Assets Needed

Ensure the following image files are in the same directory as your script:
	•	cow.gif
	•	bull.gif
	•	dice1.gif to dice6.gif
	•	win.gif (optional) – for displaying the win message

How to Run

python snakes_and_ladders.py

Follow the on-screen prompts. Players press Enter to roll the dice in turn.

File Structure

├── snakes_and_ladders.py
├── cow.gif
├── bull.gif
├── dice1.gif
├── dice2.gif
├── dice3.gif
├── dice4.gif
├── dice5.gif
├── dice6.gif
├── win.gif

Code Overview
	•	setup_turtles() – Initializes players, dice, and display elements
	•	draw_board() / draw_grid() – Draws the board and grid lines
	•	roll_dice() – Rolls a random number (1–6) and updates dice image
	•	move_player() – Moves players and checks for snakes or ladders
	•	check_winner() – Displays the win screen and restarts the game
	•	main() – Orchestrates the game setup and loop

Customization

You can easily modify:
	•	Board size (BOARD_SIZE)
	•	Player images via the PLAYER_IMAGES dictionary
	•	Snakes and ladders via the SNAKES and LADDERS dictionaries

License

MIT License
