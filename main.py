import os
from util.print import print_title, print_instruction


print_title()
print_instruction()

os.system('cls')

board=""

for letters in range(4):
  board=color.BG_GRAY + color.BOLD_BLACK + "   " + board

print(board + color.RESET)

