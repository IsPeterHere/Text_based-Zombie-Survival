"""
Name: Zombie Survival.py
Date of Creation: 6/5/20
Author: Sandy Emmerson
Description: Try to survive until you reach safety in this text based adventure.
"""
#Imports functions.
from random import randint
import random
from time import sleep




class ALL:

    def __init__(self):
        self.ALLP = []
        self.ip = True

    def start(self):

        
        #~~~~~~
        #Assigns varibles.
        #Varibles are all reassigned new values within the code so don't think about changing anything here.
        self.thingsDONE = 0
        #An old varible that I have not yet been able to extract.

        self.answer = "~~~~~~~~~~~~~~~"
        #A multi use answer varible for input().

        self.prono = "0"
        #The pronoun that will be used.

        self.prono2 = "0"
        #To allow two diffent pronouns to assigned.

        self.clr = ""
        #To allow colour to be assigned.

        self.food = 10
        #Amount of food the player has left.

        self.foodinc = 0
        #The amount of food that the player will gain during an event.

        self.health = 100
        #The players health value.

        self.daysTILLsafety = None
        #The number of 'New Days' the player has to survive to win.

        self.answer = 0
        #A single varible that constantly gets reassigned to be the player answer to any givin question.

        self.rand = 0
        #Don't think it does anything but I am going to keep it here till I'm sure.

        self.damage = 0
        #How much damage you will take.

        self.damagecha = 0
        #Don't think it does anything but I am going to keep it here till I'm sure.

        self.fightcha = 0
        #The chance you lose a fight.

        self.escapecha = 0
        #The chance you can run away from a fight, coward.

        self.tasks = 0
        #The encounter you will recive.

        self.addhealth = 0
        #The increase in health you get from healing.

        self.tradeOPTIONS = 0
        #The chance a givin item will be avilible for trade.

        self.cost = 0
        #The cost of a trade item in food.

        self.damageMULT = 1
        #The scaling of damage in diffent difficultys.

        self.damageHUN = 25
        #The damage that one day with out hunger will deal to you.

        self.costMULT = 1
        #The scaling of cost in diffent difficultys.

        self.saving = 0
        #To keep track of wether you are saving anyone in the combat you are in.

        self.activeWEP = "NONE"
        #Your active weapon.

        self.activeDEF = "NONE"
        #Your active defence item.

        self.darkSOULS = "YOU DIED" 
        #The text that displays when you die.

        self.password = ""
        #Allows players to continue their game later.
        #~~~~~~
        #Player stats.

        self.name = None
        #Your name.

        self.age = "0"
        #Your weight.

        self.gender = "0"
        #Your gender.

        self.height = "0"
        #Your height.

        self.weight = "0"
        #Your weight.

        self.attack = 0
        #Your attack stat.

        self.defence = 0
        #Your defence stat.

        self.wanted = 0
        #Wether or not you are being hunted by a npc.
        #~~~~~~
        #Stat assign varibles

        self.statPOINTS = 0
        #The number of points you can assign to the various stats

        self.statATTACK = 0
        #The increase you get to attack.

        self.statDEFENCE = 0
        #The increase you get to defence.

        self.statHEALTH = 0
        #The 1.X multiplyer you get to health.

        self.statSCAVENGE = 0
        #The increase you get to finding food.
        #~~~~~~
        #Dog stats.

        self.dog = 0
        #If you have a dog or not.

        self.dogNAME = "0"
        #Your dogs name.

        self.dogHEALTH = 50
        #Your dogs health.

        self.dogSOULS = " DIED"
        #The text that plays when your dog dies. You will only encounter this if you are a bad person.
        #~~~~~~
        self.Day = 0 

        #The list of pronouns that can be called apon.
        self.pronoun = ["happy", "sad", "angery", "tall", "small", "short", "large", "gloomy", "handsome", "rowdy",
        "disgusting", "random", "teenage", "adult", "slimey", "smiley", "cool", "rad", "way out", "dog", "cat",
        "bird", "mouse", "crab", "lonely", "English", "Scottish", "German", "Swedish", "Danish", "American", "Austian",
        "crazy", "British", "Popstarian", "Hyrulian", "Minecraft", "jazzy", "funky", "ghostly", "snazy", "sick (as in 'cool')",
        "average", "strong", "ripped", "MLG", "nerdy", "punk", "evil", "groovy", "Pokemon", "thicc boi", "500 IQ", "apple","poor","socio-economicaly disadvantaged"]

        #~~~~~~
        #Allows players to decide their characters stats.
        
        self.ALLP.append("Welcome to Zombie Survival.")
        self.ALLP.append("Copyright of 'Mop-Head Games'")
        self.ALLP.append("Press enter to continue.")

        input()
        self.ip = True

        #Allow the player to toggel the difficulty.
        while True:
                self.ALLP.append("Select difficulty.")
                self.ALLP.append("Easy - e")
                self.ALLP.append("Normal - n")
                self.ALLP.append("Hard - h")
                self.ALLP.append("")
                self.ALLP.append("Continue - c")
                answer = input()
                self.ip = True
                if answer == "e":
                        self.ALLP.append("Eh, okay, I won't judge you.")
                        self.daysTILLsafety = 14
                        self.damageHUN = -10
                        self.damageMULT = 0.5
                        self.costMULT = 0.5
                        self.statPOINTS = 5
                        self.NameCharacter()
                elif answer == "n":
                        self.ALLP.append("Okay average Joe.")
                        self.daysTILLsafety = 50
                        self.damageHUN = -25
                        self.damageMULT = 1
                        self.costMULT = 1
                        self.statPOINTS = 10
                        self.NameCharacter()
                elif answer == "h":
                        self.ALLP.append("Are you sure?")
                        answer = input()
                        self.ip = True
                        if answer == "y":
                                self.ALLP.append("Prepare for a bad time.")
                                self.daysTILLsafety = 100
                                self.damageHUN = -9999
                                self.damageMULT = 2
                                self.costMULT = 2
                                self.statPOINTS = 15
                                self.NameCharacter()
                        if answer == "n":
                                self.ALLP.append("Okey coward, but you already made a choice.")
                                self.daysTILLsafety = 100
                                self.damageHUN = -9999
                                self.damageMULT = 2
                                self.costMULT = 2
                                self.statPOINTS = 15
                                self.NameCharacter()
                elif answer == "c":
                        self.ALLP.append("Input your characters name.")
                        self.password = input()
                        self.ip = True
                        self.name = password
                        f = open(str(self.password) + ".txt", "r")
                        if f.mode == "r":
                                contents = f.read()
                                self.password = str(contents)
                        self.dog = int(password[0:1])
                        self.health = int(password[1:4])
                        self.food = int(password[4:7])
                        self.daysTILLsafety = int(password[7:10])
                        self.damageHUN = -1 * int(password[10:14])
                        self.attack = int(password[14:18])
                        self.defence = int(password[18:22])
                        self.statATTACK = int(password[22:24])
                        self.statDEFENCE = int(password[24:26])
                        self.statHEALTH = int(password[26:28])
                        self.statSCAVENGE = int(password[28:30])
                        self.dogHEALTH = int(password[30:])
                        
                        self.task()
                    
    def NameCharacter(self):
            input()
            self.ip = True
            self.ALLP.append("Welecome to Zombie Survival today you will design your character.")
            input()
            self.ip = True
            self.ALLP.append("What is your characters name?")
            self.name = input()
            self.ip = True
            self.ALLP.append("How old is your charcter?")
            self.age = input()
            self.ip = True
            self.ALLP.append("What gender is your character?('m' or 'f')")
            self.gender = input()
            self.ip = True
            self.ALLP.append("How tall is your charcter?(m)")
            self.height = input()
            self.ip = True
            self.ALLP.append("How much does your charcter weight?(kg)")
            self.weight = input()
            self.ip = True
            self.ALLP.append("Now assign your core stats.")
            self.core()

    def core(self):
            while True:
                self.ALLP.append("Attack = " + str(self.statATTACK))
                self.ALLP.append("Defence = " + str(self.statDEFENCE))
                self.ALLP.append("Health = " + str(self.statHEALTH))
                self.ALLP.append("Scavenge = " + str(self.statSCAVENGE))
                self.ALLP.append("")
                self.ALLP.append("You have " + str(self.statPOINTS) + " points remaining.")
                self.ALLP.append("To change stat type first letter of stat name. (Lower case)")
                self.ALLP.append("Enter 'DONE' when your finished.")
                while True:
                    answer = input()
                    self.ip = True
                    if answer == "a":
                        self.ALLP.append("How much do you want to change attack by?")
                        self.ALLP.append("(If you want to remove points type in a negative number.)")
                        answer = int(input())
                        self.ip = True
                        if answer > self.statPOINTS or (self.statATTACK + answer) < 1 :
                            self.ALLP.append("You don't have enough points try removing points from somewhere else first.")
                            self.ALLP.append("(If you want to remove points type in a negative number.)")
                        else:
                            self.statATTACK += answer
                            self.statPOINTS -= answer
                    elif answer == "d":
                        self.ALLP.append("How much do you want to change defence by?")
                        self.ALLP.append("(If you want to remove points type in a negative number.)")
                        answer = int(input())
                        self.ip = True
                        if answer > self.statPOINTS or (self.statDEFENCE + answer) < 1 :
                            self.ALLP.append("You don't have enough points try removing points from somewhere else first.")
                        else:
                            self.statDEFENCE += answer
                            self.statPOINTS -= answer
                    elif answer == "h":
                        self.ALLP.append("How much do you want to change health by?")
                        self.ALLP.append("(If you want to remove points type in a negative number.)")
                        answer = int(input())
                        self.ip = True
                        if answer > self.statPOINTS or (self.statHEALTH + answer) < 1 :
                            self.ALLP.append("You don't have enough points try removing points from somewhere else first.")
                        else:
                            self.statHEALTH += answer
                            self.statPOINTS -= answer
                    elif answer == "s":
                        self.ALLP.append("How much do you want to change scavenge by?")
                        self.ALLP.append("(If you want to remove points type in a negative number.)")
                        answer = int(input())
                        self.ip = True
                        if answer > self.statPOINTS or (self.statSCAVENGE + answer) < 1 :
                            self.ALLP.append("You don't have enough points ")
                            self.ALLP.append("-try removing points from somewhere else first.")
                        else:
                            self.statSCAVENGE += answer
                            self.statPOINTS -= answer
                    elif answer == "DONE":
                        self.ALLP.append("Now start your Zombie Survival " + str(self.name) + ".")
                        self.task()

                    else:
                        self.ALLP.append("That's not a valid command.")
                    self.core()

    #Starts each day cycle.
    def task(self):

        while True:
            answer = str(input())
            self.ip = True
            self.Day += 1
            self.ALLP.append("Day: "+str(self.Day))
            self.ALLP.append(" ")
    #Decides wether the player wins.
            if self.daysTILLsafety >= 1:
                    self.daysTILLsafety += -1
            else:
                    self.ALLP.append("Congratulations you made it to safety.")
                    self.ALLP.append("YOU WIN!!!")
                    quit()
    #Decides wether the player or dog dies due to starvation.
            if self.food <= 0:
                    self.health += int(self.damageHUN)
                    self.ALLP.append(str(-self.damageHUN)+" damage taken from starvation")
                    if self.dog == 1:
                            self.dogHEALTH += int(self.damageHUN)
            else:
                    self.food += -1
                    if self.dog == 1:
                            self.food -1
            if self.health <= 0:
                    self.ALLP.append(self.darkSOULS)
                    quit()
            if self.dog == 1 and self.dogHEALTH <= 0:
    #Displays the stat hud.
                    self.ALLP.append(self.dogNAME + self.dogSOULS)

            self.ip = True
            if answer == "SAVE":
                    self.save()
    #Decides the senario for that day.
            tasks = randint(1,9)
            if tasks == 1:
                    self.Encounter1()
            elif tasks == 2:
                    self.Encounter2()
            elif tasks == 3:
                    self.Encounter3()
            elif tasks == 4:
                    self.Encounter4()
            elif tasks == 5:
                    self.Encounter5()
            elif tasks == 6:
                    self.Encounter6()
            elif tasks == 7:
                    self.Encounter7()
            elif tasks == 8:
                    self.Encounter8()
            elif tasks == 9:
                    self.Encounter5e()

    def Encounter1(self):
            place = random.choice(["shop","manor house","council estate","abandoned village","shopping mall","small suburban rail depo","large office block","old tesco superstore","ex-disney resort"])
            
            self.ALLP.append("You are wandering through a "+random.choice(["forest","meadow","abandoned village","abandoned city","shopping mall","small ravine"])+ " and you see a "+place)
            self.ALLP.append("The "+place+" looks ungarded with no zombies in sight")
            self.ALLP.append("Do you wish to enter?")
            answer = input()
            self.ip = True
            if answer == "y":
                    self.foodinc = randint(1,5)
                    self.ALLP.append("You search around the "+place+"... ")
                    input()
                    self.ALLP.append("you find " + str(self.foodinc + self.statSCAVENGE) + " food.")
                    
                    self.food += self.foodinc + self.statSCAVENGE
                    if self.dog == 1:
                            self.foodinc = randint(1,2)
                            self.ALLP.append(str(self.dogNAME) + " finds " + str(self.foodinc + self.statSCAVENGE) + " food.")
                            self.food += self.foodinc + self.statSCAVENGE
                    input()
                    self.ALLP.append("You are glad that decided to stop at the "+place)
                    self.ip = True
            elif answer == "n":
                    self.ALLP.append("You continue walking along the long twisting road feeling that you made a "+random.choice(["poor","unfortunate","possibly bad","actively unhelpfull"])+" choice.")

            else:
                    self.ALLP.append("Answer only with 'y' for yes or 'n' for no.")
                    self.Encounter1()

    def Encounter2(self):
            place = random.choice(["shop","manor house","council estate","abandoned village","shopping mall","small suburban rail depo","large office block","old tesco superstore","ex-disney resort"])
            
            self.ALLP.append("You are wandering through a "+random.choice(["evil forest","dead meadow","abandoned disney restort","lower income neighborhood"])+ " and you see a "+place)
            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.ALLP.append("The "+place+" looks abandoned but off in the distance you can see a "+random.choice(["small","large","strange","sinister"]) +" group of " + self.prono + " zombies.")
            self.ALLP.append("Do you wish to enter?")
            answer = input()
            self.ip = True
            if answer == "y":
                    self.foodinc = randint(0,5)
                    self.ALLP.append("You decided to enter the "+place+" and spend some time in there looking for food...")
                    input()
                    self.ALLP.append("you find " + str(self.foodinc + self.statSCAVENGE) + " food.")
                    self.food += self.foodinc + self.statSCAVENGE
                    if self.dog == 1:
                            self.foodinc = randint(1,2)
                            self.ALLP.append(str(self.dogNAME) + " finds " + str(self.foodinc + self.statSCAVENGE) + " food.")
                            input()
                            self.food += self.foodinc + self.statSCAVENGE
                    self.damagecha = randint(1,8)
                    
                    if self.damagecha == 1:
                            self.ALLP.append("You feel a great amount of "+random.choice(["happiness","luck","despair at the state of the world,"]) +" and continue walking.")
                            input()
                            self.ip = True

                    elif self.damagecha < 4:
                        self.ALLP.append("You spend far too much time in the "+place+" and the " + self.prono + " zombies reach you.")
                        input()
                        self.ip = True
                        self.ALLP.append("But fortuantly you notice a"+random.choice([" window"," vent"," open sewage pipe"," dildo"," disguise","nother door"])+" and are able to use it to escape")


                    else:
                            self.damage = randint(10,20) * int(self.damageMULT)
                            self.ALLP.append("You spend far too much time in the "+place+" and the " + self.prono + " zombies reach you.")
                            self.combat()
            elif answer == "n":
                    self.ALLP.append("You didn't go into the "+place+" and you feel that was probably a good choice.")

            else:
                    self.ALLP.append("Answer only with 'y' for yes or 'n' for no.")
                    self.Encounter2()
                    


    #Shop encounter	
    def Encounter3(self):

            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            thing =  random.choice(["drugs","medcine","whiskey","bandages","their virginity","a medical kit","a nice cup of tea"])
            self.addhealth = randint(5,15)
            self.tradeOPTIONS = randint(1,100)
            self.cost = randint(5,15)
            if self.tradeOPTIONS < 100:
                    self.ALLP.append("While walking the long road of life you spot a " + self.prono + " trader at the side of the road.")
                    self.ALLP.append("They offer you "+thing+" in exchange for " + str(self.cost * self.costMULT) + " food.")
                    self.ALLP.append("Do you accept the offer?")
                    answer = input()
                    self.ip = True
                    if answer == "y":
                            if self.wanted == 1:
    #If you are being hunted, you are found and attacked.
                                    self.ALLP.append("The " + self.prono + " trader said 'I know you!!!!!!'")
                                    input()
                                    self.ALLP.append("your the piece of %*@? who left me to fend for myself.'")
                                    self.ALLP.append("'Now you will pay!'")
                                    input()
                                    damage = randint(10,20)
                                    self.ALLP.append(str(self.damage) + " damage.")
                                    self.ALLP.append("'Good now we're even.'")
                                    if self.health <= 0:
                                            self.ALLP.append(self.darkSOULS)
                                            quit()
                            else:	
                                    if self.food >= self.cost * self.costMULT:
                                            self.ALLP.append("You give the " + self.prono + " trader the food and get "+thing+" (+"+ str(self.addhealth + self.statHEALTH) + " health.)")
                                            self.health += self.addhealth + self.statHEALTH
                                            self.food -= self.cost * self.costMULT
                                    else:
                                            self.ALLP.append("You don't have enough food to pay.")
                    elif answer == "n":
                            self.ALLP.append("You say no to the " + self.prono + " trader because stranger danger, and go on your merry day.")

                    else:
                            self.ALLP.append("Answer only with 'y' for yes or 'n' for no.")
                            self.Encounter3()
            if self.tradeOPTIONS == 100 and self.dog == 0:
                    self.dogo(self)


    def Encounter4(self):
            self.ALLP.append("While walking along the path of life you see absolutely nothing at all.")
            if randint(0,10) == 1:
                self.ALLP.append("You feel as if the games developer just needed to put lots of senarios to make the game not seen repetative.")

            
    def Encounter5(self):
        
            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.ALLP.append("While "+ random.choice(["very drunk",
                                                      "contemplating your life",
                                                      "walking through the town centre",
                                                      "walking up a hill",
                                                      "walking through a forest",
                                                      "loosing your virginity",
                                                      "walking along the road","walking through a meadow"])+" you are suprised by a swarm of " + self.prono + " zombies.")
            input()
            self.ip = True
            self.damage = randint(15,30) * int(self.damageMULT)
            self.combat()

    def Encounter5e(self):
            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.ALLP.append("While "+ random.choice(["very drunk",
                                                      "contemplating your life",
                                                      "walking through the town centre",
                                                      "walking up a hill",
                                                      "walking through a forest",
                                                      "loosing your virginity",
                                                      "walking along the road","walking through a meadow"])+" you encounter a swarm of " + self.prono + " zombies.")
            input()
            self.ip = True
            self.damage = randint(15,30) * int(self.damageMULT)
            self.combat()
            
    def Encounter6(self):
            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.ALLP.append("As you are walking along the long road you see a... " )
            input()
            self.ip = True
            self.ALLP.append(self.prono + " man lying nearby the road.")
            input()
            self.ALLP.append("His head is missing and has bite marks along his "+random.choice(["back","torso","front"])+" and "+random.choice(["toes","arms","legs","lower ribs"])+".")
            thing = random.choice(["knife","screwdriver","broken gun","plank of wood","old mop","blade","large toenail"])
            number = randint(-1,19)
            self.ALLP.append("At his side you can see a "+thing)
            self.ALLP.append("Do you take the "+thing+"?")
            answer = input()
            self.ip = True
            if answer == "y":
                    if self.attack - self.statATTACK > number:
                            self.ALLP.append("You decide this "+thing+" is so bad it will make you worse at fighting")
                            self.ALLP.append("would you like to still take it?")
                            answer = input()
                            self.ip = True

                            if answer == "y":
                                self.ALLP.append("You take the "+thing)
                                self.activeWEP = thing
                                self.ALLP.append("Attack +"+str(number))
                                self.attack = number

                                input()
                                self.ALLP.append("As you walk down the road you now feel weaker.")

                            elif answer == "n":
                                self.ALLP.append("You don't take the "+thing)
                            else:
                                self.ALLP.append("Only answer with 'y' or 'n'.")
                                self.Encounter6()
            
                    else:
                            sleep(0.1)
                            self.ALLP.append("You take the "+thing)
                            self.activeWEP = thing
                            self.ALLP.append("Attack +"+str(number))
                            self.attack = number
                            self.ALLP.append("As you walk down the road you feel strong.")
            elif answer == "n":
                self.ALLP.append("You don't take the "+thing)
                self.ALLP.append("You walk along the road of life with one less "+thing+" to defend yourself.")
            else:
                self.ALLP.append("Only answer with 'y' or 'n'.")
                self.Encounter6()

                    
    def Encounter7(self):
            thing = random.choice(["broken pot lid","small umbrella","suit of armor","plank of wood","small white flag","small CD"])
            number = randint(2,10)
            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.ALLP.append("Going along the road you find a " + self.prono + " man missing his "+random.choice(["arms and legs","feet and eyes","lower torso","internal organs","british passport"]))
            self.ALLP.append("On his back he bares a "+thing)
            self.ALLP.append("It could be used for your defence")
            self.ALLP.append("Do you take it?")
            answer = input()
            self.ip = True
            if answer == "y":
                if random.randint(1,4) == 1:
                    self.ALLP.append("You have made a miscalculation... he is a zombie and now he is trying to attack you")
                    input()
                    self.ip = True
                    self.combat()
                    
                elif self.defence - self.statDEFENCE > number:
                        self.ALLP.append("after inspecting the"+thing+" you decide that taking it would make you less defencive")
                        self.ALLP.append("do you still want to take it?")
                        answer = input()
                        self.ip = True
                        if answer == "y":
                            self.ALLP.append("You steal the " + self.prono + " man's "+thing)
                            self.ALLP.append("Defence +"+str(number))
                            self.activeDEF = thing
                            self.defence = number
                        elif answer == "n":
                            self.ALLP.append("You don't take the " + self.prono + " man's "+thing)
                            self.ALLP.append("Kinda Respect for the dead.")
                        else:
                            self.ALLP.append("Only answer with 'y' or 'n'.")
                            self.Encounter7()
                        
                else:
                        self.ALLP.append("You steal the " + self.prono + " man's "+thing)
                        self.ALLP.append("Defence +"+str(number))
                        input()
                        self.activeDEF = thing
                        self.defence = number
                self.ALLP.append("You continue on your way")
            elif answer == "n":
                    self.ALLP.append("You don't take the " + self.prono + " man's "+thing)
                    self.ALLP.append("Respect for the dead.")
            else:
                    self.ALLP.append("Only answer with 'y' or 'n'.")
                    self.Encounter7()

    def Encounter8(self):

            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.prono2 =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.ALLP.append("As you walk along the road of life you see a " + self.prono + " group of zombies attacking a " + self.prono2 + " man.")
            self.ALLP.append("do you aproach?")
            answer = input()
            self.ip = True
            if answer == "y":
                    self.ALLP.append("You aproach the heard of " + self.prono + " zombies.")
                    self.ALLP.append("they all turn to you as if you were a dish at a cafe that has been cooking for over an hour")
                    input()
                    self.ALLP.append("(They attack you.)")
                    input()
                    self.ip = True
                    self.saving = 1
                    self.damage = randint(20,30)
                    self.combat()
            elif answer == "n":
                    self.ALLP.append("You leave the " + self.prono2 + " man to fend for himself as you walk away you hear 'I will kill you *@!#?%^ coward!")
                    self.wanted = 1
            else:
                    self.ALLP.append("Only answer with 'y' or 'n'.")
                    
    def Encounter8S(self):

            self.ALLP.append("After you DESTROY the " + self.prono + " zombies you run over to the " + self.prono2 + " man.")
            self.ALLP.append("He does not look that wounded.")
            input()
            self.ip = True
            
            wp = random.choice(["shining sword","bronze sword","japanese kinfe","fire poker","large claymore","sharp needle kit"])
            wpd = randint(2,30)

            ar = random.choice(["very fine pot lid","very large umbrella","suit of golden armor","plank of mahogany","large american flag","sheild"])
            ard = randint(2,30)
            
            self.ALLP.append("He thanks you for saving him and offers you a "+wp+" and "+ar+".")
            if self.attack - self.statATTACK > wpd:
                    self.ALLP.append("You have a better weapon so you don't take it.")
            else:
                    self.ALLP.append("You get the "+wp)
                    self.ALLP.append("+"+wpd+" attack")
                    self.activeWEP = wp
                    self.attack = wpd
            if self.defence - self.statDEFENCE > ard:
                    self.ALLP.append("You have a better defensive item so you don't take it.")
            else:
                    self.ALLP.append("You get the "+ar)
                    self.ALLP.append("+"+ard+" defence")
                    self.activeDEF = ar
                    self.defence = ard
                    
            self.saving = 0
            
    #Rare but allow the player to have a dog join them.
    def dogo(self):
            self.prono =  str(self.pronoun[randint(0,len(self.pronoun)-1)])
            self.clr =  str(self.colour[randint(1,len(colour))])
            self.ALLP.append("While walking along the road you see a " + self.prono + " " + self.clr + " dog.")
            self.ALLP.append("Do you rescue the dog.")
            answer = input()
            self.ip = True
            if answer =="y":
                    self.ALLP.append("You save the " + self.prono + " " + self.clr + " dog.")
                    self.ALLP.append("Do you want to name the " + self.prono + " " + self.clr + " dog")
                    answer = input()
                    self.ip = True
                    if answer == "y":
                            self.ALLP.append("Type your dogs name then hit enter.")
                            self.dogNAME = input()
                            self.ip = True
                            self.ALLP.append("*Fanfare* " + str(self.dogNAME) + " joins the team.")
                            self.dog = 1
                    elif answer == "n":
                            self.ALLP.append("You WANT to name the dog.")
                            self.ALLP.append("Type your dogs name then hit enter.")
                            self.dogNAME = input()
                            self.ip = True
                            self.ALLP.append("*Fanfare* " + str(self.dogNAME) + " joins the team.")
                            self.dog = 1
                    else:
                            self.dogo()
            elif answer =="n":
                    self.ALLP.append("You don't rescue the " + self.prono + " " + self.clr + " dog and will forever have a " + self.prono + " " + self.clr + " dog shaped hole of sadness in your heart.")
            else:
                    self.ALLP.append("Answer only with 'y' for yes or 'n' for no.")
                    self.dogo()		

    #Allow the player to fight the enemy.
    def combat(self):
            run_chance = randint(10,88)
            self.ALLP.append("you estimate that you have a "+str(100-run_chance)+"% of escape. Do you want to run?")
            answer = input()
            self.ip = True
    #Asks the player if they want to fight the enemy or run away.
            if answer == "n":
                    self.fightcha = randint(1,100)
    #fightcha is a random number that get added onto the players attack stat to decide they chance at winning a fight.
                    self.ALLP.append("You decide to fight.")
                    if self.fightcha + self.attack >= randint(1,100):
    #The fightcha is added on to the attack stat to favor the play and give items a value.
    #Then is compared to a random number in between 1 and 100 to decide a victor.
                            self.foodinc = randint(1,5)
                            self.ALLP.append("You heroicly DESTROY the " + self.prono + " zombies. +" + str(self.foodinc) + " food")
                            self.food += self.foodinc
                            if self.saving == 1:
    #If you got an encounter which envolved saving some one this brings you to the reward diologe because you won.
                                    self.Encounter8S()
                                    
                            else:
                                    self.ALLP.append("You continue your way along the road of life.")
                    else:
    #If you lose to the enemy you take a certain amount of damage and might die.
                            self.ALLP.append("You try to fend of the " + self.prono + " zombies, but they overwelm you.")
                            self.ALLP.append("You just barely escape the " + self.prono + " zombies. -" + str(self.damage - self.defence) + "% health.")
                            self.saving = 0
                            self.health -= self.damage - self.defence
                            if self.health <= 0:
                                    self.ALLP.append(self.darkSOULS)
                                    quit()
                            if self.dog == 1:
                                    self.ALLP.append(str(self.dogNAME) + " got hit too. -" + str(self.damage - self.defence) + "% health.")
                                    self.dogHEALTH -= self.damage - self.defence
                                    if self.dogHEALTH <= 0:
                                            self.ALLP.append(self.dogNAME + self.dogSOULS)
                                            self.dog = 0
            elif answer == "y":
    #If you decide to run then there is a 3 in 4 chance you escape but a 1 in 4 chance you get attcked while leaving.
                    self.escapecha = randint(1,100)
                    if self.escapecha >= run_chance:
                            self.ALLP.append("You relize that you are overwelmed and decide to run before it's to late...")
                            self.saving = 0
                            self.ALLP.append("You get away safely")
                    else:
                            self.ALLP.append("You relize that you are overwelmed and decide to run before it's to late...")
                            input()
                            self.ip = True
                            self.ALLP.append("You try to run but a small group of " + self.prono + " zombies catch up with you as you leave. -" + str(self.damage - self.defence) + "% health")
                            self.health -= self.damage - self.defence
                            self.saving = 0
                            if self.health <= 0:
                                    self.ALLP.append(self.darkSOULS)
                                    quit()
                                    if self.dog == 1:
                                            self.ALLP.append(str(self.dogNAME) + " got hit too. -" + str(self.damage) + "% health.")
                                            self.dogHEALTH -= self.damage - self.defence
                                            if self.dogHEALTH <= 0:
                                                    self.ALLP.append(self.dogNAME + self.dogSOULS)
                                                    self.dog = 0
                            else:
                                    self.ALLP.append("After running some more you lose the " + self.prono + " zombies in a nearby forest.")
            else:
                    self.ALLP.append("Answer only with 'y' for yes or 'n' for no.")
                    


    #~~~~~~~
    #Code that allows the player to make a save password.

    def save(self):

            self.damageHUN = self.damageHUN * -1
            if self.health < 100:
                    self.health = "0" + str(self.health)
                    if int(self.health) < 10:
                            self.health = "0" + str(self.health)
            if self.food < 100:
                    self.food = "0" + str(self.food)
                    if int(self.food) < 10:
                            self.food = "0" + str(self.food)
            if self.daysTILLsafety < 100:
                    self.daysTILLsafety = "0" + str(self.daysTILLsafety)
                    if int(self.daysTILLsafety) < 10:
                            self.daysTILLsafety = "0" + str(self.daysTILLsafety)
            if self.damageHUN < 9999:
                    self.damageHUN = "00" + str(self.damageHUN)
            if self.attack < 9999:
                    self.attack = "00" + str(self.attack)
                    if int(self.attack) < 10:
                            self.attack = "0" + str(self.attack)
            if self.defence < 9999:
                    self.defence = "00" + str(self.defence)
                    if int(self.defence) < 10:
                            self.defence = "0" + str(self.defence)
            if self.statATTACK < 10:
                    self.statATTACK = "0" + str(self.statATTACK)
            if statDEFENCE < 10:
                    self.statDEFENCE = "0" + str(self.statDEFENCE)
            if statHEALTH < 10:
                    self.statHEALTH = "0" + str(self.statHEALTH)
            if statSCAVENGE < 10:
                    self.statSCAVENGE = "0" + str(self.statSCAVENGE)       
            f = open(self.name + ".txt", "w+")
            f.write(str(self.dog) + str(self.health) + str(self.food)+ str(self.daysTILLsafety) + str(self.damageHUN) + str(self.attack) + str(self.defence) + str(self.statATTACK) + str(self.statDEFENCE) + str(self.statHEALTH) + str(self.statSCAVENGE) + str(self.dogHEALTH))
            f.close()

            input()
            self.ip = True
            quit()
    #~~~~~~~






