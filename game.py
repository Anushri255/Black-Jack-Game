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

# The display_players function displays all the players data - name, games played, lost, won, drawn, chip balance and score to the screen.
# The function doesn't return anything.
def display_players(player_list):

    counter = 0                                                             
    index = 0                                                                 
    formatting = "="*59                        
    formatting2 = "-"*59                       
    title = "Player Summary"                   
    headings = "P  W  L  D   Chips   Score  -" 

    
    print(formatting)
    print("-", format(title, '^55'), "-")
    print(formatting)
    print("-",format(headings,'^85'))
    print(formatting2)


    # A nested while loop is used to display all the elements in the list.
    while counter < len(player_list):

        index = 0
        
        while index < len(player_list[counter]):

                # The if - elif statements print the individual from player_list list of lists.  
                if index == 0:
                        print("-  ", end ="")
                        print(format(player_list[counter][index],'<21'), end = "")
                        
                elif index == 1:
                        print(format(player_list[counter][index],'>7'), end = "")
                        
                elif index == 2:
                        print(format(player_list[counter][index],'>3'), end = "")

                elif index == 3:
                        print(format(player_list[counter][index],'>3'), end = "")

                elif index == 4:
                        print(format(player_list[counter][index],'>3'), end = "")

                elif index == 5:
                        print(format(player_list[counter][index],'>8'), end = "")

                elif index == 6:
                        print(format(player_list[counter][index],'>8'), end ="")
                        print("  -")

                index = index + 1

        print(formatting2)
        counter = counter + 1
        
    print(formatting)

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

# The remove_player removes the player from the player_list list if the player exists in the player_list list of lists.
# The function returns the updated player_list once the player has been removed.
def remove_player(player_list, name):

    counter = 0         
    index = 0           
    tempList = []       
    tempListofList = [] 
    temp = ""           
    
    position = find_players(player_list, name)
    print()

    if position == -1:
        print(name,"is not found in players.")
        print()
        
    else:

        while index < len(player_list):
            
            for counter in range(0,7):

                if player_list[index][0] == name:
                    temp = player_list[index][counter]

                else:
                    tempList.append(player_list[index][counter])

                counter = counter + 1

            if player_list[index][0] != name:
                tempListofList.append(tempList)

            tempList = []
            index = index + 1

        player_list = tempListofList
        print("Successfully removed",name,"from player list.")
        print()
        
    return player_list


# The add_player function adds a player to the player_list list of lists only if the player doesn't exist in the player_list list.
# The function returns the updated  player_list.
def add_player(player_list, name):

    position = find_players(player_list, name)

    print()

    if position == -1:
        
        addPlayer = [name,0,0,0,0,100,0]
        player_list.append(addPlayer)
        print("Successfully added",name, "to player list.")

    else:
        print(name,"already exists in player list.")

    print()

    return player_list


player_list = []                       # Define list to store player information
valid = "F"                            # Stores whether the user input is valid or not.
userChoice = "choice"                  # Stores what command the user would like 
player_list = read_file("players.txt") # Reads player information from file and store in player_list


print("Please enter choice")
userChoice =input("[list, buy, search, high, add, remove, play, chips, quit]: ")


while (valid == "F") or (userChoice != "quit"):
   
    print()

    if userChoice == "list":
        display_players(player_list)
        valid = "T"
        
    elif userChoice == "buy":
        name = input("Please enter name: ")
        player_list = buy_player_chips(player_list, name)
        valid = "T"

    elif userChoice == "search":
        name = input("Please enter name: ")

        position = find_players(player_list, name)

        if position == -1:
            print(name," is not found in player list.")
            print()

        else:
            print()
            print(player_list[position][0],"stats:")
            print()
            print("P  W  L  D  Score")

            for i in range(1,7):
                if i == 1:
                    print(format(player_list[position][i],'<2'), end = "")

                elif i == 2:
                    print(format(player_list[position][i],'>2'), end = "")

                elif i == 3:
                    print(format(player_list[position][i],'>3'), end = "")

                elif i == 4:
                    print(format(player_list[position][i],'>3'), end = "")

                elif i == 6:
                    print(format(player_list[position][i],'>4'))
                
                i = i + 1
                
            print()
            print("Chips:", end = "")
            print(format(player_list[position][5],'>5'))
            print()
            
        valid = "T"

    elif userChoice == "high":
        
        highest = display_highest_chip_holder(player_list)
        print()
        valid = "T"

    elif userChoice == "add":
        name = input("Please enter name: ")
        
        player_list = add_player(player_list, name)
        valid = "T"

    elif userChoice == "remove":
        name = input("Please enter name: ")

        player_list = remove_player(player_list, name)
        valid = "T"

    elif userChoice == "play":
        name=input("Please enter name: ")

        # The find_players function is called to check if the name inputted by the user exists in the player_list.
        # The value which the find_players function returns is stored in player_pos.
        player_pos = find_players(player_list, name)

        # If the player_pos is -1, an error message is shown and the user cannot play the game.
        if player_pos == -1:
            print()
            print(name, "is not found in player list.")
            print()

        else:
            player_list = play_blackjack_games(player_list, player_pos)
        
        valid = "T"

    # If user inputs chips, the sort_by_chips function is called.
    elif userChoice == "chips":
        print()

        sortedPlayerList = sort_by_chips(player_list)
        display_sorted_player_list(sortedPlayerList)
        valid = "T"

    # If user inputs quit, the loop ends.
    elif userChoice == "quit":
        valid = "T"

    # If user enters an invalid input, they are prompted to enter it again.    
    else:
        print("Not a valid command - please try again.")
        print()
        valid = "T"
        
    print()

    print("Please enter choice")
    userChoice = input("[list, buy, search, high, add, remove, play, chips, quit]: ")



filename = "players.txt"
players = read_file(filename)
print(players)
