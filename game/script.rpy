#all the initializations are in variables_init
#friend_1 = Carlos/Carla
#friend_2 = Justin/Jasmine

init python:
    in_story = False

    def set_gender(selected_gender):
        persistent.gender = selected_gender
        global pronoun_referred
        global pronoun_belonging
        global pronoun_respect
        global friend_1
        global friend_2

        if persistent.gender == "male":
            pronoun_referred = "he"
            pronoun_belonging = "his"
            pronoun_respect = "mister"
            friend_1 = "Carlos"
            friend_2 = "Justin"

        else:
            pronoun_referred = "she"
            pronoun_belonging = "her"
            pronoun_respect = "miss"
            friend_1 = "Carla"
            friend_2 = "Jasmine"            

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
    show emil angry at right with dissolve:
        ease 0.7 xalign 0.9
    show mc confused_casual at left with dissolve:
        xoffset -400
        ease 0.6 xoffset 100

    menu:
        "Yes sir, I’m sorry I didn’t know, won’t happen again":
            $ emil_decision = "good"
            $ points += 1
            show mc shocked_casual at left with dissolve
            show emil neutral at right with dissolve
            emil "Ok, sorry for raising my voice, but please do not forget when doing so, here’s the keys to your room."

        "Silence, (*proceeds to logbook*)":
            $ emil_decision = "neutral"
            show mc sleepy_casual at left with dissolve
            emil "(*silence*)"

        "Pff! Couldn’t you be any nicer to the new guys?!":
            $ emil_decision = "bad"
            $ points -= 1
            show mc angry_casual at left with dissolve
            emil "HUH! Is that how your mother taught you how to interact with others?! Anyways, here’s your key!"

    hide emil
    scene bg roomday with dissolve
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

    scene bg roomaft with dissolve
    show mc happy_casual at left
    mc "Oh, hi there!"
    show friend_1 sad_casual at right
    friend_1 "Errr..."
    mc "You must be my new roommate! My name is [mcname], what’s your name?"
    friend_1 "Hello, my name is ugh... [friend_1]."
    mc "Nice to meet you [friend_1]! I’m from ..."
    $ place = renpy.input("Where are you from?", length=50)
    $ place = place.strip()
    mc "I’m from [place]. How about you?"
    friend_1 "I’m from eehhh……. My parents are actually from Goa, but I live in Naga actually."
    mc "That's nice! I think we should hang out more. I'm sure we'll be pretty close as days pass by."
    show friend_1 neutral_casual at right
    friend_1 "Uhm... Yeah, sure."
    mc "Would you like to join me later for dinner? I'd really like to have a conversation with you. You'll be my first ever friend here."
    friend_1 "Okay, I guess."

    hide mc
    hide friend_1
    scene cutscene3 # time passes by CLOCK ANIMATIOOOOON
    scene cutscene4 # mc and a femc bumped each other


    show mc shocked_casual at left
    show madam_alexandra shocked at right
    menu:
        "I’m sorry miss, I didn’t see you there.":
            $ points += 1
            show madam_alexandra neutral at right
            "???" "Oh, no worries."
            $ madam_decision = "good"
        "Watch where you're going miss!":
            $ points -= 1
            show mc angry_casual at left
            show madam_alexandra angry at right
            $ madam_decision = "neutral"
            "???" "Huh! Kids these days are so rude!"
            show madam_alexandra angry at right:
                linear 1.0
                xalign 2.0
            $ madam_decision = "bad"

    hide madam_alexandra
    hide mc
    hide friend_1

    scene cutscene5 # dinner mc and friend_1
    scene cutscene6 # next day arrives

    scene bg roomday with dissolve
    show mc sleepy_casual with dissolve
    mc "It's morning already?! I still want to sleep."
    # make this Itallic
    mc "I forgot that I still haven’t claimed my COR for ID and my uniform has not yet been sewn yet, I guess I should go to the registrar first and then go to the tailor to get my uniform tailored."
    scene cutscene7 # daily routine
    hide mc
    scene bg livday
    show friend_2 admiring_casual
    friend_2 "Good morning fellow dormer!"
    show friend_2 admiring_casual at right
    show mc neutral_casual at left

    menu:
        "Hello, good morning to you too!":
            $ points += 1
            show mc happy_casual at left
            friend_2 "Hello! You’re new here too huh? What course are you from? I’m [friend_2] from BS Computer Science, 1st year"
            mc "I'm [mcname]! I guess were in the same program I see."

        "*Ignores*":
            friend_2 "Quite the shy type huh, what course are you from?"
            show friend_2 happy_casual at right with dissolve
            friend_2 "I’m [friend_2] from BS Computer Science, 1st year"
            mc "I'm [mcname]! I guess were in the same program I see."

        "Who in the world are you?":
            $ points -= 1
            show mc angry_casual at left
            show friend_2 confused_casual at right with dissolve
            friend_2 "Woah woah, chill dude hehe."
            show friend_2 happy_casual at right with dissolve
            friend_2 "I mean no harm just wanted to interact, I’m [friend_2] from BS Computer Science, 1st year"
            show mc neutral_casual at left with dissolve
            mc "Oh, my bad. Anyway, I'm [mcname]. I guess were in the same program I see."

    friend_2 "Nice! By any chance do you have your COR already?"
    mc "I haven’t, I’m just about to go to the registrar to claim it."
    friend_2 "Great! Why don’t we go there together?"
    mc "Sounds great! Let's go."

    with dissolve
    scene bg registrar # this is where I left off GAMEEEEE
    n "And there [friend_2] and [mcname] goes on to go to the registrar together to claim their respective COR. Just as [mcname] came near the registrar windows, [pronoun_belonging] face turns pale as [pronoun_referred] saw the mystery woman in the registrar’s office"
    show mc shocked_uniform at left with dissolve
    show madam_alexandra neutral at right with dissolve
    mc "Uhh………. Uhm………. Hi madam, I apologise for what happened last night huhu"

    if madam_decision == "good":
        show madam_alexandra happy at right with dissolve
        madam "Hello there, [pronoun_respect]! I see that you are also from the College of Science, I also apologise for bumping into you yesterday. How may I help you?"
    elif madam_decision == "bad" or madam_decision == "neutral":
        show madam_alexandra annoyed at right with dissolve
        madam "Well well well, if it isn’t [pronoun_respect] bump, no apology here, what can you do for you?"

    show mc neutral_uniform at left with dissolve

    mc "I would like to get my COR so that if ever that our professor needs it we can show it, Madam."
    madam "Sure, however it’ll take a few minutes before we can process it."
    mc "No problem Madam, thank you!"

    hide madam_alexandra
    hide mc

    "*Waits a few minutes, [mcname] and [friend_2] goes out*"

    scene bg walkaft with dissolve
    show mc happy_uniform at left with dissolve
    show friend_2 happy_uniform at right with dissolve
    friend_2 "Now that we have already claimed the COR, where are we going now?"
    mc "I’m going to the tailor, I don't have enough uniforms to wear."
    friend_2 "Alright then, I’ll see you back to the dorm then!"
    mc "See ya!"

    scene bg tailorshop with pixellate
    show mc happy_uniform at left with dissolve
    mc "{i}Tao po! Pwede po magpatahi uniform?{/i}"
    show erin happy at right with dissolve
    aling "Good morning! Surely, what is it that you needed [pronoun_respect]?"
    mc "I need a uniform for BU, is it possible that it'd be finished this weekend?"
    aling "Sure [pronoun_respect]! Let me get your measurements."
    scene measures_mc with Pause(5)
    mc "Thank you, {i}aling{/i}! I'll be on my way. Good bye, ma'am!"
    aling "Ok [pronoun_respect]! Take care"

    scene bg dormaft with dissolve
    n "*[mcname] goes back to [pronoun_belonging] dorm, and when [pronoun_referred] arrives at [pronoun_belonging] room the door is locked and [pronoun_referred] forgot [pronoun_belonging] keys. [pronoun_referred!c] goes and asks Kuya Emil if [pronoun_referred] could borrow his keys*"

    scene bg livaft with dissolve
    show mc neutral_uniform with dissolve
    mc "Kuya Emil can I borrow the keys for our room, I might’ve forgot the key inside"

    if emil_decision == "good":
        show mc neutral_uniform:
            xalign 0.5
            ease 0.7 xalign 0.1
        show emil angry:
            xoffset 1500
            ease 0.7 xoffset 1100
        emil "Here you go, kiddo!"
    elif emil_decision == "bad" or emil_decision == "neutral":
        show mc sad_uniform:
            xalign 0.5
            ease 0.7 xalign 0.1
        show emil angry:
            xoffset 1500
            ease 0.7 xoffset 1100
        emil "Heh! Keys are given to you to use for opening the door, not for decoration! Next time you forget your key, you’ll be waiting for your roommate to come home before you open your door!"

    hide emil
    hide mc
    scene bg frontnight with dissolve
    n "The first official day for classes in Bicol University has officially began. The students and faculties are roaming as much as before, lots of students are having a hard time navigating the campus, the sound of vehicles during rush feels like the world has reverted back to normal."
    n "And just before official lectures start, orientation for freshmen will happen."

    "*Next day arrives*"

    scene bg roomday with dissolve
    show mc happy_uniform at left with dissolve
    mc "Today’s finally the day! I get to meet my new classmates, I wonder what they look like or their personality hmmm."
    mc "Guess I’ll just go with [friend_2] during the orientation, having a familiar face is always a good thing. Right, [friend_1]?"
    show friend_1 sleepy_casual at right with fade
    friend_1 "*snores*"
    show mc confused_uniform at left with dissolve
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
    show friend_2 happy_uniform with dissolve:
        xoffset 2000
        ease 1.5 xoffset 1100
    friend_2 "Just in time [mcname]! I was waiting for you so we can go out together. "
    show mc happy_uniform with dissolve
    mc "Let's go!"

    show mc:
        ease 2 xoffset 2000
    show friend_2:
        ease 1.75 xoffset 2500
    "*They proceed to the orientation hall*"

    scene bg building1 with fade
    n "As they arrrive in the room, [pronoun_referred] can hear students murmuring, the place as lively as usual."
    show friend_2 shocked_uniform at left with dissolve
    friend_2 "Sheeeesh, there are lots of students! I have no idea where we should be designated!"
    show mc shocked_uniform at right with dissolve
    mc "I guess we should just look for someone who we are familiar with, maybe a familiar face in the groupchat?"
    friend_2 "I've never checked the groupchat so far LOL"
    show mc confused_uniform at right with dissolve
    mc "Then were doooommmeeeedddd!!!!!!"
    show friend_2 neutral_uniform with dissolve
    "*another student approaches, a guy with glasses with casual shirt and braces approaches*"
    show lurs neutral_uniform:
        xoffset 2000
        ease 1.2 xoffset 650
    lurs "*bumps into [mcname]*"
    show lurs shocked_uniform with dissolve
    show mc shocked_uniform with dissolve
    show friend_2 confused_uniform with dissolve
    "???" "Ohhh... Sorry about that [pronoun_respect] hehe, may I ask where the section is for Computer Science?"

    menu:
        "Oh, hi there. Are you also a computer science freshman? My name is [mcname] and this is [friend_2]!":
            $ points += 1
            scene bg building1 with fade
            hide friend_2
            show mc happy_uniform:
                xalign 0.1
            show lurs happy_uniform:
                xalign 0.9
            lurs "Nice to meet you both! Yes, I am a freshman student of Computer Science! Thanks for having me. I'm Johnny, by the way."
            mc "Let's head to the section, shall we?"
            lurs "Sure."
            $ johnny_decision = "good"

        "*Ignores*":
            scene bg building1 with fade
            show mc confused_uniform:
                xalign 0.1
            show lurs nervous_uniform:
                xalign 0.9
            lurs "Uhmmm... I'm Johnny, nice to uhhh... meet you"
            mc "*tsk*"
            $ johnny_decision = "neutral"

        "Watch it nerd! Are your glasses just for clout?":
            $ points -= 1
            show mc angry_uniform:
                xalign 0.1
            show lurs nervous_uniform:
                xalign 0.9
            lurs "I’m sorry! I’m sorry! I didn’t mean to bump into you!"
            mc "*tsk* How could you not even see me standing here."
            $ johnny_decision = "bad"

    scene bg comlab with fade
    hide mc
    hide lurs
    "*They proceed to the computer science section*"

    "*Orientation noise and mess*"
    scene bg building1 with pixellate
    "*orientation ends*"
    show joseyde happy at center
    j "Okay, now that the orientation has ended, I highly recommend that you get to know your blocmates first to bond and create memories. Thank you everyone and have a blessed afternoon."
    "*applauses*"

    scene bg fieldday with dissolve
    show mc happy_uniform at left with dissolve
    mc "Where do we go now [friend_2]?"
    show friend_2 confused_uniform at right with dissolve
    friend_2 "I dunno, maybe let’s go talk to some of our classmates then?"
    scene cutscene_chatting # CHATTING CUTSCENE PLEEEEEAAASEEEE
    "*encounters Johnny*"
    scene bg fieldday with dissolve

    hide friend_2
    if johnny_decision == "good":
        show lurs happy_uniform with dissolve:
            xalign 0.9
        show mc neutral_uniform with dissolve:
            xalign 0.1
        lurs "Oh, hey there! It appears that we’re actually classmates! I hope to get to know you guys better!"
        show friend_2 happy_uniform:
            xoffset -300
            ease 1.3 xoffset 500
        show mc happy_uniform:
            ease 1 xalign 0.05

        mc "Hey, there. Nice seeing you here."
        friend_2 "Oh yeah. Where are you off to?"
        lurs "I'm actually heading home, I have to do something today."

    elif johnny_decision == "bad" or johnny_decision == "neutral":
        show lurs sad_uniform at right with dissolve
        lurs "Oh, hehe. Sorry about earlier."
        mc "Actually, I should be the one to say sorry."
        mc "Uhm... Sorry, Johnny, was it?"
        lurs "Ah, yes! You remembered?"
        mc "It's fine. Actually, I'll be heading home now. Nice to officially meet you, by the way."

    mc "Alright, then. See ya"
    friend_2 "See you, next time Johnny."
    lurs "Bye"
    show lurs:
        ease 2 xoffset 1500
    show friend_2:
        ease 1 xalign 0.9 xoffset 0
    show mc:
        ease 0.5 xalign 0.1
    "*Johnny goes away*"
    hide lurs

    show mc neutral_uniform with dissolve
    mc "Oh well, I just hope we get to go along with our other classmates."
    show friend_2 neutral_uniform with dissolve
    friend_2 "Yeah, let's hope for the best. Shall we go back?"
    mc "Yep. Time to go."


    hide mc
    hide friend_2
    scene bg dormday with pushup
    "*[mcname] and [friend_2] arrives at Dormitory*"
    # this is where I left off CODE REVISION
    scene bg momcall with dissolve

    menu:
        "*Answer Call*":    # CREATE A PHONE CALL BG. ROOM BEING BLURRED BG WITH PHONE CENTER AND MOM PIC INSIDE. VARIATION WITH MOM EMOTIONS
            $ points += 1
            show mom happy at right
            mom "Hi dear, you haven’t called in a while so I had to call you just to check on you. How’s college been?"
            jump mom_convo


        "*No answer*":
            $ points -= 1

label mom_convo:
    menu:
        "So far it’s been good ma! Our class haven’t officially started but so far it’s been great!":
            show mc happy_casual at left
            show mom happy at right
            mom "Oh that’s good to hear! Keep up the good work son/daughter and remember to not pressure yourself that much and just have fun alright?"

        "It’s been absolute hell! All the people here always rubs me of the wrong way!":
            show mc angry_casual at left
            show mom sad at right
            mom "I know that college is tough but don’t be like that now. There will always be something positive to look forward in tough  situations, alway remember if you ever need help we’ll be here. Take care now"

    show mc happy_casual at left with fade
    mc "Ok ma,  I better keep going now I still have to fix my things. Bye!"
    show mom happy at right
    mom " Bye *name*, mama always loves you mwa mwa"
    "*sound of phone stops*"
    scene bg dormday
    show mc happy_casual at center
    mc "I need to go fetch my uniform now since tomorrow our lectures will officially begin"

    "*Character travels to the tailor shop"

    scene bg tailorshop with pixellate
    show mc happy_casual at left with dissolve
    mc "{i}Magandang araw po! Kukuha po sana ako nung uniform kong pintahi ho nung nakaraan.{/i}"
    show erin happy at right
    aling "Well hello there iho! You’re uniform is already done, however there is one thing that is missing. I forgot to tell you that you should’ve bought your logo from the department since our store already run out of it. I sincerely apologise if I informed you way to late"
    menu:
        "No worries, Aling Erin! I’ll just buy from our department. Thank you aling! *gives money*":
            $ points += 1
            aling "I do apologise again young man for your inconvenience, I’ll just give you a discount for your troubles. Take care!"

        "*Well you could’ve told me that earlier! Now I have to pay you full for not finishing my uniform, unfair but still thanks tsk tsk *gives money*":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show erin sad at right with dissolve
            aling "My apologies young man, please do not take it to hard since I'm old and have lots of customers to accommodate,I’ll just give you a discount for your troubles, i again apologize young man"

    "*character leaves  the sewing shop, while he waits for jeeps to pass by he sees his old crush Crush walking towards him without her noticing him*"
    scene bg frontday with dissolve
    show mc shocked_casual at center with ease
    mc "Oh shizz, it's Sofia!! What do I do? What do I sayyyy??????"
    menu:
        "Hi Crush! Ho.. how… how’s… what’s up? Hehe *blushes* + Crush":
            $ points += 1
            show mc blushed_casual at left with fade
            show sophia happy_uniform at right with dissolve
            crush "Oh hey there character! It’s been summer since I last saw you huh, I would love to keep the chat going but I have a class to attend so I better be going. Bye! It was nice talking to you again!"


        "*Whit whew* hey there beautiful, hehe just kidding. Sup Crush? ":
            $ points -= 1
            show mc neutral_casual at left with dissolve
            show sophia awkward_uniform at right with dissolve
            crush "Oh hehe…. character  uhhh. I still have a class to go to so I better keep going. Bye *said in an awkward manner*"

    mc "Byee! See ya around!"
    hide sophia with fade
    "*Crush walks away hurridley since she has class to attend, meanwhile character is blushed and all*"
    scene bg frontday with dissolve
    show mc blushed_casual at center with fade
    mc "UGGGHHHHHHH!!! SHE’S AS CUTE AS EVER!!! *poker face bigla* ok calm down I still have to buy some logos for my uniforms."
    "*jeepney stops, character goes inside*"

    scene bg jeep with irisin
    show mc happy_casual at left with fade
    mc "{i}Kuya bayad po{/i}"
    show mark neutral at right with fade
    mark "{i}Sa may san toh{/i}"
    mc "{i}Sa may CM lang ho{/i}"
    "The to the fare that character gave is given back"
    scene jeep with ease
    menu:
        "{i}Kuya kulang ho ang skuli, estudyante ho ako {/i}":
            $ points += 1
            show mc confused_casual at left with dissolve
            show mark happy at right with dissolve
            mark "{i}Ayy ganon ba iho? Eto pasenya ka na ah, matanda na ang mamang hehe{/i}"


        "Kuya ba’t eto lang sukli?! Ang lapit lapit nga lang ng patahian sa BU tapos sobra ka pa maningil. Estudyante pa ako kaya dapat di ganto singil niyo!":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show mark sad at right with dissolve
            mark "{i}Hay nako nagkamali lang siguro ako panukli, ang bibig ng kabataan ngayon talagang antatalas ng mga dila{/i}"

    hide mark
    hide mc

    "*character arrives at BU, and goes straight to the CSC office*"

    scene bg csc with fade
    show mc happy_casual at left with fade
    mc "Good afternoon po! Are there still available logos for our uniform?"
    show mike happy_uniform at right with fade
    mike "Hello! Yes there are still some, come in and have a sit."
    hide mike
    "*character waits for a bit*"
    scene bg csc with dissolve
    show mc happy_casual at left with dissolve
    show mike happy_uniform at right with dissolve
    mike "sorry for the wait, here are your logos"
    hide mike
    show mike confused_uniform at right with dissolve
    mike "You look so familiar......."
    mike "Feels like I've seen you somewhere hmm"
    show mc neutral_casual at left with dissolve
    mc "Really? I've only been here for a few days"
    mike "Say weren't you in the freshmen orientation a few days ago?"
    hide mc
    show mc happy_casual at left with dissolve
    mc " Yes I am, you don’t happen to be a Computer Science student as well are you?"
    hide mike
    show mike happy_uniform at right with dissolve
    mike "What a coincidence I actually am! I am a third year student and it looks like you’d be calling me “senpai” eyy! Just kidding "
    menu:
        "Nice to meet you “senpai”! I look forward to working with you in the future, I better":
            $ points += 1
            show mc happy_casual at left with dissolve
            show mike happy_uniform at right with dissolve
            mike "I see! Take care my *kohai*"

        "Sheesh no need to be stingy about it hey hey hey! Anyways take care when you get home!":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show mike sad_uniform at right with dissolve
            mark "Sheesh no need to be stingy about it hey hey hey! Anyways take care when you get home!"

    hide mc
    hide mike

    "*After obtaining the logos, character goes to the dorm*"

    scene bg dormaft with blinds
    show emil neutral at right with dissolve
    emil "You look kinda tired kiddo, college’s been making things tough for ya huh?"
    show mc sad_casual at left with dissolve
    mc "Tell me about it, we haven’t even started official lecture classes but it already feels like I’ve had lots of things done"
    emil "Well don’t sweat, you’ll get the hang of it soon. Wish you luck kiddo"

    menu:
        "Thanks kuya Emil! Gon need it!":
            $ points += 1
            show mc happy_casual at left with dissolve
            show emil happy at right with dissolve
            emil "Sure kiddo, best of luck"

        "I don’t need your goodluck ":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show emil angry at right with dissolve
            emil "Cocky as usual"

    "*Character proceeds to his room*"

    scene bg roomaft with move
    "*Internally, the character talks to himself*"
    show mc sad_casual at center with dissolve
    mc "{b} Hays, is it really necessary that I still put a logo on this uniform? It’s not like the guard will notice me not having this already. Oh well, guess better keep doing this now{/b}"

    "*MINI GAME (IF APPLICABLE), THERE WILL BE UNIQUE DIALOGUES IF MAKAGAWA MINI GAME, IF HINDI KAYA PROCEED LANG.*"

    hide mc
    show mc neutral_casual at center with dissolve
    mc " Now that I’ve sewn these uniforms, I now need to iron the clothes so they may look presentable when going to class"

    hide mc
    "*MIGHT MINI GAME NOT SURE"
    show mc happy_casual at center with dissolve
    mc " Finally done with the chores, now I have to prepare for my classes tomorrow"

    "*INTERACTABLE PHOTOS (CAN USE IMAGE MAP feature)*"

    hide mc
    "*Next day arrives, alarm rings*"
    scene bg roomday with hpunch
    show mc sleepy_casual at center with dissolve
    mc "Uggggghhhhhhh *with hagard jwu look*……………. It’s really here the first day of classes, I just hope that the profs are nice."
    hide mc
    show mc shocked_casual at left with dissolve
    mc "Ohh [friend_1] is almost awake, I must've been very noisy"
    show friend_1 sleepy_casual at right with dissolve
    friend_1 "Uggghhhh……………. Good morning, want to go out for breakfast?"
    menu:
        "I would love to! But I need to be early for the first day so I can’t . Let’s do it next time!":
            $ points += 1
            show mc happy_casual at left with dissolve
            show friend_1 happy_casual at right with dissolve
            friend_1 "It’s alright, let’s eat next time then"
            hide friend_1
            "*[friend_1] leaves for breakfast*"

        "No thanks, I’m not interested":
            $ points -= 1
            show mc angry_casual at left with dissolve
            show friend_1 sad at right with dissolve
            friend_1 "Oh…….. Ok"
            hide friend_1
            "*[friend_1] leaves for breakfast*"

    scene bg roomday with fade
    show mc happy_casual at center with dissolve
    mc "Ok now that I have finished preparing things, time to clean myself."
    hide mc
    "*character proceeds to go to the CR*"

    scene bg crday with fade
    "*Character and Dormmate bumps into each other*"
    show friend_2 happy_casual at right with dissolve
    friend_2 " Oh hey there character! What a coincidence you just woke up too?"
    show mc neutral_casual at left with dissolve
    mc "nah I just finished preparing my things for the first day of classes, you can never be too prepared"
    show friend_2 happy_casual at right with dissolve
    friend_2 "You seem to be super excited rather than nervous in the first day huh"
    show mc neutral_casual at left with dissolve
    mc "of course! It’s exciting to get to know more people other than the orientation, plus i am somehow excited on how our professors look like and how they act"
    show friend_2 happy_casual at right with dissolve
    friend_2 "Heh…. I wish I had your enthusiasm, anyways we better get going we might be late to class. Let’s go together gooing to class i am kinda nervous hehe."
    show mc neutral_casual at left with dissolve
    mc "aight then I’ll be going now as well"
    hide mc
    hide friend_2
    "*character goes to shower and finishes preparing, character goes to the lobby waiting for their friend*"
    scene bg dormday with pushup
    show mc angry_uniform at center with dissolve
    mc "where the hell is dormmate, were about to be late for the first day of class"
    menu:
        "*Wait for dormmate, even if you get late*":
            $ points += 1
            hide mc
            show mc neutral_uniform at center with dissolve
            mc "I guess it wouldn’t wait to wait for a bit more"
            hide mc "After a few minutes, dormmate arrives"
            show mc angry_casual at left with dissolve
            mc "What the hell have you been doing? We are almost late!"
            show friend_2 sad_uniform at right with dissolve
            friend_2 "Sorry character *tired sighs* I had the urge to take a call of nature at the worst time, I’ve already had my clothes on but i had to take them of cause of the urge."
            hide mc
            show mc neutral_uniform at left with dissolve
            mc "you really had to sugarcoat the term for taking a poop. Anyways we better get going or madam will get mad at us, we should go for a run at it."
            hide mc
            hide friend_2
            "*runs to the room*"
            scene bg comlab with face
            "*Character and [friend_2] both just barely made it in time"
            show mc angry_uniform at left with dissolve
            mc "We barely made it in time! No thanks to you!"
            hide mc
            show mc happy_uniform at left with dissolve
            mc "Just kidding"
            show friend_2 sad_uniform at right with dissolve
            friend_2 "You didn’t need to be so frank with it, lol. It’s what you call being clutch"
            show mc happy_uniform at left with dissolve
            mc "Clutch your face, we better find ourselves a seat now since class is about to begin"

        "Leave Dormmate":
            $ points -= 1
            hide mc
            show mc neutral_uniform
            mc " I should just go now or I’ll be late, and maybe I’ll still arrive in time"
            hide mc
            "*Character goes through the canteen knowing that [pronoun_referred] still has some time"
            scene bg canteenday with fade
            show mc neutral_uniform at center with dissolve
            mc "mm…….. There’s still a few more minutes before time, maybe I can stop by for a little snack *nag snack sa canteen*, oh shit! It’s almost time! I might get late."
            hide mc
            "*character runs to the room*"
            scene bg comlab with fade
            show mc happy_uniform at center with dissolve
            mc "Just in time did I arrive. Now it's time to find myself a seat."
            "*after a few moments, [friend_2] arrives"
            show friend_2 angry_uniform at right with dissolve
            friend_2 "Dude! You literally left me tsk"
            hide mc
            show mc sad_uniform at left with dissolve
            mc "You were taking too long! It was the first day I can’t afford to be late, I’m truly sorry"
            hide friend_2
            show friend_2 happy_uniform at right with dissolve
            friend_2 " Nah I was just messing with ya, I took too long to prepare so that one’s on me"
            hide mc
            show mc neutral_uniform at left with dissolve
            mc "Ok then, go get yourself a seat already cause class will start"

    hide mc
    hide friend_2
    "*After a while, madam Michelle arrived*"
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
            show michelle happy at rght with dissolve
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
    show friend_2 sad_uniform at right with dissolve
    friend_2 "Yow dude, did you just see the curriculum for that subject! Just by looking at the topics it feels like it’s getting brutal"
    show mc sad_uniform at left with dissolve
    mc "Tell me about it, just reading the first topic already made my mind about to explode."
    "*Johnny walks by*"
    show lurs happy_uniform at center with dissolve
    lurs "Oh, hi there fellas! The last time we saw each other was during the freshmen orientation, how ya’ll been doing?"
    mc "Hello Johnny! Nice seeing you again and I see that your as lively as ever, the topics seem so hard don’t ya think?"
    hide friend_2
    show mc happy_uniform at left with dissolve
    show lurs happy_uniform at rght with dissolve
    mich "I think that it isn’t really that hard since it’s still just the basic when it comes to computer science, I can help you when things get rough for you!"
    show mc happy_uniform at left with dissolve
    mc "I'll keep that in min. Thanks!"

    scene bg fieldday with move
    show friend_2 neutral_uniform at right with dissolve
    friend_2 "That dude's wierd, but he is cool after all"
    show mc neutral_uniform at left with dissolve
    mc "I think so too, maybe we're just being too you know"
    hide friend_2 admiring_casual
    show just sad_uniform at right with dissolve
    friend_2 "Being too what?"
    show mc neutral_uniform at left with dissolve
    mc "Nevermind, it’s nothing you really are slow when it comes to things at times lol"
    hide friend_2
    show friend_2 happy_uniform at right with dissolve
    friend_2 "You’re not wrong there, anyways I heard that there’s going to be an event"
    hide mc
    show mc shocked_uniform at left with dissolve
    mc "Oh really? What's your source on this said event?"
    friend_2 " I just kinda heard our classmates talking about it earlier, maybe some of them has some knowledge about it?"
    hide mc
    show mc neutral_uniform at left with dissolve
    mc "Hmm maybe it’s just rumors tho. You know what I just met an upperclassmen we can ask for the credibility of the event"
    friend_2 "Alright then, let's go"
    hide mc
    hide friend_2
    "*Both character and [friend_2] goes to the CSC office"
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
            show mike happy_uniform at rght with dissolve
            mike "Oh yes there certainly is, it’s this upcoming week. There are lots of stuff coming up however the big one is an upcoming concert featuring bands from our college department!"
        "Again with this weird Japanese thing, anyways we wanna know if there really is an upcoming freshman party?":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            show lurs sad_uniform at right with dissolve
            mike "No need to be stingy! This is just a me thing, going back to your question it is true that there is an upcoming freshman party and the big stuff is that there is a concert where the bands comes from our department"
    hide mike
    show friend_2 confused_uniform at right with dissolve
    friend_2 "If that’s the case, are students excused during the said event?"
    show mike happy_uniform at center with dissolve
    mike "There is a chance that students are only excused from their 5 o clock classes onwards if it is applicable to their schedule"
    hide friend_2
    show friend_2 sad_uniform at right with dissolve
    friend_2 " Ohh it’s look’s like there are going to be some problems with our schedule during the freshman party character"
    hide mc
    show mc neutral_uniform at left with dissolve
    mc "Seems like it. Hold on lemme check our schedule first *pulls out phone and shows schedule*"
    hide friend_2
    hide mc
    hide mike
    "*screen will show a scheduler (kahit eme eme na lang)"
    show mc neutral_uniform at left with dissolve
    show friend_2 neutral_uniform at right with dissolve
    mc "Looks like it really will affect our Basic Programming subject. Speaking of we need to get our PE uniforms as well"
    "*mike overhears them*"
    show mike happy_uniform at center with dissolve
    mike "Ohh you haven’t claimed your PE uniforms yet as well?? You must be able to get that uniform you know, given that you will need that in your PE class and soon HATAw event"
    mc "You're right, we better hurry up and get going. Thanks kuya Mike!"
    show mike happy_uniform at center with dissolve
    mike "Sure sure no problem!!"
    hide mike
    hide mc
    hide friend_2
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
            friend_1 "*Oh sorry bout that character, I'm almost done now"
        "Really roommate????? Are you seriously going to take too long to take a bath!!":
            $ points -= 1
            show mc angry_uniform at left with dissolve
            friend_1 "*Oh..............."
    "*[friend_1] leaves the shower"
    show friend_1 sad_casual at right with dissolve
    friend_1 "Sorry about that character"
    hide friend_1
    hide mc
    "*Character then proceeds to the bathroom*"
    scene bg roomday with fade
    "*Character finally finsihes taking a bath"
    show mc happy_pe with dissolve
    mc "Ahh I'm finally done getting ready! I wonder we're gonna do today for PE hmm"
    scene bg liveday with fade
    show friend_2 happy_pe at right with dissolve
    friend_2 " Hey character! Are you ready for the first day of PE!"
    show mc happy_pe at left with dissolve
    mc "I sure as hell do! Let's go now"
    hide mc
    hide friend_2
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
    show friend_2 confused at left with dissolve
    friend_2 "Sir, what is it that we'll be doing today?"
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
    show friend_2 happy_pe at right with dissolve
    friend_2 "HAHAHAHAHA what are the odds character! I guess this means we begin a friendly rivalry here!"
    mc "Bring it on dormmate!"
    hide mc
    hide friend_2
    show mc confused_pe at left with dissolve
    show friend_2 confused_pe at right with dissolve
    "*someone raises their hand*"
    hide mc
    hide friend_2
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
    "*Johnny approaches character and [friend_2]"
    show lurs neutral_pe at right with dissolve
    lurs "Hi! Ahehe it’s me again, I hope you don’t mind me grouping up with you"
    menu:
        "Sure sure! I don’t mind at all! May the best man win!":
            $ points += 1
            show mc happy_pe at left with dissolve
            show friend_2 happy_pe at right with dissolve
            show lurs happy_pe at center with dissolve
            lurs "Huh, may the best man win! You to dormate"
        "HAHAHAAHAHAH loser, don’t you worry I’ll win the race in an instant WHAHAHAHA!":
            $ points -= 1
            show mc angry_pe at left with dissolve
            show friend_2 sad_pe at right with dissolve
            show lurs sad_pe at center with dissolve
            lurs "Ohh huhuhuhu"
            jus "Don't be like that character, don't mind him Johnny he can be real stingy sometimes"

    hide friend_2
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
    show friend_2 tired_pe at right with dissolve
    friend_2 " Tell me about it. Oh I almost forgot that the freshman party is nearing the horizon, what do you plan to do?"
    hide mc
    show mc neutral_pe at left with dissolve
    mc "nothing really much to be honest, there’s a quiz upcoming in our Intro to Computing class. So I need to review as much as I can"
    friend_2 "You’re right I almost forgot that! Anyways I must also study hard for the upcoming quiz, it surely won’t be easy0"
    mc "Sure as hell won't be easy"
    hide mc
    hide friend_2
    "*Fast forward to the quiz day"
    scene bg dormday with fade
    "*dormmate and character sees each other in the room"
    show mc happy_uniform at left with dissolve
    mc "Are you ready for the quiz dormmate?"
    show friend_2 happy_uniform at right with dissolve
    friend_2 "Sure as hell I am! Anyways we should get going we don’t want to be late again for this quiz"
    mc "You are really an easy goig one huh, anyways let's go"
    scene bg comlab with fade
    "*character and dormmate arrives*"
    show bg comlab with fade
    show michelle happy with dissolve
    mich "Alright class, is everyone here now?"
    "*play audible yes*"
    mich " Good, now that you are all here please keep your phones, put your bags infornt, no cheating, and goodlcuk everyone!"
    hide michelle
    "*madam michelle hands out the tests"
    show mc shocked_uniform with dissolve
    mc " Holy guacamole! What is the hell I have no idea what these are!"

    hide mc
    $ in_story = True
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
