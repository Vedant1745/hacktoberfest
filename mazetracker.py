import os

# Define the maze
maze = [
    "#########",
    "#       #",
    "# ### # #",
    "# #   # #",
    "# ### # #",
    "#       #",
    "#########"
]

# Player's starting position
player_pos = [1, 1]

def print_maze():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if [y, x] == player_pos:
                print("P", end="")  # Player's position
            else:
                print(maze[y][x], end="")
        print()

def move_player(dx, dy):
    global player_pos
    new_x = player_pos[1] + dx
    new_y = player_pos[0] + dy

    # Check for wall or boundary
    if maze[new_y][new_x] != '#':
        player_pos = [new_y, new_x]

def main():
    print_maze()
    while True:
        move = input("Enter your move (WASD for up, left, down, right; Q to quit): ").upper()
        if move == 'W':
            move_player(0, -1)
        elif move == 'A':
            move_player(-1, 0)
        elif move == 'S':
            move_player(0, 1)
        elif move == 'D':
            move_player(1, 0)
        elif move == 'Q':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Use W, A, S, D to move, or Q to quit.")
        
        print_maze()

if __name__ == "__main__":
    main()
