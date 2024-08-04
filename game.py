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
    
# The display_highest_chip_balance function takes player_list as a paramter and displays the player's name who has the highest chip balance from player_list.
def display_highest_chip_holder(player_list):

    index = 0                       # Incremental variable used to loop through player_list.
    counter = 0                     # Incremental variable used to loop through player_list.
    highest = 0                     # Stores the highest chip balance 
    position = 0                    # Stores the index of the player which has the highest cbip balance. 
    chipZero = 0                    # Incremental variable to keep count of how many players have a chip balance of 0.
    numOfPlayers = len(player_list) # Stores the length of the player_list 

    # If the numOfPlayers is 0, meaning that no players are stored inside the list, it displays an error.
    if numOfPlayers == 0:
        print("No players are added")

    else:
        
        # Nested while loop to loop through the player_list
        while index < len(player_list):
            counter = 0 
            while counter < len(player_list[index]):

                if counter == 5:

                    # if the value at player_list at index is greater than highest, then it is replaced with the value of highest.
                    # and the index is stored in position.
                    if player_list[index][counter] > highest:
                        highest = player_list[index][counter]
                        position = index

                    # If the value at player_list at index is the same as the value of highest, then
                    # it checks which player has played the least number of games. And stores that
                    # player's index in position.
                    elif player_list[index][counter] == highest:
                        if int(player_list[index][1]) < int(player_list[position][1]):
                            highest = player_list[index][counter]
                            position = index

                    # If the chip balance for player at index player_list is 0, chipZero is incremented by 1.
                    if player_list[index][counter] == 0:
                        chipZero = chipZero + 1
                            
                counter = counter + 1
            index = index + 1

        # If chipZero is the equal to numOfPlayers, meaning that all the players in the list have 0 chip balance, it displays an error message.
        if chipZero == numOfPlayers:
            print("All players have a chip balance of zero")

        else:
            
            print("Highest Chip Holder =>",player_list[position][0], "with", highest, "chips!")


# The sort_by_chips function takes player_list as a parameter and sorts the list in descending order of chip balance.
# The function returns the sortedPlayerList which is the player_list in descending order.
def sort_by_chips(player_list):
    
    sortedPlayerList = [] 
    i=0                   

    
    while i < len(player_list):
        
        sortedPlayerList.append(player_list[i])
        i = i + 1
        

    for outerIndex in range(len(sortedPlayerList)-1, 0, -1):
        
     for innerIndex in range(outerIndex):
         
        if sortedPlayerList[innerIndex][5] < sortedPlayerList[innerIndex+1][5]:
            sortedPlayerList[innerIndex], sortedPlayerList[innerIndex +1] = sortedPlayerList[innerIndex+1], sortedPlayerList[innerIndex]

    for i in range(len(sortedPlayerList)-1, 0, -1):
        
     for j in range(i):
         
        if sortedPlayerList[j][5] == sortedPlayerList[j+1][5]:

            if sortedPlayerList[j][1] > sortedPlayerList[j+1][1]:
                sortedPlayerList[j], sortedPlayerList[j+1] = sortedPlayerList[j+1], sortedPlayerList[j]
                
    return sortedPlayerList

# play_blackjack_games allows the player at position player_pos to play blackjack until they don't wish to play.
# The game statistics for the player are updated in player_list after each game. The function returns the updated player_list.
def play_blackjack_games(player_list, player_pos):
        
    game_result = 0                      
    noChips = player_list[player_pos][5] 
    play = "y"                            
    
    while play == "y":

        game_result, chipsLeft = blackjack.play_one_game(noChips)
        noChips = chipsLeft
        
        if game_result == 1:
            player_list[player_pos][4] = 1 + player_list[player_pos][4]
            player_list[player_pos][6] = player_list[player_pos][6] + 1

        elif game_result == 3:
            player_list[player_pos][2] = 1 + player_list[player_pos][2]
            player_list[player_pos][6] = player_list[player_pos][6] + 3

        elif game_result == 0:
            player_list[player_pos][3] = 1 + player_list[player_pos][3]

        player_list[player_pos][1] = 1 + player_list[player_pos][1]

        player_list[player_pos][5] = noChips
        print()
        play = input("Play again [y/n]? ")

    return player_list


filename = "players.txt"
players = read_file(filename)
print(players)
