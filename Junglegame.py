print("Jungle game")
a=int(input("I am lost , ........ you have 2 direction press 1 for left 2 for right : "))
if(a==1):
    print("you are going left")
    z=int(input("rasta ....... press 3 for left  and 4 for right : "))
    if(z==3):
        print("press 3 for game over")
    elif(z==4):
        print("press 4 for game over")

elif(a==2):
    print("you are going right")
    y=int(input("raasta............. press 1 for left  and 2 for right : "))
    if(y==1):
        print("press 1 for falling into the well")
    elif(y==2):
        print("there are again two turns : left /right :  ")
        x=input("raasta.............. HELP/NO HELP : ")
        if(x=="HELP"):
            print("WIN")
        elif(x=="NO HELP"):
            print("GAME OVER")


    elif(a==3):
        print("you are going left")
        x=int(input("raasta...... ........press 1 for left and 2 for right  "))
        if(x==1):
            print("press 1 for WIN")
        elif(x==2):
            print("press 2 for GAME OVER")
