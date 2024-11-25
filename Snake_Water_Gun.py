import random
comp=random.randint(-1,1)
you=input("Choose : Snake --> S  Water --> W  Gun --> G :")
logbook={"S":-1,"W":0,"G":1}
youc=logbook[you]
revlog={-1:"Snake",0:"Water",1:"Gun"}
print(f"Computer chose {revlog[comp]}")
if(youc==comp):
    print("Its A DRAW :| !!")
else:
    if(comp-youc==2):
        print("You Lose :( !!")
    else:
        print("You Won :) !!")
