# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("Vivian", color="#77cc77")
define n = Character("Natsuki", color="#c589c7")
define s = Character("Stelle", color="#95afdf")
define z = Character("Ms. Zoru", color="#cf6e6e")

default natsuki_points = 0
default stelle_points = 0
default natsuki_friend = 0
default natsuki_love = 0
default stelle_friend = 0
default stelle_love = 0
default stayWithNatsuki = False
default leaveWithStelle = False
default literatureClub = False
default iceCreamPoem = False
default soccerGame = False
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
    n "WAIT FOR ME!"  #(try to get the text to go like "meeeeeeeeeeeeeeeeee")
    
    "A high pitched voice squeals behind me."

    v "Natsuki, school is going to start in ten minutes. What are you so worried about?"

    n "Ten minutes is cutting way too close. You should pick up the place so we can make it on time."

    v "Stop being a nerd. Ms. Zoru won't be pissed if we're a couple minutes late."

    n "Shut up! I don't care! Leave me alone then!"

    "Damn, she just sprinted away."

    #add more

    "The library is loud today. It's probably because of exam season, but still."

    n "Are you even paying attention?? Ms. Zoru is definitely going to assign a project or test or whatever soon and we have to be prepared."

    v "Sorry! But we don't even know what's coming up, why should I be worried now?"

    n "Groans."

    n "That's not the point, we should-"

    s "Natsuki, this is a library you know? You're screaming your head off like a tick bit you."

    v "I never took you as someone who studies, Stelle."

    s "Ew no. I'm working as a library assistant!"

    n "Why the hell would they hire you and not me?? I come here way more often and I always turn my library books on time and-"

    s "It's because you don't shut up. They said that they hired me because I'm such a hard worker and they admire my skills."

    v "You sound like a liar."

    s "You sound like you don't want money."

    s "Anyways, my shift is almost over and you don't like you're doing anything productive. Vivian, do you wanna hang out with me?"

    menu:
        "Who will you choose?"

        "Stay with Natsuki":
            $ stayWithNatsuki = True
            $ natsuki_points += 1
            jump stay_with_natsuki

        "Leave with Stelle":
            $ leaveWithStelle = True
            $ stelle_points += 1
            jump leave_with_stelle

label stay_with_natsuki:

    v "No thanks, I'm going to stay with Natsuki."
    
    v "I don't feel like going outside right now."
    
    s "That's lame. Whatever, see you around I guess"
    
    "She leaves in a rush. Is she embarrassed?"
    
    n "Yay! I'm glad you decided to stay."
    
    n "I mean, you owe me, so obviously it would make sense that you should stay."
    
    v "I need a job like Stelle, then I wouldn't need to rely on you so much."
    
    n "Hey! I'm joking, you know? I don't mind paying for you."
    
    "She's right, I shouldn't care."
    
    "Or maybe?"
    
    "Nah."
    
    v "You should go back to studying since you're soo worried about that project."
    
    n "I am! This is incredibly serious to my grades!"
    
    v "Hush Natsuki!"

    jump go_home

label leave_with_stelle:

    v "Sorry Natsuki, I don't feel like studying. I'm going to leave with Stelle."
    
    n "Oh..."
    
    n "I mean it's fine. I didn't need you to study anyways. Go if you want, I don't care."
    "Natsuki seems down, but Stelle's never asked me to hangout before."
    
    s "Nice!"
    
    s "Not gonna lie, you looked super bored with Natsuki. Why do you hang with her so much anyways?"
    
    v "I mean, I knew her for a long time. I feel like I should branch out with more people, but I don't want to leave her behind."
    
    "Stelle furrows her eyebrows for a second, but then just as quickly relaxes and smiles."
    
    s "Okay."
    
    s "Hurry, let's run before the sun sets! I don't have a flashlight and my phone's about to die."
    
    v "Are you serious??"
    
    "Stelle just laughs and runs faster. I don't want to be behind, so I rush to keep up."
    
    "I follow her to an empty playground."
    
    "Wait, did I seriously waste my energy to go play on the swings with her?"
    
    s "So...do you wanna swing?"
    
    "I regret this so much."
    
    v "If I fail my class, I'm going to blame you library assistant."
    
    s "Don't be so pissy. Of course this isn't the reason I got you to chase me here. Just be patient."
    
    v "Patience? Coming from you?"
   
    "She pretends to ignore me and heads to the swings. I just follow her."

    "Soon, it's getting dark out."
    
    v "Ugh, I'm getting tired."
    
    s "Didn't I tell you to wait? C'mon, look up."
    
    "Wow, the sky is so clear here."
    
    v "This is awesome, how did you know about this?"
    
    s "I skip here all the time. Once, I fell asleep and woke up to this. Pretty cool right?"
    
    "I've never seen her in this light before. Were her eyes always this pretty?"

    menu:
        "What will you do?"

        "Complement Stelle":
            $ stelle_love += 1
            jump complement_stelle

        "Say nothing":
            $ stelle_friend += 1
            jump say_nothing

label complement_stelle:

    v "You know, I've never noticed how pretty your eyes are."
    
    s "Hey! What made you say that?"
    
    s "Just focus on the sky."

    jump continue_looking_at_the_stars

label say_nothing:
    
    v "Never mind. There's no need to ruin this nice moment with her."

    jump continue_looking_at_the_stars

label continue_looking_at_the_stars:

    "We continue laying there for a while, but soon we have to leave."

    s "Whoops, forgot I'm out of charge."
    
    v "Do you want me to walk home with you? You can use my phone as a flashlight."
    
    s "Nah. I know how to get home safely."
    
    v "Ok! Thanks for taking me out here, it was really fun."
    
    s "No problem, but remember, you owe me next time! See you tomorrow, Vivian."

    jump go_home

label go_home:

    "This was a pretty fun day. Hopefully tomorrow will be the same."

    "It's the next day."

    if stayWithNatsuki == True:
        v "Maybe I should hangout with Stelle today? But it was nice being with Natsuki yesterday..."
    elif leaveWithStelle == True:
        v "Maybe I should hangout with Natsuki today? But yesterday was pretty fun..."

    "I step out of the house and see someone familiar in the distance."

    v "Hey Natsuki! Don't be in such a rush again!"

    if stayWithNatsuki == True:
        "Natsuki pouts and sprints faster. She yells at me not to be late, but like always, I pretend like I don't hear her."
    elif leaveWithStelle == True:
        "She's acting a little more distant. Why is she still hung up over yesterday?"

    "Later..."
    
    "School is over!"
    
    "Hm, I know that Natsuki is waiting for me in the literature club, but Stelle also has a soccer game today."

    menu:
        "Where will you go?"

        "Go to the literature club with Natsuki":
            $ literatureClub == True
            $ natsuki_points += 1
            jump literature_club

        "Go to Stelle's soccer game":
            $ soccerGame == True
            $ stelle_points += 1
            jump soccer_game

label literature_club:

    "I shouldn't ditch Natsuki. She's probably waiting for me."

    "Natsuki is nervously outside the club door, looking around. I was right."
    
    n "Hey Vivian! Why are you so late? Stop doing that or it's going to become a habit."
    
    v "I needed to talk with my teacher. Anyways, what are we doing today?"
    
    n "The club president was just saying that she thinks that we should be working on our writing skills more. We need to diversify by writing poems."
    
    v "What? That sounds boring!"
    
    n "No it isn't! Poems are a unique way to present your ideas to the world."
    
    v "I don't have any ideas. I wanted to read manga with you again."
    
    n "Just make a poem first and we can!"
    
    "Natsuki goes to get me some paper."

    menu:
        "What poem should you write?"

        "Write a poem about Natsuki":
            $ natsuki_love += 1
            jump love_poem

        "Write a poem about ice cream":
            $ natsuki_friend += 1
            jump ice_cream_poem

label love_poem:

    "I guess I'll just write a poem about Natsuki."

    "Natsuki comes back with the supplies and I get to work."

    v "Ok, I'm done."

    "I present my poem to Natsuki, talking about her sweet personality and hardworking energy."
    
    n "H-hey! Why'd you write a poem about me."
    
    v "It was the easiest to write. I mean, I know so much about you."
    
    n "You didn't have to write all those nice things though..."
    
    v "Well, it made for a better poem right?"
    
    n "I-it's not like I like it or anything!"
    
    n "I'm just happy you can finally read manga with me. Do you know how long you took?"
    
    "She seems flustered."

    jump walk_home_with_natsuki

label ice_cream_poem:

    "I'm pretty hungry. I'm just going to write a poem about ice cream."

    "Natsuki comes back with the supplies and I get to work."
    
    v "Ok, I'm done."

    "I present my poem to Natsuki, talking about the different flavors of ice cream and whether cones or bowls are better."
    
    n "What the heck? What kinda poem was that?"
    
    v "Were you even paying attention? That's a poem about my love for ice cream."
    
    n "There's no way this helped your writing skills at all."
    
    n "Now I'm craving ice cream too..."
    
    v "See? That's how moving my poem was."
    
    n "You're completely missing the point of this! Ugh, why even bother."
    
    n "Let's just read manga now."

    jump walk_home_with_natsuki

label walk_home_with_natsuki:

    n "Oh, club's over! TIme to clean up!"

    v "Why are you so energetic over this.."

    "Maybe writing poems isn't so bad."

    if 
    v "I'm so glad it's over. I'm hungry for ice cream."
    n "You definitely baited me with that poem."
    n "Let's just eat."
    v "Yay!!"


    jump home_2

label soccer_game:
    
    v "She looks super surprised."

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

    "Later.."

    v "WOW! You're a lot better at soccer than I thought!"
    
    s "I win and that's the first thing you say?"
    
    v "Yep. I thought you were going to be the benchwarmer "
    
    s "Vivian, I'm exhausted. If you're not going to say anything nice, then please, shut up."
    
    if stayWithNatsuki == True:
        v "Be patient, remember?" 
    elif leaveWithStelle == True:
        v "Ok, I'll respect the winning team"

    v "You were pretty good out there."
    
    s "Thanks. I like winning."
    
    v "Want me to buy you something? You look pretty tired right now."
    
    s "YES."
    
    s "I would kill for some fried chicken, sushi, and a liter of soda right now."
    
    v "HEY! You're the one with the job here, try to be more mindful of what you're ordering?"
    
    s "Fine, I'll just go for the chicken today."
    
    v "Ok, but you're getting the cheapest one on the menu."
    
    "I can tell Stelle's trying not to complain."
    
    "She better not. I could've spent this on skincare..."

    jump home_2

label home_2:
    
    #add z

    #maybe add more flavor text
    if leaveWithStelle == True & soccerGame == True:
        "I never knew Stelle was so fun! But knowing her, I don't know if I would trust my grade with her."
    elif stayWithNatsuki == True & literature_club == True:
        "Natsuki is such a reliable friend, but there's no harm in trying out new teammates. Should I play it safe with our project?"

    menu:
        "Who do you work with?"

        "Work with Natsuki":
            $ natsuki_points += 1
            jump work_with_natsuki

        "Work with Stelle":
            $ stelle_points += 1
            jump work_with_stelle

label work_with_natsuki:

    menu:
        "What will you do?"

        "Complement Natsuki":
            $ natsuki_love += 1
            jump complement_natsuki

        "Be normal":
            $ natsuki_friend += 1
            jump be_normal

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
            $ stelle_friend += 1
            jump lock_in

        "Listen to Stelle, we can do this later":
            $ stelle_friend += 1
            jump listen_to_stelle

label lock_in:

    jump home_3

label listen_to_stelle:

    "Ms. Zoru, I have something to tell you."

    menu:
        "What will you do?"

        "Throw Stelle under the bus":
            $ throwStelleUnderTheBus = True
            jump throw_stelle_under_the_bus

        "Take the blame":
            $ stelle_love += 1
            jump take_the_blame

label throw_stelle_under_the_bus:

    jump home_3

label take_the_blame:

    jump home_3

label home_3:

    if throwStelleUnderTheBus == True:
        "Wow, that sucked."
    #else:
        
    if throwStelleUnderTheBus == True:
        jump natsuki_friendship_ending
    if natsuki_points > stelle_points:
        if natsuki_love > natsuki_friend:
            jump natsuki_yuri_ending
        else:
            jump natsuki_friendship_ending
    elif stelle_points > natsuki_points:
        if stelle_love > stelle_friend:
            jump stelle_yuri_ending
        else:
            jump stelle_friendship_ending

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
