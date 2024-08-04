# Dice Blackjack Game

## Description
This program allows users to play a dice version of blackjack against the computer. It also includes features to manage players and game statistics. Users can:

- View the list of players and game stats.
- Identify the player with the highest chip balance.
- Buy chips.
- Add or remove players.
- Sort the list of players.
- Search for players within the `player_list`.

The contents of `player_list` are read from a text file called `players.txt` and the updated contents are saved to `new_players.txt` once the user has finished using the program.

## Features

### Read Player List
Reads the contents of `players.txt` and loads it into a list of lists called `player_list`.

### Buy Chips
Allows players to buy chips if they exist in the `player_list`.

### Display Players
Displays all players' data including name, games played, won, lost, drawn, chip balance, and score.

### Display Highest Chip Balance
Displays the player with the highest chip balance.

### Write to File
Writes the `player_list` to `new_players.txt`.

### Sort Players by Chips
Sorts players in descending order based on chip balance.

### Play Blackjack
Allows a player to play blackjack, updating their game statistics in `player_list` after each game.

### Find Players
Checks if a player exists in `player_list`.

### Remove Player
Removes a player from `player_list` if they exist.

### Add Player
Adds a new player to `player_list` if they don't already exist.

## How to Use

1. **Start the Program:**

2. **Main Menu: Enter a choice from the following options:**
- `list`: View the list of players.
- `buy`: Buy chips for a player.
- `search`: Search for a player.
- `high`: Display the player with the highest chip balance.
- `add`: Add a new player.
- `remove`: Remove a player.
- `play`: Play a game of blackjack.
- `chips`: Sort players by chip balance.
- `quit`: Exit the program.

3. **Player List Management:**
   
  **Add Player**
```python
name = input("Please enter name: ")
player_list = add_player(player_list, name)

```

**Remove Player**
```python
name = input("Please enter name: ")
player_list = remove_player(player_list, name)

```

**Buying Chips**
```python
name = input("Please enter name: ")
player_list = buy_player_chips(player_list, name)

```








   
