"""
TODO:
    NOW:
        add the ability to dodge moves, based on a skill that the player has. It is dependent on level, but at a certain
        point, it has to cap, so you don't dodge every move.

        London Reed, Coral, and Plain Bagel Easter Eggs

        saying "no" to a move still acts as if you said yes

        Vegetarian option. lol

        GUI?

    ALWAYS:
        implement all of the things added in "Area 2" Into area 3.



DONE:

Integrate inventory option into the game. Its all set up, it just needs to be added as a prompt

Add weapons into the game. Wepons reuqire a system where the player is wearing things.

do nothing crashes the program


NOTES:
    Last night, we implemented the GUI for equipping armour. The GUI for equiping weapons should be pretty similar,
    but it needs error handling
    Comment

"""

try:
    import time
    # we import time to use the sleep function. It lets the terminal stay open for a bit after we raise a sysExit
    x = 1
    # x is = to 1 if time can be imported. This is so that the program will run on sys's w/o time
except:
    x = 0
# used to randomize moves that are used
from random import randint

import wx




#inventory
global inv
inv = {1: "Mutton", 2: "potion", 3: "sword", 4: "Nothing", 5: "Nothing", 6: "Nothing", 7: "Nothing", 8: "Nothing",
       9: "Nothing", 10: "Nothing"}
classify = {"Mutton": "food", "potion": "food", "metal plate": "armour", "leather plate": "armour",
            "Nothing": "Nothing", "sword": "weapon", "spear": "weapon"}
defenseItems = {"Nothing": 0, "leather plate": 3, "metal plate": 5}
offenseItems = {'Nothing': 0, "sword": 60, "spear": 75}
invDesc = {"Mutton": "a meat that heals 100 health", "potion": "a weak health potion that heals 150 health"}
invFunc = {'Mutton': 100, 'potion': 150}
#list the starting health of opponents
health = {'Alex': 100, 'Nathan': 100, 'Demas': 200, 'Pries': 225, 'Bosma': 175, 'Laurie': 200, 'Jacobsen': 150,
          'Dipzinski'
          : 225, 'Bebee': 300, 'Gymory': 350, 'Lestage': 325, 'Koss': 250, 'Gartrell': 400, 'Halstead': 350}
allMoves = {'do nothing': 0, 'punch': 50, 'kick': 60, 'karate': 60, 'roundhouse': 80, 'smack': 90}
oppMoves2 = ['hit', 'yell']
oppDamage2 = {'hit': 50, 'yell': 60}
oppMoves3 = ['hard hit', 'screech']
oppDamage3 = {'hard hit': 75, 'screech': 100}
heldmoves = ["punch", 'do nothing', "do nothing", "do nothing"]
wades = ['Alex', "Nathan"]
v2Teach = ["Demas", "Pries", "Bosma", "Laurie", "Jacobsen", "Dipzinski"]
v3Teach = ["Bebee", "Gymory", "Lestage", "Koss", "Gartrell", "Halstead"]




#global strength  implement this as a modifyer to the damage the player deals
global pHealth
pHealth = 3000
chestItem = "Nothing"
rightHand = "Nothing"


def checkWornDefenseItemsVerbose(chestItem):
    """This function checks how much defense buff the player gains from chest armour"""
    print "Your " + `chestItem` + " gives you a + " + `defenseItems[chestItem]` + " defense buff"
    return defenseItems[chestItem]


def checkWornDefenseItems(chestItem):
    return defenseItems[chestItem]


def checkRightHandItem(rightHand):
    return offenseItems[rightHand]


def equipArmour(number):
    global chestItem
    #loops through inv,
    for i in inv:
        if classify[inv[i]] == "armour":
            print `i` + " : " + `inv[i]`
        else:
            pass
    chestItemHolder = chestItem
    chestItem = inv[number]
    inv[number] = chestItemHolder
    print "The new armour gives you a defense buff of +" + `defenseItems[chestItem]`


def equipWeapon(number):
    global rightHand
    #loop through your inv looking for weapons
    weaponHolder = rightHand
    rightHand = inv[number]
    inv[number] = weaponHolder

    print "Your weapon does " + `offenseItems[rightHand]` + " damage"


def useItem(itemToUse, itemNum):
    #pHealth is the players health
    global pHealth
    #prints a description of the item
    if classify[itemToUse] == "food":
        print invDesc[itemToUse]
        print "That healed " + `invFunc[itemToUse]`
        inv[itemNum] = "Nothing"
        pHealth += invFunc[itemToUse]
    else:
        print "You cant eat that"


def selectItem():
    #itemToUse is an integer that is passed by the user. We need to compare this against the dictionary of items
    print "You have"
    for i in inv:
        if inv[i] != "Nothing":
            print `i` + " : " + `inv[i]`

    print "What number item do you want to use?"
    #takes input from user on which item they want to use

    try:
        itemNumToUse = int(raw_input(""))
    except:
        print "That is not a number"

    try:
        itemToUse = inv[itemNumToUse]
        useItem(itemToUse, itemNumToUse)
    except:
        print "You cant use that item"


def getItem():
    firstNum = randint(1, 5)
    secondNum = randint(1, 2)
    if firstNum == 1 or 2:
        if secondNum == 1:
            print "You got a leather plate. Do you want to keep it? Y or N"
            keep = raw_input("")
            keep = keep.lower()
            if keep == "y":
                print "What number inventory slot do you want to store the armour in?"
                for i in inv:
                    print `i` + " : " + `inv[i]`
                invSlot = int(raw_input(""))
                inv[invSlot] = "leather plate"

        if secondNum == 2:
            print "You got a metal plate. Do you want to keep it? Y or N"
            keep = raw_input("")
            keep = keep.lower()
            if keep == "y":
                print "What number inventory slot do you want to store the armour in?"
                for i in inv:
                    print `i` + " : " + `inv[i]`
                invSlot = int(raw_input(""))
                inv[invSlot] = "metal plate"

    if firstNum == 3:
        if secondNum == 1:
            print "You got a potion"
            print "What number inventory slot do you want to put this item in?"
            for i in inv:
                print `i` + " : " + `inv[i]`
            invSlot = int(raw_input(""))
            inv[invSlot] = "potion"
        if secondNum == 2:
            print "You got some mutton"
            print "What number inventory slot do you want to put this item in?"
            for i in inv:
                print `i` + " : " + `inv[i]`
            invSlot = int(raw_input(""))
            inv[invSlot] = "mutton"

    else:
        pass


def changeArea():
    """This function is called when a player wants to change areas"""

    print "What area do you want to change into? 2 or 3?"
    areaChoice = raw_input()
    return areaChoice


level = 1


def LevelUp(exp):
    global level
    global strength
    global defense
    #this should be addressed later: If you gain more than one level at a time, it has no way of knowing. use while loop
    if (level * 5) ** 2 < exp:
        level += 1
        print "you leveled up."
        print "you are now level " + `level`
        strength += randint(2, 5)
        defense += randint(1, 4)
    else:
        print "you didn't level up"


def gainMove(level):
    if level == 2:
        print "do you want to learn roundhouse kick? Y or N"
        updateMoveButtons()
        moveYorN = raw_input("")
        if moveYorN == "Y" or "y":
            print "which move do you want to replace? (type the number)"
            print "0: " + heldmoves[0]
            print "1: " + heldmoves[1]
            print "2: " + heldmoves[2]
            print "3: " + heldmoves[3]
            getRidOf = int(raw_input(""))

            try:
                heldmoves[getRidOf] = "roundhouse"
            except:
                print "That isn't a valid value"

        elif moveYorN == "N" or "n":
            pass

    elif level == 3:
        print "do you want to learn heal Y or N?"
        moveYorN = raw_input("")
        if moveYorN == "Y" or "y" or "yes":
            print "which move do you want to replace? (type the number)"
            print "0: " + heldmoves[0]
            print "1: " + heldmoves[1]
            print "2: " + heldmoves[2]
            print "3: " + heldmoves[3]

            getRidOf = int(raw_input(""))
            try:
                heldmoves[getRidOf] = "heal"
            except:
                print "That isn't a valid value"

        elif moveYorN == "N" or "n":
            pass

    elif level == 4:
        print "do you want to learn smack? Y or N"
        moveYorN = raw_input("")
        if moveYorN == "Y" or "y":
            print "which move do you want to replace? (type the number)"
            print "0: " + heldmoves[0]
            print "1: " + heldmoves[1]
            print "2: " + heldmoves[2]
            print "3: " + heldmoves[3]
            getRidOf = int(raw_input(""))
            try:
                heldmoves[getRidOf] = "smack"
            except:
                print "That isn't a valid value"

        elif moveYorN == "N" or "n":
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
    global pHealth
    if move == "heal":
        pHealth += 100
        return 0
    else:
        if allMoves[move] > 0:
            return allMoves[move] + strength
        else:
            return 0


def moveUsed(currentArea):
    """Calculates which move the opponent is to use. It is different if they are in different areas, hence the if
    statement"""
    if currentArea == 2:
        moveRandom = randint(0, 1)
        usedMove = oppMoves2[moveRandom]
        return usedMove
    elif currentArea == 3:
        moveRandom = randint(0, 1)
        usedMove = oppMoves3[moveRandom]
        return usedMove


def whatMove():
    """
    prints all of the users held moves. Takes input from the user. turns that input lowercase.return lowercase input
    """
    print "Do you want to " + heldmoves[0] + " , " + heldmoves[1] + " , " + heldmoves[2] + " , " + heldmoves[3]
    moveOption = raw_input("")
    moveOption = moveOption.lower()
    return moveOption


def invList():
    global inv
    invList = ""
    for i in inv:
        invList = invList + " " + `i` + " " + inv[i] + "\n"
    return invList

#This function runs once at the start of the game. It's the intro.
def firstPrompt():
    global pHealth
    global exp
    print "You arrive at ICHS, a mystical land filled with mosterous Wades, and"
    print "friendly fairys."
    print "You arrive at the front doors of the high school. What do you want to do?"
    print "Go [in], or stay [out]"
    inOrOut = raw_input("")
    inOrOut = inOrOut.lower()
    if inOrOut == "in":
        print "You go into the high school"
    elif inOrOut == "out":
        print "youre a little slow, arent you?"
        raise SystemExit
    print "As you enter the school, you see a menacing figure come out of the shadows"
    wade = wades[randint(0, 1)]
    print "OH NO! It's a wild " + wade
    print "What do you want to do? [F]ight or [R]un?"
    FightOrRun = raw_input("")
    FightOrRun = FightOrRun.lower()
    if FightOrRun == "f":
        oppHealth = health[wade]
        while oppHealth > 0 and pHealth > 0:

            print "He has " + `oppHealth` + " health"
            print "You have " + `pHealth` + " health"
            moveOption = whatMove()

            if checkMoves(moveOption) == True:
                print "You " + moveOption + " your oponent"
                oppHealth = oppHealth - 50
                print "Wade used cry"
                print "It did 10 damage"
                pHealth = pHealth - 10

            else:
                print "You dont have that move"
    elif FightOrRun == "r":
        raise SystemExit

    if oppHealth < 1:
        print "You won"
    elif pHealth < 0:
        print "You lost"
        raise SystemExit

    print "Which new move do You want to learn? [Kick], or [Karate] Chop?"
    newMove = raw_input("")
    newMove = newMove.lower()
    if newMove == "kick":
        heldmoves[1] = "kick"
        print heldmoves
    elif newMove == "karate":
        heldmoves[1] = "karate"
        print heldmoves
    exp += 10
    print "You have passed the first area. You gained 10 exp. You have now moved onto area two of ICHS."
    getItem()
    global currentArea
    currentArea = 2

#initializes the players stats
strength = 1
defense = 1
global exp
exp = 0

class Main(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "ICHS RPG")
        global mainPanel
        mainPanel = wx.Panel(self)

        invButton = wx.Button(mainPanel, label="Inventory", pos=(0, 0), size=(100, 100))
        self.Bind(wx.EVT_BUTTON, self.ShowInventory, invButton)

        fightButton = wx.Button(mainPanel, label="Fight!", pos=(150, 0), size=(100, 100))
        self.Bind(wx.EVT_BUTTON, self.startFight, fightButton)

        areaButton = wx.Button(mainPanel, label="Change\nArea", pos=(300, 0), size=(100,100))
        self.Bind(wx.EVT_BUTTON, self.changeArea, areaButton)


        equipArmourButton = wx.Button(mainPanel, label="Equip Armour", pos=(0, 150), size=(100,100))
        self.Bind(wx.EVT_BUTTON, self.ArmourEquip, equipArmourButton)

        equipWeaponButton = wx.Button(mainPanel, label="Equip Weapon", pos=(150,150), size=(100,100))
        self.Bind(wx.EVT_BUTTON, self.weaponEquip, equipWeaponButton)

        global firstMoveButton
        firstMoveButton = wx.Button(mainPanel, label=(heldmoves[0]), pos=(0, 300), size=(100, 50))

        global secondMoveButton
        secondMoveButton = wx.Button(mainPanel, label=(heldmoves[1]), pos=(60, 300), size=(100, 50))


        firstPrompt()

    global updateMoveButtons

    #This function will only update the moves after the fight is done, due to GIL (I think)
    def updateMoveButtons():

        firstMoveButton.SetLabel(heldmoves[0])

    def ShowInventory(self, event):
        box = wx.MessageDialog(None, invList())
        box.ShowModal()

    def changeArea(self, event):
        global currentArea
        box=wx.TextEntryDialog(None, "Which area do you want to switch to?", "Area")
        if box.ShowModal()==wx.ID_OK:
            newArea = int(box.GetValue())
            currentArea = newArea
    def ArmourEquip(self, event):
        #print "you are currently wearing a " + chestItem + " on your body"
        #checkWornDefenseItemsVerbose(chestItem)  #gives the buff of the worn armour
        #print "Do you want to equip new [A]rmour, [W]eapons, or [N]either?"
        #equip = raw_input("")
        #equip = equip.lower()
        #if equip == "a":

        equipBox = wx.TextEntryDialog(None, "Which item do you want to equip?", "Equip", "Armour")
        if equipBox.ShowModal()==wx.ID_OK:
            itemToEquip = equipBox.GetValue()
            equipArmour(int(itemToEquip))
        #elif equip == "w":
            #equipWeapon()
        else:
            pass

    def weaponEquip(self, event):
        equipBox = wx.TextEntryDialog(None, "Which item do you want to equip?""Weapon")

        if equipBox.ShowModal() == wx.ID_OK:
            itemToEquip = equipBox.GetValue()
            equipWeapon(int(itemToEquip))


    def startFight(self, event):
        global pHealth
        global exp
        if currentArea == 2:
            opponent = v2Teach[randint(0, 5)]
            print "A wild " + opponent + " appeared"
            oppHealth = health[opponent]
            while pHealth > 0 and oppHealth > 0:
                print "the opponent has " + `oppHealth` + " health"
                print "Do you want to " + heldmoves[0] + " , " + heldmoves[1] + " , " + heldmoves[2] + " , " + \
                      heldmoves[3] + " or use a [w]eapon?"
                moveOption = raw_input("")
                moveOption = moveOption.lower()
                if checkMoves(moveOption) == True:
                    damage = moveDamage(moveOption)
                    #change all instances of " a = a - b" to "a-=b"
                    oppHealth = oppHealth - damage

                elif moveOption == "w":
                    if offenseItems[rightHand] == 0:
                        damage = 0
                    else:
                        damage = int(offenseItems[rightHand]) + strength

                    oppHealth = oppHealth - damage

                else:
                    print "That isn't a move"

                usedMove = moveUsed(currentArea)
                print opponent + " used " + usedMove
                pHealth -= (oppDamage2[usedMove]) - (defense + checkWornDefenseItems(chestItem))
                print "You have " + `pHealth` + " health left"

            if pHealth <= 0:

                print "You lost"
                if x == 1:
                    time.sleep(10)
                    print "I'm sleeping"
                    raise SystemExit

                elif x == 0:

                    print "i didnt sleep"
                    raise SystemExit

            elif oppHealth <= 0:
                print "You won"
                exp += 100
                LevelUp(exp)
                gainMove(level)
                print "You have " + `exp` + " exp"
                getItem()

        elif currentArea == 3:

            opponent = v3Teach[randint(0, 5)]
            print "A wild " + opponent + " appeared"
            oppHealth = health[opponent]
            while pHealth > 0 and oppHealth > 0:

                print "The opponent has " + `oppHealth` + " health"
                print "Do you want to " + heldmoves[0] + " , " + heldmoves[1] + " , " + heldmoves[2] + " , " + \
                      heldmoves[3] + " or use a [w]eapon?"
                moveOption = raw_input("")
                moveOption = moveOption.lower()
                if checkMoves(moveOption) == True:
                    damage = moveDamage(moveOption)
                    #change all instances of " a = a - b" to "a-=b"
                    oppHealth = oppHealth - damage

                elif moveOption == "w":
                    if offenseItems[rightHand] == 0:
                        damage = 0
                    else:
                        damage = int(offenseItems[rightHand]) + strength

                    oppHealth = oppHealth - damage

                else:
                    print "That isn't a move"

                usedMove = moveUsed(currentArea)
                print opponent + " used " + usedMove
                pHealth -= oppDamage3[usedMove] - (defense + checkWornDefenseItems(chestItem))
                print "You have " + `pHealth` + " health left"

            if pHealth <= 0:

                print "You lost"
                if x == 1:
                    time.sleep(10)
                    raise SystemExit

                elif x == 0:
                    raise SystemExit

            elif oppHealth <= 0:
                print
                exp += 150
                print "You have " + `exp` + " exp"
                LevelUp(exp)
                gainMove(level)

        else:
            print "I dont know which area you're in"



if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Main(parent=None, id=-1)
    frame.Show()
    app.MainLoop()





#add more






while 1 == 1:

    print "You are in area " + `currentArea`
    print "What do you want to do? [F]ight, [C]hange area, look at your [inv], [e]quip things?"
    whatToDo = raw_input("")
    whatToDo = whatToDo.lower()

    if whatToDo == "c":
        currentArea = changeArea()
        currentArea = int(currentArea)
        print currentArea

