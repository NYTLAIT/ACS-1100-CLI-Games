from random import randint

roles = ["Bear", "Ninja", "Cowboy"]

player = input("Bear, Ninja, or Cowboy? > ")
computer = roles[randint(0,2)]

if computer == player:
  print("DRAW!")
elif computer == "Cowboy":
  if player == "Bear":
    print("You lose!", player, "is shot by", computer)
  else:
    print("You win!", player, "assasinates", computer)
elif computer == "Bear":
  if player == "Cowboy":
    print("You win!", player, "shoots", computer)
  else:
    print("You lose!", player, "is mauled and eaten by", computer)
elif computer == "Ninja":
  if player == "Cowboy":
    print("You lose!", player, "is assasinated by", computer)
  else:
    print("You win!", player, "mauls and eats", computer)

else:
    print(computer, player)