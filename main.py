# This is a sample Python script.

# Press Shift+F6 to execute it or replace it with your code.

# cd C:\Users\jacsi\Documents\NetBeansProjects\TicTacToe

import keyboard 
import datetime
import platform

#print(dir(platform))

y = datetime.datetime.now()
print(y)
print(' ')
print("Hi, welcome to the tic tac toe game!")
print("enjoy!")
print('  ')

name1 = input("Player 1, What is your name? ")
print("Hello, " + name1 + "!")
print('  ')
name2 = input("Player 2, What is your name? ")
print("Hello, " + name2 + "!")
print('  ')

player1 = " "
player2 = " "

array1 = [['-' for i in range(3)] for i in range(3)]
PlayerInput1 = 0
x = ' '
 

def chooseXO():

 global player1
 global player2
 global array1
 
 array1 = [['-' for i in range(3)] for i in range(3)]
 x = ' '
 print('  ')
 print(name1 +" Your decision. You want to be X or 0 ? choose:")
 print('  ')
 player1 = input("enter x or 0:")
 print('  ')
 if player1 == 'x' or 'X':
  player2 = '0'
  print('  ')
  print(name1 + " you choose X," + name2 + " will be 0")

 elif player1 == '0':
  player2 = 'x'
  print(name1 + " you chose 0," + name2 + " will be X")
  print('  ')
  
 else:
  print('  ')
  print('you had to choose.. press "y" if you want play')
  if input() == 'y':
    chooseXO()
  else:
   quit()  
    

chooseXO()


print(" ")
print(" ")
print(player1)
print(player2)

#print(array1[0][0], array1[0][1], array1[0][2])
#print(array1[1][0], array1[1][1], array1[1][2])
#print(array1[2][0], array1[2][1], array1[2][2])



def endGame(name):
 
 print('the winner is again.. ' + name)
 print('do you want to play again?')
 press = input('N or Y?')
 if press == 'y':
   
   chooseXO()
   
 else:
   print('was nice with your ass, bitch')
   quit()
   
   
def checkWinner(array1):
 
 for row in array1:
  if row[0] == row[1] == row[2] and row[0] != '-':
   return row[0]
  
 for col in range(3):
  if array1[0][col] == array1[1][col] == array1[2][col] and array1[0][col] != '-':
   return array1[0][col]
 
 if array1[0][0] == array1[1][1] == array1[2][2] and array1[0][0] != '-':
  return array1[0][0]
 if array1[0][2] == array1[1][1] == array1[2][0] and array1[0][2] != '-':
  return array1[0][2]
  
 return None 
  
def noWinners(array1):
 
 for row in array1:
  for cell in row:
   if cell == '-':
    return False
 return True   
 
    
def checkInput():

 print("  ")
 print(array1[0][0], array1[0][1], array1[0][2])
 print(array1[1][0], array1[1][1], array1[1][2])
 print(array1[2][0], array1[2][1], array1[2][2])
 print("  ")
 
 variable = 'IM INSIDE'

 winner = checkWinner(array1)
 if winner:
   
  variable = str(winner)
  print(variable + " this is the winner bitch")

  if variable == player1:
   print("the winner is " + name1)
   endGame(name1)  
  elif variable == player2:
   print("the winner is " + name2)
   endGame(name2)
 
 noWinner = noWinners(array1)
 if noWinner:
  print('  ')
  print('The board is full')
  print('  ')
  endGame()
   
 if x == ' ':
  makeInput1()
 elif x == player1:
   makeInput2()
 else:
   makeInput1() 
 
 
def makeInput1():
 global PlayerInput1
 global x
 print(name1 + ' choose where you want to mark your ' + player1)
 PlayerInput1 = input('press:')
 print('  ')
 x = ' '
 x = player1
 print("this is the X --- " + x)
 print('  ')
 defineKey()

def makeInput2():
 global PlayerInput1
 global x 
 print(" ")
 print("great,")
 print(name2 + ' choose the where you want to mark your ' + player2)
 PlayerInput1 = input('press:')
 print('  ')
 x = player2
 defineKey()

def reverse():
 print('  ')
 print('this field is already marked, mark another one...')
 if x == player1:
   makeInput1()
 if x == player2:
   makeInput2() 


def defineKey():
   
 def on_key_1():
    global array1
    if array1[2][0] != '-':
     reverse()
          
    elif array1[2][0] == '-':
     array1[2][0] = x
     checkInput()
     
 def on_key_2():
    global array1
    if array1[2][1] != '-':
     reverse()
     
    elif array1[2][1] == '-':
     array1[2][1] = x
     checkInput()
     
 def on_key_3():
    global array1
    global x
    if array1[2][2] != '-':
     reverse()
     
    elif array1[2][2] == '-':
     array1[2][2] = x
     checkInput()
     
 def on_key_4():
    global array1
    global x
    if array1[1][0] != '-':
     reverse()
     
    elif array1[1][0] == '-':
     array1[1][0] = x
     checkInput()
     
 def on_key_5():
    global array1
    global x
    if array1[1][1] != '-':
     reverse()
     
    elif array1[1][1] == '-':
     array1[1][1] = x
     checkInput()
     
 def on_key_6():
    global array1
    global x
    if array1[1][2] != '-':
     reverse()
     
    elif array1[1][2] == '-':
     array1[1][2] = x
     checkInput()
     
 def on_key_7():
    global array1
    global x
    if array1[0][0] != '-':
     reverse()
     
    elif array1[0][0] == '-':
     array1[0][0] = x
     checkInput()
     
 def on_key_8():
    global array1
    global x
    if array1[0][1] != '-':
     reverse()
     
    elif array1[0][1] == '-':
     array1[0][1]  = x
     checkInput()
     
 def on_key_9():
    global array1
    global x
    if array1[0][2] != '-':
     reverse()
     
    elif array1[0][2] == '-':
     array1[0][2] = x
     checkInput()
     
 if PlayerInput1 == "1":
    on_key_1()
 
 if PlayerInput1 == "2":
    on_key_2()
  
 if PlayerInput1 == "3":
    on_key_3()
 
 if PlayerInput1 == "4":
    on_key_4()
    
 if PlayerInput1 == "5":
    on_key_5()
 
 if PlayerInput1 == "6":
    on_key_6()
    
 if PlayerInput1 == "7":
    on_key_7()
    
 if PlayerInput1 == "8":
    on_key_8()
    
 if PlayerInput1 == "9":
    on_key_9()   
    
 else: 
  reverse()
     
checkInput()





