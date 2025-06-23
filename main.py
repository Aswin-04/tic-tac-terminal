import sys

class Player:
  def __init__(self, name, sign):
    self.name = name
    self.sign = sign

  def get_name(self):
    return self.name;

  def get_sign(self):
    return self.sign
  

class Cell:
  def __init__(self, index):
    self.index = index
    self.sign = "-"

  def get_sign(self):
    return self.sign

  def get_index(self):
    return self.index
  
  def set_sign(self, sign):
    self.sign = sign


class Game:
  board_size = 9
  winning_combos = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
  ]    
  
  def __init__(self, player1, player2):
    self.player1 = player1
    self.active_player = player1
    self.player2 = player2

    
  def create_board(self):
    self.board = []
    for idx in range(1, Game.board_size+1):
      cell = Cell(idx)
      self.board.append(cell)


  def display_board(self):
    row_size = self.board_size//3
    col_size = self.board_size//3
    crnt_idx  = 1;

    for row in range(row_size):
      for _ in range(col_size):

        crnt_cell = self.board[crnt_idx-1]
        sign = crnt_cell.get_sign()

        if crnt_idx not in [3, 6, 9]:
          print(f" {sign} |", end="")
        else: 
          print(f" {sign} ")
        
        crnt_idx+=1
      
      if row != 2: 
        print("-----------")
      else:
        print()


  def set_cell_sign(self, idx, sign):
    target_cell = self.board[idx-1]
    
    if target_cell.get_sign() != "-":
      print(f"Invalid: cell {target_cell.get_index()} is already occupied")
      print("please enter a valid cell number\n")
      return -1
    
    target_cell.set_sign(sign)

  
  def check_for_win_or_tie(self):
    is_tie = True
    for [idx1, idx2, idx3] in Game.winning_combos:
      sign1 = self.board[idx1-1].get_sign()
      sign2 = self.board[idx2-1].get_sign()
      sign3 = self.board[idx3-1].get_sign()

      if sign1 == "-" or sign2 == "-" or sign3 == "-":
        is_tie = False
        continue

      elif sign1 == sign2 and sign1 == sign3:
        return "win"
      
    return "tie" if is_tie else None
  
  
  def get_active_player(self):
    return self.active_player
  
  def set_active_player(self, player):
    self.active_player = player
  

  def display_result(self, status):
    
    if status != None:
      self.display_board()

    if status == "tie":
      print("Shit.. it's a tie!")
      sys.exit()

    if status == "win":
      player = self.get_active_player()
      print(f"Congratulations! {player.get_name()} won the game")
      sys.exit()

  
  def switch_player_turn(self):
    if self.get_active_player() is self.player1:
      self.set_active_player(self.player2)
    else:
      self.set_active_player(self.player1)


  def get_input(self):
    player_name = self.get_active_player().get_name()
    print(f"({player_name}'s turn)")
    try:
      idx = int(input("Enter a number from (1-9): "))

    except ValueError:
      print("Invalid input: Enter a valid number..\n")
      return -1
    
    except KeyboardInterrupt:
      print("\nGame interrupted by user. Exiting....")
      sys.exit()
      
    if idx < 1 or idx > 9:
      print("Invalid input: The number must be in the range(1-9)")
      return -1
    
    return idx
  

def prompt_player_name(player):
  while(True):
    try:
      name = input(f"Enter {player}'s name: ").strip().upper()

    except KeyboardInterrupt:
      print("\nGame interrupted by user. Exiting....")
      sys.exit()

    if name == "":
      print("Please enter a valid name..")
    
    else: return name


def main():

  try:
    key_pressed = input("Enter any key to start the game / q to quit: ")
  except KeyboardInterrupt:
    print("\nGame interrupted by user. Exiting....")
    sys.exit()

  if(key_pressed == "q"):
    sys.exit()
  
  name1 = prompt_player_name("Player_1")
  name2 = prompt_player_name("Player_2")
  print()

  player1 = Player(name1, "X")
  player2 = Player(name2, "O")

  game = Game(player1, player2)
  game.create_board()

  while True:

    game.display_board()
    cell_idx = game.get_input()
    print()
    if cell_idx == -1:
      continue
    
    sign = game.get_active_player().get_sign()
    if game.set_cell_sign(cell_idx, sign) == -1:
      continue

    status = game.check_for_win_or_tie()
    game.display_result(status)
    game.switch_player_turn()

if __name__ == "__main__":
  main()
  


      



  

  




  

    
    

    

  






