import os
import platform

turn    = 1 # 1 - Player 1 | 2 - Player 2
clean   = ('clear','cls')[platform.system() == 'Windows']
p_char  = 'X'
c_char  = 'O'
table   = ['1','2','3', '4','5','6','7','8','9']

def view():
    global table

    print (" %s | %s | %s " % (table[0], table[1], table[2]))
    print ("---+---+---")
    print (" %s | %s | %s " % (table[3], table[4], table[5]))
    print ("---+---+---")
    print (" %s | %s | %s " % (table[6], table[7], table[8]))
    print ("---+---+---")