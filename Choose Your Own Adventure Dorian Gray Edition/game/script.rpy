# @author Marina Semenova
# November 2019
# This file is for the game script

# define characters
define n = Character("Narrator")
define d = Character("Dorian")
define b = Character("Basil")
define h = Character("Harry")
define s = Character("Sibyl")

# define scenes
image bg_room = "bg_room.png"
image dorian_at_piano = "dorian_at_piano.png"
image dorian_standing = "dorian_standing.png"
image garden = "garden.png"
image theatre = "theatre.png"
image sibyl_performs = "sibyl_performs.png"
image backstage = "backstage.png"
image home_w_painting = "home_w_painting.png"
image harry_visits = "harry_visits.png"
image harry_visits_inside = "harry_visits_inside.png"
image basil_visit_1 = "basil_visit_1.png"
image home_w_tea = "home_w_tea.png"
image book = "book.png"
image home_w_book = "home_w_book.png"
image outside_w_basil = "outside_w_basil.png"
image inside_w_basil = "inside_w_basil.png"
image room_w_painting = "room_w_painting.png"
image revealed_painting = "revealed_painting.png"
image knife = "knife.png"
image rip_basil = "rip_basil.png"
image talk_w_harry = "talk_w_harry.png"
image room_w_painting_2 = "room_w_painting_2.png"
image body = "body.png"

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
        n "You are going to be taking on the role of Dorian Gray and you will have to make some very important choices for him!"
        d "The choices made affect the outcome of his life, so be careful what you choose!"
        n "Of course, you could just follow the plot of the book, but what fun is that?"
        n "In these choices, there will be the path that Dorian takes in the book, but there will be others that are not quite what happens, and others that are complete fiction."
        n "At each turning point in Dorian’s life, you will have 2 choices, and the outcome depends on the choice you choose."
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
            n "Furthermore, Dorian has both inner dialogue and actual speech, the second being indicated by single quotation marks."
            n "Now it’s time to seal the fate of Dorian Gray. *dun dun dunnnnnn*"
            scene dorian_at_piano
            n "Before we start, let’s get to know your character."
            n "Dorian, as seen in his first appearance, is a very boyish character; he is the image of innocence and purity. But at the end of the novel, he is as corrupt as people get."
            n "So what happened? How, and when, did he lose his innocence?"
            n "As you play this game there will be significant choices which either lead to Dorian’s demise, as in the novel, or, as this is a fictitious game, it may lead to new stories..."
            jump game
    # skip tutorial path
    label notut:
        n "Alrighty then! Welcome back! Came back to try to find new outcomes, eh?"
        jump game
    # gameplay
    label game:
        # canon scene 1
        scene dorian_standing
        n "Dorian is at Basil’s studio, having his painting done..."
        d "I have just met Harry, who is quite intriguing, and not the type to hang around Basil. The things he has talked about since I’ve come to know him..."
        d "Oh, I never even wanted this painting in the first place, and standing here is quite boring!"
        # canon choice 1
        menu:
            "Excuse yourself to hear more from Harry in the garden":
                jump canon1
        # canon event 1
        label canon1:
            d "‘Basil, I am tired of standing. I must go out and sit in the garden. The air is stifling here.’"
            # canon scene 2
            scene garden
            d "Ah yes, the things Harry has to say, they truly are remarkable! Yet, in a way, they are quite horrid. I can feel fresh influences at work within me..."
            b "‘I am waiting! Do come in. The light is quite perfect.’"
            d "There’s Basil calling us back in. I must talk to Harry once more at a later time!"
            # canon scene 3
            scene dorian_standing
            b "‘It is quite finished!’"
            d "Ah! It’s so beautiful and youthful! I’m so jealous of it! After what Harry said, I can see what he means when he says beauty matters above all else..."
            d "‘How sad it is! How sad it is!’"
            d "‘I shall grow old, and horrible, and dreadful. It will never be older than this particular day of June....’"
            d "‘If it were only the other way! If it were I who was to be always young, and the picture that was to grow old!’"
            d "‘For that – for that – I would give everything! Yes, there is nothing in the whole world I would not give! I would give my soul for that!’"
            h "‘You would hardly care for such an arrangement, Basil.’"
            b "‘I should object very strongly, Harry.’"
            h "‘Let us go to the theatre to-night.’"
            b "‘Don’t go to the theatre to-night, Dorian. Stop and dine with me.’"
            # canon choice 2
            menu:
                "‘I can’t.’":
                    jump canon2
        # canon event 2
        label canon2:
            d "‘I can’t, Basil.’"
            b "‘Why?’"
            d "‘Because I have promised Lord Henry Wotton to go with him.’"
            # canon scene 4
            scene theatre
            n "It has been a while since Dorian met Harry, and they have only bonded further in the time since then."
            n "Dorian has invited Harry and Basil to watch Sibyl, his new fiancé, perform in a play."
            d "I have just recently met Sibyl, whom I adore! She is an amazing actress, simply a born artist!"
            d "I have had the arms of Rosalind around me, and kissed Juliet on the mouth. Sibyl is the only thing I care about."
            d "The mere touch of Sybil Vane’s hand makes me forget Harry and all his wrong, fascinating, poisonous, delightful theories."
            d "I have invited Harry and Basil to see her skill!"
            # canon scene 5
            scene sibyl_performs
            n "Sibyl performs badly that evening, contrary to her previous performances..."
            # canon scene 6
            scene theatre
            n "After the performance..."
            h "‘She is quite beautiful, Dorian, but she can’t act. Let us go.’"
            d "‘I am going to see the play through. I am awfully sorry that I have made you waste an evening, Harry. I apologize to you both.’"
            b "‘My dear Dorian, I should think Miss Vane was ill. We will come some other night.’"
            d "‘I wish she were ill, but she seems to me to be simply callous and cold. She has entirely altered.’"
            d "‘Last night she was a great artist. This evening she is merely a commonplace, mediocre actress.’"
            # canon scene 7
            scene backstage
            d "How heartbroken I am! I must go to confront her about it!"
            s "‘How badly I acted to-night, Dorian!’"
            d "‘Horribly! Horribly! It was dreadful. Are you ill? You have no idea what it was. You have no idea what I suffered.’"
            s "‘Dorian... Dorian, you should have understood. But you understand now, don’t you?’"
            d "‘Understand what?’"
            s "‘Why I was so bad to-night. Why I shall always be bad. Why I shall never act well again.’"
            s "‘You had brought me something higher, something of which all art is but a reflection. You had made me understand what love really is.’"
            # canon choice 3
            menu:
                "Tell her she disappointed you":
                    jump canon3
        # canon event 3
        label canon3:
            d "‘You have killed my love.’"
            d "‘I wish I had never laid eyes upon you! You have spoiled the romance of my life.’"
            d "‘How little you can know of love, if you say it mars your art! Without your art you are nothing.’"
            d "‘I would have made you famous, splendid, magnificent. The world would have worshipped you, and you would have borne my name.’"
            d "‘What are you now? A third-rate actress with a pretty face.’"
            s "‘Kiss me again, my love. Don’t go away from me. I couldn’t bear it. Oh! don’t go away from me.’"
            d "‘I am going. I don’t wish to be unkind, but I can’t see you again. You have disappointed me.’"
            # canon scene 8
            scene home_w_painting
            d "..."
            d "Is there something different about Basil’s painting of me?"
            d "Ah! There is! The expression! It has altered! It is horribly apparent!"
            d "On no! I remember now... I had wished back at Basil’s studio that I would remain young and the portrait were to grow old!"
            d "That my beauty would be untarnished and that the canvas would bear the burden of my passions and sins!"
            d "The expressions looks cruel... Could it be caused by what I said to Sybil? It was her fault, but I do regret it..."
            d "It must be a mistake, merely an illusion wrought on the troubled senses. How foolish of me to think it had altered!"
            d "I will go back to Sibyl Vane, make her amends, marry her, try to love her again..."
            # canon scene 9
            scene harry_visits
            h "‘My dear boy, I must see you. Let me in at once. I can’t bear your shutting yourself up like this.’"
            # canon scene 10
            scene harry_visits_inside
            h "‘Didn’t you get my letter? I wrote to you this morning, and sent the note down, by my own man.’"
            d "‘Your letter? Oh, yes, I remember. I have not read it yet, Harry. I was afraid there might be something in it that I wouldn’t like. You cut life to pieces with your epigrams.’"
            h "‘Dorian, my letter – don’t be frightened – was to tell you that Sibyl Vane is dead.’"
            d "‘So I have murdered Sibyl Vane.’"
            h "‘Mourn for Ophelia, if you like. Put ashes on your head because Cordelia was strangled. Cry out against Heaven because the daughter of Brabantio died.’"
            h "‘But don’t waste your tears over Sibyl Vane. She was less real than they are.’"
            d "‘I am awfully obliged to you for all that you have said to me. You are certainly my best friend. No one has ever understood me as you have.’"
            # canon scene 11
            scene home_w_painting
            d "I will continue to live, I will leave behind Sybil’s death."
            d "The portrait will bear the burden of my shame, and I will live on, as youthful as ever, with infinite passions to pursue. But no one must see. I must cover it, and hide it away."
            # canon scene 12
            scene basil_visit_1
            n "Basil has come to visit Dorian and to console his friend about his beloved’s death, but alas, he needs no consoling as he has put if far, far behind him."
            n "But Basil has another thing on his mind..."
            b "‘Of course I won’t look at it if you don’t want me to, but, really, it seems rather absurd that I shouldn’t see my own work, especially as I am going to exhibit it in Paris in the autumn.’"
            b "‘I shall probably have to give it another coat of varnish before that, so I must see it some day, and why not to-day?’"
            d "‘To exhibit it! You want to exhibit it?’"
            b "‘Yes; I don’t suppose you will object to that.’"
            # canon choice 4
            menu:
                "Strongly object":
                    jump canon4
        label canon4:
            d "He must not exhibit it! I can’t let the world see into my soul!"
            b "‘Good-bye. I am sorry you won’t let me look at the picture once again.’"
            # canon scene 13
            scene home_w_painting
            d "The portrait must be hidden away at all costs. I cannot run such a risk of discovery again."
            # canon scene 14
            scene home_w_tea
            d "I have long neglected Harry’s messages, I guess I shall take a look..."
            # canon scene 15
            scene book
            n "Dorian's eyes fall upon a yellow book..."
            # canon choice 5
            menu:
                "Read it":
                    jump canon5
        # canon event 5
        label canon5:
            # canon scene 16
            scene home_w_book
            n "Dorian begins to turn the leaves of the novel, becoming absorbed in minutes."
            n "Things that he had dimly dreamed of were suddenly made real to him, and things of which he had never dreamed were gradually revealed."
            d "Oh, I am late for meeting Harry at the club! I lost myself in the book!"
            n "Harry, yet again, had to reveal me to myself. I’m sure I won’t be able to free myself from the influence of this book, and I won’t seek to. It is quite poisonous."
            # canon scene 17
            scene outside_w_basil
            n "Fow 18 years, Dorian has lived a sinful, pleasure-seeking lifestyle, completely obsessed with the yellow book Harry gave him and the painting that bore his sins."
            n "His reputation is tarnished because of the strange rumours and evil things that are said amongst the public, but many dismiss these stories because of how innocent he looks."
            n "He grew more and more enamoured of his own beauty, more and more interested in the corruption of his own soul."
            n "It was on the ninth of November, the eve of Dorian’s own thirty-eighth birthday, as he often remembered afterwards."
            n "He was walking home from dinner with Harry when suddenly..."
            b "‘Dorian! What an extraordinary piece of luck! Here we are at your door. Let me come in for a moment. I have something to say to you. It is about yourself.’"
            # canon scene 18
            scene inside_w_basil
            b "‘It is not much to ask of you, Dorian, and it is entirely for your own sake that I am speaking.’"
            b "‘I think it right that you should know that the most dreadful things are being said against you in London.’"
            d "‘I don’t wish to know anything about them. I love scandals about other people, but scandals about myself don’t interest me. They have not got the charm of novelty.’"
            b "‘I wonder do I know you? Before I could answer that, I should have to see your soul.’"
            # canon choice 6
            menu:
                "Show Basil the painting":
                    jump canon6
        # canon event 6
        label canon6:
            d "‘You shall see it yourself, to-night! Come: it is your own handiwork. Why shouldn’t you look at it?’"
            # canon scene 19
            scene room_w_painting
            d "‘So you think that it is only God who sees the soul, Basil? Draw that curtain back, and you will see mine.’"
            b "‘You are mad, Dorian, or playing a part.’"
            d "‘You won’t? Then I must do it myself.’"
            # canon scene 20
            scene revealed_painting
            b "Ahhhhhhhh"
            b "‘You told me you had destroyed it.’"
            d "‘I was wrong. It has destroyed me.’"
            b "‘‘‘Lead us not into temptation. Forgive us our sins. Wash away our iniquities.’’ Let us say that together.’"
            b "‘The prayer of your pride has been answered. The prayer of your repentance will be answered also.’"
            d "‘It is too late, Basil.’"
            b "‘It is never too late, Dorian.’"
            # canon choice 7
            menu:
                "Kill Basil":
                    jump canon7
        # canon event 7
        label canon7:
            d "Ah I hate him so much right now!"
            # canon scene 21
            scene knife
            d "..."
            # canon scene 22
            scene rip_basil
            d "Before I knew it, I had stabbed Basil."
            # canon scene 23
            scene talk_w_harry
            n "Dorian continues to live his life, but his conscience burdens him."
            n "After what happened to Sybil, Basil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
            h "‘There is no use your telling me that you are going to be good.’"
            d "‘No, Harry, I have done too many dreadful things in my life. I am not going to do any more.’"
            d "‘I am tired to-night, Harry. I sha’n’t go to the club. It is nearly eleven, and I want to go to bed early.’"
            h "‘Do stay. You have never played so well as to-night. There was something in your touch that was wonderful. It had more expression than I had ever heard from it before.’"
            d "‘It is because I am going to be good. I am a little changed already.’"
            # canon scene 24
            scene room_w_painting_2
            d "I regret my wish to have the portrait take the toll for my wrongdoings. I want to start anew, and change my ways for the better. Maybe the painting will revert itself..."
            d "..."
            d "I can see no change, save that in the eyes there was a look of cunning, and in the mouth the curved wrinkle of the hypocrite."
            d "The thing was still loathsome - more loathsome than before - and the scarlet dew that spotted the hand seemed brighter, and more like blood newly spilt."
            # canon choice 8
            menu:
                "Stab the painting":
                    jump canon8
        # canon event 8
        label canon8:
            n "Dorian takes the knife, the very same one that he had used to stab Basil, and thrusts it into the painting."
            scene body
            n "There was a cry heard, and a crash. The servants eventually find the source of the sound."
            n "When they entered, they found hanging upon the wall a splendid portrait of their master as they had last seen him, in all the wonder of his exquisite youth and beauty."
            n "Lying on the floor was a dead man, in evening dress, with a knife in his heart. He was withered, wrinkled, and loathsome of visage."
            n "It was not till they had examined the rings that they recognized who it was. In an attempt to be rid of the sins he has committed, Dorian ends up killing himself."
            jump outro
    # end of game
    label outro:
        scene bg_room
        n "Hey! You’ve completed the game! Thank you for playing! Hope you enjoyed the experience and learned something new!"
        return