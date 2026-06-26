# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vivian", color="#84dd84")
define n = Character("Natsuki", color="#e7a5e9")
define s = Character("Stelle", color="#a1bcee")
define z = Character("Ms. Zoru", color="#e07979")

default natsuki_friend = 0
default natsuki_love = 0
default stelle_friend = 0
default stelle_love = 0
default stayWithNatsuki = False
default leaveWithStelle = False
default throwStelleUnderTheBus = False


# The game starts here.

label start:

    #I'm going to use this as reference!

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "Who will you choose?"

        "Stay with Natsuki":
            jump stay_with_natsuki
            $ stayWithNatsuki = True
            $ natsuki_friend += 1
            $ natsuki_love += 1

        "Leave with Stelle":
            jump leave_with_stelle
            $ leaveWithStelle = True
            $ stelle_friend += 1
            $ stelle_love += 1

label stay_with_natsuki:

    v "No thanks, I'm going to stay with Natsuki."

    v "I don't feel like going outside right now."

    s "That's lame. Whatever, see you around I guess"

    "She leaves in a rush. Is she embarrassed?"

    n "Yay! I'm glad you decided to stay."

    n "I mean, this project would be pretty hard without you. You always keep me on track!"

    jump go_home

label leave_with_stelle:

    v "Sorry Natsuki, I don't feel like studying. I'm going to leave with Stelle."

    n "Oh..."

    n "I mean it's fine. I didn't need you to study anyways. Go if you want, I don't care."

    "Natsuki seems down, but Stelle's never asked me to hangout before."

    s "Nice! I knew you weren't boring!"

    s "Hurry, let's run before the sun sets. I don't have a flashlight and my phone's about to die."

    v "Are you serious??"

    menu:
        "What will you do?"

        "Complement Stelle":
            jump complement_stelle
            $ stelle_love += 1

        "Say nothing":
            jump say_nothing
            $ stelle_friend += 1

label complement_stelle:

    jump continue_looking_at_the_stars

label say_nothing:
    
    e "Never mind. There's no need to ruin this nice moment with her."

    jump continue_looking_at_the_stars

label continue_looking_at_the_stars:

    jump go_home

label go_home:

    if stayWithNatsuki == True:
        v "Maybe I should hangout with Stelle today? But it was nice being with Natsuki yesterday..."
    elif leaveWithStelle == True:
        v "Maybe I should hangout with Natsuki today? But yesterday was pretty fun..."

    if stayWithNatsuki == True:
        "She's acting a little more distant. Why is she still hung up over yesterday?"

    menu:
        "Where will you go?"

        "Go to the literature club with Natsuki":
            jump literature_club
            $ natsuki_friend += 1
            $ natsuki_love += 1

        "Go to Stelle's soccer game":
            jump soccer_game
            $ stelle_friend += 1
            $ stelle_love += 1

label literature_club:

    menu:
        "What poem should you write?"

        "Write a poem about love":
            jump love_poem
            $ natsuki_love += 1

        "Write a poem about ice cream":
            jump ice_cream_poem
            $ natsuki_friend += 1

label love_poem:

    jump walk_home_with_natsuki

label ice_cream_poem:

    jump walk_home_with_natsuki

label walk_home_with_natsuki:

    jump home_2

label soccer_game:
    
    v "She looks super surprised"

    s "WOAH!"
    
    if stayWithNatsuki == True:
        s "Vivian, what are you doing here?"

        v "I mean it's Friday, the soccer team always has their games today."

        s "I can't lie, it's pretty random of you to pull up today but it's cool"
    elif leaveWithStelle == True:
        s "Vivian, you actually showed up?" 

        v "You literally asked me to yesterday, why wouldn't I."

        s "It was more like I blurted something out, but that's not the point. I'm happy you're here."

    s "Watch me win, okay?"

    jump home_2

label home_2:

    menu:
        "Who do you work with?"

        "Work with Natsuki":
            jump work_with_natsuki
            $ natsuki_friend += 1
            $ natsuki_love += 1

        "Work with Stelle":
            jump work_with_stelle
            $ stelle_friend += 1
            $ stelle_love += 1

label work_with_natsuki:

    menu:
        "What will you do?"

        "Complement Natsuki":
            jump complement_natsuki
            $ natsuki_love += 1

        "Be normal":
            jump be_normal
            $ natsuki_friend += 1

label complement_natsuki:

    v "You're so good at writing! I really liked how energetic you were when we were presenting."
    n "U-um, thanks."

    jump home_3

label be_normal:

    v "We did a great job presenting! Ms. Zoru has to give us an A on this."

    jump home_3

label work_with_stelle:

    menu:
        "What will you do?"

        "Lock in":
            jump lock_in

        "Listen to Stelle, we can do this later":
            jump listen_to_stelle

label lock_in:

    jump home_3

label listen_to_stelle:

    "Ms. Zoru, I have something to tell you."

    menu:
        "What will you do?"

        "Throw Stelle under the bus":
            jump throw_stelle_under_the_bus

        "Take the blame":
            jump take_the_blame

label throw_stelle_under_the_bus:

    $ throwStelleUnderTheBus = True

    jump home_3

label take_the_blame:

    jump home_3

label home_3:

    if throwStelleUnderTheBus == True:
        "Wow, that sucked."
    else:
        

label natsuki_friendship_ending:

    "These past few days have been hectic."

    "I'm glad I could spend a lot of it with my good friend, Natsuki."
    
    "Despite her grudges, she's a really sweet person."

    "Stelle and I talk sometimes, but it's mostly if I approach her first."

    "At least I can go get ice cream with Natsuki today!"

    return


label natsuki_yuri_ending:

    "These past few days have been hectic."

    "I'm glad I could spend a lot of it with my girlfriend, Natsuki."

    "Despite her grudges, she's a really sweet person."

    "Stelle and I don't talk much. I can feel her glancing at me, but when I look back she turns away."

    "It's kinda weird, but I'm super excited to share an ice cream with Natsuki today!"

    return

label stelle_friendship_ending:

    "These past few days have been hectic."

    "I'm glad I could spend a lot of it with my good friend, Stelle."

    "Even though we bicker a lot, it's fun hanging out with her."

    "Natsuki and I still walk together to school, but I don't really talk to her when we're there."

    "I'm excited to see Stelle in a soccer match again, I'll be cheering her on the entire time!"

    return

label stelle_yuri_ending:

    "These past few days have been hectic."

    "I'm glad I could spend a lot of it with my girlfriend, Stelle."

    "Even though we bicker a lot, it's fun hanging out with her."
    
    "Natsuki and I sometimes walk together to school, but I don't talk to her much anytime else."

    "I'm excited to go out with Stelle again. I hear the stars are going to look amazing tonight!"

    return

    # This ends the game.

    #return
