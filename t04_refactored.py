######################################################################
# Author: Mason Richardson Joey Martin
# Username: richardsonmas martinj2
#
# Assignment: T04: Adventure in Gitland
#
# Purpose: To recreate a choose-your-own-adventure style game
# by refactoring T01.
#
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
#
# This new version will take advantage of functions, as well as
# demonstrate the value of git as a tool for collaborating.
# https://docs.google.com/document/d/12AqOblfS_IRP24dKtyJrNh9a8E8JcmrvfzseTkbixyU/edit#
######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
#
######################################################################
import random
from time import sleep

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False


def start_story():
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(delay)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(delay)
    return user


def end_story(user):
    """
    This is the ending to the story. Don't modify this function, either.

    :param user: the user's name
    :return: None
    """
    print(
        "Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay * 5)
    print("Now go play again.")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead

    :param dead: A boolean value where false let's the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()


###################################################################################


def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """
    global dead  # You'll need this to be able to modify the dead variable
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(delay * 2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print(
            "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)


###################################################################################


def team_1_adv():
    global dead
    sleep(delay * 2)
    print("\n\nYou continue on with your journey. You happen to stumble across a bomb.")
    print("God offers you some wirecutters. With nothing to lose, you decide to be a hero.")
    print("You unscrew the bomb. In front of you are three wires: red, blue, and yellow.")
    sleep(delay * 2)
    print("Which wire will you choose, dude?")
    color = input("Red, Blue, or Yellow?")
    if color == "red":
        # The good choice
        print("You suck in a breath and then cut the wire. The LEDs flicker, then shut off. You did it!")
    elif color == "blue":
        # The bad choice
        print("You suck in a breath and then cut the wire. ")
        print("The bomb explodes into a white light. You die instantly.")
        dead = True
    else:
        print("You suck in a breath and cut the yellow wire.")
        print("")
        print("Nothing explicitly happens, but suddenly you have a loaf of banana nut bread in your pocket.")
        print("... You decide to move on.")
    kill_if_dead(dead)
    """This function runs one room where you have to choose which wire to cut in a bomb. Choose wisely!"""



def team_2_adv():
    ######################################################################
    # Author: Jose Zapata & Ben Maynard
    # Username: zapatamezaj & maynardb
    #
    # Assignment: T04: Adventure in Gitland
    #
    # Purpose: To recreate a choose-your-own-adventure style game
    # by refactoring T01.
    ######################################################################
    """
    Google Document Link:
    https://docs.google.com/document/d/1N2BXxH4VsnbuLDMHqq_gNpbawFb-_D3vbwr5oPuuR8g/edit?usp=sharing"""
    global dead
    print("Congratulations! \n"
          "You have survived so far. But the journey does not end for the gold still lays undiscovered. \n ")
    sleep(delay * 2)
    direction = input("Which way would you like to go now? Choose wisely North, East, West or South?\n")
    if direction == "East":
        # Good choice
        print("You have proven how worthy you are so the gods have decided to reward you with Gold. \n "
              "You are rich now go home and spread your wealth! \n")
    elif direction == "North":
        # Bad choice
        print("This trip is only for the worthy. You have been found unworthy and the gods have sacked your soul.\n")
        dead = True
    elif direction == "West":
        # Bad choice
        print("Some wolves come by and urinate all over your stuff, then eat your face off. \n"
              "Tragic, you could have been rich but now you're dead.")
        dead = True

    else:
        print("You were found by a group of robbers. They know you have enough food and gold to last you days. \n"
              "They loot you and leave you for the bears.")
        dead = True
    sleep(delay)
    kill_if_dead(dead)

    print("You're in the cave, its night time and you began to hear screams from one of two paths.")
    direction = input("Which path will you take, East or West? Choose wisely.")
    if direction == "East":
        print("""Congratulations! You have found the exit and have made it out with only a few scratches 
        and maybe some broken bones, but look on the bright side, at least you're alive.""")
    else:
        print("You become curious of the screams and follow them. \n"
              "You stumble upon a group of rich cave people that party and they invite you to join them")
    kill_if_dead(dead)


def team_3_adv():
    """
    Authors: Jeremy, Concepta
    Google Link: https://docs.google.com/document/d/1OFzXphHUyPa6YQpFq5rVqsW-1NFc8JwoCqsTKO79Lbw/edit?usp=sharing
    :return: N/A
    """
    username = input("What do you call yourself?")

    action = input_action()
    ask_action(username, action)

    sleep(delay)



def input_action():
    """
    Starts the story, asks user to select an option.
    :return: Returns the result of the variable 'action'.
    """
    print("You are being chased by a group of goblins.")
    print("You and your friend for some reason decide to run to a cliff. What do you do?")
    action = input("[Sleep | Jump | Do Nothing | Fight] ")
    return action


def ask_action(username, my_input):
    """
    This function will generate a set list of prompts based upon the my_input variable.
    :param username: Utilizes the users name in the print functions.
    :param my_input: Allows the user to input a finite selection of options to further the program.
    :return: N/A
    """
    if my_input == "sleep" or my_input == "Sleep":
        # Good choice
        sleep(delay)
        print("Amazing! Good job, ", username, "! You have found their weakness! Goblins can't see sleeping people...")
        sleep(delay)
        print("As you awake, you notice some golden coins one of the goblins left behind.")
        sleep(delay)
    elif my_input == "do nothing" or my_input == "Do nothing":
        # Bad choice
        print("Do nothing? YOU DIE!!!!")
        sleep(delay)
        if dead:
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            kill_if_dead(dead)
    elif my_input == "fight" or my_input == "Fight":
        print("You have proved so brave", username, ". Go on with your journey!")
    elif my_input == "jump" or my_input == "Jump":
        print("At the bottom of this cliff lies waves of fast flowing water. Jumping was not a good choice!")
    else:
        print("The choice you entered is not available. Please enter a valid choice.")
# Finished, yay!


def team_4_adv():
    pass
    # TODO Add your code here


def test_the_rainbow(flavor):
    """
    Editors: Bryar Frank
             Shawn Villahermosa
     Function takes the input given by the user and checks to see if it is similar to one of the three options given.
     If it isn't, it returns "True" so the question can be repeated.
    :return: True
    """
    if len(flavor) == 9 and flavor[0] == "s" and flavor[8] == 'y':
        # Good choice!
        print("Good choice!This makes you feel a lot better")
        print("considering your friend disappeared mysteriously the other day.\n")
        sleep(delay)

    elif len(flavor) == 10 and flavor[0] == "p" and flavor[9] == 'o':
        # Neutral choice
        print("You feel a tingling sensation in your throat, and you start puking blood and pistachios.")
        print("As everything starts going black, you vaguely hear evil laughter. ")
        print("The ice cream van starts up and a merry song starts playing and slowly fades away \n")

    elif len(flavor) == 9 and flavor[0] == "c" and flavor[8] == 'e':
        # Oh... Bad choice
        print("Here you go, this is a van favorite!")
        sleep(delay)
        print("Oh it tastes so familiar but not in a good way")
        print("At first you don't realize it but then you start feeling nauseous")
        print("You start vomiting and ask 'What the hell was that?'")
        print("The ice cream people tells you: Don't worry! It's just your friend! \n")

        # Kill the player and end the program if this choice is made
        kill_if_dead(True)

    else:
        return True


def team_5_adv():
    """
    ######################################################################
    # Assignment: T04: Adventure in Gitland
    #    Editors: Bryar Frank
    #         Shawn Villahermosa
    #    Google Doc: https://docs.google.com/document/d/1icOBu4PV5DDGkWtmThEnmaj2JaOW1aoW9Yujh0_caLo/edit?usp=sharing
    ######################################################################
    :return:
    """
    typo = True

    while typo == True:
        flavor = input("Which flavor would you like? [Strawberry/Pistachio/Chocolate]")
        print()
        flavor.lower()
        typo = test_the_rainbow(flavor)
        if typo == True:
            print("Looks like the answer you provided isn't close to your choices")
            sleep(delay)
            print("Please try again unless you want to be stuck here forever... \n")


def team_6_adv():
    pass
    # TODO Add your code here


def team_7_adv():
    """
    https://docs.google.com/document/d/1Dh_Zd3X9bS8DijgocvDM0IqgX9UTT2eTzIUM_Pj_I-U/edit?ts=5d7ba1f3#heading=h.f6tumop9n7at
    :return: None
    """
    global dead
    direction = input("Which direction would you like to go? [Right/Forward/Backward/Left]")
    direction = direction.lower()  #changes the user's input to lowercase
    if direction == "right":
        # Good Choice!
        print("You rush into the nearby trees for cover. There you find a mystical coconut that will slay the dragon.")
        sleep(delay)
    elif direction == "forward":
        # Bad Choice
        integer = int(
            input(
                "You have made a bad choice! You have one more chance to avoid being burnt alive. Pick a number."))
        if integer <= 50:
            print("You have saved yourself and spared yourself from the dragon!")
        elif integer > 50:
            print("You failed to make a better decision and gave the dragon time to get the BBQ sauce.")
            print("You have decided to run towards the dragon. The dragon scoffs and burns you to a crisp.")
            dead = True
            kill_if_dead(dead)
            sleep(delay)
    else:
        pass
        # Oh...Bad Choice
        print("You reach the end of the cave uneventfully. Continue on!")





def team_8_adv():
    """
    https://docs.google.com/document/d/1_Qj83TBpX5Doe6TMSEJ5TJ3kR8oNaE6qu6pPN4iCceA/edit?usp=sharing
    :return:
    """
    # TODO Add your code here


    #######################################################################################
    # eubanksn and mualcinp
    # T04
    # Fixing code
    ######################################################################################
    # TODO Team 8





    sleep(delay)

    username = input("Who are you?")

    print()
    print("Thum.. Thum.. Thum.. You hear footsteps approaching.")
    sleep(delay * 2)
    print("Hello,", username, "I am the spirit of this cave. Here, take some food to help you with your journey.")

    choice = input("Take the food? [yes/no]")
    choice = choice.lower()

    if choice == "yes":
        print("You took the food and ate it. Now you have enough energy to continue on your journey.")
        sleep(delay)
        print("Congratulations! You made a wise choice.")
    elif choice == "no":
        second_choice = int(input(
            "\nOkay, you don't have to eat all the food but you must take some bites. How many bites are you going to "
            "take? [0-200]"))
        while True:
            if second_choice >= 0:
                if second_choice > 100:
                    print("\nYou ate too much and exploded, you gluttonous fiend!")
                    deceased = True
                elif second_choice == 0:
                    print("\nYou get hungry and your energy level drops. You pass out.")
                    deceased = True
                elif 100 >= second_choice > 0:
                    print("\nYou took the food and ate it. Now, you have enough energy to continue on your journey.")
                    print("Congratulations! You made a wise choice.")
                break
            second_choice = int(input(
                "That is not possible. Now, lets try again. How many bites would you like to take? Input a number from "
                "0-200 this time. "))

    else:
        print("Enter either 'yes' or 'no'. The spirit of the cave would not take any other answers.")
    if deceased:
        print("A bear comes across your mangled, exploded body. You wake up dead.")
        quit()

# TODO Don't forget to check if your user is dead at the end of your chapter!



def team_9_adv():
    ######################################################################
    # Author: Taran Wells & Dakota Miller
    # Username: Wellst & Millerd2
    #
    # Assignment: T04: Adventure in Gitland
    #
    # Google docs: https://docs.google.com/document/d/1tQqF_Y0WmdpPVzTq3wAzf5_kX4x5tzHtdvdRv92qHp8/edit?usp=sharing
    ######################################################################

    death = False
    print("You see a dim light glowing behind a loose boulder. Do you choose to investigate?")
    choice = input("[Yes/no/leave]")
    sleep(delay)

    if choice == "Yes":
        print("You place your hand against the boulder and it dissipates into the air like fine mist. Behind it you")
        print("see a giant sword bigger than most men.")
        sleep(delay)
        print("A giant humanoid creature enters your view and begins to grab the sword.")
        sleep(delay * 2)
        print("He swings the sword in your direction causing the timid ceiling to collapse in between you saving ")
        print("yourself from the giant beast. ")
        print("You are safe for now, and you begin to search for a way out..")
        #
        #
        sleep(delay)
    elif choice == "no":
        print("You choose to hastily run away from the boulder and you begin to lose your footing.")
        sleep(delay)
        print("You trip and fall forward breaking your neck in the most boring possible fashion")
        death = True
    else:
        print("You decide against your gut and move away from the glowing boulder.")
        sleep(delay)
        print("You leave the cave by following the sounds of wilderness outside. You begin to hear some disgruntled")
        print("shuffling in the cave as you leave.")

    kill_if_dead(death)

    pass


def team_10_adv():

  #  Google Doc: https://docs.google.com/document/d/1XwjthTBbExLqfs_fXTbGp70kUGsyPTzwsMwP5XOjrJ4/edit?usp=sharing
    # TODO Team 10

    # Beginning of the Amulet Encounter Chapter

    global dead
    print()
    print("You are in a room with strange symbols all over the walls.")
    print("Looking at the eldritch markings makes your head hurt just by looking at them.")
    print("You see an amulet floating in the middle of the room over a pedestal.")
    print()

    amuletAction = input("What do you want to do? [Wear/Ignore/Destroy]")
    print()
    if amuletAction == "Wear" or "wear" or "WEAR":
        # Bad choice
        print("Nothing happens... ")
        sleep(delay * 3)
        print("...")
        sleep(delay * 3)
        print("You feel strange, your hands starts twitching uncontrollably.")
        print("You start walking back into the darkness, not in control of your own actions.")

        # Begin Test of Wills

        print()
        print("You're body is under new management at the moment.")
        print("The walls begin to morph, forming words you can comprehend, requesting a number.")
        amuletSave = input("What is The Ultimate Answer to Life, The Universe and Everything?")

        if int(amuletSave) == 42:
            print()
            print("Your body starts responding again.")
            print("You seem to have shaken off the evil manipulation.")
            print("Harrowed by your brush with death, you carry on, deeper into the labyrinth")
        elif 41 <= int(amuletSave) <= 43:
            print()
            print("Close enough!")
            print("You shake off the control with moments to spare and come to your senses.")
            print("You twitch one last time and run for you life, towards (unlikely) safety...")
        else:
            print("INCORRECT MORTAL!!!")
            print("NOW DIE FOR YOUR IGNORANCE!")
            dead = True

    elif amuletAction == "Destroy" or "destroy" or "DESTROY":
        # Good option
        print("As you cast the amulet into some previously un-narrated lava, you feel watched by a giant eye.")
        print("As the amulet disintegrated, you feel a cursed being lifted from the Median-Earth.")
        print("Satisfied with your good deed for the day you carry on deeper into the labyrinth...")
        print()
    elif amuletAction == "Ignore" or "ignore" or "IGNORE":
        # Boring option
        print("So you ignore the floating mystical artifact in the middle of the room.")
        print(
            "We went through all of the trouble in making a cool, levitating, magic item for you and you ignore it...")
        print("Way to go, you hurt our creative pride.")
        print("Well, I guess you can carry on, further deeper into the depths of the labyrinth...")
        print("Away from anything fun...")
        print()

    else:
        # Just in case option
        print("Somehow, our scenario wasn't interesting enough for you to even answer properly.")
        print("Whatever you just did somehow broke the laws of causality and you glitch")
        print("through a lamp using a backwards long jump and end up in a parallel dimension in another room...")
        print()

    if dead == True:
        print("Congratulations! You've been possessed by an ancient evil!")
        print("Don't mess with cursed objects kids!")
        print("Better luck next time! Try again by hitting the green play button in the top right. ")
        kill_if_dead()

    print()
    print()


def team_11_adv():
    pass
    # TODO Add your code here


# This is the start of team twelve's work.
def choosing(choice2):
    """ this function present the user with the yes or no choice. Yes: progress, No:dead
    """
    if choice2 == "yes":
        print("Great you refilled your health ")
    elif choice2 == "no":
        print("you die from starvation?!")
        sleep(delay)
        dead()
    else:
        # neutral choice
        print("you later found berries in the dark hall")


def choosing1(choice3):
    """This function gives you two choices, one opens the door, the other is death
    """
    if 0 < choice3 <= 10:
        print("A door opens")
    elif choice3 > 10:
        print(" You fall to your death")
        dead()


def team_12_adv():
    """ This is Imma and Sama's part of the adventure. Enjoy!
    here's our google doc: https://docs.google.com/document/d/1vQBVi9MWeufUl-xCIQGYaNfP7oAsKXdWE0a3dMO0pmo/edit?usp=sharing
    """

    # def choosing(choice):

    # def dead():
    #       quit()

    print("You walk into a room and see a glass of milk sitting on a table. Do you drink it?)")
    choice1 = input("[yes/no] ")

    choosing(choice1)
    sleep(1)
    print("In the dark hall you see a libra scale. You have to set the scale equal to a bar of silver.")
    choice = int(input("Pick a number"))
    choosing1(choice)

    # TODO Don't forget to check if your user is dead at the end of your chapter!

    #########################################################################################################
    # TODO Add your code here


def team_13_adv():
    sleep(delay * 3)
    global dead
    print("")
    print("")
    print("It seems like you will be here a while.")
    print("You see two doors in front of you. One is made of wood. It looks like it is about to fall off.")
    print("The other door is just plants. All you gotta do is walk through and you're on the other side. ")
    print("There is also a doorway with no door. ")
    choice = input("Where will you go? [Wood/Plant/No door]   ")
    if choice == "Wood":
        print("As you push the door open, it falls off. ")
        print("The loud noise wakes up the polar bear sleeping inside. It then proceeds to devour you with salt.")
        dead = True
    elif choice == "Plant":
        print("You brush the plants to the side and walk through the doorway.")
        print("This opens up a secret path. You follow this path for hours.")
        print(" You somehow ended up at the same doorways that you encountered earlier.")

    elif choice == "No door":
        print(" You walk through the doorway and you see a faint light in the distance. You run to this light.")
        print("You discover a chest. You open the chest and find food and water in the chest!.")
        print("After eating, you continue to walk on and eventually find the Exit. ")
        print("You are free!")

    if dead:
        print("You have been eaten by the polar bear!")

    kill_if_dead(dead)



    pass
    # TODO Add your code here

####################################################################################################################


def team_14_adv():
    """
    Google Drive:   https://docs.google.com/document/d/1hVrBRHrbbXxCU74zEOyzQhHAzuYbB5O3eAddp6hoWnw/edit?usp=sharing
    Partner 1: Thy Nguyen
    Partner 2: Jenifer Fidelia
    :return:
    """


    global dead
    print("\nYou stumble into the woods. \nThere are three paths in front of you.\n")

    answer = input( "Which direction do you want to go? [North (N) /East (E) /West(W)] ")

    if answer.lower() == "north" or answer.lower() == "n":
        # Bad choice
        print("\n You are being chased by wolves.")
        sleep(1)
        print("Try to run away! Good luck!")
        sleep(1)
        safe = input("How long do want to run? [1-10]")
        try:
            a = int(safe)
            if int(safe) >= 7:
                print("\nThe wolves get tired of chasing you.")
            else:
                print("Oh no. They caught you.")
        except ValueError:
                print("\nOh no. They caught you.")
                dead = True
    elif answer.lower() == "west" or answer.lower() =="w":
        # Good choice
        print("You stumbled into a clearing. \nYou escape the woods.")

    elif answer.lower() == "east" or answer.lower() == "e":
        # Neutral choice
        print("The path leads you deeper into the woods. \nYou are now lost.")
    else:
        print("You can't think clearly. \nYou sit there for eternity.")
        dead = True

    if dead:
        kill_if_dead(dead)

    else:
        print("Keep going. You are still alive.")

############################################################################################################
def team_15_adv():
    """
    https://docs.google.com/document/d/1vE7M-wYzNrrqdWcMP472itZB_IBkW2anDfiU1cYA3Sk/edit?usp=sharing
    :return:
    """
    global dead

    # TODO Add your code here
#########################################################################################################
    # TODO Team 15
    ######################################################################
    # Author: Vidya Mastriyana, Alex Meadors
    # Username: mastriyanag, AlexMeadors
    #
    # Assignment: T04: Adventure in Gitland
    #
    # Purpose: To recreate a choose-your-own-adventure style game
    # by refactoring T01.
    #
    # Each "twist" in the story is from a different group. The resulting story
    # will either be incoherently random, or entertainingly "Mad Lib" like.
    # Either way, it should be fun!
    #
    # This new version will take advantage of functions, as well as
    # demonstrate the value of git as a tool for collaborating.
    ######################################################################
    # Acknowledgements:
    #   Original Author: Scott Heggen
    #
    ######################################################################
    messages = ["You come upon three doors.", "The one on the left has a light glowing from underneath.",
                "The one in the middle looks old and cracked.", "The one on the right is made of rusted metal."]
    for i in messages:
        print(i)
        sleep(delay * 3)

    direction = input("Which door will you choose? [Left, Middle, Right]")
    if direction.lower() == "right":
        # Good choice
        print(
            "You can barely see because the room is so dark and dusty. "
            "\nYou light your torch and see the room is filled to the brim with gold and jewels!.")
        sleep(delay * 4)
        print("Congratulations, you're rich!")
        choice = 0

    elif direction.lower() == "left":
        # Worst choice
        print(
            "You step through the door onto a thin sheet of ice. Below the ice, electricity arcs from one "
            "electric eel to another.\nYou turn quickly to walk back out the door and...")
        sleep(delay * 3)
        print("A golden dragon appears, he offers to help if and only if you can guess a number between 1 to 10")
        number = input("What number do you choose?")
        dragon_guess = False
        for i in range(5):
            if ord(number[0]) == (54 + i) or (ord(number[0]) == 49 and (ord(number[-1]) == 48) and (len(number) == 2)):
                dragon_guess = True
        if dragon_guess:
            print("He offers you a ride to safety, you come out with no major injuries.")
            choice = 2
    # Death

        else:
            print("The ice breaks! You are electrocuted while you are drowned... ")
            dead = True
            choice = 1
    else:
        # Boring choice
        messages = ["You open the middle door. Behind the door you find a long passage with stairs that seem to go up"
                    " forever.", "...", "....", ".....",
                    "You realize this tunnel is leading to nowhere and close your eyes, wishing for an escape."]
        for i in messages:
            print(i)
            sleep(delay * 2)
        choice = 2


    choicestrings = ["You collect your treasure and you move on to the next part of the cave",
                     "You die, try again to test your fate again!",
                "You open your eyes and you are in a new place. You are alive, but somewhat bored and disappointed."]

    print(choicestrings[choice])


    kill_if_dead(dead)

def check_if_exist(string):
    """
    Checks to see if the direction the user choose exists, and if it does it continues the story line.
    :param string:

    """
    global dead
    available_inputs = ["right", "left", "backwards", "forwards"]  # Directions the user can choose
    given_input = string.lower()

    if given_input in available_inputs:
        if given_input == "right":
            # Good Choice!
            print("You rush into the nearby trees for cover. There you find a mystical coconut that will slay the"
                  + " dragon.")
            sleep(delay)

        elif given_input == "forwards":
            # Bad Choice
            # print("You almost made a bad choice! The dragon hasn't seen you yet! Pick a number.")
            integer = int(
                input(
                    "You have made a bad choice! You have one more chance to avoid being burnt alive. Pick a "
                    + "number. [1,2]"))
            if integer == 1:
                print("You have saved yourself and spared yourself from the dragon!")
            elif integer == 2:
                print("You failed to make a better decision and gave the dragon time to get the BBQ sauce.")
                print("You have decided to run towards the dragon. The dragon scoffs and burns you to a crisp.")
                dead = True
                sleep(delay * 2)
                # Finished!
        else:
            # Oh...Bad Choice
            print("You just got eaten by man-eating roaches!")
            sleep(delay * 2)
            print("Try to pick another direction to follow next time!")
            dead = True
            # Finished the user has died!
    else:
        print("I do not exist, choose another direction...")
        ask()

def ask():
    """
    asks a question about which direction the user wants to go

    """
    x = input("Which direction would you like to go? [Right/Forwards/Backwards/Left]")
    check_if_exist(x)


def team_16_adv():

    ######################################################################################################
    # Author: Zyshavia Garrett and Abe Moreno

    # Username: garrettz and morenoa

    # Assignment: T04_Adventures in Gitland

    # Google Drive Link: smallyourl.appspot.com/B5odmlCDM

    # Acknowledgements:

    ######################################################################################################
    global dead                                                        # If user chooses wrong direction they will die

    ask()

    if dead:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button.")
        quit()


def team_17_adv():
    pass
    # TODO Add your code here


def team_18_adv():
    pass
    # TODO Add your code here


def team_19_adv():
    pass
    # TODO Add your code here


def team_20_adv():
    pass
    # TODO Add your code here


def main():
    """
    The main function, where the program starts.
    :return: None
    """

    user = start_story()
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv]
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
