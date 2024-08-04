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


# buy_player_chips function allows a player to buy chips, only if the player exits in the player_list list of lists.
# The function returns the updated player_list.
def buy_player_chips(player_list, name):

    # The find_players function is called to check if the player name entered is included in the player_list.
    # The function returns a position of the player in the player list, if the player doesn't exist, it returns -1.
    position = find_players(player_list, name)
    print()
    

    # If the function returns a position of -1, an error message is displayed.
    if position == -1:
        print(name,"is not found in player list.")


    # If the player exists in player_list, the player is allowed to update the chip balance.
    else:
        print(name, "currently has", player_list[position][5], "chips.")
        print()
        qty = int(input("How many chips would you like to buy? "))


        # The while loop continues until the user enters a valid input (i.e between 1 and 100)
        while qty > 100 or qty < 1:
            print("You may only buy between 1-100 chips at a time!")
            print()
            qty = int(input("How many chips would you like to buy? "))
   
        player_list[position][5] = player_list[position][5] + qty
        print()
        print("Successfully updated ", name,"'s chip balance to ",player_list[position][5], sep = "")

    # The player list with the updated chip balance is returned. 
    return player_list
    


filename = "players.txt"
players = read_file(filename)
print(players)
