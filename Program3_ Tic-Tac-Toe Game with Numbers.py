#Tic_Tac-Toe Game With Numbers

while True:
    Boolean = False
    ChDraw = False
    Count = 0
    Tic_Tac_Toe = [-15, -15, -15, -15, -15, -15, -15, -15, -15]
    Choice = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Odd = [1, 3, 5, 7, 9]
    Even = [0, 2, 4, 6, 8]
    from random import randint
    print("Enter (1)Player Vs Computer.")
    print("Enter (2)Player Vs Player.")
    print("Enter (3)Game Description")
    print("Enter (0)Exit.")
    try:
        UserInput = int(input("Please Enter Choice: "))
        if(UserInput <= 3 and UserInput >= 0):
            if(UserInput == 0):
                break


            elif(UserInput == 1):
                
                print("\n\n**    ***** ******** *****     *********  **********")
                print("**    **    ******** **        **         **********    ")
                print("**    *****    **    *****     **   ****  ***    ***    ")
                print("***** **       **       **     **   ****  **********    ")
                print("***** *****    **    *****     *********  **********\n\n")

                try:
                    print("-------------------")
                    print("| ", Tic_Tac_Toe[0], " | ", Tic_Tac_Toe[1], " | ", Tic_Tac_Toe[2], " |")
                    print("-------------------")
                    print("| ", Tic_Tac_Toe[3], " | ", Tic_Tac_Toe[4], " | ", Tic_Tac_Toe[5], " |")
                    print("-------------------")
                    print("| ", Tic_Tac_Toe[6], " | ", Tic_Tac_Toe[7], " | ", Tic_Tac_Toe[8], " |")
                    print("-------------------")
                    while (not Boolean):
                        if(ChDraw == False) and (Count >= 9):
                            print("\n\n*********    ***    ***     *******      ***                   ***")
                            print("**********   ***   ***     *********     ***                   ***    ")
                            print("***********  ***  ***     ***     ***    ***                   ***    ")
                            print("***     ***  *** ***     *************   ***        ***        ***    ")
                            print("***     ***  *****       *************   ***       ******      ***    ")
                            print("***********  ****        ***       ***    ***     ***  ***     ***    ")
                            print("**********   ***         ***       ***     *********    *********     ")
                            print("*********    ***         ***       ***      ******       ******   \n\n")
                            print("\n --------------------------------------------------------------   \n")
                            Boolean = True
                        
                        else:
                            while True:
                                Player = int(input("Please Enter Odd Number Between 1 and 9: "))
                                if(Player % 2 == 1) and (Odd[int((Player-1)/2)] == Player):
                                    Odd[int((Player-1)/2)] = -1
                                    print("-------------------")
                                    print("| ", Choice[0], " | ", Choice[1], " | ", Choice[2], " |")
                                    print("-------------------")
                                    print("| ", Choice[3], " | ", Choice[4], " | ", Choice[5], " |")
                                    print("-------------------")
                                    print("| ", Choice[6], " | ", Choice[7], " | ", Choice[8], " |")
                                    print("-------------------")
                                    while True:
                                        Location = int(input("Please Enter Location Between 1 and 9: "))
                                        if(Location <= 9 and Location >= 1) and (Tic_Tac_Toe[Location-1] == -15) and (Choice[Location-1] != "*"):
                                            Choice[Location-1] = "*"
                                            Tic_Tac_Toe[Location-1] = Player
                                            Count += 1
                                            print("-------------------")
                                            print("| ", Tic_Tac_Toe[0], " | ", Tic_Tac_Toe[1], " | ", Tic_Tac_Toe[2], " |")
                                            print("-------------------")
                                            print("| ", Tic_Tac_Toe[3], " | ", Tic_Tac_Toe[4], " | ", Tic_Tac_Toe[5], " |                      CURRENT")
                                            print("-------------------")
                                            print("| ", Tic_Tac_Toe[6], " | ", Tic_Tac_Toe[7], " | ", Tic_Tac_Toe[8], " |")
                                            print("-------------------")
                                            
                                            if((Tic_Tac_Toe[0]+Tic_Tac_Toe[1]+Tic_Tac_Toe[2])==15 or (Tic_Tac_Toe[3]+Tic_Tac_Toe[4]+Tic_Tac_Toe[5])==15 or (Tic_Tac_Toe[6]+Tic_Tac_Toe[7]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[3]+Tic_Tac_Toe[6])==15 or (Tic_Tac_Toe[1]+Tic_Tac_Toe[4]+Tic_Tac_Toe[7])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[5]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[4]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[4]+Tic_Tac_Toe[6])==15):
                                                print("\n\n***           ***    ***     ***         ")
                                                print("***           ***    ***     **********      ")
                                                print("***     **    ***    ***     **********      ")
                                                print("***    ****   ***    ***     ***    ***      ")
                                                print("*****************    ***     ***    ***      ")
                                                print("*****************    ***     ***    ***  \n\n")
                                                print("\n -------------------------------------------------------------- \n")
                                                Boolean = True
                                                ChDraw = True

                                            elif(Count >=9):
                                                break
                                                
                                            else:
                                                while True:
                                                    Computer = randint(0,8)
                                                    if(Computer % 2 == 0) and (Even[int(Computer/2)] == Computer):
                                                        print("Computer: ", Computer)
                                                        Even[int(Computer/2)] = -1
                                                        print("-------------------")
                                                        print("| ", Choice[0], " | ", Choice[1], " | ", Choice[2], " |")
                                                        print("-------------------")
                                                        print("| ", Choice[3], " | ", Choice[4], " | ", Choice[5], " |")
                                                        print("-------------------")
                                                        print("| ", Choice[6], " | ", Choice[7], " | ", Choice[8], " |")
                                                        print("-------------------")
                                                        while True:
                                                            ComLocation = randint(1,9)
                                                            if(ComLocation <= 9 and ComLocation >= 1) and (Tic_Tac_Toe[ComLocation-1] == -15) and (Choice[ComLocation-1] != "*"):
                                                                print("Location: ", ComLocation)
                                                                Choice[ComLocation-1] = "*"
                                                                Tic_Tac_Toe[ComLocation-1] = Computer
                                                                Count += 1
                                                                print("-------------------")
                                                                print("| ", Tic_Tac_Toe[0], " | ", Tic_Tac_Toe[1], " | ", Tic_Tac_Toe[2], " |")
                                                                print("-------------------")
                                                                print("| ", Tic_Tac_Toe[3], " | ", Tic_Tac_Toe[4], " | ", Tic_Tac_Toe[5], " |                      CURRENT")
                                                                print("-------------------")
                                                                print("| ", Tic_Tac_Toe[6], " | ", Tic_Tac_Toe[7], " | ", Tic_Tac_Toe[8], " |")
                                                                print("-------------------")
                                                                
                                                                if((Tic_Tac_Toe[0]+Tic_Tac_Toe[1]+Tic_Tac_Toe[2])==15 or (Tic_Tac_Toe[3]+Tic_Tac_Toe[4]+Tic_Tac_Toe[5])==15 or (Tic_Tac_Toe[6]+Tic_Tac_Toe[7]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[3]+Tic_Tac_Toe[6])==15 or (Tic_Tac_Toe[1]+Tic_Tac_Toe[4]+Tic_Tac_Toe[7])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[5]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[4]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[4]+Tic_Tac_Toe[6])==15):
                                                                    print("\n\n**       **********  **********  **********")
                                                                    print("**       **********  **          **            ")
                                                                    print("**       ***    ***  **          **            ")
                                                                    print("**       ***    ***  **********  **********    ")
                                                                    print("*******  **********          **  **            ")
                                                                    print("*******  **********  **********  **********\n\n")
                                                                    print("\n -------------------------------------------------------------- \n")
                                                                    Boolean = True
                                                                    ChDraw = True
                                                                break
                                                        break
                                            break
                                break
                except:
                    print("Please enter number.")
                

            elif(UserInput == 2):
                
                print("\n\n**    ***** ******** *****     *********  **********")
                print("**    **    ******** **        **         **********    ")
                print("**    *****    **    *****     **   ****  ***    ***    ")
                print("***** **       **       **     **   ****  **********    ")
                print("***** *****    **    *****     *********  **********\n\n")

                try:
                    print("-------------------")
                    print("| ", Tic_Tac_Toe[0], " | ", Tic_Tac_Toe[1], " | ", Tic_Tac_Toe[2], " |")
                    print("-------------------")
                    print("| ", Tic_Tac_Toe[3], " | ", Tic_Tac_Toe[4], " | ", Tic_Tac_Toe[5], " |")
                    print("-------------------")
                    print("| ", Tic_Tac_Toe[6], " | ", Tic_Tac_Toe[7], " | ", Tic_Tac_Toe[8], " |")
                    print("-------------------")
                    while (not Boolean):
                        if(ChDraw == False) and (Count >= 9):
                            print("\n\n*********    ***    ***     *******      ***                   ***")
                            print("**********   ***   ***     *********     ***                   ***    ")
                            print("***********  ***  ***     ***     ***    ***                   ***    ")
                            print("***     ***  *** ***     *************   ***        ***        ***    ")
                            print("***     ***  *****       *************   ***       ******      ***    ")
                            print("***********  ****        ***       ***    ***     ***  ***     ***    ")
                            print("**********   ***         ***       ***     *********    *********     ")
                            print("*********    ***         ***       ***      ******       ******   \n\n")
                            print("\n --------------------------------------------------------------   \n")
                            Boolean = True
                        
                        else:
                            while True:
                                Player1 = int(input("(Player1) Please Enter Odd Number Between 1 and 9: "))
                                if(Player1 % 2 == 1) and (Odd[int((Player1-1)/2)] == Player1):
                                    Odd[int((Player1-1)/2)] = -1
                                    print("-------------------")
                                    print("| ", Choice[0], " | ", Choice[1], " | ", Choice[2], " |")
                                    print("-------------------")
                                    print("| ", Choice[3], " | ", Choice[4], " | ", Choice[5], " |")
                                    print("-------------------")
                                    print("| ", Choice[6], " | ", Choice[7], " | ", Choice[8], " |")
                                    print("-------------------")
                                    while True:
                                        Location1 = int(input("(Player1) Please Enter Location Between 1 and 9: "))
                                        if(Location1 <= 9 and Location1 >= 1) and (Tic_Tac_Toe[Location1-1] == -15) and (Choice[Location1-1] != "*"):
                                            Choice[Location1-1] = "*"
                                            Tic_Tac_Toe[Location1-1] = Player1
                                            Count += 1
                                            print("-------------------")
                                            print("| ", Tic_Tac_Toe[0], " | ", Tic_Tac_Toe[1], " | ", Tic_Tac_Toe[2], " |")
                                            print("-------------------")
                                            print("| ", Tic_Tac_Toe[3], " | ", Tic_Tac_Toe[4], " | ", Tic_Tac_Toe[5], " |                      CURRENT")
                                            print("-------------------")
                                            print("| ", Tic_Tac_Toe[6], " | ", Tic_Tac_Toe[7], " | ", Tic_Tac_Toe[8], " |")
                                            print("-------------------")
                                            
                                            if((Tic_Tac_Toe[0]+Tic_Tac_Toe[1]+Tic_Tac_Toe[2])==15 or (Tic_Tac_Toe[3]+Tic_Tac_Toe[4]+Tic_Tac_Toe[5])==15 or (Tic_Tac_Toe[6]+Tic_Tac_Toe[7]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[3]+Tic_Tac_Toe[6])==15 or (Tic_Tac_Toe[1]+Tic_Tac_Toe[4]+Tic_Tac_Toe[7])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[5]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[4]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[4]+Tic_Tac_Toe[6])==15):
                                                print("\n\nPlayer1")
                                                print("\n\n***           ***    ***     ***         ")
                                                print("***           ***    ***     **********      ")
                                                print("***     **    ***    ***     **********      ")
                                                print("***    ****   ***    ***     ***    ***      ")
                                                print("*****************    ***     ***    ***      ")
                                                print("*****************    ***     ***    ***  \n\n")
                                                print("\n -------------------------------------------------------------- \n")
                                                Boolean = True
                                                ChDraw = True

                                            elif(Count >=9):
                                                break
                                                
                                            else:
                                                while True:
                                                    Player2 = int(input("(Player2) Please Enter Even Number Between 1 and 9: "))
                                                    if(Player2 % 2 == 0) and (Even[int(Player2/2)] == Player2):
                                                        Even[int(Player2/2)] = -1
                                                        print("-------------------")
                                                        print("| ", Choice[0], " | ", Choice[1], " | ", Choice[2], " |")
                                                        print("-------------------")
                                                        print("| ", Choice[3], " | ", Choice[4], " | ", Choice[5], " |")
                                                        print("-------------------")
                                                        print("| ", Choice[6], " | ", Choice[7], " | ", Choice[8], " |")
                                                        print("-------------------")
                                                        while True:
                                                            Location2 = int(input("(Player2) Please Enter Location Between 1 and 9: "))
                                                            if(Location2 <= 9 and Location2 >= 1) and (Tic_Tac_Toe[Location2-1] == -15) and (Choice[Location2-1] != "*"):
                                                                Choice[Location2-1] = "*"
                                                                Tic_Tac_Toe[Location2-1] = Player2
                                                                Count += 1
                                                                print("-------------------")
                                                                print("| ", Tic_Tac_Toe[0], " | ", Tic_Tac_Toe[1], " | ", Tic_Tac_Toe[2], " |")
                                                                print("-------------------")
                                                                print("| ", Tic_Tac_Toe[3], " | ", Tic_Tac_Toe[4], " | ", Tic_Tac_Toe[5], " |                      CURRENT")
                                                                print("-------------------")
                                                                print("| ", Tic_Tac_Toe[6], " | ", Tic_Tac_Toe[7], " | ", Tic_Tac_Toe[8], " |")
                                                                print("-------------------")
                                                                
                                                                if((Tic_Tac_Toe[0]+Tic_Tac_Toe[1]+Tic_Tac_Toe[2])==15 or (Tic_Tac_Toe[3]+Tic_Tac_Toe[4]+Tic_Tac_Toe[5])==15 or (Tic_Tac_Toe[6]+Tic_Tac_Toe[7]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[3]+Tic_Tac_Toe[6])==15 or (Tic_Tac_Toe[1]+Tic_Tac_Toe[4]+Tic_Tac_Toe[7])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[5]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[0]+Tic_Tac_Toe[4]+Tic_Tac_Toe[8])==15 or (Tic_Tac_Toe[2]+Tic_Tac_Toe[4]+Tic_Tac_Toe[6])==15):
                                                                    print("\n\nPlayer2")
                                                                    print("\n\n***           ***    ***     ***         ")
                                                                    print("***           ***    ***     **********      ")
                                                                    print("***     **    ***    ***     **********      ")
                                                                    print("***    ****   ***    ***     ***    ***      ")
                                                                    print("*****************    ***     ***    ***      ")
                                                                    print("*****************    ***     ***    ***  \n\n")
                                                                    print("\n -------------------------------------------------------------- \n")
                                                                    Boolean = True
                                                                    ChDraw = True
                                                                break
                                                        break
                                            break
                                break
                except:
                    print("Please enter number.")

            elif(UserInput == 3):
                print("\n\n--------------------------------------------------------\nTic-Tac-Toe with numbers. A board of 3 x 3 is displayed and player 1 takes odd \nnumbers 13, 5, 7, 9 and player 2 takes even numbers 0, 2, 4, 6, 8. Players take turns to write theirnumbers. Odd numbers start. Use each number only once. The \nfirst person to complete a linethat adds up to 15 is the winner. The line can \nhave both odd and even numbers.\n--------------------------------------------------------\n\n")    


    except:
        print("Please enter number between 0 and 3")
