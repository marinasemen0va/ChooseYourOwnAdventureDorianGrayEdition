# @author Marina Semenova
# November 2019
# This file is for the game script

# define characters
define n = Character("Narrator", image="narrator")
define d = Character("Dorian", image="dorian")
define d_happy = Character("Dorian", image="dorian_happy")
define d_sad = Character("Dorian", image="dorian_sad")
define d_angry = Character("Dorian", image="dorian_angry")
define b = Character("Basil", image="basil")
define b_sad = Character("Basil", image="basil_sad")
define b_happy = Character("Basil", image="basil_happy")
define h = Character("Harry", image="harry")
define s = Character("Sibyl", image="sibyl")
define s_sad = Character("Sibyl", image="sibyl_sad")
define nd = Character("Narrator", image="narrator_n_dorian")
define ns = Character("Narrator", image="narrator_n_sibyl")

#character images
image side narrator = "narrator.png"
image side dorian = "dorian.png"
image side basil = "basil.png"
image side harry = "harry.png"
image side sibyl = "sibyl.png"
image side narrator_n_dorian = "narrator_n_dorian.png"
image side narrator_n_sibyl = "narrator_n_sibyl.png"
image side dorian_happy = "dorian_happy.png"
image side dorian_sad = "dorian_sad.png"
image side dorian_angry = "dorian_angry.png"
image side sibyl_sad = "sibyl_sad.png"
image side basil_sad = "basil_sad.png"
image side basil_happy = "basil_happy.png"

# define scenes
image bg_room = "bg_room.png"
image dorian_at_piano = "dorian_at_piano.png"
image dorian_standing = "dorian_standing.png"
image garden = "garden.png"
image theatre = "theatre.png"
image backstage = "backstage.png"
image home_w_painting = "home_w_painting.png"
image home_w_painting_clean = "home_w_painting.png"
image home_w_painting_covered = "home_w_painting_covered.png"
image outside_home = "outside_home.png"
image inside_home = "inside_home.png"
image home_w_tea = "home_w_tea.png"
image book = "book.png"
image outside_w_basil = "outside_w_basil.png"
image og_room_w_painting = "og_room_w_painting.png"
image knife = "knife.png"
image talk_w_harry = "talk_w_harry.png"
image club = "club.png"
image book_in_hand = "book_in_hand.png"
image room_w_painting = "room_w_painting.png"
image room_w_painting_covered = "room_w_painting_covered.png"

# game starts here
label start:
    # variables
    $ influence = False
    $ deal = False
    $ close = False
    $ basil_dead = False
    $ painting_gone = False
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
        n "The choices made affect the outcome of his life, so be careful what you choose!"
        n "Of course, you could just follow the plot of the book, but what fun is that?"
        n "In these choices, there will be the path that Dorian takes in the book, but there will be others that are not quite what happens, and others that are complete fiction."
        n "At each turning point in Dorian’s life, you will have 2 choices, and the outcome depends on the choice you make."
        n "Here, let’s try making a choice!"
        menu:
            "I’m sure excited for this!":
                jump hype
            "Let’s go!":
                jump go
        label hype:
            n "You chose ‘I’m sure excited for this!’ which is why I’m going to say ‘That’s great! Let’s go!’. If you had chosen ‘Let’s go!’, I would have replied ‘Alright, let’s go!’."
            jump afttest
        label go:
            n "You chose ‘Let’s go!’ which is why I’m going to say ‘Alright, let’s go!’. If you had chosen ‘I’m sure excited for this!’, I would have replied ‘That’s great! Let’s go!’."
            jump afttest
        label afttest:
            n "As you can see, your choices make a difference!"
            n "Furthermore, Dorian has both inner dialogue and actual speech, the latter being indicated by single quotation marks."
            n "Now it’s time to seal the fate of Dorian Gray. *dun dun dunnnnnn*"
            scene dorian_at_piano
            n "Before we start, let’s get to know your character."
            nd "Dorian, as seen in his first appearance, is a very boyish character; he is the image of innocence and purity. But at the end of the novel, he is as corrupt as people get."
            n "So what happened? How, and when, did he lose his innocence?"
            n "As you play this game there will be significant choices which either lead to Dorian’s demise, as in the novel, or, as this is a fictitious game, it may lead to new stories..."
            jump game
    # skip tutorial path
    label notut:
        n "Alrighty then! Welcome back! Came back to try to find new outcomes, eh?"
        jump game
    # gameplay
    label game:
        scene dorian_standing
        n "Dorian is at Basil’s studio, having his painting done..."
        d "I have just met Harry, who is quite intriguing, and not the type to hang around Basil. The things he has talked about since I’ve come to know him..."
        d "Oh, I never even wanted this painting in the first place, and standing here is quite boring!"
        menu:
            "Excuse yourself to hear more from Harry in the garden":
                $ deal = True
                $ influence = True
                d "‘Basil, I am tired of standing. I must go out and sit in the garden. The air is stifling here.’"
                scene garden
                d "Ah yes, the things Harry has to say, they truly are remarkable! Yet, in a way, they are quite horrid. I can feel fresh influences at work within me..."
                b_happy "‘I am waiting! Do come in. The light is quite perfect.’"
                d "There’s Basil calling us back in. I must talk to Harry once more at a later time!"
                scene dorian_standing
                b_happy "‘It is quite finished!’"
                scene og_room_w_painting
                d_sad "Ah! It’s so beautiful and youthful! I’m so jealous of it! After what Harry said, I can see what he means when he says beauty matters above all else..."
                d_sad "‘How sad it is! How sad it is!’"
                d_sad "‘I shall grow old, and horrible, and dreadful. It will never be older than this particular day of June....’"
                d_sad "‘If it were only the other way! If it were I who was to be always young, and the picture that was to grow old!’"
                d_sad "‘For that – for that – I would give everything! Yes, there is nothing in the whole world I would not give! I would give my soul for that!’"
                scene dorian_standing
                h "‘You would hardly care for such an arrangement, Basil.’"
                b_sad "‘I should object very strongly, Harry.’"
            "Keep sitting for Basil":
                n "Dorian stays, thus never hearing more from Harry, and therefore he is not overtaken by the painting’s beauty and youthfulness."
                n "After a while Basil announces..."
                b_happy "‘It is quite finished!’"
                d "‘Sorry, my friend, but that was dreadful! I was awfully bored standing here for so long! Although the work is very nice...’"
        h "‘Let us go to the theatre to-night.’"
        b "‘Don’t go to the theatre to-night, Dorian. Stop and dine with me.’"
        menu:
            "‘I can’t.’":
                $ close = True
                $ influence = True
                d "‘I can’t, Basil.’"
                b_sad "‘Why?’"
                d "‘Because I have promised Lord Henry Wotton to go with him.’"
                if deal == False:
                    scene home_w_painting_clean
                    n "One night, Dorian returns from the club, where he was with Harry..."
                    n "Basil's painting has been sent to its rightful owner..."
                    d_sad "Ah! It’s so beautiful and youthful! I’m so jealous of it! After what Harry said, I can see what he means when he says beauty matters above all else..."
                    d_sad "How sad it is! How sad it is!"
                    d_sad "I shall grow old, and horrible, and dreadful. It will never be older than this particular day of June...."
                    d_sad "If it were only the other way! If it were I who was to be always young, and the picture that was to grow old!"
                    d_sad "For that – for that – I would give everything! Yes, there is nothing in the whole world I would not give! I would give my soul for that!"
                scene theatre
                n "It has been a while since Dorian met Harry, and they have only bonded further in the time since then."
                n "Dorian has invited Harry and Basil to watch Sibyl, his new fiancé, perform in a play."
                d_happy "I have just recently met Sibyl, whom I adore! She is an amazing actress, simply a born artist!"
                d_happy "I have had the arms of Rosalind around me, and kissed Juliet on the mouth. Sibyl is the only thing I care about."
                d_happy "The mere touch of Sybil Vane’s hand makes me forget Harry and all his wrong, fascinating, poisonous, delightful theories."
                d_happy "I have invited Harry and Basil to see her skill!"
                ns "Sibyl performs badly that evening, contrary to her previous performances..."
                n "After the performance..."
                h "‘She is quite beautiful, Dorian, but she can’t act. Let us go.’"
                d_sad "‘I am going to see the play through. I am awfully sorry that I have made you waste an evening, Harry. I apologize to you both.’"
            "‘Yes, I’ll stay.’":
                d "‘Yes, I’ll stay.’"
                b_happy "‘That's great, Dorian!’"
                h "I will take my leave then."
                b "Goodbye Harry."
                n "Dorian chose not to go with Harry, therefore preventing further bonding and influence."
                scene theatre
                n "A while after Dorian's encounter with Harry, Dorian has invited Basil to watch Sibyl, his new fiancé, perform in a play."
                d_happy "I have just recently met Sibyl, whom I adore! She is an amazing actress, simply a born artist!"
                d_happy "I have had the arms of Rosalind around me, and kissed Juliet on the mouth. Sibyl is the only thing I care about."
                if influence == True:
                    d_happy "The mere touch of Sybil Vane’s hand makes me forget Harry and all his wrong, fascinating, poisonous, delightful theories."
                d_happy "I have invited Basil to see her skill!"
                ns "Sibyl performs badly that evening, contrary to her previous performances..."
                n "After the performance..."
                b "‘Dorian...’"
                d_sad "‘Yes, I know she acted poorly. I am going to see the play through. I am awfully sorry that I have made you waste an evening, Basil.’"
        b "‘My dear Dorian, I should think Miss Vane was ill. We will come some other night.’"
        d_sad "‘I wish she were ill, but she seems to me to be simply callous and cold. She has entirely altered.’"
        d_sad "‘Last night she was a great artist. This evening she is merely a commonplace, mediocre actress.’"
        b_sad "‘Don’t talk like that about any one you love, Dorian. Love is a more wonderful thing than Art.’"
        if close:
            h "‘They are both simply forms of imitation, but do let us go.’"
        scene backstage
        d_sad "How heartbroken I am! I must go to confront her about it!"
        s "‘How badly I acted to-night, Dorian!’"
        d_sad "‘Horribly! Horribly! It was dreadful. Are you ill? You have no idea what it was. You have no idea what I suffered.’"
        s "‘Dorian... Dorian, you should have understood. But you understand now, don’t you?’"
        d_sad "‘Understand what?’"
        s "‘Why I was so bad to-night. Why I shall always be bad. Why I shall never act well again.’"
        s "‘You had brought me something higher, something of which all art is but a reflection. You had made me understand what love really is.’"
        if influence == False:
            if close == False:
                d_happy "‘Ah my love, I guess it is for the better. You know how I loved your art, but I love you more. Let us leave this place...’"
                s "‘Let's!’"
                scene bg_room
                n "Dorian and Sibyl marry, and live a happy life."
                n "This is the path in which Dorian had essentially no significant influence from Harry, which means he did not make the deal with the painting or bond with Harry."
                jump outro
        menu:
            "Tell her she disappointed you":
                d "‘You have killed my love.’"
                d "‘I wish I had never laid eyes upon you! You have spoiled the romance of my life.’"
                d "‘How little you can know of love, if you say it mars your art! Without your art you are nothing.’"
                d "‘I would have made you famous, splendid, magnificent. The world would have worshipped you, and you would have borne my name.’"
                d "‘What are you now? A third-rate actress with a pretty face.’"
                s_sad "‘Kiss me again, my love. Don’t go away from me. I couldn’t bear it. Oh! don’t go away from me.’"
                d "‘I am going. I don’t wish to be unkind, but I can’t see you again. You have disappointed me.’"
            "Forgive her, and love her":
                d "‘Ah, you know how I loved your art! But no matter, you are still the same as when I first met you... Perhaps you’ll be able to pick the art again...’"
                scene club
                if close:
                    n "Later, at the club..."
                    d_happy "‘I have made amends with Sibyl! She told me she loved me and that’s why she acted badly! We are to marry soon!’"
                    h "‘Are you sure about this, Dorian? She looked such a child, and seemed to know so little about acting.’"
                else:
                    n "One night, Dorian runs into Harry at the club..."
                    d_happy "‘Hello Harry! Long time no see! Have you heard? I am engaged to Sibyl Vane!’"
                    h "‘Really? I didn't think that you would do such a thing. Perhaps I was wrong...’"
                    d "‘What do you mean?’"
                    h "‘The real drawback to marriage is that it makes one unselfish. And unselfish people are colourless. They lack individuality.’"
                    h "‘Are you sure about this, Dorian?’"
                menu:
                    "‘Yes, I'm sure. I love her.’":
                        d_happy "‘Yes, I'm sure. I love her.’"
                        h "‘Alright, be it on your head.’"
                        scene bg_room
                        n "Dorian and Sibyl marry, and live a happy life."
                        n "In this path, Dorian does undergo influence and does make the deal with the painting, but in the end he chooses to love Sibyl."
                        n "He has shown a love for Sibyl which transcends his love for pleasures and sin, which results in him taking her as his loving wife."
                        n "Though, he is, in theory, immortal..."
                        jump outro
                    "‘No, Harry. I'm not.’":
                        d "‘No, Harry. I'm not.’"
                        h "‘Ah, I knew you were not so foolish as to marry!’"
                        d "‘I believe you're right. I don't think the married life is for me...’"
                        d "‘Ah, I must break it off! I need to see her immediately! She’s at the theatre to-night! I will go now!’"
                        d "‘Thank you, Harry for helping me see the error in my ways!’"
                        scene backstage
                        d "‘Sibyl!’"
                        s "‘Yes, love?’"
                        d "‘I wish I had never laid eyes upon you! You have spoiled the romance of my life.’"
                        d "‘How little you can know of love, if you say it mars your art! Without your art you are nothing.’"
                        d "‘I would have made you famous, splendid, magnificent. The world would have worshipped you, and you would have borne my name.’"
                        d "‘What are you now? A third-rate actress with a pretty face.’"
                        s_sad "‘Kiss me again, my love. Don’t go away from me. I couldn’t bear it. Oh! don’t go away from me.’"
                        d "‘I am going. I don’t wish to be unkind, but I can’t see you again. You have disappointed me.’"
        scene home_w_painting
        d "..."
        d "Is there something different about Basil’s painting of me?"
        d "Ah! There is! The expression! It has altered! It is horribly apparent!"
        d "On no! I remember now... I had wished back at Basil’s studio that I would remain young and the portrait were to grow old!"
        d "That my beauty would be untarnished and that the canvas would bear the burden of my passions and sins!"
        d "The expressions looks cruel... Could it be caused by what I said to Sybil? It was her fault, but I do regret it..."
        d "It must be a mistake, merely an illusion wrought on the troubled senses. How foolish of me to think it had altered!"
        d "I will cover it for now and examine it later."
        d "I will go back to Sibyl Vane, make her amends, marry her, try to love her again..."
        scene inside_home
        n "Next morning..."
        if close:
            scene outside_home
            h "‘My dear boy, I must see you. Let me in at once. I can’t bear your shutting yourself up like this.’"
            scene inside_home
            h "‘Didn’t you get my letter? I wrote to you this morning, and sent the note down, by my own man.’"
            d "‘Your letter? Oh, yes, I remember. I have not read it yet, Harry. I was afraid there might be something in it that I wouldn’t like. You cut life to pieces with your epigrams.’"
            h "‘Dorian, my letter – don’t be frightened – was to tell you that Sibyl Vane is dead.’"
            d_sad "‘So I have murdered Sibyl Vane.’"
            h "‘Mourn for Ophelia, if you like. Put ashes on your head because Cordelia was strangled. Cry out against Heaven because the daughter of Brabantio died.’"
            h "‘But don’t waste your tears over Sibyl Vane. She was less real than they are.’"
            d "‘I am awfully obliged to you for all that you have said to me. You are certainly my best friend. No one has ever understood me as you have.’"
            scene home_w_painting
            d "I will continue to live, I will leave behind Sybil’s death."
            d "The portrait will bear the burden of my shame, and I will live on, as youthful as ever, with infinite passions to pursue. But no one must see. I must cover it, and hide it away."
            scene inside_home
            n "Basil has come to visit Dorian and to console his friend about his beloved’s death, but alas, he needs no consoling as he has put if far, far behind him."
            n "But Basil has another thing on his mind..."
        else:
            scene inside_home
            n "Basil has come to visit Dorian and to console his friend about his beloved’s death, of which Dorian does not know..."
            scene outside_home
            b_sad "‘Dorian! Let me in, Dorian!’"
            scene inside_home
            b_sad "‘I am so glad I have found you, Dorian. I passed a dreadful evening, half afraid that one tragedy might be followed by another.’"
            b_sad "‘I read of it quite by chance in a late edition of The Globe, that I picked up at the club.’"
            b_sad "‘I came here at once, and was miserable at not finding you. I can’t tell you how heartbroken I am about the whole thing. I know what you must suffer.’"
            d "‘Dear Basil, what are you talking about?’"
            b_sad "‘Oh? Haven't you heard?’"
            d "‘Heard what?’"
            b_sad "‘Sibyl is dead, Dorian.’"
            d_sad "‘Dead! Sibyl dead! It is not true! It is a horrible lie! How dare you say it?’"
            b_sad "‘It is quite true.’"
            d_sad "‘So I have murdered Sibyl Vane.’"
            b_sad "‘Now, that is not true at all! It is done. Grieve, but do not blame yourself.’"
        b "‘On another note, let me see the painting I did of you. It is the best thing I have ever done.’"
        d_angry "‘No, Basil, I do not wish you to see it.’"
        b "‘Of course I won’t look at it if you don’t want me to, but, really, it seems rather absurd that I shouldn’t see my own work, especially as I am going to exhibit it in Paris in the autumn.’"
        b "‘I shall probably have to give it another coat of varnish before that, so I must see it some day, and why not to-day?’"
        d "‘To exhibit it! You want to exhibit it?’"
        b "‘Yes; I don’t suppose you will object to that.’"
        menu:
            "Strongly object":
                d_angry "He must not exhibit it! I can’t let the world see into my soul!"
                b "‘Good-bye. I am sorry you won’t let me look at the picture once again.’"
                scene home_w_painting
                d "The portrait must be hidden away at all costs. I cannot run such a risk of discovery again."
            "Let Basil take the painting":
                d "Here's my chance to get that thing away from me..."
                scene home_w_painting_covered
                d "‘Alright! Take it! I want to be rid of it!’"
                b "‘I didn't know you hated it so!’"
                scene home_w_painting_covered
                b "..."
                b "‘What is wrong with the expression??? I don't remember painting you to look so... cruel.’"
                d "‘One day you introduced me to a friend of yours, who explained to me the wonder of youth, and you finished a portrait of me that revealed to me the wonder of beauty.’"
                d "‘In a mad moment, that, even now, I don’t know whether I regret or not, I made a wish, perhaps you would call it a prayer...’"
                b_sad "‘I remember it! Oh, how well I remember it!’"
                d "‘It is too late, Basil. The deal is made.’"
                b_sad "‘It is never too late, Dorian.’"
                menu:
                    "Kill Basil":
                        $ basil_dead = True
                        d_angry "He cannot know the truth! I will be ruined! I hate him!"
                        n "Dorian grabs a knife from breakfast setting at the table he was sitting at, and before he knew it he had stabbed Basil..."
                        scene home_w_painting
                        d "The portrait must be hidden away at all costs. I cannot run such a risk of discovery again."
                        d "And the body must be dealt with..."
                    "Tell Basil the truth":
                        $ painting_gone = True
                        d_sad "‘Oh, how I wish that were true...’"
                        b_sad "‘Of course it is, Dorian!’"
                        b "‘Here, I will take the painting, but I won't display it. Don't worry, your secret is safe with me...’"
        if close:
            scene home_w_tea
            d "I have long neglected Harry’s messages, I guess I shall take a look..."
        else:
            scene club
            n "One night, Dorian runs into Harry at the club..."
            h "‘Dorian, my boy! How long has it been since we last saw each other? Too long, I believe.’"
            d "‘Yes, too long... How have you been?’"
            h "‘Oh, just the usual. I heard about your fiancé. Sibyl Vane, was it?’"
            d "‘Yes, very unfortunate...’"
            h "‘No, I don't believe so.’"
            d "‘Harry!’"
            h "‘I assure you that in any case the whole thing would have been an absolute failure.’"
            d "‘Still, she's dead.’"
            h "‘No matter now... Say, I have this book that I think you would enjoy. Care to borrow it?’"
            scene book_in_hand
            menu:
                "Take the book":
                    scene club
                    d "‘Alright, if you think so...’"
                    scene home_w_tea
                    n "Sometime later..."
                "Decline the offer":
                    scene club
                    d "‘No, thank you. I'm quite busy these days anyways.’"
                    d "‘See you around, Harry. I must get on now.’"
                    if basil_dead == False:
                        if painting_gone:
                            scene bg_room
                            n "At this point, Dorian no longer has the painting, and he has rejected Harry’s attempts to influence him."
                            n "He lives him life without constantly indulging his pleasures and sinful tendencies, the painting forgotten."
                            n "His relationship with Basil is not ruined as he trusted him enough to reveal the truth and did not murder him, and he is not in any close relationship with Harry."
                            n "Though, he is, in theory, immortal..."
                            jump outro
                    n "By not taking and reading the book, which is very closely linked with the cause of his scandalous lifestyle, Dorian avoids said lifestyle, although the painting is still an influence."
                    n "His life is now more of a mimic of Harry’s; still involving indulgences, yet not as horrid."
                    n "Dorian continues to live his life, but his conscience burdens him."
                    if basil_dead:
                        n "After what happened to Sybil, Basil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
                    else:
                        n "After what happened to Sybil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
                    jump painting_death
        scene book
        n "Dorian's eyes fall upon a yellow book..."
        menu:
            "Read it":
                scene home_w_tea
                n "Dorian begins to turn the leaves of the novel, becoming absorbed in minutes."
                n "Things that he had dimly dreamed of were suddenly made real to him, and things of which he had never dreamed were gradually revealed."
                d "Oh, I am late for meeting Harry at the club! I lost myself in the book!"
                n "Harry, yet again, had to reveal me to myself. I’m sure I won’t be able to free myself from the influence of this book, and I won’t seek to. It is quite poisonous."
            "Leave it":
                scene home_w_tea
                if basil_dead == False:
                    if painting_gone:
                        scene bg_room
                        n "At this point, Dorian no longer has the painting, and he has rejected Harry’s attempts to influence him."
                        n "He lives him life without constantly indulging his pleasures and sinful tendencies, the painting forgotten."
                        if close == False:
                            n "His relationship with Basil is not ruined as he trusted him enough to reveal the truth and did not murder him, and he is not in any close relationship with Harry."
                        else:
                            n "His relationship with Basil is not ruined as he trusted him enough to reveal the truth and did not murder him."
                            n "Furthermore, by not reading the book, he has effectively rejected Harry's attempts to influence him and to bond with him."
                        n "Though, he is, in theory, immortal..."
                        jump outro
                n "By not reading the book, which is very closely linked with the cause of his scandalous lifestyle, Dorian avoids said lifestyle, although the painting is still an influence."
                n "His life is now more of a mimic of Harry’s; still involving indulgences, yet not as horrid."
                if close:
                    jump harry_talk
                else:
                    n "Dorian continues to live his life, but his conscience burdens him."
                    if basil_dead:
                        n "After what happened to Sybil, Basil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
                    else:
                        n "After what happened to Sybil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
                    jump painting_death
        if basil_dead == True:
            jump painting_death
        else:
            scene outside_w_basil
            n "For 18 years, Dorian has lived a sinful, pleasure-seeking lifestyle, completely obsessed with the yellow book Harry gave him and the painting that bore his sins."
            n "His reputation is tarnished because of the strange rumours and evil things that are said amongst the public, but many dismiss these stories because of how innocent he looks."
            n "He grew more and more enamoured of his own beauty, more and more interested in the corruption of his own soul."
            n "It was on the ninth of November, the eve of Dorian’s own thirty-eighth birthday, as he often remembered afterwards."
            n "He was walking home from dinner with Harry when suddenly..."
            b "‘Dorian! What an extraordinary piece of luck! Here we are at your door. Let me come in for a moment. I have something to say to you. It is about yourself.’"
            scene inside_home
            b_sad "‘It is not much to ask of you, Dorian, and it is entirely for your own sake that I am speaking.’"
            b_sad "‘I think it right that you should know that the most dreadful things are being said against you in London.’"
            d "‘I don’t wish to know anything about them. I love scandals about other people, but scandals about myself don’t interest me. They have not got the charm of novelty.’"
            if painting_gone == True:
                b_sad "‘I saw the painting change! I thought you said you would stop with the sin!’"
                d_angry "‘And then Harry saved me from such a boring lifestyle!’"
                b_sad "‘Remember what I told all that time ago? How it's not too late? It still isn't, Dorian. Please, listen to me...’"
                menu:
                    "Kill Basil":
                        $ basil_dead = True
                        d_angry "Ah, I hate him so much right now!"
                        scene knife
                        d_angry "..."
                        scene inside_home
                        n "Before he knew it, he had stabbed Basil."
                        n "Dorian continues his sinful lifestyle, and as Dorian has not destroyed the painting, he is therefore, in theory, immortal..."
                        jump outro
                    "Don't kill him":
                        d_sad "‘I believe you...’"
                        scene bg_room
                        n "At this point, Dorian no longer has the painting, and he has rejected his lifestyle."
                        n "He lives him life without constantly indulging his pleasures and sinful tendencies, the painting forgotten."
                        n "Basil moves on to Paris, where he takes a studio and shuts himself up till he has finished a great picture he has in his head, just as he intended to do."
                        n "Basil also salvaged his relationship with Dorian as he helped him find his way again."
                        if close == False:
                            n "Furthermore, he is not in any close relationship with Harry."
                        else:
                            n "Furthermore, by choosing to abandon his lifestyle, he is no longer influenced by Harry."
                        n "Though, he is, in theory, immortal..."
                        jump outro
            else:
                b_sad "‘I wonder do I know you? Before I could answer that, I should have to see your soul.’"
                menu:
                    "Show Basil the painting":
                        d "‘You shall see it yourself, to-night! Come: it is your own handiwork. Why shouldn’t you look at it?’"
                        scene room_w_painting_covered
                        d "‘So you think that it is only God who sees the soul, Basil? Draw that curtain back, and you will see mine.’"
                        b_sad "‘You are mad, Dorian, or playing a part.’"
                        d "‘You won’t? Then I must do it myself.’"
                        scene room_w_painting
                        b "!!!"
                        b_sad "‘You told me you had destroyed it.’"
                        d "‘I was wrong. It has destroyed me.’"
                        b_sad "‘‘‘Lead us not into temptation. Forgive us our sins. Wash away our iniquities.’’ Let us say that together.’"
                        b_sad "‘The prayer of your pride has been answered. The prayer of your repentance will be answered also.’"
                        d "‘It is too late, Basil.’"
                        b_sad "‘It is never too late, Dorian.’"
                        menu:
                            "Kill Basil":
                                $ basil_dead = True
                                d_angry "Ah, I hate him so much right now!"
                                scene knife
                                d_angry "..."
                                scene room_w_painting
                                n "Before he knew it, he had stabbed Basil."
                                if close:
                                    jump harry_talk
                                else:
                                    scene room_w_painting_covered
                                    n "Dorian continues to live his life, but his conscience burdens him."
                                    n "After what happened to Sybil, Basil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
                                    jump painting_death
                            "Tell Basil the truth":
                                $ painting_gone = True
                                d_sad "‘Oh, how I wish that were true...’"
                                b_sad "‘Of course it is, Dorian!’"
                                b "‘Here, I will take the painting, but I won't display it. Don't worry, your secret is safe with me...’"
                                scene bg_room
                                n "At this point, Dorian no longer has the painting, and he has rejected his lifestyle."
                                n "He lives him life without constantly indulging his pleasures and sinful tendencies, the painting forgotten."
                                n "Basil moves on to Paris, where he takes a studio and shuts himself up till he has finished a great picture he has in his head, just as he intended to do."
                                n "Basil also salvaged his relationship with Dorian as he helped him find his way again."
                                if close == False:
                                    n "Furthermore, he is not in any close relationship with Harry."
                                else:
                                    n "Furthermore, by choosing to abandon his lifestyle, he is no longer influenced by Harry."
                                n "Though, he is, in theory, immortal..."
                                jump outro
                    "Listen to Basil":
                        d_sad "‘There's no need. I can tell you it is corrupt.’"
                        d_sad "‘The rumours are all true, and there are some that you most likely haven't even heard...’"
                        d_sad "‘I think it's too late for me...’"
                        b_sad "‘Of course it isn't, Dorian!’"
                        b_sad "‘This is Harry's doing, not yours. Just, please, find yourself again.’"
                        b_sad "‘You can be the man you were before you met him, back when you were in my studio everyday.’"
                        d_sad "‘You really think so?’"
                        b_happy "‘Yes, Dorian...’"
                        n "Basil moves on to Paris, where he takes a studio and shuts himself up till he has finished a great picture he has in his head, just as he intended to do."
                        n "Basil also salvaged his relationship with Dorian as he helped him find his way again."
                        n "While Dorian stops his sinful lifestyle after the confrontation with Basil, his past deeds still haunt him."
                        n "The painting is no longer a strong influence, but it is not completely gone from Dorian’s memory..."
                        if close:
                            jump harry_talk
                        else:
                            d "One day, Dorian goes to examine the painting..."
                            jump painting_death
        label harry_talk:
            scene talk_w_harry
            n "Dorian continues to live his life, but his conscience burdens him."
            if basil_dead:
                n "After what happened to Sybil, Basil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
            else:
                n "After what happened to Sybil, James, and others he had corrupted, he was beginning to feel guilty. When finally..."
            h "‘There is no use your telling me that you are going to be good.’"
            d "‘No, Harry, I have done too many dreadful things in my life. I am not going to do any more.’"
            d "‘I am tired to-night, Harry. I sha’n’t go to the club. It is nearly eleven, and I want to go to bed early.’"
            h "‘Do stay. You have never played so well as to-night. There was something in your touch that was wonderful. It had more expression than I had ever heard from it before.’"
            d "‘It is because I am going to be good. I am a little changed already.’"
        label painting_death:
            scene room_w_painting
            d "I regret my wish to have the portrait take the toll for my wrongdoings. I want to start anew, and change my ways for the better. Maybe the painting will revert itself..."
            d "..."
            d_sad "I can see no change, save that in the eyes there was a look of cunning, and in the mouth the curved wrinkle of the hypocrite."
            d_sad "The thing was still loathsome - more loathsome than before - and the scarlet dew that spotted the hand seemed brighter, and more like blood newly spilt."
            menu:
                "Stab the painting":
                    n "Dorian takes the knife, the very same one that he had used to stab Basil, and thrusts it into the painting..."
                    scene bg_room
                    n "There was a cry heard, and a crash. The servants eventually find the source of the sound."
                    n "When they entered, they found hanging upon the wall a splendid portrait of their master as they had last seen him, in all the wonder of his exquisite youth and beauty."
                    n "Lying on the floor was a dead man, in evening dress, with a knife in his heart. He was withered, wrinkled, and loathsome of visage."
                    n "It was not till they had examined the rings that they recognized who it was. In an attempt to be rid of the sins he has committed, Dorian ends up killing himself."
                    jump outro
                "Leave the painting be":
                    scene bg_room
                    if basil_dead == True:
                        n "Dorian continues his sinful lifestyle, and as Dorian has not destroyed the painting, he is therefore, in theory, immortal..."
                    else:
                        n "Dorian stays alive, and thanks to Basil he does not pursue his sinful passions anymore. Though, he is, in theory, immortal..."
                    jump outro
    # end of game
    label outro:
        n "Hey! You’ve completed the game! Thank you for playing! Hope you enjoyed the experience and learned something new!"
        return
