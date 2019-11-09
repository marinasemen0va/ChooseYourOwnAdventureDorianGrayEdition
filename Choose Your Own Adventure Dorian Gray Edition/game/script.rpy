# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrator")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    menu:
        n "Hello, and welcome to Choose Your Own Adventure: Dorian Gray Edition. Would you like a tutorial or are you a returning player ready to get into the action?"
        "I would like a tutorial.":
            jump tut
        "No, I’m good.":
            jump notut
    label tut:
        n "So, here’s a little tutorial on how this game is going to work!"
        n "You are going to be taking on the role of Dorian Gray and you will have to make some very important choices for him! The choices made affect the outcome of his life, so be careful what you choose! Of course, you could just follow the plot of the book, but what fun is that?"
        n "In these choices, there will be the path that Dorian takes in the book, but there will be others that are not quite what happens, and others that are complete fiction. At each turning point in Dorian’s life, you will have 2 choices, and the outcome depends on the choice you choose."
        n "Here, let’s try making a choice!"
        menu:
            "I’m sure hyped for this!":
                jump hype
            "Let’s go!":
                jump go
        label hype:
            n "You chose “I’m sure hyped for this!” which is why I’m going to say “That’s great! Let’s go!”.  If you had chosen “Let’s go!”, I would have replied “Alright, let’s go!”."
            jump afttest
        label go:
            n "You chose “Let’s go!” which is why I’m going to say “Alright, let’s go!”. If you had chosen “I’m sure hyped for this!”, I would have replied “That’s great! Let’s go!”."
            jump afttest
        label afttest:
            n "As you can see, your choices make a difference!"
            n "Now it’s time to seal the fate of Dorian Gray. *dun dun dunnnnnn*"
            jump game
    label notut:
        n "Alrighty then! Welcome back! Came back to try to find new outcomes, eh?"
        jump game
    label game:
        n "Code game time boi!"

    # This ends the game.

    return
