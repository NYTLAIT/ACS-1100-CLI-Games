from random import randint

player = input("Bear, Ninja, or Cowboy? > ")
print(player)

roles = ["Bear", "Ninja", "Cowboy"]
computer = roles[randint(0,2)]
print(computer)
