import random
import sys
import time
import textwrap

DuctTape = False
Handcuffs = False
Rope = False
Crowbar = False
kaboom = False
Exit = False
skipB = False
continueBchoice2 = False

print("Welcome to the Crime Simulator 2000!")
time.sleep(2)
print("To experience the daring adventure that is robbing a bank, enter 'Play'")
time.sleep(1)
print("To try one of the other criminal experiences, enter 'Other'")
startchoice = input()

if startchoice == 'Other':
    print("ERROR 404 Not Found ... Developer was too lazy to program a second adventure ... ERROR")
    sys.exit()
else:
    if startchoice != 'Play':
        print("Please enter an actual choice .-.")
        sys.exit()
    else:
        print("Welcome to the Bank Heist simulator! Your criminal adventures begin here!")

p1 = "From the roof top of a near by shopping center you use a pair of binoculars to survey the target. The bank itself is quite the impressive architectural feat, with giant pillars rivaling those of the white house. Despite its historical background and classic design, unlike many of the newer banks which have opted for a contemporary approach, the bank is equipped with state of the art security systems. Breaking in will be no easy task."
paragraph1 = textwrap.fill(p1)
print (paragraph1)
print()
time.sleep(15)

p2 = "Before you decide the best way to begin the heist, you'll have to choose some items to take with you. On the table in front of you are the following items, DuctTape, Rope, Pliers, a Crowbar, and Handcuffs."
paragraph2 = textwrap.fill(p2)
print (paragraph2)
print()
print("Which two items will you pick? Choose carefully as some items will help you during your heist.")
print()
print("Hint- Type the exact name of the item as listed to choose it.")

itemchoice1 = input()

if itemchoice1 == 'DuctTape':
    DuctTape = True
    print("You pick up the DuctTape.")

if itemchoice1 == 'Rope':
    Rope = True
    print("You pick up the Rope")

if itemchoice1 == 'Pliers':
    Pliers = True
    print("You pick up the Pliers")

if itemchoice1 == 'Crowbar':
    Crowbar = True
    print("You pick up the Crowbar")

if itemchoice1 == 'Handcuffs':
    Handcuffs = True
    print("You pick up the Handcuffs")

print()
print("Now choose a second item.")
itemchoice2 = input()

if itemchoice2 == 'DuctTape':
    DuctTape = True
    print("You pick up the DuctTape.")

if itemchoice2 == 'Rope':
    Rope = True
    print("You pick up the Rope")

if itemchoice2 == 'Pliers':
    Pliers = True
    print("You pick up the Pliers")

if itemchoice2 == 'Crowbar':
    Crowbar = True
    print("You pick up the Crowbar")

if itemchoice2 == 'Handcuffs':
    Handcuffs = True
    print("You pick up the Handcuffs")

p3 = "In certain situations you may have to use an item in your inventory or look for an item around you. In order to use an item in your inventory enter 'Use ' and then the name of the item. To check for possible items around you, enter 'Check ' and then the name of the location you would like to check."
paragraph3 = textwrap.fill(p3)
print(paragraph3)

time.sleep(10)
print()

print("As you pack your bag, a fellow heist member taps you on the shoulder, it's go time.")

time.sleep(2)
print()
p4 = "It is time to decide how you would like to enter the bank. The garage provides the most direct route to the bank vault and with little commotion it is the best choice if you like to take on a stealthy approach, however you will be caught in the open if security guards happen to be around. Alternatively you could climb up to the roof, no guards will see you but its along ways away from the vault. Finally you could just storm the entrance, it works in the movies!"
paragraph4 = textwrap.fill(p4)
print(paragraph4)

time.sleep(15)

print("To proceed via the garage, enter 'A'.")
print("To climb up to the roof, enter 'B'.")
print("To storm the front door, enter 'C'.")

p4choice = input()
print()

if p4choice == 'C':
    pC = "What were you thinking??? Your crew of clearly unexperienced criminals is stopped by security before you could even get into lobby. Have fun in jail."
    paragraphC = textwrap.fill(pC)
    print(paragraphC)
    sys.exit()

if p4choice == 'A':
    print("The garage is not a bad choice, you hope there are no security officers around as you creep through.")
    securityA = random.randint (1, 4)
    if securityA == 1:
        time.sleep(3)
        print()
        print("It seems luck was not on your side, a patrol of guards aprehends you and your crew, better luck next time.")
        sys.exit()
    else:
        print()
        pA1 = "You slowly enter the bank through the lowest level of the underground garage. Peering around the corner you can see a single guard covering the entrance to the vault. What will you do? Perhaps there is an item you can use to subdue the guard? Looking around you see that there is a Closet near by, perhaps there is something usefull in the closet."
        paragraphA1 = textwrap.fill(pA1)
        print(paragraphA1)
        print()
        Achoice1 = input()
        time.sleep(1)

        if Achoice1 == 'Check Closet':
            pA2 = "The closet appears to be some sort of janitor's closet. As you open the door you find, to your surprise, none other than THE JANITOR. I guess they do use those closets afterall. Shocked by your ominous gear, the janitor yells for help and you are apprehended by the guard."
            paragraphA2 = textwrap.fill(pA2)
            print(pA2)
            sys.exit()
        else:
            if (Achoice1 == 'Use DuctTape' and DuctTape == True):
                pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                paragraphA3 = textwrap.fill(pA3)
                print(paragraphA3)
                print("What will you do?")
                Achoice2 = input()
                print()
            else:
                if (Achoice1 == 'Use Handcuffs' and Handcuffs == True):
                    pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                    paragraphA3 = textwrap.fill(pA3)
                    print(paragraphA3)
                    print("What will you do?")
                    Achoice2 = input()
                    print()
                else:
                    if (Achoice1 == 'Use Rope' and Rope == True):
                        pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                        paragraphA3 = textwrap.fill(pA3)
                        print(paragraphA3)
                        print("What will you do?")
                        Achoice2 = input()
                        print()
                    else:
                        print("That item didn't work.")
                        sys.exit()

            if Achoice2 == 'Check Guard':
                pA4 = "With no time to spare you rush over the the tied up guard. Quickly scanning through his pockets and tool belt you seem to be out of luck. However, a brilliant idea comes to mind. You can use his shoe laces as a form of rope. You quickly take the shoe laces out of his boots and begin to tie them together, finally you fasten the makeshift cord to the lever. From a safe distance you tug on the laces enough to pull down the lever."
                paragraphA4 = textwrap.fill(pA4)
                print(paragraphA4)
                kaboom = True
                print()
            else:
                if (Achoice2 == 'Use DuctTape' and DuctTape == True):
                    print("This will have to do.")
                    print()
                    print("You tie up the lever and walk away to a safe distance. A swift pull is all it takes.")
                    kaboom = True
                else:
                    if (Achoice2 == 'Use Rope' and Rope == True):
                        print("This will have to do.")
                        print()
                        print("You tie up the lever and walk away to a safe distance. A swift pull is all it takes.")
                        kaboom = True
                    else:
                        print("This item didn't work.")
                        sys.exit()

if p4choice == 'B':
    print("You climb up on to the roof with no problem.")
    print("Sure enough the rooftop is completely almost empty.")
    print("Do you want to try and sneak down the Elevator shaft? (Enter 'Elevator')")
    print("Or do you want to repel down the SkyLight?")
    Bchoice1 = input()
    print()

    if Bchoice1 == 'Elevator':
        pB1 = "With the help of your crew, you pry open the hatch that connects to the elevator shaft. Cautiously, you climb down the elevator shaft taking advatage of the cables and poles."
        paragraphB1 = textwrap.fill(pB1)
        print(paragraphB1)
        time.sleep(8)
        print()
        pA1 = "You slowly enter the lowest level of the Bank through the elevator doors. Peering around the corner you can see a single guard covering the entrance to the vault. What will you do? Perhaps there is an item you can use to subdue the guard? Looking around you see that there is a Closet near by, perhaps there is something usefull in the closet."
        paragraphA1 = textwrap.fill(pA1)
        print(paragraphA1)
        print()
        Achoice1 = input()
        time.sleep(1)
        if Achoice1 == 'Check Closet':
            pA2 = "The closet appears to be some sort of janitor's closet. As you open the door you find, to your surprise, none other than THE JANITOR. I guess they do use those closets afterall. Shocked by your ominous gear, the janitor yells for help and you are apprehended by the guard."
            paragraphA2 = textwrap.fill(pA2)
            print(pA2)
            sys.exit()
        else:
            if (Achoice1 == 'Use DuctTape' and DuctTape == True):
                pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                paragraphA3 = textwrap.fill(pA3)
                print(paragraphA3)
                print("What will you do?")
                Achoice2 = input()
                print()
            else:
                if (Achoice1 == 'Use Handcuffs' and Handcuffs == True):
                    pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                    paragraphA3 = textwrap.fill(pA3)
                    print(paragraphA3)
                    print("What will you do?")
                    Achoice2 = input()
                    print()
                else:
                    if (Achoice1 == 'Use Rope' and Rope == True):
                        pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                        paragraphA3 = textwrap.fill(pA3)
                        print(paragraphA3)
                        print("What will you do?")
                        Achoice2 = input()
                        print()
                    else:
                        print("That item didn't work.")
                        sys.exit()

            if Achoice2 == 'Check Guard':
                pA4 = "With no time to spare you rush over the the tied up guard. Quickly scanning through his pockets and tool belt you seem to be out of luck. However, a brilliant idea comes to mind. You can use his shoe laces as a form of rope. You quickly take the shoe laces out of his boots and begin to tie them together, finally you fasten the makeshift cord to the lever. From a safe distance you tug on the laces enough to pull down the lever."
                paragraphA4 = textwrap.fill(pA4)
                print(paragraphA4)
                kaboom = True
                print()
            else:
                if (Achoice2 == 'Use DuctTape' and DuctTape == True):
                    print("This will have to do.")
                    print()
                    print("You tie up the lever and walk away to a safe distance. A swift pull is all it takes.")
                    kaboom = True
                else:
                    if (Achoice2 == 'Use Rope' and Rope == True):
                        print("This will have to do.")
                        print()
                        print("You tie up the lever and walk away to a safe distance. A swift pull is all it takes.")
                        kaboom = True
                    else:
                        print("This item didn't work.")
                        sys.exit()

    if Bchoice1 == 'SkyLight':
        print("How on earth are you going to repel down? You see a small ToolBox nearby, and you always have the two items on you.")
        Bchoice2 = input()
        print()

        if Bchoice2 == 'Check ToolBox':
            print("You open up the toolbox and find enough rope to repel down.")
            continueBchoice2 = True
        else:
            if (Bchoice2 == 'Use DuctTape' and DuctTape == True):
                continueBchoice2 = True
            else:
                if (Bchoice2 == 'Use Rope' and Rope == True):
                    continueBchoice2 = True
                else:
                    print("This item didn't work.")
                    sys.exit()

        if continueBchoice2 == True:
            print("You break through the skylight and lower yourself to the floor in proper hollywood action.")
            time.sleep(2)
            print()
            print("You find yourself standing in the middle of a bunch of shocked civilians. Welp, its a hostage situation now .-.")
            time.sleep(2)
            print()
            print("You need to tie everyone up and quickly before they begin to panick. With no time to search for items, what can you do?")
            Bchoice3 = input()
            print()

            if (Bchoice3 == 'Use Rope' and Rope) or (Bchoice3 == 'Use Handcuffs'):
                print("You manage to secure the hostages, yet with nothing covering their mouths, yells for help spread like wildfire.")
                print("Perhaps next time you should bring some DuctTape.")
                sys.exit()

            if Bchoice3 != 'Use DuctTape':
                print("This item didn't work.")
                sys.exit()
            else:
                print("You manage to secure all of the hostage. Now its time to get to the vault before police arrive.")
                time.sleep(2)
                print()
                pA1 = "You slowly make your way down the stairs to the lowest level of the bank. Peering around the corner you can see a single guard covering the entrance to the vault. What will you do? Perhaps there is an item you can use to subdue the guard? Looking around you see that there is a Closet near by, perhaps there is something usefull in the closet."
                paragraphA1 = textwrap.fill(pA1)
                print(paragraphA1)
                print()
                Achoice1 = input()
                time.sleep(1)

                if Achoice1 == 'Check Closet':
                    pA2 = "The closet appears to be some sort of janitor's closet. As you open the door you find, to your surprise, none other than THE JANITOR. I guess they do use those closets afterall. Shocked by your ominous gear, the janitor yells for help and you are apprehended by the guard."
                    paragraphA2 = textwrap.fill(pA2)
                    print(pA2)
                    sys.exit()
                else:
                    if (Achoice1 == 'Use DuctTape' and DuctTape == True):
                        pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                        paragraphA3 = textwrap.fill(pA3)
                        print(paragraphA3)
                        print("What will you do?")
                        Achoice2 = input()
                        print()
                    else:
                        if (Achoice1 == 'Use Handcuffs' and Handcuffs == True):
                            pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                            paragraphA3 = textwrap.fill(pA3)
                            print(paragraphA3)
                            print("What will you do?")
                            Achoice2 = input()
                            print()
                        else:
                            if (Achoice1 == 'Use Rope' and Rope == True):
                                pA3 = "Good thinking, you can use that to tie up and get past the guards. As you move forward into the vault, one of your heist members begins to set up explosives that can be used to blow open the door of the vault. Suddenly a look of anger which quickly turns to shame passes over his face, he forgot the detonator! The only other way to trigger the explosives would be to pull down the small lever on the face of the bomb. It is far too dangerous to try and pull down the lever while standing so close to the bomb. The hallway leading up to the vault is baren, however, the Guard is still sitting there, perhaps there he has something on him that you could use. Or maybe there is an item you could use."
                                paragraphA3 = textwrap.fill(pA3)
                                print(paragraphA3)
                                print("What will you do?")
                                Achoice2 = input()
                                print()
                            else:
                                print("That item didn't work.")
                                sys.exit()

            if Achoice2 == 'Check Guard':
                pA4 = "With no time to spare you rush over the the tied up guard. Quickly scanning through his pockets and tool belt you seem to be out of luck. However, a brilliant idea comes to mind. You can use his shoe laces as a form of rope. You quickly take the shoe laces out of his boots and begin to tie them together, finally you fasten the makeshift cord to the lever. From a safe distance you tug on the laces enough to pull down the lever."
                paragraphA4 = textwrap.fill(pA4)
                print(paragraphA4)
                kaboom = True
                print()
            else:
                if (Achoice2 == 'Use DuctTape' and DuctTape == True):
                    print("This will have to do.")
                    print()
                    print("You tie up the lever and walk away to a safe distance. A swift pull is all it takes.")
                    kaboom = True
                else:
                    if (Achoice2 == 'Use Rope' and Rope == True):
                        print("This will have to do.")
                        print()
                        print("You tie up the lever and walk away to a safe distance. A swift pull is all it takes.")
                        kaboom = True
                    else:
                        print("This item didn't work.")
                        sys.exit()

if kaboom == True:
    time.sleep(15)
    print()
    print("The vault doors blows open with a thunderous noise loud enough to leave all ears ringing.")
    time.sleep(5)
    print("You rush into the vault along with your crew and work quickly to fill you bags with unimaginable riches.")
    print()
    Exit = True

if Exit == True:
    print("With bags full of cash it is time to make an exit, and fast.")
    time.sleep(3)
    print()
    print("Do you exit through the Garage? Or do you attempt to escape through the bank's Back Exit?")
    Exitchoice = input()

    if Exitchoice == 'Garage' and p4choice == 'A':
        print("The guards had recieved word of suspicous activity in the garage.")
        print("Exiting the same way you came in turned out to be a bad idea.")
        print("You and your team are apprehended the moment you step into the garage.")
        sys.exit()
    else:
        if Exitchoice == 'Garage':
            print("Lucky for you the garage seems to be empty, and you have no trouble making a getaway.")
            print("You just stole millions of dollars, and the bank has yet to even notice!")
            time.sleep(8)
            print()
            print("Congratulations you beat the Bank Heist Simulator. Don't test your luck on a real one.")
            sys.exit()
        else:
            print("Lucky for you the back entrance seems to be empty, and you have no trouble making a getaway.")
            print("You just stole millions of dollars, and the bank has yet to even notice!")
            time.sleep(8)
            print()
            print("Congratulations you beat the Bank Heist Simulator. Don't test your luck on a real one.")
            sys.exit()

