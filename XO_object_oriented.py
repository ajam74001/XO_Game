# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 22:33:27 2021

@author: ajamshidi18
"""

import numpy as np 
board=[[' ', '|', ' ', '|',' ' ],['- ', '- ', '- ', '- '],[' ', '|', ' ', '|',' ' ],['- ', '- ', '- ', '- '], [' ', '|', ' ', '|',' ' ]]
player_pos= []
cpu_pos= []
#
#def gameboard(board):
#    for i in range(len(board)):
#        for j in range(len(board[i])):
#            print(board[i][j], end= " " )
#        print('\n')    
#
#gameboard(board)        
#
#def checkwinner(pos):
#    if set([1,2,3]).issubset(set(pos)) or set([4,5,6]).issubset(set(pos)) or set([7,8,9]).issubset(set(pos)) or set([1, 4, 7]).issubset(set(pos)) or set([2,5,8]).issubset(set(pos)) or set([3,6,9]).issubset(set(pos)) or set([1,5,9]).issubset(set(pos)) or set([3,5,7]).issubset(set(pos)):
#        return True
#    else:
#        return False
#
#def cpu_move(empty_pos):
#    if empty_pos==set({}):
#        return print('no winner!')
#        
#   
#    for i in range(len(empty_pos)):
#        cpu_p = list(empty_pos)[i]
#        cpu_pos_helper= cpu_pos+[cpu_p]
#        if checkwinner(cpu_pos_helper):
##            cpu_pos.append(cpu_p)
##            positioning(cpu_p, 'O')
##            gameboard(board)
##            print('the CPU WON!')
#            return cpu_p
#            break
#    for i in range(len(empty_pos)):
#        helper = player_pos+ [list(empty_pos)[i]]
#        if checkwinner(helper):
##            cpu_pos.append(list(empty_pos)[i])
##            positioning(list(empty_pos)[i], 'O')
##            gameboard(board)
#            return list(empty_pos)[i]
#            break
#    return list(empty_pos)[np.random.randint(0,len(empty_pos))]    
#def positioning(p, player):
#    symbol= player
#    if p==1:
#        board[0][0]= symbol
#    elif p==2:
#        board[0][2]=symbol
#    elif p==3:
#        board[0][4]=symbol
#    elif p==4:
#        board[2][0]=symbol
#    elif p==5:
#        board[2][2]=symbol
#    elif p==6:
#        board[2][4]=symbol
#    elif p==7:
#        board[4][0]=symbol
#    elif p==8:
#        board[4][2]= symbol
#    elif p==9:
#        board[4][4]=symbol
#    else:
#        print('fucker, enter a valid number')
#    
#    return p
#
#empty_pos={1,2,3,4,5,6,7,8,9}
#
#while True:
#    if empty_pos==set({}):
#        print('no winner!')
#        break
#    print('specify the location of your move (1-9): ')
#    p= int(input('enter now '))
#    if p not in empty_pos:
#       print('location is already filled; try again ')
#       p= int(input('enter now '))
#    positioning(p, 'X')
#    player_pos.append(p)
#    empty_pos = empty_pos - {p}
#    gameboard(board) 
#    
#    if checkwinner(player_pos):
#        print('the player WON!')
#        break
#    
#    
#    cpu_p= cpu_move(empty_pos)
#    cpu_pos.append(cpu_p)
#    empty_pos = empty_pos - {cpu_p}
#    positioning(cpu_p, 'O')
#    gameboard(board)
#    if checkwinner(cpu_pos):
#        print('the CPU WON!')
#        break
#     
 
class XO:
    def __init__(self,borad):
         self.board= board
         player_pos= []
         cpu_pos= []
         
    def gameboard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end= " " )
            print('\n')
            
    def checkwinner(self, pos):
        if set([1,2,3]).issubset(set(pos)) or set([4,5,6]).issubset(set(pos)) or set([7,8,9]).issubset(set(pos)) or set([1, 4, 7]).issubset(set(pos)) or set([2,5,8]).issubset(set(pos)) or set([3,6,9]).issubset(set(pos)) or set([1,5,9]).issubset(set(pos)) or set([3,5,7]).issubset(set(pos)):
            return True
        else:
            return False
        
    def positioning(self, p, player):
        symbol= player
        if p==1:
            board[0][0]= symbol
        elif p==2:
            board[0][2]=symbol
        elif p==3:
            board[0][4]=symbol
        elif p==4:
            board[2][0]=symbol
        elif p==5:
            board[2][2]=symbol
        elif p==6:
            board[2][4]=symbol
        elif p==7:
            board[4][0]=symbol
        elif p==8:
            board[4][2]= symbol
        elif p==9:
            board[4][4]=symbol
        else:
            print('fucker, enter a valid number')
        
        return p
    
    def cpu_move(self, empty_pos):
#        if empty_pos==set({}):
#            return print('no winner!!')
        
        for i in range(len(empty_pos)):
            cpu_p = list(empty_pos)[i]
            cpu_pos_helper= cpu_pos+[cpu_p]
            if self.checkwinner(cpu_pos_helper):
    
                return cpu_p
                break
        for i in range(len(empty_pos)):
            helper = player_pos+ [list(empty_pos)[i]]
            if self.checkwinner(helper):
    #            cpu_pos.append(list(empty_pos)[i])
    #            positioning(list(empty_pos)[i], 'O')
    #            gameboard(board)
                return list(empty_pos)[i]
                break
        return list(empty_pos)[np.random.randint(0,len(empty_pos))]    
    
    def main(self):
        empty_pos={1,2,3,4,5,6,7,8,9}
        self.gameboard()
        while True:
            
            print('specify the location of your move (1-9): ')
            p= int(input('enter now '))
            if p not in empty_pos:
               print('location is already filled; try again ')
               p= int(input('enter now '))
            self.positioning(p, 'X')
            player_pos.append(p)
            empty_pos = empty_pos - {p}
            self.gameboard() 
            
            if self.checkwinner(player_pos):
                print('the player WON!')
                break
            
            if empty_pos==set({}):
                print('no winner!')
                break
            
            cpu_p= self.cpu_move(empty_pos)
            cpu_pos.append(cpu_p)
            empty_pos = empty_pos - {cpu_p}
            self.positioning(cpu_p, 'O')
            self.gameboard()
            if self.checkwinner(cpu_pos):
                print('the CPU WON!')
                break
             
ins= XO(board)                
ins.main()
