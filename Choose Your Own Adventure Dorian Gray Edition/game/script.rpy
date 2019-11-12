# @author Marina Semenova
# November 2019
# This file is for the game script

# define characters
define n = Character("Narrator")
define d = Character("Dorian")
define b = Character("Basil")
define h = Character("Harry")

# define scenes
image bg_room = "bg_room.png"
image dorian_at_piano = "dorian_at_piano.png"
image dorian_standing = "dorian_standing.png"

# game starts here
label start:
    # show a bg
    scene bg_room
    # intro
    menu:
        n "Hello, and welcome to Choose Your Own Adventure: Dorian Gray Edition. Would you like a tutorial or are you a returning player ready to get into the action?"
        "I would like a tutorial.":
            jump tut
        "No, I’m good.":
            jump notut
    # the tutorial path
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
            n "You chose “I’m sure hyped for this!” which is why I’m going to say “That’s great! Let’s go!”. If you had chosen “Let’s go!”, I would have replied “Alright, let’s go!”."
            jump afttest
        label go:
            n "You chose “Let’s go!” which is why I’m going to say “Alright, let’s go!”. If you had chosen “I’m sure hyped for this!”, I would have replied “That’s great! Let’s go!”."
            jump afttest
        label afttest:
            n "As you can see, your choices make a difference!"
            n "Now it’s time to seal the fate of Dorian Gray. *dun dun dunnnnnn*"
            scene dorian_at_piano
            n "Before we start, let’s get to know your character."
            n "Dorian, as seen in his first appearance, is a very boyish character; he is the image of innocence and purity. But *spoiler* at the end of the novel, he is as corrupt as people get. So what happened? How, and when, did he lose his innocence?"
            n "As you play this game there will be significant choices which either lead to Dorian’s demise, as in the novel, or, as this is a fictitious game, it may lead to new stories…"
            jump game
    # skip tutorial path
    label notut:
        n "Alrighty then! Welcome back! Came back to try to find new outcomes, eh?"
        jump game
    # gameplay
    label game:
        scene dorian_standing
        n "Code game time boi!"
    # end of game
    return
