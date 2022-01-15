"""Tic-Tac-Toe: A Solution
Author: Elizeu Ferreira"""

import os
import random
from colorama import Fore

playAgain="s"
plays=0
whoPlays=2  #1 = CPU | #2 = Jogador
maxPlays=9
winner=""
old=[
    [" "," "," "],#L0C0 L0C1 L0C2
    [" "," "," "],#L1C0 L1C1 L1C2
    [" "," "," "] #L2C0 L2C1 L2C2
]

def main():
   global old
   global plays
   os.system("cls")
   print("    1   2  3")
   print("1:  " + old[0][0] + " | " + old[0][1] + " | " + old[0][2])
   print("   -----------")
   print("2:  " + old[1][0] + " | " + old[1][1] + " | " + old[1][2])
   print("   -----------")
   print("3:  " + old[2][0] + " | " + old[2][1] + " | " + old[2][2])
   print("plays: " + Fore.GREEN + str(plays) + Fore.RESET)

def playerPlays():
    global plays
    global whoPlays
    global maxPlays
    if whoPlays==2 and plays < maxPlays:
        line=int(input("line...: "))
        line=line-1
        
        collum=int(input("collum..: "))
        collum=collum-1
        
        try:
            while old[line][collum]!=" ":
                line=int(input("line...: "))
                line=line-1
                collum=int(input("collum..: "))
                collum=collum-1
            old[line][collum]="X"
            whoPlays=1
            plays+=1
        except: 
            print("Invalid move")
            os.system("Pause")
def cpuPlays():
    global plays
    global whoPlays
    global maxPlays
    if whoPlays==1 and plays<maxPlays:
        line=random.randrange(0,3)
        collum=random.randrange(0,3)
        
        while old[line][collum]!=" ":
            line=random.randrange(0,3)
            collum=random.randrange(0,3)
        
        old[line][collum]="O"
        plays+=1
        whoPlays=2
        
def checkVictory():
    global old
    victory="n"
    simbol=["X", "O"]
    for s in simbol:
        victory="n" 
        iline=icollum=0
        
        #check lines
        while iline>3: 
            sum=0
            icollum=0
            while icollum>3:
                if (old[iline][icollum]==s):
                    sum+=1
                icollum+=1
            if(sum==3):
                victory= s
                break
            iline+=1
        if (victory!="n"):
            break
        
        #check collums
        iline = icollum = 0
        while icollum<3: 
            sum=0
            iline=0
            while iline<3:
                if (old[iline][icollum]==s):
                    sum+=1
                iline+=1
            if(sum==3):
                victory= s
                break
            icollum+=1
        if (victory!="n"):
            break
        #check diagonal e-d
        sum=0
        idiag=0
        while idiag<3:
            if (old[idiag][idiag]==s):
                sum+=1
            idiag+=1
        if(sum==3):
            victory= s
            break
        #check diagonal d-e
        sum=0
        idiagl=0
        idiagc=2
        while idiagc>=0:
            if(old[idiagl][idiagc]==s):
                sum+=1
            idiagl+=1
            idiagc-=1
        if(sum==3):
            victory= s
            break 
    return victory

def reset():
    global old
    global plays
    global whoPlays
    global maxPlays
    global winner 
    plays=0
    whoPlays=2
    maxPlays=9
    winner="n"
    old=[
        [" "," "," "],#L0C0 L0C1 L0C2
        [" "," "," "],#L1C0 L1C1 L1C2
        [" "," "," "] #L2C0 L2C1 L2C2
    ] 

while (playAgain=="s"):
    while True:
       main()
       playerPlays()
       cpuPlays()
       winner=checkVictory()
       if(winner!="n")or (plays>=maxPlays):
           break
       
    print(Fore.RED + "GOOD GAME. Thanks for playing!" + Fore.YELLOW)
    if winner=="X":
        print("You won")
    elif winner == "O":
        print("The Machine won")  
    else: 
        print("tied the game")
    playAgain=input(Fore.BLUE + "PLAY AGAIN? [s/n]: " + Fore.RESET)
    reset()

if __name__ == "__main__":
    main()