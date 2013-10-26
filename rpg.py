try:
    import time
    # we import time to use the sleep function. It lets the terminal stay open for a bit after we raise a sysExit
    x=1
    # x is = to 1 if time can be imported. This is so that the program will run on sys's w/o time
except:
    x=0
# used to randomize moves that are used
from random import randint

#global strength  implement this as a modifyer to the damage the player deals

def changeArea():
    """This function is called when a player wants to change areas"""

    print "What area do you want to change into? 2 or 3?"
    areaChoice = raw_input()
    return areaChoice
#Make moves based on expereience, not level. Make exp a running total


def expStuff(exp):
    if exp >= 100 and exp < 200:
        print "do you want to learn roundhouse kick? Y or N"
        moveYorN = raw_input("")
        if moveYorN == "Y" or "y":
            print "which move do you want to replace? (type the number)"
            print "0: " + heldmoves[0]
            print "1: " + heldmoves[1]
            print "2: " + heldmoves[2]
            print "3: " + heldmoves[3]
            getRidOf = int(raw_input(""))
            heldmoves[getRidOf] = "roundhouse"
        else:
            pass








def checkMoves(moveOption):
    """Checks move that the player wants to use against list of held moves"""
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

def moveUsed(currentArea):
    """Calculates which move the opponent is to use. It is different if they are in different areas, hence the if
    statement"""
    if currentArea == 2:
        moveRandom=randint(0,1)
        usedMove=oppMoves2[moveRandom]
        return usedMove
    elif currentArea == 3:
        moveRandom=randint(0,1)
        usedMove=oppMoves3[moveRandom]
        return usedMove


def whatMove():
    """
    prints all of the users held moves. Takes input from the user. turns that input lowercase.return lowercase input
    """
    print "Do you want to " + heldmoves[0] + " , " + heldmoves[1] + " , " + heldmoves[2] + " , " + heldmoves[3]
    moveOption=raw_input("")
    moveOption=moveOption.lower()
    return moveOption

#initializes the players health
pHealth=300
#list the starting health of opponents
health={'Alex': 100, 'Nathan': 100, 'Demas':200, 'Pries': 225, 'Bosma': 175, 'Laurie': 200, 'Jacobsen': 150, 'Dipzinski'
: 225, 'Bebee': 300, 'Gymory': 350, 'Lestage': 325, 'Koss': 250, 'Gartrell': 400, 'Halstead':350}
allMoves = {'punch':50, 'kick':60, 'karate':60, 'roundhouse':80}
oppMoves2=['hit', 'yell']
oppDamage2={'hit':50, 'yell':60}
oppMoves3=['hard hit', 'screech']
oppDamage3={'hard hit':75, 'screech':100}
heldmoves = ["punch", "kick", "do nothing", "do nothing"]
wades=["Alex", "Nathan"]
v2Teach=["Demas", "Pries", "Bosma", "Laurie", "Jacobsen", "Dipzinski"]
v3Teach=["Bebee", "Gymory", "Lestage", "Koss", "Gartrell", "Halstead"]
exp=0

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

                usedMove=moveUsed(currentArea)
                print opponent + " used " + usedMove
                pHealth -= oppDamage2[usedMove]
                print "you have "+`pHealth` + " health left"

            if pHealth <=0:

                print "you lost"
                if x==1:
                    time.sleep(10)
                    print "i'm sleeping"
                    raise SystemExit

                elif x==0:

                    print "i didnt sleep"
                    raise SystemExit

            elif oppHealth<=0:
                print "you won"
                exp+=100
                expStuff(exp)





        elif currentArea==3:

            opponent = v3Teach[randint(0,5)]
            print "A wild " + opponent + " appeared"
            oppHealth=health[opponent]
            while pHealth>0 and oppHealth>0:

                print "The opponent has "+`oppHealth` + " health"
                print "Do you want to " + heldmoves[0] + " , "+ heldmoves[1]+ " , " +heldmoves[2]+ " , " +heldmoves[3] + "?"
                moveOption=raw_input("")
                moveOption=moveOption.lower()
                if checkMoves(moveOption)==True:
                    damage=moveDamage(moveOption)
                    oppHealth=oppHealth-damage

                else:
                    print "That isn't a move"

                usedMove=moveUsed(currentArea)
                print opponent + " used " + usedMove
                pHealth -= oppDamage3[usedMove]
                print "you have "+`pHealth` + " health left"

            if pHealth <= 0:

                print "you lost"
                if x == 1:
                    time.sleep(10)
                    raise SystemExit

                elif x == 0:
                    raise SystemExit

            elif oppHealth<=0:
                print "you won"
        else:
            print "I dont know which area you're in"
    













