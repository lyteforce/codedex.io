# Write code below 💖
# Rock Paper Scissors Lizard Spock

# Importing the random module to generate a random choice for the computer
import random

# Initializing player choice, computer choice, result, and game conditions
player = 0
result = ""
play_again = ""
game_over = False

print("=== Rock Paper Scissors Lizard Spock ===\n")

print("Scissors cuts Paper,\nPaper covers Rock,\nRock crushes Lizard,\nLizard poisons Spock,\nSpock smashes Scissors,\nScissors decapitates Lizard,\nLizard eats Paper,\nPaper disproves Spock,\nSpock vaporizes Rock,\n(and as it always has) Rock crushes Scissors.\n")
while game_over == False:
  print("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖")
  player = int(input("Pick a number: "))
  while player < 1 or player > 5:
    print("Invalid choice!!")
    player = int(input("Pick a number: "))
  computer = random.randint(1, 5)

  if player == 1:
    print("You chose: ✊")
  elif player == 2:
    print("You chose: ✋")
  elif player == 3:
    print("You chose: ✌️")
  elif player == 4:
    print("You chose: 🦎")
  else:
    print("You chose: 🖖")

  if player == computer:
    result = "It's a draw!"
  elif computer == 1:
    print("CPU chose: ✊")
    if player == 4 or player == 3:
      result = "The CPU won!"
  elif computer == 2:
    print("CPU chose: ✋")
    if player == 1 or player == 5:
      result = "The CPU won!"
  elif computer == 3:
    print("CPU chose: ✌️")
    if player == 2 or player == 4:
      result = "The CPU won!"
  elif computer == 4:
    print("CPU chose: 🦎")
    if player == 5 or player == 2:
      result = "The CPU won!"
  elif computer == 5:
    print("CPU chose: 🖖")
    if player == 1 or player == 3:
      result = "The CPU won!"
  else:
    result = "The player won!"

  print(result)
  play_again = input("Do you want to play again? Y or N: ").upper()
  while play_again != "Y" and play_again != "N":
    print(f"You entered {play_again} - Invalid choice!!")
    play_again = input("Do you want to play again? Y or N: ").upper()

  if play_again == "N":
    game_over = True