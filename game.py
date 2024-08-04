import blackjack


# The read_file function reads the contents of the players.txts and adds it into a list of list called players_list.
# The function returns player_list list of lists.
def read_file(filename):

    player_list = []
    index = 0
    infile = open(filename, "r")

    # Read first line of file.
    line = infile.readline()

    # While not end of file reached i.e. empty string not returned from readline method.
    while line != '':

        # Read name
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()
        
        # Split line into games played, no won, no lost, etc
        info_list = line.split()
        games_played = int(info_list[0])
        no_won = int(info_list[1])
        no_lost = int(info_list[2])
        no_drawn = int(info_list[3])
        chips = int(info_list[4])
        total_score = int(info_list[5])
        
        # Create new player list with player info
        new_player = [name, games_played, no_won, no_lost, no_drawn, chips, total_score]
        
        # Add new player to player_list list
        player_list.append(new_player)
        
        # Read next line of file.
        line = infile.readline()
    
    return player_list


filename = "players.txt"
players = read_file(filename)
print(players)
