# -*- coding: utf-8 -*-
import time
import os
from colorama import Fore, Back, Style

####

board = ["1","2","3","4","5","6","7","8","9"]

def draw_board(board):
	try:
		os.system('clear')
	except:
		os.system('cls')
	print(Fore.RED + """
	   ___________________________________
	» | 匚尺乇卂ㄒ乇Ɗ  乃ㄚ  ㄒ卄ㄖ爪卂丂 | «
	» |    ㄒㄖ爪爪ㄚ  G凵几  ㄒ乇卂爪    | «
	» |        ㄒ丨匚 ㄒ卂Ҡ ㄒㄖ乇        | «
	» |___________________________________| «
""" + Style.RESET_ALL)
	print("-"*7)
	for i in range(3):
		print("|" + Fore.RED +  Back.GREEN + str(board[0+i*3]) + Style.RESET_ALL + "|" + Fore.RED +  Back.GREEN + str(board[1+i*3]) + Style.RESET_ALL + "|" +Fore.RED +  Back.GREEN + str(board[2+i*3]) + Style.RESET_ALL + "|")
		print("-"*7)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input(Fore.CYAN + "Куда поставим " + player_token+"? " + Fore.MAGENTA)
        try:
            player_answer = int(player_answer)
        except:
            print(Style.RESET_ALL + Fore.GREEN + Back.RED+"Некорректный ввод. Вы уверены, что ввели число?" + Style.RESET_ALL)
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print(Style.RESET_ALL + Back.RED + "Эта клеточка уже занята"+Style.RESET_ALL)
        else:
            print(Style.RESET_ALL + Back.RED + Fore.YELLOW+"Некорректный ввод. Введите число от 1 до 9 чтобы походить."+Style.RESET_ALL)

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False
    
    
def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        draw_board(board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(Fore.YELLOW + tmp + " выиграл!" + Style.RESET_ALL)
                print(Fore.CYAN + """
  ____  ____  ____  ____  ____  ____ 
 ||T ||||h ||||o ||||m ||||a ||||s ||
 ||__||||__||||__||||__||||__||||__||
 |/__\||/__\||/__\||/__\||/__\||/__\|

                """ + Style.RESET_ALL)
                print("""
 .___..__..  ..  ..   ,  .__ .  ..  .
   |  |  ||\/||\/| \./   [ __|  ||\ |
   |  |__||  ||  |  |    [_./|__|| \|
                                     
 .___..___.__..  .
   |  [__ [__]|\/|
   |  [___|  ||  |
                  

                """)
                win = True
                break
        if counter == 9:
            print(Back.YELLOW + Fore.BLACK + "Ничья!" + Style.RESET_ALL)
            print(Fore.CYAN + """
  ____  ____  ____  ____  ____  ____ 
 ||T ||||h ||||o ||||m ||||a ||||s ||
 ||__||||__||||__||||__||||__||||__||
 |/__\||/__\||/__\||/__\||/__\||/__\|


            """ + Style.RESET_ALL)
            print("""
 .___..__..  ..  ..   ,  .__ .  ..  .
   |  |  ||\/||\/| \./   [ __|  ||\ |
   |  |__||  ||  |  |    [_./|__|| \|
                                     

 .___..___.__..  .
   |  [__ [__]|\/|
   |  [___|  ||  |
                  


            """)
            break
    
    
main(board)




