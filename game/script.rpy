#all the initializations are in variables_init
#roommate = Carlos/Carla
#dormmate = Justin/Jasmine
#I CHANGED THE NAMES OF THE SUB CHARS

init python:
    in_story = False

    def set_gender(selected_gender):
        persistent.gender = selected_gender #this is only for the quiz ui
        global current_gender
        global pronoun_referred
        global pronoun_belonging
        global pronoun_respect
        global pronoun_object
        global roommate
        global dormmate
        global crush
        global crush_referred
        global crush_belonging
        global crush_respect
        global crush_object 
        current_gender = selected_gender

        if selected_gender == "male":
            pronoun_referred = "he"
            pronoun_belonging = "his"
            pronoun_object = "him"
            pronoun_respect = "mister"
            roommate = "Carlos"
            dormmate = "Justin"
            crush = "Sophia"
            crush_referred = "she"
            crush_belonging = "her"
            crush_object = "her"
            crush_respect = "miss"

        else:
            pronoun_referred = "she"
            pronoun_belonging = "her"
            pronoun_object = "her"
            pronoun_respect = "miss"
            roommate = "Carla"
            dormmate = "Jasmine"  
            crush = "Matt"
            crush_referred = "he"
            crush_belonging = "his"
            crush_object = "him"
            crush_respect = "mister"


screen gender_choose:
    image "bg mirror1"
    imagebutton auto "male_%s.png" action Function(lambda: set_gender("male")), Jump("start_2"):
        xalign 0.17
        yalign 0.28

    imagebutton auto "female_%s.png" action Function(lambda: set_gender("female")), Jump("start_2"):
        xalign 0.84
        yalign 0.28

label start:
    with fade
    scene bg disclaimer with Pause(5)
    scene bg frontday

    n "It's been 2 long years since the pandemic wreaked havoc upon the world,
    economies were put on hold, people were confined within their homes, jobs were put on hold and so school transitioned
    from face-to-face classes to online classes."
    n "And now that the pandemic has settled down everything went back to normal,
    so did classes and for some this opened a new chapter in their lives where they get to be in a new environment and meet new people."

    scene bg calendar with Pause(5)
    scene bg alarmclock with Pause(5)
    scene bg roomday

    show mom happy
    mom "Honey, it's time to wake up!"
    # Character is preparing to stand, looks one’s self in the mirror
    # Proceeds to choosing of name and gender

    hide mom
    show bg mirror with dissolve
    "..."

    $ mc = renpy.input("What is your name?", default="Alex", length=32).capitalize()
    $ mc = mc.strip()
    if mc == "":
        $ mc = "Alex"

    "What is your gender?"
    call screen gender_choose with dissolve

label start_2:
    scene bg room
    show mc neutral_casual
    mc "Yes, ma. I'll be there."

    scene bg table with dissolve
    show mc neutral_casual at left with dissolve
    mc "Ma, what day is it?"
    show mom neutral at right with dissolve
    mom "Well, it's Monday, honey."
    mc "No, like, what's the day of the month is it?"
    mom "Oh, it is June 14. Why? Has something come up?"
    mc "It's nothing, it just feels like there's something I need to do today."
    mc "Ah, nevermind. I'll just enjoy this time of the year, having a rest after a long year."

    # insert text messaging

    hide mom

    nvl_narrator "Gregory is now online!"
    g_nvl "Yo, [mcname]! Have you seen the result?"
    mc_nvl confused_casual "What result are you talking about?"

    g_nvl "The BUCET result! It's already out. Go check it out already."

    mc_nvl "Really?!"

    mc_nvl "This must have been why I'm so anxious today. Fine, I'll check it out right away."

    mc_nvl shocked_casual "{image=Phone Texting Images/Result.jpg}"
    mc_nvl happy_casual "Gregory, I made it. I'm so happy!"
    mc_nvl sad_casual "But I don't see your name there. Are you not qualified?"

    g_nvl "Yeah, I kinda figured it out."
    g_nvl "Don't worry, I have a backup school so we might be seeing each other sometime during our college days."
    mc_nvl "It feels so bad being happy that I passed but you don't. I was really thinking of the places we'd go there."
    g_nvl  "Oh, cheer up [mcname]."
    g_nvl "Let's look into what we could do for the meantime."
    mc_nvl neutral_casual "I gotta tell this to Mommy. Let's go out later tonight to celebrate, shall we?"

    g_nvl "Yeah, that'll be fun! I'll see you tonight, [mcname]."
    g_nvl "Bye."

    # ends the text messaging
    scene bg table with dissolve
    show mc happy_casual at left with dissolve
    show mom neutral at right with dissolve

    mc "*Giggles*"
    mom "What's this I'm hearing, honey?"
    mc "Ma, I passed the entrance exam. I'll be going to Bicol University this coming school year."
    show mom happy with dissolve
    mom "Oh honey! That's some big news. You know what this calls for. ICE CREAM!"
    mc "Yey! I've been wanting ice cream for a long time."
    mc "Mine's chocolate!"

    show mom neutral with dissolve

    mom "Slow down, we'll wait until lunch time, okay?"

    # Family Celebrating
    hide mc
    hide mom

    scene bg luggage 
    n "[mcname], an incoming first year college student of Bicol University. It was [pronoun_belonging] first time being away from home and had no friends going to the new school [pronoun_referred] enrolled in..."
    scene bg luggage2
    n "and now that [pronoun_referred] has arrived [pronoun_referred] now has to face the challenges that every freshman must face."


    jump chapter1

label chapter1:
    scene bg calendar_aug with dissolve
    scene bg calendar_aug with Pause(4)
    scene bg dormday with dissolve

    show mc happy_casual
    mc "Oh wow! This is what the prestigious BU looks like! I feel so anxious, will I ever get new friends? Oh well guess we’ll find out when classes start."

    scene bg livday
    show emil angry
    emil "Oyy you! Always sign in the logbook before going in or outside the dormitory? Got it?!"
    show emil angry:
        ease 0.7 xalign 0.9
    show mc confused_casual:
        xoffset -700
        ease 0.9 xoffset 100

    menu:
        "Yes sir, I’m sorry I didn’t know, won’t happen again":
            $ emil_decision = "good"
            $ points += 1
            show mc shocked_casual with dissolve
            show emil neutral with dissolve
            emil "Ok, sorry for raising my voice, but please do not forget when doing so, here’s the keys to your room."
            show mc neutral_casual with dissolve
            mc "It's okay, {i}kuya{/i}. Thank you."

        "Silence, (*proceeds to logbook*)":
            $ emil_decision = "neutral"
            show mc sleepy_casual with dissolve
            emil "(*silence*)"

        "Pff! Couldn’t you be any nicer to the new comers?!":
            $ emil_decision = "bad"
            $ points -= 1
            show mc angry_casual with dissolve
            emil "HUH! Is that how your mother taught you how to interact with others?! Anyways, here’s your key!"

    scene bg roomday with fade
    show mc confused_casual
    mc "This room is kinda messy! I guess I need to clean up first since I’m the first one to arrive."

    hide mc
    $ in_story = True
    jump dormicleaning

label chapter1_1:
    show mc happy_casual with dissolve
    mc "Whew, finally I’m done cleaning and unpacking, I guess I’ll go for a little campus tour first."

    hide mc
    # campus tour
    scene bg walkday with dissolve 
    scene bg walkday with Pause(3) 
    scene bg ovalday with dissolve
    scene bg ovalday with Pause(3) 
    scene bg schoolday with dissolve 
    scene bg schoolday with Pause(3) 
    scene bg building1 with dissolve 
    scene bg building1 with Pause(3) 
    scene bg fieldaft with dissolve
    scene bg fieldaft with Pause(3) 
    scene bg torchaft with dissolve 
    scene bg torchaft with Pause(3) 
    scene bg sidewalkaft with dissolve 
    scene bg sidewalkaft with Pause(3) 
    
    scene bg dormaft with dissolve
    show mc neutral_casual with dissolve
    mc "I think that's all for today. It was fun walking inside the campus. It feels like this whole school is my kingdom."
    mc "Time to go back to the room and check if someone's already here." 

    scene bg roomaft with fade
    show mc happy_casual with dissolve:
        xalign 0.1
    mc "Oh, hi there!"
    show roommate sad_casual with dissolve:
        xalign 0.9
    roommate "Errr..."
    mc "You must be my new roommate! My name is [mcname], what’s your name?"
    roommate "Hello, my name is ugh... [roommate]."
    mc "Nice to meet you [roommate]! I’m from ..."
    $ place = renpy.input("Where are you from?", length=50)
    $ place = place.strip()
    mc "I’m from [place]. How about you?"
    roommate "I’m from eehhh……. My parents are actually from Goa, but I live in Naga actually."
    mc "That's nice! I think we should hang out more. I'm sure we'll be pretty close as days pass by."
    show roommate neutral_casual with dissolve
    roommate "Uhm... Yeah, sure."
    mc "Would you like to join me later for dinner? I'd really like to have a conversation with you. You'll be my first ever friend here."
    roommate "Okay, I guess."

    scene cutscene3 # time passes by CLOCK ANIMATIOOOOON
    scene cutscene4 # mc and a femc bumped each other

    scene bg sidewalknight with fade

    show roommate neutral_casual:
        xoffset -700
        ease 1.6 xalign 0.99 xoffset 0
    with Pause(1)

    show mc neutral_casual:
        xoffset -700 
        ease 1.5 xalign 0.7 xoffset 0 


    show madam_alexandra neutral:
        xoffset 1700
        ease 1.8 xalign 0.1 xoffset 0
    with Pause(1.5)
    show madam_alexandra annoyed with dissolve
    show mc shocked_casual with dissolve    
    menu:
        "I’m sorry miss, I didn’t see you there.":
            $ points += 1
            show mc shocked_casual with dissolve
            show madam_alexandra neutral with dissolve
            "???" "Oh, no worries."
            $ madam_decision = "good"
        "Watch where you're going miss!":
            $ points -= 1
            show mc angry_casual with dissolve
            show madam_alexandra angry with dissolve
            $ madam_decision = "neutral"
            "???" "Huh! Kids these days are so rude!"
            show madam_alexandra angry with dissolve:
                linear 1.0
                xalign 2.0
            $ madam_decision = "bad"
    
    show madam_alexandra:
        ease 2 xoffset -1100
    with Pause(1)
    show roommate:
        ease 2 xoffset 1700
    with Pause(0.5)
    show mc:
        ease 3 xoffset 1700

        
    n "[mcname] and [roommate] continues to walk and have their dinner."
    hide madam_alexandra
    hide mc
    hide roommate

    scene cutscene5 with Pause(3) # dinner mc and roommate
    scene cutscene6 with Pause(3) # next day arrives

    scene bg roomday with dissolve
    show mc sleepy_casual with dissolve
    mc "It's morning already?! I still want to sleep."
    # make this Itallic
    "[mcname] subconscious" "{b}I forgot that I still haven’t claimed my COR for my ID and I don't have enough uniforms. 
    I guess I should go to the registrar first and then go to the tailor to get my uniform tailored.{/b}"

    scene bg livday with fade
    show mc neutral_casual with dissolve:
        xalign 0.1
    show dormmate admiring_casual with dissolve:
        xalign 0.9
    dormmate "Good morning fellow dormer!"
    show dormmate admiring_casual

    menu:
        "Hello, good morning to you too!":
            $ points += 1
            show mc happy_casual with dissolve
            dormmate "Hello! You’re new here too huh? What course are you from? I’m [dormmate] from BS Computer Science, 1st year."
            mc "I'm [mcname]! I guess were in the same program I see."

        "*Ignores*":
            dormmate "Quite the shy type huh, what course are you from?"
            show dormmate happy_casual with dissolve
            dormmate "I’m [dormmate] from BS Computer Science, 1st year."
            mc "I'm [mcname]! I guess were in the same program I see."

        "Who in the world are you?":
            $ points -= 1
            show mc angry_casual with dissolve
            show dormmate confused_casual with dissolve
            dormmate "Woah woah, chill dude hehe."
            show dormmate happy_casual with dissolve
            dormmate "I mean no harm just wanted to interact, I’m [dormmate] from BS Computer Science, 1st year."
            show mc neutral_casual with dissolve
            mc "Oh, my bad. Anyway, I'm [mcname]. I guess were in the same program I see."

    dormmate "Nice! By any chance do you have your COR already?"
    mc "I haven’t, I’m just about to go to the registrar to claim it."
    dormmate "Great! Why don’t we go there together?"
    mc "Sounds great! Let's go."

    scene bg registrar with fade 
    show dormmate neutral_uniform:
        xoffset -1500
        ease 2.5 xoffset 0 xalign 0
    with Pause(0.5)

    show mc neutral_uniform:
        xoffset -1000
        ease 2 xoffset 0 xalign 0.3

    n "And there [dormmate] and [mcname] goes on to go to the registrar together to claim their respective COR. Just as [mcname] came near the registrar windows, [pronoun_belonging] face turns pale as [pronoun_referred] saw the mystery woman in the registrar’s office"
    show madam_alexandra neutral with dissolve:
        xoffset 1700
        ease 2 xoffset 0 xalign 0.95
    show dormmate shocked_uniform with dissolve
    show mc shocked_uniform with dissolve

    mc "Uhh... Uhm... Hi madam, I apologise for what happened last night huhu."

    if madam_decision == "good":
        show madam_alexandra happy with dissolve
        madam "Hello there, [pronoun_respect]! I see that you are also from the College of Science, I also apologise for bumping into you yesterday. How may I help you?"
    elif madam_decision == "bad" or madam_decision == "neutral":
        show madam_alexandra annoyed with dissolve
        madam "Well well well, if it isn’t [pronoun_respect] bump, no apology here, what can you do for you?"

    show mc sad_uniform with dissolve
    show dormmate confused_uniform with dissolve

    mc "I would like to get my COR so that if ever that our professor needs it we can show it, Madam."
    madam "Sure, however it’ll take a few minutes before we can process it."
    mc "No problem Madam, thank you!"
    scene bg registrar with fade 

    show mc neutral_uniform with dissolve:
        xalign 0.7
    show dormmate neutral_uniform with dissolve:
        xalign 0.2
    n "[dormmate] waited for [pronoun_belonging] turn."
    show dormmate:
        ease 2 xoffset -1000
    with Pause(0.5)
    show mc:
        ease 2.5 xoffset -1600
    n "And after that they both left out the registrar."

    scene bg walkaft with dissolve
    show mc happy_uniform with dissolve:
        xalign 0.1
    show dormmate happy_uniform with dissolve:
        xalign 0.9
    dormmate "Now that we have already claimed the COR, where are we going now?"
    mc "I’m going to the tailor, I don't have enough uniforms to wear."
    dormmate "Alright then, I’ll see you back to the dorm then!"
    mc "See ya!"

    scene bg tailorshop with pixellate
    show mc happy_uniform with dissolve:
        xalign 0.1
    mc "{i}Tao po! Pwede po magpatahi uniform?{/i}"
    show erin happy with dissolve:
        xalign 0.9
    aling "Good morning! Surely, what is it that you needed [pronoun_respect]?"
    mc "I need a uniform for BU, is it possible that it'd be finished this weekend?"
    aling "Sure [pronoun_respect]! Let me get your measurements."
    scene measures_mc with Pause(5)
    scene bg tailorshop with fade
    
    show mc happy_uniform with dissolve:
        xalign 0.1
    show erin happy with dissolve:
        xalign 0.9

    mc "Thank you, {i}aling{/i}! I'll be on my way. Good bye, ma'am!"
    aling "Ok [pronoun_respect]! Take care."

    scene bg dormaft with dissolve
    n "[mcname] goes back to [pronoun_belonging] dorm, and when [pronoun_referred] arrives at [pronoun_belonging] room the door is locked 
    and [pronoun_referred] forgot [pronoun_belonging] keys. [pronoun_referred!c] goes and asks Kuya Emil if [pronoun_referred] could borrow his keys."

    scene bg livaft with dissolve
    show mc neutral_uniform with dissolve
    mc "Kuya Emil can I borrow the keys for our room, I might’ve forgot the key inside."

    if emil_decision == "good":
        show mc neutral_uniform:
            xalign 0.5
            ease 1 xalign 0.1
        show emil neutral:
            xoffset 2000
            ease 1.2 xoffset 1100
        emil "Here you go, kiddo!"
    elif emil_decision == "bad" or emil_decision == "neutral":
        show mc sad_uniform:
            xalign 0.5
            ease 0.7 xalign 0.1
        show emil angry:
            xoffset 1500
            ease 0.7 xoffset 1100
        emil "Heh! Keys are given to you to use for opening the door, not for decoration! Next time you forget your key, you’ll be waiting for your roommate to come home before you open your door!"

    # add more scenes
    hide emil
    hide mc
    scene bg frontnight with dissolve
    n "The first official day for classes in Bicol University has officially began. The students and faculties are roaming as much as before, lots of students are having a hard time navigating the campus, the sound of vehicles during rush feels like the world has reverted back to normal."
    n "And just before official lectures start, orientation for freshmen will happen."

    scene bg dormday with fade
    "*Next day arrives*"

    scene bg roomday with dissolve
    show mc happy_uniform with dissolve
    mc "Today’s finally the day! I get to meet my new classmates, I wonder what they look like or their personality hmmm."
    mc "Guess I’ll just go with [dormmate] during the orientation, having a familiar face is always a good thing. Right, [roommate]?"
    show mc confused_uniform with dissolve
    roommate "*snores*"
    mc "Oh, nevermind. [pronoun_referred!c]'s still asleep."

    scene bg livday with fade
    show mc neutral_uniform:
        xoffset 1900
        ease 6.5 xoffset -800
    "*[mcname] proceeds outside*"
    scene bg dormday with dissolve
    show mc neutral_uniform:
        xoffset -400
        ease 1.2 xoffset 200
    show dormmate happy_uniform with dissolve:
        xoffset 2000
        ease 1.5 xoffset 1100
    dormmate "Just in time [mcname]! I was waiting for you so we can go out together. "
    show mc happy_uniform with dissolve
    mc "Let's go!"

    show mc:
        ease 2.3 xoffset 2000
    show dormmate:
        ease 2 xoffset 2500
    n "They then proceed to the computer science building."

    scene bg building1 with fade
    show dormmate shocked_uniform with dissolve:
        xalign 0.1
    show mc shocked_uniform with dissolve:
        xalign 0.9

    n "As they arrrive in the building, [pronoun_referred] can hear students murmuring, the place as lively as usual."
    dormmate "Sheeeesh, there are lots of students! I have no idea where we should be designated!"
    show mc confused_uniform with dissolve
    mc "I guess we should just look for someone who we are familiar with, maybe a familiar face in the groupchat?"
    show dormmate happy_uniform with dissolve
    dormmate "I've never checked the groupchat so far LOL."
    show mc shocked_uniform with dissolve
    mc "Then were doooommmeeeedddd!!!!!!"
    show dormmate neutral_uniform with dissolve
    show mc neutral_uniform with dissolve
    n "Another student approaches, a guy with glasses with casual shirt and braces."
    show lurs neutral_casual:
        xoffset 2000
        ease 1.2 xoffset 650
    lurs "*bumps into [mcname]*"
    show lurs shocked_casual with dissolve
    show mc shocked_uniform with dissolve
    show dormmate confused_uniform with dissolve
    "???" "Ohhh... Sorry about that [pronoun_respect] hehe, may I ask where the section is for Computer Science?"

    menu:
        "Oh, hi there. Are you also a computer science freshman? My name is [mcname] and this is [dormmate]!":
            $ points += 1
            scene bg building1 with fade
            hide dormmate
            show mc happy_uniform:
                xalign 0.1
            show lurs happy_casual:
                xalign 0.9
            lurs "Nice to meet you both! Yes, I am a freshman student of Computer Science! Thanks for having me. I'm Johnny, by the way."
            mc "Let's head to the section, shall we?"
            lurs "Sure."
            $ johnny_decision = "good"

        "*Ignores*":
            scene bg building1 with fade
            show mc confused_uniform:
                xalign 0.1
            show lurs nervous_casual:
                xalign 0.9
            lurs "Uhmmm... I'm Johnny, nice to uhhh... meet you."
            mc "*tsk*"
            $ johnny_decision = "neutral"

        "Watch it nerd! Are your glasses just for clout?":
            $ points -= 1
            scene bg building1 with fade
            show mc angry_uniform:
                xalign 0.1
            show lurs nervous_casual:
                xalign 0.9
            lurs "I’m sorry! I’m sorry! I didn’t mean to bump into you!"
            mc "*tsk* How could you not even see me standing here."
            $ johnny_decision = "bad"

    scene bg comlab with fade

    n "They proceed to the computer science section."
    n "When they enter the room, it was a mixture of noise and disaster. The students were loud as if they already knew each other."
    scene bg building1 with pixellate
    n "The orientation ends, and the class was out of the building."
    show joseyde happy at center
    j "Okay, now that the orientation has ended, I highly recommend that you get to know your blocmates first to bond and create memories. Thank you everyone and have a blessed afternoon."
    "Everyone" "*applauses*"

    scene bg fieldday with dissolve
    show mc happy_uniform with dissolve:
        xalign 0.1
    mc "Where do we go now [dormmate]?"
    show dormmate confused_uniform with dissolve:
        xalign 0.9
    dormmate "I dunno, maybe let’s go talk to some of our classmates then?"
    scene bg fieldday with fade
    show carla happy_uniform
    show jasmine admiring_uniform at right
    show sophia awkward_casual:
        xalign 0.1
    with Pause(1.5)
    scene bg fieldday with fade
    show matt neutral_uniform
    show mike senpai_casual at right
    show lurs neutral_casual:
        xalign 0.1
    with Pause(1.5)
    show lurs nervous_casual with dissolve
    show lurs nervous_casual with Pause(1):
        ease 2 xoffset -700 
    with Pause(2)
    scene bg fieldday with fade
    
    show dormmate neutral_uniform with dissolve:
        xalign 0.1 xoffset -100
    show mc neutral_uniform with dissolve:
        xalign 0.35
    show lurs nervous_casual:
        xoffset 1700
        ease 2.5 xoffset 0 xalign 0.85
    n "And suddenly, Johnny appears beside [mcname] and [dormmate]."

    if johnny_decision == "good":
        show lurs happy_casual with dissolve
        show mc neutral_uniform with dissolve
        lurs "Oh, hey there! It appears that we’re actually classmates! I hope to get to know you guys better!"
        show dormmate happy_uniform:
            xoffset -300
            ease 1.3 xoffset 500
        show mc happy_uniform:
            ease 1 xalign 0.05

        mc "Hey, there. Nice seeing you here."
        dormmate "Oh yeah. Where are you off to?"
        lurs "I'm actually heading home, I have to do something today."

    elif johnny_decision == "bad" or johnny_decision == "neutral":
        show mc confused_uniform with dissolve
        show lurs sad_casual with dissolve
        lurs "Oh, hehe. Sorry about earlier."
        mc "Actually, I should be the one to say sorry."
        show mc neutral_uniform with dissolve
        mc "Uhm... Sorry, Johnny, was it?"
        show lurs happy_casual with dissolve
        lurs "Ah, yes! You remembered?"
        mc "Yeah, I have never forget a name, and a face. I am [mcname]."
        dormmate "Hi, my name is [dormmate]. So, where are you off to now?"
        lurs "Actually, I'll be heading home now. Nice to officially meet you, by the way."

    mc "Alright, then. See ya."

    show lurs:
        ease 2 xoffset 1500
    show dormmate neutral_uniform:
        ease 2.5 xalign 0.9 xoffset 0

    dormmate "See you next time, Johnny."
    n "And Johnny leaves the two alone."
    hide lurs

    show mc neutral_uniform with dissolve
    mc "Oh well, I just hope we get to go along with our other classmates."
    show dormmate neutral_uniform with dissolve
    dormmate "Yeah, let's hope for the best. Shall we go back?"
    mc "Yep. Time to go."

    scene bg dormaft with pushup
    n "[mcname] and [dormmate] arrives at Dormitory."
    scene bg blur_livaft with dissolve
    show mom phonecall:
        yoffset 1500 xalign 0.5
        ease 2 yoffset 200
    play sound "phonering.mp3" loop
    with Pause(4) 
    menu:
        "*Answer Call*": 
            $ points += 1
            stop sound
            show mom phonecall_neutral with fade:
                xalign 0.25 yoffset 0 yalign 0.25
            show mc neutral_casual with dissolve:
                xalign 0.8
            mom "Hi dear, you haven’t called in a while so I had to call you just to check on you. How’s college been?"
            jump mom_convo


        "*Don't answer*":
            $ points -= 1
            stop sound
            jump chapter1_2

label mom_convo:
    menu:
        "So far it’s been good ma! Our class haven’t officially started but so far it’s been great!":
            show mom phonecall_happy with dissolve
            show mc happy_casual:
                xalign 0.8
            mom "Oh that’s good to hear! Keep up the good work dear and remember to not pressure yourself that much and just have fun, alright?"

        "It’s been absolute mess! All the people here always rubs me of the wrong way!":
            show mom phonecall_sad with dissolve
            show mc angry_casual:
                xalign 0.8
            mom "I know that college is tough but don’t be like that now. There will always be something positive to look forward in tough situations. Always remember, if you ever need help, we’ll be here."

    show mc neutral_casual with dissolve:
        xalign 0.8
    mc "Thanks, ma. Oh, I've also meet my classmates, and my roommate, and even one of my classmate which I didn't know was also the same class as mine!"
    show mom phonecall_happy
    mom "Well that's great! At least you have someone you can hangout and company you throughout this college journey."
    mc "I know, ma. You'll love [pronoun_object]. [pronoun_referred!c]'s always cheerful and I really hope to be close with [pronoun_object]."
    show mom phonecall_neutral with dissolve
    mom "Now you have someone to lean on. Just be sure who you are getting friends with. Your generation is a lot complicated to take in."
    mom "Choose your friends wisely..."
    show mc confused_casual with dissolve
    "[mcname] and Mom" "and make sure they don't hold you down."
    mc "Yes yes, I know. Just trust me, I'll be alright here."
    show mom phonecall_sad with dissolve
    mom "I trust you. It's just... I care and this is your first time living on your own."
    mc "It's for the better and also for my future, ma."
    show mom phonecall_neutral with dissolve
    show mc neutral_casual with dissolve
    mc "By the way, I better keep going now I still have to fix my things. Bye!"
    mom "Bye [mcname], mama always loves you mwaaah"
    hide mom with dissolve
    hide mc with dissolve
    "*sound of phone stops*"

label chapter1_2:
    scene bg dormaft with dissolve
    show mc neutral_casual
    mc "I guess I could use this time to check on the uniform. Maybe she's a fast tailor."
    
    show mc neutral_casual:
        ease 4 xoffset -4000
    n "[mcname] travels to the tailor shop"

    scene bg tailorshop with pixellate
    show mc happy_casual with dissolve:
        xalign 0.1
    mc "{i}Magandang araw po! Kukuha po sana ako nung uniform kong pintahi ho nung nakaraan.{/i}"
    show erin happy with dissolve:
        xalign 0.9
    aling "Well, hello there [pronoun_respect]! You’re uniform is already done, however, there is one thing that is missing." 
    show erin sad with dissolve
    show mc neutral_casual with dissolve
    aling "I forgot to tell you that you should’ve bought your logo from the department since our store already run out of it. I sincerely apologise if I informed you way to late."
    menu:
        "No worries, Aling Erin! ":
            $ points += 1
            mc "I’ll just buy from our department. Thank you aling! *gives money*"
            show money with dissolve:
                xalign 0.2 yalign 0.7
            show money with Pause(2):
                ease 2 xalign 0.75
            hide money with dissolve
            aling "I do apologise again [pronoun_respect] for the inconvenience, I’ll just give you a discount for your troubles. Take care!"

        "Well, you could’ve told me that earlier!":
            $ points -= 1
            show mc angry_casual with dissolve
            show erin sad with dissolve
            mc "Now I have to pay you full for not finishing my uniform, unfair but still thanks tsk tsk *gives money*"
            aling "My apologies [pronoun_respect], please do not take it top hard since I'm old and have lots of customers to accommodate." 
            aling "I’ll just give you a discount for your troubles, I again apologize [pronoun_respect]."

    scene bg sidewalkaft with dissolve
    show mc confused_casual:
        xoffset -500
        ease 2 xalign 0.2 xoffset 0
    n "[mcname] leaves the tailor shop."

    show crush neutral_uniform:
        xoffset 1800
        ease 5 xoffset 300
    show mc confused_casual:
        ease 4 xalign 0.7

    n "While [pronoun_referred] waits for jeepneys to pass by, [pronoun_referred] sees [pronoun_belonging] old crush crush walking towards [pronoun_object] without [pronoun_object] noticing [pronoun_object]."
    show mc shocked_casual with dissolve
    mc "*Oh gosh, it's [crush]! What do I do? What do I say?*"
    menu:
        "Hi, [crush]!":
            $ points += 1
            show mc blushed_casual with dissolve
            show crush happy_uniform with dissolve
            mc "Ho.. how… how’s… what’s up? Hehe"
            crush "Oh hey there [mcname]! It’s been a long time since I last saw you huh. I would love to keep the chat going but..."
            show crush sad_uniform with dissolve
            crush "I have a class to attend so I better be going. Bye! It was nice talking to you again!"


        "*Whistles*":
            $ points -= 1
            show mc neutral_casual with dissolve
            show crush awkward_uniform with dissolve
            if current_gender == "male":
                mc "Hey there beautiful, hehe just kidding. Sup [crush]?"
            else:
                mc "Hey, cutie. Where are you going? Want to me to company you?"
            crush "Oh hehe…. [mcname] uhhh. I still have a class to go to so I better keep going. Bye"
            show mc sad_casual
            mc "Oh, uhhm. Okay."

    show crush neutral_uniform:
        ease 2.5 xoffset -700
    mc "Byee! See ya around!"
    hide crush
    show mc blushed_casual:
        ease 4 xoffset 1800
    n "*[crush] walks away hurridley since she has class to attend, meanwhile [mcname] is blushed and all*"
    scene bg frontaft with dissolve
    show mc blushed_casual:
        xoffset -700
        ease 4 xalign 0.5 xoffset 0
    mc "UGGGHHHHHHH!!! [crush_referred!u] AS CUTE AS EVER!!!"
    show mc neutral_casual
    mc "Okay, calm down I still have to buy some logos for my uniforms."
    n "A jeepney stops in front of [mcname], and [pronoun_referred] ride the jeepney to buy [pronoun_belonging] logo."

    scene bg caraft with irisin
    show mc neutral_casual with dissolve:
        xalign 0.1
    show mark neutral with dissolve:
        xalign 0.9
    mc "{i}Kuya bayad po.{/i}"
    mark "{i}Sa may san ito?{/i}"
    mc "{i}Sa may BU Main lang ho.{/i}"
    n "And [mcname] was given [pronoun_belonging] change. Yet the change was not enough."
    menu:
        "{i}Manong kulang ho ang sukli, estudyante ho ako.{/i}":
            $ points += 1
            show mc confused_casual with dissolve
            show mark confused with dissolve
            mark "{i}Ayy ganon ba iho? Eto pasenya ka na ah, matanda na ang mamang hehe{/i}"
            show mc neutral_casual
            mc "{i}Okay lang po, salamat.{/i}"


        "{i}Manong ba’t eto lang sukli?!{/i}":
            $ points -= 1
            show mc angry_casual with dissolve
            show mark sad with dissolve
            mc "{i}Ang lapit lapit nga lang ng patahian sa BU tapos sobra ka pa maningil. Estudyante pa ako kaya dapat di ganto singil niyo!{/i}"
            mark "{i}Hay nako nagkamali lang siguro ako panukli, ang bibig ng kabataan ngayon talagang antatalas ng mga dila.{/i}"

    scene bg frontaft with fade
    n "As [mcname] arrives at the university, [pronoun_referred] went straight to the CSC office."

    scene bg cscoffice_1 with fade
    show mc neutral_casual with dissolve:
        xalign 0.1
    mc "Good afternoon! Are there still available logos for our uniform?"
    show mike happy_uniform with dissolve:
        xalign 0.9
    mike "Hello! Yes there are still some, come in and have a sit."
    show mike:
        ease 2 xoffset 1000
    n "[mcname] waited for them to get the logo"
    scene bg cscoffice_2 with fade
    show mc neutral_casual with dissolve:
        xalign 0.1
    show mike happy_uniform with dissolve:
        xalign 0.9
    mike "Sorry for the wait, here are your logos." # ANIMATION GIVING SEALS AND PLATES
    show BUseal1 with dissolve:
        xalign 0.75 yalign 0.7
    show BUplate1 with dissolve:
        xalign 0.78 yalign 0.7

    show BUseal1 with Pause(2):
        ease 2 xalign 0.2
    show BUplate1 with Pause(2):
        ease 2 xalign 0.23

    hide BUseal1 with dissolve
    hide BUplate1 with dissolve

    show mike confused_uniform with dissolve
    mike "By the way, you look so familiar..."
    mike "Feels like I've seen you somewhere hmm."
    show mc confused_casual with dissolve
    mc "Really? I've only been here for a few days."
    mike "Say, weren't you in the freshmen orientation a few days ago?"
    show mc happy_casual with dissolve
    mc "Yes I am, you don’t happen to be a Computer Science student as well, are you?"
    show mike happy_uniform with dissolve
    mike "What a coincidence I actually am! I am a third year student and it looks like you’d be calling me {i}“senpai”{/i} eyy! Just kidding."
    menu:
        "Nice to meet you {i}“senpai”{/i}! I look forward to working with you in the future, I better.":
            $ points += 1
            show mc happy_casual with dissolve
            show mike happy_uniform with dissolve
            mike "I see! Take care my {i}\"kohai\".{/i}"

        "Ha! As if I'd call someone {i}\"senpai\".":
            $ points -= 1
            show mc angry_casual with dissolve
            show mike sad_uniform with dissolve
            mark "Sheesh, no need to be harsh about it hey hey hey!"
            show mc:
                ease 3 xoffset -800
            show mike neutral_uniform with dissolve
            mark "Anyways, take care when you get home!"

    scene bg dormaft with fade
    n "After obtaining the logos, [mcname] goes to the dorm."

    show emil neutral with dissolve:
        xalign 0.9
    show mc sad_casual with dissolve:
        xalign 0.1
    emil "You look kinda tired kiddo, college’s been making things tough for ya, huh?"
    mc "Tell me about it, we haven’t even started official lecture classes but it already feels like I’ve had lots of things done."
    emil "Well don’t sweat, you’ll get the hang of it soon. Wish you luck kiddo."

    menu:
        "Thanks kuya Emil! Gonna need it!":
            $ points += 1
            show mc happy_casual with dissolve
            show emil happy with dissolve
            emil "Sure kiddo, best of luck."

        "I don’t need your goodluck.":
            $ points -= 1
            show mc angry_casual with dissolve
            show emil angry with dissolve
            emil "Cocky as usual. *tsk*"

    scene bg roomaft with move
    n "After that, [mcname] proceeds to [pronoun_belonging] room."

    n "*Internally, [mcname] talks to [pronoun_object]self*"
    show mc sad_casual with dissolve
    mc "{b}Hays, is it really necessary that I still put a logo on this uniform? It’s not like the guard will notice me not having this already. Oh well, guess better keep doing this now.{/b}"

    hide mc
    #jump init_sewing
    # "*MINI GAME (IF APPLICABLE), THERE WILL BE UNIQUE DIALOGUES IF MAKAGAWA MINI GAME, IF HINDI KAYA PROCEED LANG.*"

label chapter1_3: # 4/24 start of editting again
    scene bg roomaft
    show mc neutral_casual at center
    with dissolve
    mc "Now that I’ve sewn these uniforms, I now need to iron the clothes so they may look presentable when going to class."

    hide mc
    # "*MIGHT MINI GAME NOT SURE"
    show mc happy_casual at center with dissolve
    mc "Finally done with the chores, now I have to prepare for my classes tomorrow."

    "*INTERACTABLE PHOTOS (CAN USE IMAGE MAP feature)*"

    hide mc
    "*Next day arrives, alarm rings.*"
    scene bg roomday with hpunch
    show mc sleepy_casual at center with dissolve
    mc "Uggggghhhhhhh……………"
    mc "It’s really here, THE first day of classes, I just hope that the professor are nice."
    hide mc
    show mc shocked_casual with dissolve:
        xalign 0.5
        ease 0.8 xalign 0.1
    mc "Ohh [roommate] is almost awake, I must've been very noisy."
    show roommate sleepy_casual with dissolve:
        xalign 0.9
    roommate "Uggghhhh…………… Good morning, want to go out for breakfast?"
    menu:
        "I would love to!":
            $ points += 1
            show mc neutral_casual with dissolve:
                xalign 0.1
            mc "It's a great way to start the day."
            
            show mc sad_casual with dissolve
            mc "But I need to be early for the first day so I can’t. Let’s do it next time!"

            show roommate happy_casual with dissolve:
                xalign 0.9
            show mc neutral_casual with dissolve
            roommate "It’s alright, let’s eat next time then."
            show roommate:
                ease 1.9 xoffset 900
            
            "*[roommate] leaves for breakfast.*"

        "No thanks, I’m not interested.":
            $ points -= 1
            show mc angry_casual with dissolve:
                xalign 0.1
            show roommate sad_casual with dissolve:
                xalign 0.9
            roommate "Oh... Okay."
            show roommate:
                ease 1.9 xoffset 900
            "*[roommate] leaves for breakfast.*"

    scene bg roomday with fade
    show mc happy_casual at center with dissolve
    mc "Ok now that I have finished preparing things, time to clean myself."
    show mc:
        ease 2.8 xoffset 1600
    "*[mc] proceeds to go to the CR.*"

    scene bg crday with fade
    show dormmate happy_casual:
        xoffset -1300
        ease 2.5 xoffset 0 xalign 0.9

    show mc neutral_casual:
        xoffset -900
        ease 2.1 xoffset 0 xalign 0.1

    "*[mc] and [dormmate] bumps into each other.*"

    dormmate "Oh hey there, [mc]! What a coincidence you just woke up, too?"
    mc "Nah, I just finished preparing my things for the first day of classes, you can never be too prepared."
    show dormmate neutral_casual with dissolve
    dormmate "You seem to be super excited rather than nervous in the first day, huh?"
    show mc happy_casual with dissolve
    mc "Of course! It’s exciting to get to know more people other than the orientation, plus I am somehow excited on how our professors look like and how they act."
    dormmate "Heh... I wish I had your enthusiasm, anyways we better get going we might be late to class. Let’s go together going to class I am kinda nervous, hehe."
    show mc neutral_casual with dissolve
    mc "Alright then. I’ll be going now as well!"
    hide mc with dissolve
    hide dormmate with dissolve
    "*[mc] goes to shower and finishes preparing, [pronoun_referred] goes to the lobby waiting for [pronoun_belonging] friend.*"
    scene bg livday with pushup
    show mc angry_uniform at center with dissolve
    mc "Where the in the world is [dormmate], we're about to be late for the first day of class!"
    # this is where i end
    menu:
        "*Wait for [dormmate], even if you get late.*":
            $ points += 1
            hide mc
            show mc neutral_uniform at center with dissolve
            mc "I guess it wouldn’t hurt to wait for a bit longer."
            hide mc "After a few minutes, [dormmate] arrives."
            show mc angry_casual at left with dissolve
            mc "What the hell have you been doing? We are almost late!"
            show dormmate sad_uniform at right with dissolve
            dormmate "Sorry [mc] *tired sighs* I had the urge to take a call of nature at the worst time, I’ve already had my clothes on but I had to take them of cause of the urge."
            hide mc
            show mc neutral_uniform at left with dissolve
            mc "You really had to sugarcoat the term for taking a poop. Anyways we better get going or Ma'am will get mad at us, we should go for a run at it."
            hide mc
            hide dormmate
            "*runs to the room*"
            scene bg comlab with face
            "*[mc] and [dormmate] both just barely made it in time.*"
            show mc angry_uniform at left with dissolve
            mc "We barely made it in time! No thanks to you!"
            hide mc
            show mc happy_uniform at left with dissolve
            mc "Just kidding"
            show dormmate sad_uniform at right with dissolve
            dormmate "You didn’t need to be so frank with it, lol. It’s what you call being clutch."
            show mc happy_uniform at left with dissolve
            mc "Clutch your face, we better find ourselves a seat now since class is about to begin."

        "*Leave [dormmate].*":
            $ points -= 1
            hide mc
            show mc neutral_uniform
            mc " I should just go now or I’ll be late, and maybe I’ll still arrive in time."
            hide mc
            "*[mc] goes through the canteen knowing that [pronoun_referred] still has some time."
            scene bg canteenday with fade
            show mc neutral_uniform at center with dissolve
            mc "mm…….. There’s still a few more minutes before time, maybe I can stop by for a little snack..."
            "*{i}nag snack sa canteen{/i}*"
            mc "Oh shit! It’s almost time! I might get late."
            hide mc
            "*[mc] runs to the room.*"
            scene bg comlab with fade
            show mc happy_uniform at center with dissolve
            mc "Just in time did I arrive. Now it's time to find myself a seat."
            "*After a few moments, [dormmate] arrives."
            show dormmate angry_uniform at right with dissolve
            dormmate "Dude! You literally left me tsk"
            hide mc
            show mc sad_uniform at left with dissolve
            mc "You were taking too long! It was the first day I can’t afford to be late, I’m truly sorry"
            hide dormmate
            show dormmate happy_uniform at right with dissolve
            dormmate "Nah I was just messing with ya, I took too long to prepare so that one’s on me"
            hide mc
            show mc neutral_uniform at left with dissolve
            mc "Ok then, go get yourself a seat already cause class will start"

    hide mc
    hide dormmate
    "*After a while, ma'am Michelle arrived.*"
    show michelle neutral at center with dissolve
    mich " Hello class! My name is Michelle and I will be your teacher this semester for your Introduction to Computing subject, this class won’t be as easy as you guys think. That is why I expect your full cooperation so that we may be able to get along well."
    show michelle happy at center with dissolve
    mich "Now that I have introduced myself, how about you introduce yourselves this time,"
    hide mich
    show mich neutral
    hide mich
    show mich happy with fade
    "*looks around*"
    mich "alright let’s begin with you [pronoun_respect]."
    menu:
        "Hello! My name is *character name*! I am from [loc] and I am pleased to meet you too madam Michelle!":
            $ points += 1
            show mc happy_casual at left with dissolve
            show michelle happy at right with dissolve
            mich "Nice to meet you too character! Am also looking forward that you enjoy and learn lots in this class! Ok next. "

        "Errr…….. Why did you choose to begin with me? Anyways the Name is  *character name*. Pleased to meet you ":
            $ points -= 1
            show mc confused_casual at left with dissolve
            show michelle angry at right with dissolve
            mich "Hmm, don’t you think as the teacher it is my choice whom I wanted to call to introduce themselves first. Anyways nice meeting you too, character. Ok next"


    hide mc
    hide Michelle
    "*cutscene where there students will introduce themselves*"

    scene bg comlab with fade
    show michelle happy at center with dissolve
    mich "Ok everyone, that you have finished introducing yourselves, it is time to give you a brief description of our class curriculum"
    hide Michelle
    "*press to check the curriculum* (IMAGE BUTTON)"
    show michelle happy at center with dissolve
    mich "Now that I have given you the possible topics for the class, I expect everyone to have their expectations set on how the subject will, again I look forward to this semester with everyone and class dismissed."
    hide michelle
    "*everyone goes into frenzy as the class ends*"
    scene bg fieldday with move
    show dormmate sad_uniform at right with dissolve
    dormmate "Yow dude, did you just see the curriculum for that subject! Just by looking at the topics it feels like it’s getting brutal"
    show mc sad_uniform at left with dissolve
    mc "Tell me about it, just reading the first topic already made my mind about to explode."
    "*Johnny walks by*"
    show lurs happy_uniform at center with dissolve
    lurs "Oh, hi there fellas! The last time we saw each other was during the freshmen orientation, how ya’ll been doing?"
    mc "Hello Johnny! Nice seeing you again and I see that your as lively as ever, the topics seem so hard don’t ya think?"
    hide dormmate
    show mc happy_uniform at left with dissolve
    show lurs happy_uniform at right with dissolve
    mich "I think that it isn’t really that hard since it’s still just the basic when it comes to computer science, I can help you when things get rough for you!"
    show mc happy_uniform at left with dissolve
    mc "I'll keep that in min. Thanks!"

    scene bg fieldday with move
    show dormmate neutral_uniform at right with dissolve
    dormmate "That dude's wierd, but he is cool after all"
    show mc neutral_uniform at left with dissolve
    mc "I think so too, maybe we're just being too you know"
    hide dormmate admiring_casual
    show just sad_uniform at right with dissolve
    dormmate "Being too what?"
    show mc neutral_uniform at left with dissolve
    mc "Nevermind, it’s nothing you really are slow when it comes to things at times lol"
    hide dormmate
    show dormmate happy_uniform at right with dissolve
    dormmate "You’re not wrong there, anyways I heard that there’s going to be an event"
    hide mc
    show mc shocked_uniform at left with dissolve
    mc "Oh really? What's your source on this said event?"
    dormmate " I just kinda heard our classmates talking about it earlier, maybe some of them has some knowledge about it?"
    hide mc
    show mc neutral_uniform at left with dissolve
    mc "Hmm maybe it’s just rumors tho. You know what I just met an upperclassmen we can ask for the credibility of the event"
    dormmate "Alright then, let's go"
    hide mc
    hide dormmate
    "*Both character and [dormmate] goes to the CSC office"
    scene bg csc with fade
    show mike neutral_uniform at right with dissolve
    mike "Hi th....... Oh haven't I seen you before"
    "*brief pause*"
    hide mike
    show mike happy_uniform at right with dissolve
    mike "Oh you're that one that once brought logos! How may I help my dearest kohai"
    menu:
        "Koninchiwa Senpai! Were just here to ask if there really is a freshmen party upcoming":
            $ points += 1
            show mc happy_uniform at left with dissolve
            show mike happy_uniform at right with dissolve
            mike "Oh yes there certainly is, it’s this upcoming week. There are lots of stuff coming up however the big one is an upcoming concert featuring bands from our college department!"
        "Again with this weird Japanese thing, anyways we wanna know if there really is an upcoming freshman party?":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            show lurs sad_uniform at right with dissolve
            mike "No need to be stingy! This is just a me thing, going back to your question it is true that there is an upcoming freshman party and the big stuff is that there is a concert where the bands comes from our department"
    hide mike
    show dormmate confused_uniform at right with dissolve
    dormmate "If that’s the case, are students excused during the said event?"
    show mike happy_uniform at center with dissolve
    mike "There is a chance that students are only excused from their 5 o clock classes onwards if it is applicable to their schedule"
    hide dormmate
    show dormmate sad_uniform at right with dissolve
    dormmate " Ohh it’s look’s like there are going to be some problems with our schedule during the freshman party character"
    hide mc
    show mc neutral_uniform at left with dissolve
    mc "Seems like it. Hold on lemme check our schedule first *pulls out phone and shows schedule*"
    hide dormmate
    hide mc
    hide mike
    "*screen will show a scheduler (kahit eme eme na lang)"
    show mc neutral_uniform at left with dissolve
    show dormmate neutral_uniform at right with dissolve
    mc "Looks like it really will affect our Basic Programming subject. Speaking of we need to get our PE uniforms as well"
    "*mike overhears them*"
    show mike happy_uniform at center with dissolve
    mike "Ohh you haven’t claimed your PE uniforms yet as well?? You must be able to get that uniform you know, given that you will need that in your PE class and soon HATAw event"
    mc "You're right, we better hurry up and get going. Thanks kuya Mike!"
    show mike happy_uniform at center with dissolve
    mike "Sure sure no problem!!"
    hide mike
    hide mc
    hide dormmate
    "*character and roommate leaves the room, and they proceed to the registar to claim their PE*"
    scene bg registar with fade
    show mc happy_uniform at left with dissolve
    mc " Hi! Manong guard where could the office for claiming the PE uniform be?"
    show emil angry at right with dissolve
    guard "Just go inside in the registrar and from their you would be able to claim your uniform."
    show mc happy_uniform at left with dissolve
    mc "Thank you po!"
    hide mc
    hide emil
    scene bg registrar with fade
    show madam_alexandra happy at right with dissolve
    madam "Here to claim your PE uniform?"
    show mc happy_uniform at left with fade
    mc "Yes ma'am hehe"
    hide madam
    show madam_alexandra happy at right with dissolve
    madam "Here you go boy, That's (n) pesos"
    show mc happy_uniform at left with dissolve
    mc "Yes Madam! Duly noted"

    hide mc
    hide madam
    "*character returns back to the dormitory*"
    scene bg roomaft with fade
    show mc happy_casual with fade
    mc "Finally got my PE uniform, now that I look at it we have a PE schedule upcoming! Better get some rest because tomorrows going to be one hell of a day!"
    "*goes to bed early*"
    scene bg roomday with fade
    show mc sleepy_casual
    mc "Ughhhh……………. Oh shit I’m latee for class!! I better get my things together and get ready."
    scene bg crday with fade
    show mc confused_casual with dissolve
    menu:
        "Roommate is that you? I’m sorry if I am being too persistent but can you go a little faster in your bath?":
            $ points += 1
            show mc happy_uniform at left with dissolve
            roommate "*Oh sorry bout that character, I'm almost done now"
        "Really roommate????? Are you seriously going to take too long to take a bath!!":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            roommate "*Oh..............."
    "*[roommate] leaves the shower"
    show roommate sad_casual at right with dissolve
    roommate "Sorry about that character"
    hide roommate
    hide mc
    "*Character then proceeds to the bathroom*"
    scene bg roomday with fade
    "*Character finally finsihes taking a bath"
    show mc happy_pe with dissolve
    mc "Ahh I'm finally done getting ready! I wonder we're gonna do today for PE hmm"
    scene bg liveday with fade
    show dormmate happy_pe at right with dissolve
    dormmate " Hey character! Are you ready for the first day of PE!"
    show mc happy_pe at left with dissolve
    mc "I sure as hell do! Let's go now"
    hide mc
    hide dormmate
    "*both of them proceeds to the oval*"
    scene bg ovalday with fade
    show devier happy with dissolve
    dev "All right class! Is everybody here?? *Good! Now before we start I am your professor Mr. Devier for this PE class! Now that you know who I am, it is your time to tell me about yourselves."
    hide Devier
    "*mini cutscene where everyone introdcues smthn like that*"
    show devier neutral at right with dissolve
    dev "And lastly we have........."
    dev "*character*"
    show mc happy_pe at left with dissolve
    mc "Hello sir! My name is [mcname] and I am from [loc], it’s nice to meet you sir!"
    dev "You don't look so so athletic there, just kidding HAHA"
    menu:
        "Hehehe, maybe sir, tho I am somehow confident in what I can do!":
            $ points += 1
            show mc happy_uniform at left with dissolve
            show devier happy at right with dissolve
            dev "HAHAHAAHAHA! That's spirit kiddo! I love the confidence!"
        "Pfft! Don’t you understand me old man! I’ll show you what I can do!":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            show devier angry at right with dissolve
            dev "ou know there’s a fine line between confidence and arrogance son!"
    hide mc
    hide dev
    show dev neutral with dissolve
    dev "Anyways let me get straight to the point"
    dev "as you all know this is the PE class, so from here on there will be lots of tiring activities to do"
    dev "Prepare yourselves as this class will not be easy"
    hide devier
    show dormmate confused at left with dissolve
    dormmate "Sir, what is it that we'll be doing today?"
    show devier happy at right with dissolve
    dev "That’s a good question, let’s start off with athletics! I’ll pair you up with someone and then we can begin the exercise."
    hide devier
    "*proceeds to group up the class"
    show devier happy with dissolve
    dev "Now that you’ve seen your partner, we fetch you up to play against each other. Whoever scores the first in the finish line wins and gets additional points! Alright settle down with your pair and goodluck!"
    hide devier
    "*everyone proceeds to their partner"
    show mc happy_pe at left with dissolve
    mc "Huh I guess it’s you and me that gets partnered again here huh dormate"
    show dormmate happy_pe at right with dissolve
    dormmate "HAHAHAHAHA what are the odds character! I guess this means we begin a friendly rivalry here!"
    mc "Bring it on dormmate!"
    hide mc
    hide dormmate
    show mc confused_pe at left with dissolve
    show dormmate confused_pe at right with dissolve
    "*someone raises their hand*"
    hide mc
    hide dormmate
    show lurs confused_pe with dissolve
    lurs "Uhmm………. Sir I don’t have a partner yet."
    hide lurs
    show devier happy with dissolve
    dev "Ok then, anyone who doesn't have a partner yet?"
    "*awkward silence*"
    hide devier
    show devier neutral with dissolve
    dev "Alright it seems like everyone has been paired already, now one pair is going to have to adopt him."
    "*dev looks around*"
    show dev happy with dissolve
    dev "You there character! Take Johnny in and you three will race it out later."
    hide devier
    "*Johnny approaches character and [dormmate]"
    show lurs neutral_pe at right with dissolve
    lurs "Hi! Ahehe it’s me again, I hope you don’t mind me grouping up with you"
    menu:
        "Sure sure! I don’t mind at all! May the best man win!":
            $ points += 1
            show mc happy_pe at left with dissolve
            show dormmate happy_pe at right with dissolve
            show lurs happy_pe at center with dissolve
            lurs "Huh, may the best man win! You to dormate"
        "HAHAHAAHAHAH loser, don’t you worry I’ll win the race in an instant WHAHAHAHA!":
            $ points -= 1
            show mc angry_pe at left with dissolve
            show dormmate sad_pe at right with dissolve
            show lurs sad_pe at center with dissolve
            lurs "Ohh huhuhuhu"
            dormmate "Don't be like that character, don't mind him Johnny he can be real stingy sometimes"

    hide dormmate
    hide mc
    hide lurs
    show devier happy at right with dissolve
    dev " Alright you three get ready as you will all play together, are you ready?"
    show mc happy_pe at left with dissolve
    mc "Yes sir!"
    dev "Alright then, on your marks, get set, GOOOOOOOOO!!!!"
    #MINI GAME NA MAY RACE MAN DAA
    scene bg ovalday with fade
    show devier happy with dissolve
    dev "Well done everyone! You all seem so fit to be great at this, as expected, you surpassed my expectation there character!"
    hide devier
    show mc tired_pe with dissolve
    mc "Thank you sir *gasping for air*"
    hide mc
    show devier happy with dissolve
    dev "Ok now everyone, now that we are done with our first meeting, get some rest and prepare for your next subject. Class dismissed"
    hide devier
    "*Everyone goes away from the oval as they all prepare for their next class*"
    "*Character and dormmate go back into the dorm*"
    show mc shocked_pe at left with dissolve
    mc "Holy macaroni, I did not expect that we’d get put into the fire that quickly. *gasping*"
    show dormmate tired_pe at right with dissolve
    dormmate " Tell me about it. Oh I almost forgot that the freshman party is nearing the horizon, what do you plan to do?"
    hide mc
    show mc neutral_pe at left with dissolve
    mc "Nothing really much to be honest, there’s a quiz upcoming in our Intro to Computing class. So I need to review as much as I can."
    dormmate "You’re right, I almost forgot that! Anyways, I must also study hard for the upcoming quiz, it surely won’t be easy."
    mc "Sure as hell won't be easy."
    hide mc
    hide dormmate
    "*Fast forward to the quiz day.*"
    scene bg dormday with fade
    "*[dormmate] and [mc] sees each other in the room."
    show mc happy_uniform at left with dissolve
    mc "Are you ready for the quiz [dormmate]?"
    show dormmate happy_uniform at right with dissolve
    dormmate "Sure as hell I am! Anyways we should get going! We don’t want to be late again for this quiz."
    mc "You really are an easy going one, huh? Anyways, let's go."
    scene bg comlab with fade
    "*[mc] and [dormmate] arrives.*"
    show bg comlab with fade
    show michelle happy with dissolve
    mich "Alright class, is everyone here now?"
    "*play audible yes*"
    mich "Good, now that you are all here please keep your phones, put your bags in front, no cheating, and good luck everyone!"
    hide michelle
    "*Madam Michelle opens the test on the class LMS.*"
    show mc shocked_uniform with dissolve
    mc " Holy guacamole! What the hell, I have no idea what these are!"
    show halfblack 
    centered "{color=#ffffff}{size=+24}Answer each questions presented...{/color}"
    centered "{color=#ffffff}{size=+24}You'll only have 12 seconds for each. Good luck!{/color}"

    hide mc

    $ in_story = True
    #set the quiz
    $ set_quiz_loc("standard") 
    $ set_quiz("Os Fundamentals")
    jump init_quiz
    "*MINI GAME QUIZ PLAYS*"
    "*CHAPTER 1 ends (after the choice)"
    #There will be choice where the character can cheat or finish the exam honestly
    #Based on his score/choice will chapter 2 start

label cheat_quiz:
    show bg comlab with fade
    "add the choices here" #cheat starts during the 10th question or pwede namang baguhin

    #to restart timer
    show screen countdown
    #return to quiz
    call screen quiz_proper

label chapter_2:
    "chapter 2"

return
