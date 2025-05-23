# Ashley's Snakes and Ladders Game (Refactored)

import turtle
import random

# Game configuration constants
BOARD_SIZE = 5  # Size of the board (5x5 grid)
WIN_POSITION = 25  # The winning position on the board
PLAYER_IMAGES = {"cow": "cow.gif", "bull": "bull.gif"}  # Player icons
DICE_IMAGES = [f"dice{i}.gif" for i in range(1, 7)]  # Dice images for each roll (1-6)
SNAKES = {8: 2, 20: 0, 24: 13}  # Snakes defined as {start_position: end_position}
LADDERS = {5: 14, 9: 11, 18: 22}  # Ladders defined as {start_position: end_position}

# Initialize turtles
players = {}  # Dictionary to store player turtles
dice = turtle.Turtle()  # Turtle for displaying dice
maindraw = turtle.Turtle()  # Turtle for drawing the board
win_display = turtle.Turtle()  # Turtle for displaying the win message

def setup_turtles():
    """
    Initialize player turtles with their corresponding images and set up dice and win display.
    """
    for name, image in PLAYER_IMAGES.items():
        player_turtle = turtle.Turtle()
        player_turtle.shape(image)
        player_turtle.penup()
        players[name] = player_turtle  # Add each player to the players dictionary
    dice.penup()  # Prepare dice turtle
    win_display.hideturtle()  # Hide win display initially

def draw_board():
    """
    Draws the main game board and borders.
    """
    maindraw.speed(0)
    maindraw.width(2)
    maindraw.penup()
    maindraw.goto(-250, 250)  # Top-left corner of the board
    maindraw.pendown()
    # Draw a square board boundary
    for _ in range(4):
        maindraw.forward(500)
        maindraw.right(90)
    draw_grid()  # Draw grid lines within the board

def draw_grid():
    """
    Draws the grid lines inside the main board to create a 5x5 grid.
    """
    # Draw vertical grid lines
    for i in range(BOARD_SIZE + 1):
        maindraw.penup()
        maindraw.goto(-250 + i * 100, 250)
        maindraw.pendown()
        maindraw.goto(-250 + i * 100, -250)
    # Draw horizontal grid lines
    for j in range(BOARD_SIZE + 1):
        maindraw.penup()
        maindraw.goto(-250, 250 - j * 100)
        maindraw.pendown()
        maindraw.goto(250, 250 - j * 100)

def position_players():
    """
    Set initial player positions outside the game board.
    """
    players["cow"].goto(-200, -180)
    players["bull"].goto(-230, -220)

def roll_dice():
    """
    Simulates rolling a dice by selecting a random number between 1 and 6.
    Displays the corresponding dice image.
    Returns:
        int: Random dice roll result between 1 and 6.
    """
    result = random.randint(1, 6)
    dice.shape(DICE_IMAGES[result - 1])  # Update dice turtle with correct image
    dice.goto(-300, 150)  # Move dice to display position
    return result

def move_player(player_name, steps):
    """
    Moves the specified player by the number of steps rolled.
    Checks for snakes and ladders on the target position.
    Args:
        player_name (str): Name of the player ("cow" or "bull").
        steps (int): Number of steps to move the player.
    Returns:
        int: The final board position of the player after moving.
    """
    player = players[player_name]
    position = get_position(player)
    target_position = position + steps
    target_position = min(target_position, WIN_POSITION)  # Cap position at WIN_POSITION

    # Apply snake or ladder if present at target position
    if target_position in SNAKES:
        target_position = SNAKES[target_position]
    elif target_position in LADDERS:
        target_position = LADDERS[target_position]

    player.goto(get_coordinates(target_position))  # Move player to new position
    return target_position

def get_position(player):
    """
    Determines the current position of a player on the board based on coordinates.
    Args:
        player (Turtle): The turtle representing the player.
    Returns:
        int: The player's current position (1-25).
    """
    pos = player.pos()
    x, y = round(pos[0]), round(pos[1])
    for i in range(BOARD_SIZE ** 2):
        if (x, y) == get_coordinates(i + 1):
            return i + 1
    return 1

def get_coordinates(position):
    """
    Converts a board position (1-25) to (x, y) coordinates.
    Args:
        position (int): The position on the board.
    Returns:
        tuple: (x, y) coordinates on the screen.
    """
    row = (position - 1) // BOARD_SIZE
    col = (position - 1) % BOARD_SIZE
    # Alternate row direction to create a "snake-like" pattern on board
    if row % 2 == 1:
        col = BOARD_SIZE - 1 - col
    x = -250 + col * 100 + 50
    y = 250 - row * 100 - 50
    return x, y

def check_winner(position, player_name):
    """
    Checks if the player has reached the winning position.
    If won, displays win message and resets the game.
    Args:
        position (int): Current position of the player.
        player_name (str): Name of the player.
    """
    if position == WIN_POSITION:
        win_display.penup()
        win_display.goto(0, 0)
        win_display.shape("win.gif")  # Display winning image
        print(f"{player_name.capitalize()} wins the game!")
        turtle.clearscreen()
        main()  # Restart the game

def game_turn(player_name):
    """
    Executes a single turn for the specified player.
    Args:
        player_name (str): Name of the player taking the turn.
    """
    input(f"{player_name.capitalize()} - press Enter to roll the dice.")
    steps = roll_dice()  # Roll the dice
    position = move_player(player_name, steps)  # Move player by dice result
    check_winner(position, player_name)  # Check if player has won

def main():
    """
    Main function to set up the game and initiate the game loop.
    """
    turtle.setup(width=600, height=600)
    turtle.bgcolor("white")
    setup_turtles()  # Initialize player turtles and dice
    draw_board()  # Draw the game board
    position_players()  # Position players outside the board initially

    # Game loop: alternate turns for each player
    while True:
        game_turn("cow")
        game_turn("bull")

# Run the main game function
main()
