# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vivian", color="#c8ffc8")
define n = Character("Natsuki", color="#e7a5e9")
define s = Character("Stelle", color="#a1bcee")

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

        "Stay with Natsuki"
        jump stay_with_natsuki

        "Leave with Stelle"
        jump leave_with_stelle

label stay_with_natsuki

    $ stayWithNatsuki = True

    v "No thanks, I'm going to stay with Natsuki."

    v "I don't feel like going outside right now."

    s "That's lame. Whatever, see you around I guess"

    "She leaves in a rush. Is she embarrassed?"

    n "Yay! I'm glad you decided to stay."

    n "I mean, this project would be pretty hard without you. You always keep me on track!"

    jump go_home

label leave_with_stelle

    $ leaveWithStelle = True

    v "Sorry Natsuki, I don't feel like studying. I'm going to leave with Stelle."

    n "Oh..."

    n "I mean it's fine. I didn't need you to study anyways. Go if you want, I don't care."

    "Natsuki seems down, but Stelle's never asked me to hangout before."

    s "Nice! I knew you weren't boring!"

    s "Hurry, let's run before the sun sets. I don't have a flashlight and my phone's about to die."

    v "Are you serious??"

    menu:
        "What will you do?"

        "Complement Stelle"
        jump complement_stelle

        "Say nothing"
        jump say_nothing

label complement_stelle

    jump continue_looking_at_the_stars

label say_nothing
    
    e "Never mind. There's no need to ruin this nice moment with her."

    jump continue_looking_at_the_stars

label continue_looking_at_the_stars

    jump go_home

label go_home

    menu:
        "Where will you go?"

        "Go to the literature club with Natsuki"
        jump literature_club

        "Go to Stelle's soccer game"
        jump soccer_game

label literature_club

    menu:
        "What poem should you write?"

        "Write a poem about love"
        jump love_poem

        "Write a poem about ice cream"
        jump ice_cream_poem

label love_poem

    jump walk_home_with_natsuki

label ice_cream_poem

    jump walk_home_with_natsuki

label walk_home_with_natsuki

    jump home_2

label soccer_game

    jump home_2

label home_2

    menu:
        "Who do you work with?"

        "Work with Natsuki"
        jump work_with_natsuki

        "Work with Stelle"
        jump work_with_stelle

label work_with_natsuki


label work_with_stelle

    menu:
        "What will you do?"

        "Lock in"
        jump lock_in

        "Listen to Stelle, we can do this later"
        jump listen_to_stelle

label lock_in

label listen_to_stelle

    menu:
        "What will you do?"

        "Throw Stelle under the bus"
        jump lock_in

        "Take the blame"
        jump listen_to_stelle



    # This ends the game.

    return
