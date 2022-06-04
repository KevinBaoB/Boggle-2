# You should re-use and modify your old BoggleBoard class to support the new requirements

import random
import string

class BoggleBoard:
  alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

  def __init__(self):
    self.game_board = ['_'] * 16
    self.dice = [
      'AAEEGN',
      'ELRTTY',
      'AOOTTW',
      'ABBJOO',
      'EHRTVW',
      'CIMOTU',
      'DISTTY',
      'EIOSST',
      'DELRVY',
      'ACHOPS',
      'HIMNQU',
      'EEINSU',
      'EEGHNW',
      'AFFKPS',
      'HLNNRZ',
      'DEILRX'
    ]
    


  def shake(self):
    random.shuffle(self.dice)
    for i, under_score in enumerate(self.game_board): 
      random_letter = (random.choice(self.dice[i]))
      if(random_letter == 'Q'):
        self.game_board[i] = 'QU'
      else:
        self.game_board[i] = random_letter


  def view_game_board(self):
    return self.game_board

  def print_board(self):
    for i in range(0, len(self.game_board), 4):
      print(" ".join(self.game_board[i:i+4]))

  

boggle = BoggleBoard()
boggle.shake()
boggle.print_board()