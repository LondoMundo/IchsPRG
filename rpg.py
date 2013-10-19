import os
from random import randint
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
print "OH NO! It's a wild " + v1Teach[randint(0,5)]
