game = [[0,0,0],[0,0,0],[0,0,0]]
player1 = "Player 1"
player2 = "Player 2"
turn = 1


def check_if_full(game):
    """Checks to see if the game board is completly full of inputs
    game = a list of lists for use in the game board
    """
    score = 0
    for row in game:
        for piece in row:
            if piece != 0:
                score += 1
    if score == 9:
        return True
    else:
        return False
def get_input(player):
    """Takes in the player's input of coordinates, accepting only 2 values seperated by a comma which are within the game board.
    Returns both coordinates x and y seperated and decreased by one for proper indexing.
    
    player = a string of which player is giving an input
    """
    while True:
        try:
            for row in game:
                print(row)
            coord = str(input(player + ", please give your x, y coordinates:")).split(',')
            x,y = coord[0],coord[1]
            if int(y) <= len(game):
                if int(x) <= len(game[0]):
                    break
        except IndexError:
            print("Please enter a valid response")
        else:
            print("Please enter in the proper range")
    return (int(x) - 1, int(y) - 1)

def checkwin(game):
    """Checks the game board to see if either player has connected 3 in a row and won the game.
       If a player has won, the game returns true and prints which player has won.
       Also calls check_if_full to see if the game is over due to the board being full, if the board is full, the funciton returns false.
    """
    players = ['X', 'O']
    player = 0
    for i in players:
        player += 1
        row1 = game[0]
        row2 = game[1]
        row3 = game[2]
        if (i == row1[0] and i == row1[1] and i == row1[2]) or (i == row2[0] and i == row2[1] and i == row2[2]) or (i == row3[0] and i == row3[1] and i == row3[2]) or (i == row1[0] and i == row2[1] and i == row3[2]) or (i == row1[0] and i == row2[0] and i == row3[0]) or (i == row1[1] and i == row2[1] and i == row3[1]) or (i == row1[2] and i == row2[1] and i == row3[0]) or (i == row1[2] and i == row2[2] and i == row3[2]):
            print("Player ", player, " wins!")
            return True
  
    if check_if_full(game):
        print( "No winner.")
        return True
    return False

def play_round():
    """Plays a round of Tic-Tac-Toe by selecting a player based on whose turn it is and asking for their input.
    Adds the player's move to the game board unless the spot is already full.
    Increments turn by one.
    
    """
    global turn
    while True:
        player = turn % 2
        if player == 0:
            player = player2
            piece = "O"
        else:
            player = player1
            piece = "X"
            
        (x,y) = get_input(player)
        if game[y][x] == 0:
            game[y][x] = piece
            break
        else:
            print("That coordinate is already full")
    turn += 1

        
def play_game():
    """
    Play's rounds of Tic-Tac-Toe until someone wins the game or the board fills up.
    """
    while not checkwin(game):
        play_round()
play_game()
    