define v = Character("Vivian", color="#60a860")
define n = Character("Natsuki", color="#a36fa5")
define s = Character("Stelle", color="#5981ca")
define z = Character("Ms. Zoru", color="#d16a6a")

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
default lockIn = False
default throwStelleUnderTheBus = False
default takeTheBlame = False

image side v embarrassed1 = Image("hoshi_school_embarrassed1.png", oversample = 2)
image side v embarrassed2 = Image("hoshi_school_embarrassed2.png", oversample = 2)
image side v sad = Image("hoshi_school_sad.png", oversample = 2)
image side v smile = Image("hoshi_school_smile.png", oversample = 2)
image side v surprised = Image("hoshi_school_surprised.png", oversample = 2)
image side v upset = Image("hoshi_school_upset.png", oversample = 2)

image n neutral = Image("Eve_Neutral.png", oversample = 2.1)
image n smile = Image("Eve_Smile.png", oversample = 2.1)
image n shy = Image("Eve_Shy.png", oversample = 2.1)
image n laugh = Image("Eve_Laugh.png", oversample = 2.1)
image n cry = Image("Eve_Cry.png", oversample = 2.1)
image n angry = Image("Eve_Angry.png", oversample = 2.1)
image n surprise = Image("Eve_Surprise.png", oversample = 2.1)

image s default = Image("Alice_Default.png", oversample = 1.7)
image s happy = Image("Alice_Happy.png", oversample = 1.7)
image s teasing = Image("Alice_Teasing.png", oversample = 1.7)
image s blush = Image("Alice_Blush.png", oversample = 1.7)
image s embarrassed = Image("Alice_Embarrassed.png", oversample = 1.7)
image s doubt = Image("Alice_Doubt.png", oversample = 1.7)
image s worried = Image("Alice_Worried.png", oversample = 1.7)

image bg street morning = "Street_Summer_Day.png"
image bg street evening = "Street_Summer_Evening.png"
image bg street stars = "Street_Summer_Stars.png"
image bg classroom day = "Classroom_Day.png"
image bg backstreet afternoon = "Backstreet_Summer_Afternoon.png"
image bg school = "Old_School.png"
#need library bg and soccer field

label start:

    scene bg street morning with dissolve
    show side v smile
    #this looks kinda weird 
    show n angry with moveinleft 
    with hpunch

    n "WAIT FOR ME!"  #(try to get the text to go like "meeeeeeeeeeeeeeeeee")
    
    "A high pitched voice squeals behind me."

    v "Natsuki, school is going to start in ten minutes. What are you so worried about?"

    show n neutral

    n "Ten minutes is cutting way too close. You should pick up the place so we can make it on time."

    v "Stop being a nerd. Ms. Zoru won't be pissed if we're a couple minutes late."
    
    show n angry

    n "Shut up! I don't care! Leave me alone then!"
    
    hide n angry with moveoutright

    "Damn, she just sprinted away."

    with dissolve

    #add more!

    "The library is loud today. It's probably because of exam season, but still."

    show n surprise with dissolve

    n "Are you even paying attention? Ms. Zoru is definitely going to assign a project or test or whatever soon and we have to be prepared."

    v "Sorry! But we don't even know what's coming up, why should I be worried now?"

    show n angry 

    "Natsuki groans."

    n "That's not the point, we should-"

    show n angry at left with move
    show s default at right with moveinright

    s "Natsuki, this is a library you know? You're screaming your head off like a tick bit you."

    v "I never took you as someone who studies, Stelle."

    show s doubt

    s "Ew no. I'm working as a library assistant!"

    n "Why the hell would they hire you and not me?? I come here way more often and I always turn my library books on time and-"

    show s teasing

    s "It's because you don't shut up. They also said that they hired me because I'm such a hard worker and they admire my skills."

    v "You sound like a liar."

    show s happy

    s "You sound like you don't want money."

    show s default

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

    show s doubt 
    
    s "That's lame. Whatever, see you around I guess."

    hide s doubt with moveoutright
    
    "She leaves in a rush. Is she embarrassed?"

    show n smile at center with move
    
    n "Yay! I'm glad you decided to stay."

    show n laugh
    
    n "I mean, you owe me, so obviously it would make sense that you should stay."
    
    v "I need a job like Stelle, then I wouldn't need to rely on you so much."
    
    n "Hey! I'm joking, you know? I don't mind paying for you."
    
    "She's right, I shouldn't care."
    
    "Or maybe?"
    
    "Nah."
    
    v "You should go back to studying since you're soo worried about that project."

    show n angry with hpunch
    
    n "I am! This is incredibly serious for my grades!"
    
    v "Hush Natsuki!"

    jump go_home

label leave_with_stelle:

    v "Sorry Natsuki, I don't feel like studying. I'm going to leave with Stelle."

    show n shy at left 
    
    n "Oh..."

    n "I mean it's fine. I didn't need you to study anyways. Go if you want, I don't care."

    hide n shy at left with moveoutleft
    
    "Natsuki seems down, but Stelle's never asked me to hangout before."

    #stelle moving is kinda weird
    show s blush at center with moveinright

    s "Nice!"
    
    with dissolve
    scene bg school
    show s teasing

    s "Not gonna lie, you looked super bored with Natsuki. Why do you hang with her so much anyways?"
    
    v "I mean, I knew her for a long time. I feel like I should branch out with more people, but I don't want to leave her behind."
    
    show s default

    "Stelle furrows her eyebrows for a second, but then just as quickly relaxes and smiles."
    
    s "Okay."

    show s blush
    
    s "Hurry, let's run before the sun sets! I don't have a flashlight and my phone's about to die."
    
    v "Are you serious??"
    
    "Stelle just laughs and runs faster. I don't want to be behind, so I rush to keep up."

    hide s blush with moveoutright
    with dissolve
    show s default

    "I follow her to an empty playground."
    
    "Wait, did I seriously waste my energy to go play on the swings with her?"

    show s teasing
    
    s "So...do you wanna play?"
    
    "I regret this so much."
    
    v "If I fail my class, I'm going to blame you library assistant."

    show s doubt
    
    s "Don't be so pissy. Of course this isn't the reason I got you to chase me here. Just be patient."
    
    v "Patience? Coming from you?"
   
    "She pretends to ignore me and heads to the swings. I just follow her."

    hide s doubt with moveoutright

    "Soon, it's getting dark out."

    show s happy
    
    v "Ugh, I'm getting tired."

    show s doubt
    
    s "Didn't I tell you to wait? C'mon, look up."
    
    "Wow, the sky is so clear here!"
    
    v "This is awesome, how did you know about this?"

    show s happy
    
    s "I skip here all the time."

    show s blush
    
    s "Once, I fell asleep and woke up to this. Pretty cool right?"
    
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

    show s embarrassed
    
    s "Hey! What made you say that?"

    show s happy
    
    s "Just focus on the sky."

    jump continue_looking_at_the_stars

label say_nothing:
    
    v "Never mind. There's no need to ruin this nice moment with her."

    jump continue_looking_at_the_stars

label continue_looking_at_the_stars:

    "We continue laying there for a while, but soon we have to leave."

    show s teasing

    s "Whoops, forgot I'm out of charge."
    
    v "Do you want me to walk home with you? You can use my phone as a flashlight."

    show s default
    
    s "Nah. I know how to get home safely."
    
    v "Ok! Thanks for taking me out here, it was really fun."

    show s blush
    
    s "No problem, but remember, you owe me next time! See you tomorrow, Vivian."

    hide s blush

    jump go_home

label go_home:

    "This was a pretty fun day. Hopefully tomorrow will be the same."

    scene bg street morning with dissolve

    "It's the next day."

    if stayWithNatsuki == True:
        v "Maybe I should hangout with Stelle today? But it was nice being with Natsuki yesterday..."
    elif leaveWithStelle == True:
        v "Maybe I should hangout with Natsuki today? But yesterday was pretty fun..."

    "I step out of the house and see someone familiar in the distance."

    show n neutral at right

    v "Hey Natsuki! Don't be in such a rush again!"

    if stayWithNatsuki == True:
        show n angry
        "Natsuki pouts and sprints faster. She yells at me not to be late, but like always, I pretend like I don't hear her."
        hide n angry with moveoutright
    elif leaveWithStelle == True:
        show n shy
        hide n shy with moveoutright
        "She's acting a little more distant. Is she still hung up over yesterday?"

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

    show n shy

    "Natsuki is nervously outside the club door, looking around. I was right."

    show n surprise
    
    n "Hey Vivian! Why are you so late? Stop doing that or it's going to become a habit."
    
    v "I needed to talk with my teacher. Anyways, what are we doing today?"
    
    show n laugh

    n "The club president was just saying that she thinks that we should be working on our writing skills more. We need to diversify by writing poems."
    
    v "What? That sounds boring!"

    show n angry with hpunch
    
    n "No it isn't! Poems are a unique way to present your ideas to the world."
    
    v "I don't have any ideas. I wanted to read manga with you again."

    show n smile
    
    n "Just make a poem first and we can!"
    
    hide n smile with moveoutright

    "Natsuki goes to get me some paper."

    menu:
        "What poem should you write?"

        "Write a poem about Natsuki":
            $ natsuki_love += 1
            jump love_poem

        "Write a poem about ice cream":
            $ iceCreamPoem == True
            $ natsuki_friend += 1
            jump ice_cream_poem

label love_poem:

    "I guess I'll just write a poem about Natsuki."

    show n neutral with moveinleft

    "Natsuki comes back with the supplies and I get to work."

    v "Ok, I'm done."

    "I present my poem to Natsuki, talking about her sweet personality and hardworking energy."
    
    show n shy
    
    n "H-hey! Why'd you write a poem about me!"
    
    v "It was the easiest to write. I mean, I know so much about you."
    
    n "You didn't have to write all those nice things though..."
    
    v "Well, it made for a better poem right?"
    
    n "I-it's not like I like it or anything!"

    show n angry
    
    n "I'm just happy you can finally read manga with me. Do you know how long you took?"
    
    "She seems flustered."

    jump walk_home_with_natsuki

label ice_cream_poem:

    "I'm pretty hungry. I'm just going to write a poem about ice cream."

    show n default with moveinleft

    "Natsuki comes back with the supplies and I get to work."
    
    v "Ok, I'm done."

    "I present my poem to Natsuki, talking about the different flavors of ice cream and whether cones or bowls are better."
    
    show n angry
    
    n "What the heck? What kinda poem was that?"
    
    v "Were you even paying attention? That's a poem about my love for ice cream."
    
    n "There's no way this helped your writing skills at all."

    show n neutral
    
    n "Now I'm craving ice cream too..."
    
    v "See? That's how moving my poem was."
    
    show n angry

    n "You're completely missing the point of this! Ugh, why even bother."

    show n shy
    
    n "Let's just read manga now."

    jump walk_home_with_natsuki

label walk_home_with_natsuki:

    show n surprise

    n "Oh, club's over! Time to clean up!"

    v "Why are you so energetic over this?"

    "Maybe writing poems isn't so bad."

    if iceCreamPoem == True:
        v "I'm so glad it's over. I'm hungry for ice cream."

        show n angry
        
        n "You definitely baited me with that poem."

        show n shy
        
        n "Whatever, let's just eat."
        
        v "Yay!!"

    jump home_2

label soccer_game:

    show s default
    
    v "She looks super surprised."

    show s blush

    s "WOAH!"
    
    if stayWithNatsuki == True:
        s "Vivian, what are you doing here?"

        v "I mean it's Friday, the soccer team always has their games today."

        show s embarrassed

        s "I can't lie, it's pretty random of you to pull up today but it's cool!"
    elif leaveWithStelle == True:
        s "Vivian, you actually showed up?" 

        v "You literally asked me to yesterday, why wouldn't I."

        show s embarrassed

        s "It was more like I blurted something out, but that's not the point. I'm happy you're here."

    show s teasing

    s "Watch me win, okay?"

    "Later.."

    v "WOW! You're a lot better at soccer than I thought!"
    
    show s doubt

    s "I win and that's the first thing you say?"
    
    v "Yep. I thought you were going to be the benchwarmer."
    
    s "Vivian, I'm exhausted. If you're not going to say anything nice, then please, shut up."
    
    if stayWithNatsuki == True:
        v "Ok, I'll respect the winning team"
    elif leaveWithStelle == True:
        v "Be patient, remember?" 

    v "You were pretty good out there."

    show s happy
    
    s "Thanks. I like winning."
    
    v "Want me to buy you something? You look pretty tired right now."

    show s blush
    
    s "YES."
    
    show s teasing

    s "I would kill for some fried chicken, sushi, and a liter of soda right now."
    
    v "HEY! You're the one with the job here, try to be more mindful of what you're ordering?"
    
    show s doubt
    
    s "Fine, I'll just go for the chicken today."
    
    v "Ok, but you're getting the cheapest one on the menu."

    show s default
    
    "I can tell Stelle's trying not to complain."
    
    "She better not. I could've spent this on skincare..."

    hide s default

    jump home_2

label home_2:

    #maybe add more flavor text
    if leaveWithStelle == False & soccerGame == True:
        "I never knew Stelle was so fun! But knowing her, I don't know if I would trust my grade with her."
    elif (stayWithNatsuki == False & literatureClub == True) or (stayWithNatsuki == True & literatureClub == True):
        "Natsuki is such a reliable friend, but there's no harm in trying out new teammates. Should I play it safe with our project?"

    "Walking to school.."

    if leaveWithStelle == True & soccerGame == True:
        "I don't see Natsuki out here. She seems to be leaving earlier and earlier. Hopefully I can catch her at school."
    else:
        show n neutral at right
        "Natsuki is waiting a couple blocks away from me, darting her eyes around."

        show n surprise at center with move 
        with hpunch

        "She sees me and waves her hand frantically."

        show n angry

        n "Why am I the one waiting? This sucked."
        
        n "You should've ran the second you saw me."
        
        v "I don't think I want to waste all my energy before lunch."
        
        n "I'm not buying you anymore food."
        
        v "You mean 'our' food, but I'll respect it."
        
        v "Just don't complain when I show up late again."
        
        n "You're so annoying!"
        
        hide n angry

    #add z

    "Afterschool.."
    
    "Man, this project is going to suck."
    
    "When I arrive to the library, I see Natsuki struggling to get a book."
    
    "It's way too tall for her to reach, but she's too embarrassed to get a stool."
    
    "Stelle is handling the help desk."
    
    " 'Handling'. I can see her phone screen brightening up her face. "

    menu:
        "Who do you work with?"

        "Work with Natsuki":
            $ natsuki_points += 1
            jump work_with_natsuki

        "Work with Stelle":
            $ stelle_points += 1
            jump work_with_stelle

label work_with_natsuki:

    "What am I thinking? Obviously Natsuki would be a better partner."
    
    "I grab the stool and plop it next to her feet."

    show n angry at center
    
    n "So much for discrete!"

    show n shy
    
    n "Can you just grab that book for me? I don't want to be caught using that creaky stool."
    
    v "You're so fussy!"
    
    "I grab it anyways and look at the cover."
    
    v "Is this what our project is going to be? A presentation about nature?"

    show n laugh
    
    n "Yep! Nature has a lot of interesting topics we can approach so we can add a lot of research about-"
    
    v "I'm not writing all that!"

    show n angry
    
    n "You're not writing anything! Wait-"

    show n surprise
    
    n "Did you come here so we could work on the project together?"
    
    v "Yeah, you're the best candidate."

    if leaveWithStelle == True & soccerGame == True:

        show n angry

        n "Was the other candidate Stelle? Why would you even consider her as an option?"
        
        n "We can work together but you have to actually work on the project, ok?" #(italics)
    else:
        show n laugh
        n "What other option would there be?" #(beaming)
        
        n "Let's make an awesome project!"

    v "Ok! But you're going to be the one that has to write all the in-depth research. It sounds boring."
    
    show n angry

    n "Ugh, fine."

    "One week later.."

    show n laugh with hpunch

    n "- and that's why the preservation of lush flora is vital to ensuring that our land can stay verdantly frondescence!"

    z "Well done girls! This was a great presentation about the importance of environmentalism, especially in your generation."
    
    show n smile
    
    n "Thanks, our research had a lot to do with-"
    
    "I have no idea what they're talking about."
    
    v "Thanks Ms. Zoru! We'll let the next group present now."
    
    "I shoot a look to Natsuki."

    show n shy
    
    "She pouts but agrees and we go back to our seats."

    hide n shy with moveoutright
    
    "Stelle's group presents next!"

    show s default at center with moveinleft
    
    "..."
    
    "It's really bad. There's no research done at all about their topic. I can see Ms. Zoru's face frown the entire time. Thank goodness I didn't choose her."

    hide s default

    "After class.."
    
    "I have nothing to do, so I'll just hang out with Natsuki."
    
    "Our project was actually pretty cool, even if I didn't really understand what she was saying."


    menu:
        "What will you do?"

        "Complement Natsuki":
            $ natsuki_love += 1
            jump complement_natsuki

        "Act normal":
            $ natsuki_friend += 1
            jump be_normal

label complement_natsuki:

    show n laugh

    v "You're so good at writing! I really liked how energetic you were when we were presenting."
    
    show n laugh
    
    n "Thanks Vivian."

    show n smile
    
    n "You did great too! The way you formatted the information made it easier to follow."
    
    v "It wasn't that hard. You just put everything in giant blocks of text. I couldn't see anything you put."
    
    show n angry
    
    n "Hey! It had a lot of important information and was needed so that-"
    
    v "Ack! Whatever then!"
    
    v "Anyways, after all this, we should celebrate!"

    show n neutral
    
    n "That's not a bad idea."

    show n surprise
    
    n "Wanna come to my house? We can bake cupcakes."

    show n shy
    
    n "Only if you want too! No pressure, I can bake them by myself."
    
    v "(laughs)"
    
    v "I like baking, c'mon, I'll actually run this time!"

    show n angry
    
    n "Wait up! You don't even have the key to my house!"

    hide n angry with moveoutright

    jump home_3

label be_normal:

    v "We did a great job presenting! Ms. Zoru has to give us an A on this."

    n "Of course she's going to give us an A. Did you not pay attention to her interest after we presented?"
    
    n "She asked us so many questions!"
    
    v "She asked us one."
    
    v "And you were the one that tried to keep talking for the rest of the class!"
    
    n "I was answering her question!"

    jump home_3

label work_with_stelle:

    "I go up to Stelle. I don't think she notices I'm in her face."

    show s happy
    
    v "Hello?"
    
    show s worried

    s "Ahh!"
    
    "She drops her phone in surprise."
    
    show s doubt

    s "Hey! If my screen cracks because of you, you owe me bad." #(italics, mad?)
    
    v "Aren't you supposed to be attentive on the job?"
    
    s "I am paying attention. My high score was on the line!"
    
    "I might be dead for this project. Oh well."
    
    v "I don't care about that!"
    
    v "I came here to ask you about something."

    "She looks at me suspiciously and raises her eyebrows."
    
    s "I think you know how to use the library computers."
    
    v "What? No I'm-"
    
    s "The dewey decimal system chart is right here. Find your genre and leave me alone."
    
    v "Can you quit it! I'm here to ask if you can be my partner for the project."

    if stayWithNatsuki == True & literatureClub == True:
        s "..."
        
        s "Why?"
        
        v "Why..not?"
        
        s "Wouldn't you wanna to partner up with Natsuki more?"
        
        v "I want to partner up with you. You seem more fun!" #(italics)

        show s default
        
        s "Um, cool!"
    else:
        show s default

        s "Oh sure!"

    show s embarrassed

    s "But I'm not really in the mood to do it right now."

    show s teasing
    
    s "Plus, isn't it due next week? I think we have time to hang around first."

    menu:
        "What will you do?"

        "Lock in":
            $ lockIn = True
            $ stelle_love += 1
            jump lock_in

        "Listen to Stelle, we can do this later":
            $ stelle_friend += 1
            jump listen_to_stelle

label lock_in:

    v "Wouldn't you like it if we finished the project now rather than do it all later?"
    
    v "You aren't even doing anything right now! Lets just start today."

    show s doubt
    
    s "Fine."

    show s default with hpunch
    
    "Stelle jumps over the help desk and hops to my side."
    
    v "???"
    
    v "Couldn't you use the swinging door instead?"

    show s teasing
    
    s "I lost the key to it so it won't swing anymore." #:)
    
    "I'm doomed."

    scene bg classroom day with dissolve

    "One week later.."

    show s blush
    
    s "-and that's why cats are better than dogs!"
    
    z "What an interesting project! I like the niche research you found."

    show s happy
    
    s "Thanks Ms. Zoru!"
    
    "We head back to our seats."

    hide s happy with moveoutright
    
    "Natsuki's group presents next!"

    show n neutral with moveinleft
    
    "..."
    
    "It's really boring. I think I fell asleep at the first slide. There's absolutely no pictures and it's just walls text on a white screen."
    
    "Ms. Zoru is the only one awake. At least they're going to get a good grade."

    scene bg school
    
    "After class..."
    
    v "That was pretty good! I'm surprised you didn't mess it up."

    show s doubt
    
    s "Me? You're the one who kept adding things after I thought we were done."

    show s default
    
    s "But I agree. I kinda need her to raise my grade."
    
    v "She totally will. She complemented us and everything!"

    show s blush
    
    "Stelle smiles."

    show s embarrassed
    
    s "Thanks for keeping me on track. If I get a B, I'll treat you to some fries."

    show s happy
    
    s "Wanna come with me? I got soccer practice now."

    v "Sure!"

    hide s happy

    jump home_3

label listen_to_stelle:

    v "You're right, we have a lot of time."
    
    v "What are you playing?"

    show s blush
    
    s "Oh it's-"
    
    "We spend the rest of her shift playing video games."
    
    "And the day after that. And maybe a bit more."

    scene bg classroom day with dissolve

    "One week later"
    
    "We end up doing our slides the day before it's due."
    
    "I'm so sleep derived."
    
    "I quickly review the presentation before we're up."
    
    "WAIT."
    
    "Did Stelle just copy and paste her slides?"
    
    "I look through the rest and they look horrible."
    
    "My grade is so screwed."

    
    v "Stelle! What the hell is this?"
    
    s "It's my slides."
    
    v "Did you literally just copy and paste everything? You don't write this professionally."
    
    s "Hey, this is a last minute project. There's no way I could fill up all those slides in time."
    
    v "Seriously? Ms. Zoru can tell this is fake. Everyone can tell this is fake."
    
    s "You're the one that wanted to partner with me!"
    
    "Before we can keep arguing, it's our turn to present."
    
    "Ms. Zoru's face is not looking good."
    
    z "Girls, I'd like for you to see me after class."
    
    "Ack!"

    "After class..."
    
    z "Your project is clearly not written by you."
    
    z "What do you have to say about that?"

    menu:
        "What will you do?"

        "Throw Stelle under the bus":
            $ throwStelleUnderTheBus = True
            jump throw_stelle_under_the_bus

        "Share the blame":
            $takeTheBlame = True
            $ stelle_friend += 1
            jump take_the_blame

label throw_stelle_under_the_bus:

    "Ms. Zoru, I have something to tell you."

    v "Stelle's slides were just copy and pasted from our sources. Mine are written by me."
    
    s "Hey!"
    
    v "It's true though. You were too lazy to do them, weren't you?"
    
    s "B-but it's not like I should take all the blame!"
    
    z "That's enough. I've decided to give Stelle a zero on this assignment since you clearly stated that it was her doing."
    
    s "You can't! I'm going to have to retake this class!"
    
    z "That's entirely on you. There's always summer school."
    
    "Stelle looks heartbroken."

    "Later.."
    
    s "What the hell Vivian?"
    
    s "You were the one that asked to work with me. You procrastinated too."
    
    s "I don't understand why you needed to rat me out like that."
    
    v "I didn't expect you to do that! I actually worked on my part."
    
    s "That's not the- ugh, what's the point."
    
    s "Whatever Vivian, thanks for making me retake her stupid class."
    
    "She stomps away."
    
    "That's not my fault, but whatever."

    jump home_3

label take_the_blame:

    v "I'm sorry Ms. Zoru. I was the one that suggested it since we waited last minute."
    
    z "I'm pretty disappointed in the both of you."
    
    z "Since you were honest about it, I'll let you redo the project with 10% off."
    
    s "Seriously?"
    
    z "Or not. You both could get a zero."
    
    s "NO! I mean, thanks, we'll redo the presentation."

    "Later.."
    
    s "Vivian, thank you so much."
    
    s "You didn't need to put yourself down too."
    
    v "It was kinda my fault too. We both procrastinated a lot on this, but you shouldn't have used copied in such an obvious way."
    
    s "Yea, I'm sorry about that."
    
    s "We should probably get started on the redo, right?"
    
    v "Definitely! Let's go to library before it closes."
    
    s "Okay!"

    jump home_3

label home_3:

    if throwStelleUnderTheBus == True:
        "Wow, that sucked."
    elif lockIn == True:
        "That was a lot better than I thought!"
    elif takeTheBlame == True:
        "Hopefully we can make it up to Ms. Zoru."
    else:
        "Natsuki is intense, but our project ended up great!"
        
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
