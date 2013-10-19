import os
from random import randint
global strength

def checkMoves(moveOption):
    n=0
    while n<3:
        if moves[n] == moveOption:
            return True
            pass
        elif moves[n]!=moveOption:
            return False
        n+=1

def whatMove():
    print "Do you want to " + moves[0] + " , " + moves[1] + " , " + moves[2] + " , " + moves[3]
    moveOption=raw_input("")
    moveOption=moveOption.lower()
    return moveOption
pHealth=200
health={'Alex':100, 'Nathan':100}
moves = ["punch", "do nothing", "do nothing", "do nothing"]
wades=["Alex", "Nathan"]
v1Teach=["Demas", "Pries", "Bosma", "Laurie", "Jacobsen", "Dipzinski"]
print "You arrive at ICHS, a mystical land filled with mosterous Wades, and"
print "friendly fairys."
print "you arrive at the front doors of the high school. What do you want to do?"
print "Go [in], or stay [out]"
inOrOut=raw_input("")
inOrOut=inOrOut.lower()
if inOrOut == "in":
    print "you go into the high school"
elif inOrOut == "out":
    raise SystemExit
print "As you enter the school, you see a menacing figure come out of the shadows"
wade = wades[randint(0,1)]
print "OH NO! It's a wild " + wade
print "what do you want to do? [F]ight or [R]un?"
FightOrRun=raw_input("")
FightOrRun=FightOrRun.lower()
if FightOrRun=="f":
    
    oppHealth=health[wade]
    while oppHealth >=0 and pHealth >=0:
        
        print "he has "+`oppHealth`+" health"
        print "you have "+`pHealth` + "health"
        moveOption = whatMove()
       
        if checkMoves(moveOption) == True:
            print "you " + moveOption + " your oponent"
            oppHealth = oppHealth - 50
            print "wade used cry"
            print "it did 10 damage"
            pHealth=pHealth-10
            
        else:
            print "you dont have that move"
            
if oppHealth <= 0:
    print "you won"
elif pHealth<=0:
    print "you lost"

