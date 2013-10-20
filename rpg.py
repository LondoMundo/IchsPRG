import os
from random import randint
global strength
def changeArea():
    print "What area do you want to change into? 2 or 3?"
    areaChoice = raw_input()
    return areaChoice
def checkMoves(moveOption):
    if moveOption == heldmoves[0]:
        return True
    elif moveOption == heldmoves[1]:
        return True
    elif moveOption == heldmoves[2]:
        return True
    elif moveOption == heldmoves[3]:
        return True
    else:
        return False

def moveDamage(move):
    return allMoves[move]
    

def whatMove():
    print "Do you want to " + heldmoves[0] + " , " + heldmoves[1] + " , " + heldmoves[2] + " , " + heldmoves[3]
    moveOption=raw_input("")
    moveOption=moveOption.lower()
    return moveOption
pHealth=200
health={'Alex':100, 'Nathan':100, 'Demas':200, 'Pries':225, 'Bosma': 175, 'Laurie':200, 'Jacobsen':150, 'Dipzinski':225}
allMoves = {'punch':50, 'kick':60, 'karate':60}
heldmoves = ["punch", "kick", "do nothing", "do nothing"]
wades=["Alex", "Nathan"]
v2Teach=["Demas", "Pries", "Bosma", "Laurie", "Jacobsen", "Dipzinski"]
v3Teach=["Bebee", "Gymory", "Lestage", "Koss", "Gartrell", "Halstead"]
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
    while oppHealth >0 and pHealth >0:
        
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
            
if oppHealth < 1:
    print "you won"
elif pHealth<0:
    print "you lost"
    raise SystemExit

print "Which new move do you want to learn? [Kick], or [Karate] Chop?"
newMove = raw_input("")
newMove=newMove.lower()
if newMove == "kick":
    heldmoves[1]="kick"
    print heldmoves
elif newMove == "karate":
    heldmoves[1]="karate"
    print heldmoves
print "You have passed the first area. You gained 10 exp. You have now moved onto area two of ICHS."
currentArea=2
while 1==1:
    print "you are in area "+`currentArea`
    print "What do you want to do? [F]ight, [C]hange area?"
    whatToDo=raw_input("")
    whatToDo=whatToDo.lower()
    if whatToDo == "c":
        currentArea=changeArea()
        currentArea=int(currentArea)
        print currentArea
    elif whatToDo == "f":
        if currentArea==2:
            opponent = v2Teach[randint(0,5)]
            print "A wild " + opponent + " appeared"
            oppHealth = health[opponent]
            while pHealth>0 and oppHealth>0:
                print "the opponent has " + `oppHealth` + " health"
                print "Do you want to " + heldmoves[0] + " , "+ heldmoves[1]+ " , " +heldmoves[2]+ " , " +heldmoves[3] + "?"
                moveOption=raw_input("")
                moveOption = moveOption.lower()
                if checkMoves(moveOption) == True:
                    damage = moveDamage(moveOption)
                    oppHealth = oppHealth-damage
                else:
                    print "That isn't a move"
                
                

        elif currentArea==3:
            opponent = v3Teach[randint(0,5)]
            print "A wild " + opponent + " appeared"
        else:
            print "I dont know which area you're in"
    













