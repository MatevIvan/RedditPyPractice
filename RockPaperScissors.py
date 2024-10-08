import random

# for this game I am assuming the player will input correct values
"""
Build a rock paper scissors game, that takes in input from a player and has them play against a computer.
Once you have the basic, make it best of 3
If you want it harder, make it two player
"""

def roundWinner(user1, user2):
  # this functions decides who wins the round
  """
  input: 
    Rock = 1
    Paper = 2
    Scissors = 3
  output:
    user1 lost: 0
    user1 won: 1
    user1 tie: 2
  """
  # all the win conditions
  if (user1 == 1 and user2 == 3) or (user1 == 2 and user2 == 1) or (user1 == 3 and user2 == 2):
    return 1
  # all the lose conditions
  if (user1 == 1 and user2 == 2) or (user1 == 2 and user2 == 3) or (user1 == 3 and user2 == 1):
    return 0
  # if its a tie
  return 2


prompt = "Enter \"1\" for rock, \"2\" for paper, \"3\" for scissors, any key for random. "
user1RoundScore = 0
user2RoundScore = 0
while True:
  print() # empty line for spacing
  # set up default values for both players
  user1 = 0
  user2 = 0
  userInput = input("Would you like to play a bot, or a 1v1?\n(Enter \"1\" for bot, \"2\" for 1v1, or any other key to quit.) ")
  
  match userInput:
    # Bot
    case "1":
      gamesPlayed = 0
      while gamesPlayed < 3:
        print() # for spacing
        user1 = (int)(input(prompt))
        user2 = random.randint(1, 3)
        if user1 < 1 or user1 > 3:
          user1 = random.randint(1,3)
        winner = roundWinner(user1,user2)
        # user2 (bot) wins
        if winner == 0:
          print("The bot won that round!")
          user2RoundScore += 1
          gamesPlayed += 1
        # user1 wins
        if winner == 1:
          print("You won that round!")
          user1RoundScore += 1
          gamesPlayed += 1
        # A tie!
        if user1 == user2:
          print("Its a tie!! Current standing:",user1RoundScore,":",user2RoundScore)
        # user1 wins the match
        if user1RoundScore == 2:
          print("You beat the Bot!!")
          break
        # user2 wins the match
        if user2RoundScore == 2:
          print("The bot won this round.")
          break

    # Human
    case "2":
      gamesPlayed = 0
      print("Player 1, please enter your value first. Then player 2 can enter their value.")
      while gamesPlayed < 3:
        user1 = (int)(input(prompt))
        user2 = (int)(input(prompt))
        if user1 < 1 or user1 > 3:
          user1 = random.randint(1,3)
        if user2 < 1 or user2 > 3:
          user2 = random.randint(1,3)
        winner = roundWinner(user1,user2)
        # user2 wins
        if winner == 0:
          print("Player 2 won that round!")
          user2RoundScore += 1
          gamesPlayed += 1
        # user1 wins
        if winner == 1:
          print("Player 1 won that round!")
          user1RoundScore += 1
          gamesPlayed += 1
        # A tie!
        if user1 == user2:
          print("Its a tie!! Current standing:",user1RoundScore,":",user2RoundScore)
        # user1 wins the match
        if user1RoundScore == 2:
          print("Player 1 beat Player 2!")
          break
        # user2 wins the match
        if user2RoundScore == 2:
          print("Player 2 beat Player 1!")
          break

    # Quit game
    case _:
      break