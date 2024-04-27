"""
things to fix:
    1. edit quiz ui its shit
    2. edit dormicleaning
    3. add crumpled paper on the side for the cheating
"""

init:
    $ question_num = 0
    $ score = 0
    $ timer_range = 0
    $ timer_jump = 0
    $ paused_time = 0

    $ timeout = 12 # Sets how long in seconds the user has to make a choice
    $ timeout_label = 'wrong'

    #bkt
    $ T = 0.1 #pprobability that the student will learn a skill on the next practice opportunity
    $ S = 0.1 #probability that the student will answer incorrectly despite knowing a skill
    $ G = 0.3 #that the student will answer correctly despite not knowing a skill
    $ A = 0 #action
    $ mastery_threshold = 0.8

image halfblack = "#00000088"
image clock:
    'images/Minigames Menu/timer/12.png'
    pause 1.0
    'images/Minigames Menu/timer/11.png'
    pause 1.0
    'images/Minigames Menu/timer/10.png'
    pause 1.0
    'images/Minigames Menu/timer/9.png'
    pause 1.0
    'images/Minigames Menu/timer/8.png'
    pause 1.0
    'images/Minigames Menu/timer/7.png'
    pause 1.0
    'images/Minigames Menu/timer/6.png'
    pause 1.0
    'images/Minigames Menu/timer/5.png'
    pause 1.0
    'images/Minigames Menu/timer/4.png'
    pause 1.0
    'images/Minigames Menu/timer/3.png'
    pause 1.0
    'images/Minigames Menu/timer/2.png'
    pause 1.0
    'images/Minigames Menu/timer/1.png'
    pause 1.0
    'images/Minigames Menu/timer/0.png'

init python:
    import random
    import os

    global time
    time = 12

    def get_quiz_list():
        global quiz_list
        global list_path
        list_path = get_path(f"kodigo/game/python/quizzes/Quiz_List.json")

        if not os.path.exists(list_path):
            init_quiz_list()

        with open(list_path, 'r') as file:
            quiz_list = json.load(file)

    def init_quiz_list():
        init_data = {
            "standard": [], #this needs to be edited on the json itself
            "custom": []
        }

        with open(list_path, 'w') as file:
            json.dump(init_data, file)

    def set_quiz_loc(type):
        global quiz_loc
        quiz_loc = type

    def set_quiz(quiz):
        global current_quiz
        global fp
        global quiz_data    
        global learned
        current_quiz = quiz

        fp = get_path(f"kodigo/game/python/quizzes/{quiz_loc}/{current_quiz}.json") 
        with open(fp, 'r') as file:
            quiz_data = json.load(file)

        learned = quiz_data["learned"] #probability that player learned something

        #get quiz
        global questions
        global answers
        global letters
        global options
        global all_options

        all_options = []
        letters = []
        options = []

        for i in range(len(quiz_data["questions"])):
            options.append(None)
            letters.append(None)
        
        questions = quiz_data["questions"].copy()
        answers = quiz_data["answers"].copy()
        q_and_a = list(zip(questions, answers))
        random.shuffle(q_and_a)
        questions, answers = zip(*q_and_a)

        #get all options without repetition
        for answer in answers:
            if answer not in all_options:
                all_options.append(answer)

        for i in range(len(questions)):
            choices = random.sample(all_options, 3)
            if answers[i] in choices:
                choices.remove(answers[i])
                while True:
                    choice = random.sample(all_options, 1)
                    if choice not in choices:
                        choices.append(choice[0])
                        break
            choices.append(answers[i])
            random.shuffle(choices)
            options[i] = choices
            index = choices.index(answers[i])
            if index == 0:
                letters[i] = 'A'
            elif index == 1:
                letters[i] = 'B'
            elif index == 2:
                letters[i] = 'C'
            else:
                letters[i] = 'D'

        # get_notes and get_keys can be combined
    def get_notes():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        if quiz["notes"]:
            return quiz["notes"]

        return None

    def get_boldened_notes():
        with open(fp, 'r') as file:
            quiz_data = json.load(file)

        sentences = quiz_data["sentences"]
        answers = quiz_data["answers"]
        boldened = []

        for i in range(len(sentences)):
            pattern = re.compile(answers[i], re.IGNORECASE)
            match = pattern.search(sentences[i])
            matched_word = sentences[i][match.start():match.end()]
            sentence = pattern.sub('{b}{color=#007FFF}' + matched_word + '{/color}{/b}', sentences[i], count=1)
            boldened.append(sentence)
            
        return boldened

    def get_words():
        with open(fp, 'r') as file:
            quiz_data = json.load(file)

        sentences = quiz_data["notes"]
        words = re.findall(r"[\w']+|[.,!?;]", sentences)
        
        return words

    def get_text(quiz_notes):
        file_path = get_path(f"kodigo/game/python/docs/{quiz_notes}.txt")
        with open(file_path, 'r') as file:
            # Read the entire file contents into a string
            texts = file.read()

        return texts

    def set_bool(b):
        global bool
        bool = b

    def get_quiz_record():
        global quiz_record #for all for now
        quiz_record = {} #put this somewhere else

        file_path = get_path(f"kodigo/game/python/quizzes/q_records.json")

        with open(file_path, 'r') as file:
            quiz_record = json.load(file)

    def notes(quiz_notes):
        file_path = get_path(f"kodigo/game/python/docs/{quiz_notes}.txt")
        with open(file_path, 'r') as file:
            notes = file.readlines()
        return notes
    
    def save_quiz_record():
        with open(fp, "w") as json_file:
            json.dump(quiz_data, json_file)

    def exit_quiz():
        if quiz_type == "standard":
            renpy.show_screen("standard_quizzes")

    #def timer_function():

screen quiz_instructions:
    tag menu
    add "bg roomnight"

    imagebutton auto "images/Button/exit_%s.png" action ShowMenu("minigame"):
        align (0.97, 0.06)
        activate_sound "audio/click.ogg"

    frame:
        xpadding 40
        ypadding 50
        xalign 0.5
        yalign 0.6
        background "#D9D9D9"

        vbox:
            spacing 25

            text "Program Quiz Protocol":
                style "minigame_title_font"
                color "#000000"
                xalign 0.5
                yalign 0.5

            text "Objective: Engage in an academic and entertaining\n challenge about Computer Science Concepts in a quiz format.":
                color "#000000"
                font "Inter-Bold.ttf"
                size 40
            text "Gameplay:\n• Use the mouse to navigate through the quiz interface.\n• Click on your chosen answers for each multiple-choice question presented.\n• Click on buttons or tabs to access AI-generated hints or explanations.\n• Navigate between different quiz categories or user-generated quizzes by\n clicking on respective options.\n• Review your progress, check answers, and navigate through different quiz\n sections by clicking on appropriate icons/buttons.":
                color "#000000"
                font "Inter-Regular.ttf"
                size 32

            imagebutton auto "images/Button/play_%s.png" action ShowMenu("program_quiz_protocol"):
                align (0.5, 0.5)
                activate_sound "audio/click.ogg"

screen program_quiz_protocol():
    tag menu
    add "bg quiz main"

    $ get_quiz_list()

    image "quiz title":
        align (0.5, 0.2)

    imagebutton auto "images/Minigames Menu/exit_%s.png" action ShowMenu("minigame"):
        align (0.86, 0.04)
        activate_sound "audio/click.ogg"

    imagebutton auto "images/Button/standard_quiz_%s.png" action [Function(set_quiz_loc, "standard"), ShowMenu("quiz_list_screen")]:
        align (0.5, 0.55)
        activate_sound "audio/click.ogg"

    imagebutton auto "images/Button/custom_quiz_%s.png"action [Function(set_quiz_loc, "custom"), ShowMenu("quiz_list_screen")]:
        align (0.5, 0.7)
        activate_sound "audio/click.ogg"

screen quiz_list_screen:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("custom_quizzes"), ShowMenu("program_quiz_protocol")]:
        align (0.86, 0.04)
        activate_sound "audio/click.ogg"

    if quiz_loc == "standard":
        $ screen_title = "STANDARD QU/ZZES"
        $ empty_list = "No quiz available. The story mode quizzes updates here once it gets played."
    else:
        $ screen_title = "CUSTOM QU/ZZES"
        $ empty_list = "No quiz available. Try creating a quiz."

    text screen_title:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        size 50
        color "#FFFFFF"
        align (0.199, 0.0341)

    #ui is temporary
    if quiz_list[quiz_loc]:
        vpgrid:
            cols 3
            scrollbars "vertical"
            mousewheel True
            align (0.5, 0.44)
            spacing 20
            xysize (1449, 740)
            yfill True
            for quiz in quiz_list[quiz_loc]:
                #frame within a frame to add space away from the scrollbar
                frame:
                    xpadding 40
                    ypadding 40
                    xysize (420, 232)
                    background "#f7f2f200"
                    frame:
                        align (0.5, 0.5)
                        xpadding 40
                        ypadding 40
                        xysize (400, 212)
                        background "#D9D9D9"
                        vbox:
                            align (0.5, 0.5)
                            spacing 6
                            text quiz style "title"
                            imagebutton auto "images/Button/quiz_play_%s.png" xalign 0.5 yalign 0.5 action [Function(set_quiz, quiz), Jump("init_quiz")]:
                                activate_sound "audio/click.ogg"
                            imagebutton auto "images/Button/status_%s.png" xalign 0.5 yalign 0.5 action [Function(set_quiz, quiz), Show("quiz_status", transition=dissolve)]:
                                activate_sound "audio/click.ogg"
                            imagebutton auto "images/Button/notes_%s.png" xalign 0.5 yalign 0.5 action [Function(set_quiz, quiz), Show("display_notes", transition=dissolve)]:
                                activate_sound "audio/click.ogg"
    else:
        frame:
            xysize (1449, 740)
            align (0.64, 0.5)
            background "#d9d9d900"
            text empty_list:
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#FFFFFF"

    if quiz_loc == "custom":
        imagebutton auto "images/Button/create_quiz_%s.png" action [Function(init_json), ShowMenu("preprocess_text")]:
            align (0.95, 0.984)
            activate_sound "audio/click.ogg"

style title:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 30
    color "#000000"
    align (0.5, 0.5) 

#probobaly better if we separate it by sentences via bullets
screen display_notes:
    add "bg quiz main"

    $ notes = '\n\n'.join(get_boldened_notes()) #quiz_data["notes"]

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("display_notes"), ShowMenu("quiz_list_screen")]:
        align (0.86, 0.04)
        activate_sound "audio/click.ogg"

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        align (0.5, 0.15)

    frame:
        align (0.523, 0.55)
        xysize (1263, 626)
        background "#D9D9D9"

        vpgrid:
            cols 1
            scrollbars "vertical"
            spacing 5
            mousewheel True

            vbox:
                text notes style "notes"

    imagebutton auto "images/Button/play_%s.png" action [Hide("display_notes"), Jump("init_quiz")]:
        align (0.98, 0.98)
        activate_sound "audio/click.ogg"

style notes:
    font "KronaOne-Regular.ttf"
    #justify True
    size 24
    color "#303031"

#status of quiz etc
screen quiz_status:
    add "bg quiz main"

    python:
        if len(quiz_data["mastery"]) == 0:
            mastery = 0
        else:
            mastery = quiz_data["mastery"][-1]

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("quiz_status"), ShowMenu("quiz_list_screen")]: #don't know yet
        align (0.86, 0.04)
        activate_sound "audio/click.ogg"

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        align (0.5, 0.15)

    text "Mastery":
        font "Copperplate Gothic Bold Regular.ttf"
        size 40
        color "#FFFFFF"
        align (0.5, 0.3)

    text "[mastery]%":
        font "Copperplate Gothic Bold Regular.ttf"
        size 30
        color "#FFFFFF"
        align (0.5, 0.38)

    imagebutton auto "images/Button/retry_%s.png" action [Hide("quiz_status"), Call("init_quiz")]:
        align (0.5, 0.5)
        activate_sound "audio/click.ogg"

    imagebutton auto "images/Button/pass_attempts_%s.png" action [Hide("quiz_status"), ShowMenu("scoreboard")]:
        align (0.5, 0.65)
        activate_sound "audio/click.ogg"

screen scoreboard:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("scoreboard"), ShowMenu("quiz_status")]: #don't know yet
        align (0.86, 0.04)
        activate_sound "audio/click.ogg"

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        align (0.5, 0.15)

    text "Passed Attempts":
        font "Copperplate Gothic Bold Regular.ttf"
        size 40
        color "#FFFFFF"
        align (0.5, 0.25)

    vpgrid:
        cols 1
        mousewheel True
        scrollbars "vertical"
        align (0.5, 0.5)
        ysize 450

        vbox:
            spacing 10

            if len(quiz_data['records']) == 0:
                text "No records found.":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 40
                    color "#FFFFFF"
            else:
                text "SCORE               MASTERY       " style "status"

                for i in range(len(quiz_data['records'])):
                    $ score = quiz_data['records'][i]
                    $ mastery = quiz_data['mastery'][i]
                    text "      [score]                       [mastery]%        " style "status"

    python:
        if len(quiz_data['mastery']) == 0:
            mastery = 0
        else:
            mastery = quiz_data['mastery'][-1]

    text "[mastery]%" style "status":
        align (0.5, 0.8)
        yoffset 20

    imagebutton auto "images/Button/play_%s.png" action [Hide("scoreboard"), Jump("init_quiz")]:
        align (0.98, 0.98)
        activate_sound "audio/click.ogg"

style status:
    font "Copperplate Gothic Bold Regular.ttf"
    size 30
    color "#FFFFFF"

label init_quiz:
    $ time = 12
    $ question_num = 0

    if not in_story:
        show bg quiz main

    screen ready:
        if not in_story:
            imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("ready"), ShowMenu("quiz_list_screen")]:
                align (0.86, 0.04)
                activate_sound "audio/click.ogg"

        text "READY...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("ready"), Show("one")]

    screen one:
        if not in_story:
            imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("one"), ShowMenu("quiz_list_screen")]:
                align (0.86, 0.04)
                activate_sound "audio/click.ogg"

        text "1...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("one"), Show("two")]

    screen two:
        if not in_story:
            imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("two"), ShowMenu("quiz_list_screen")]:
                align (0.86, 0.04)
                activate_sound "audio/click.ogg"
            
        text "2...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("two"), Show("three")]

    screen three:
        if not in_story:
            imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("three"), ShowMenu("quiz_list_screen")]:
                align (0.86, 0.04)
                activate_sound "audio/click.ogg"

        text "3...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("three"), Show("go")]

    screen go:
        if not in_story:
            imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("go"), ShowMenu("quiz_list_screen")]:
                align (0.86, 0.04)
                activate_sound "audio/click.ogg"
            
        text "GO!":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("go"), Jump("init_question")]

    call screen ready with dissolve

style init_quiz_font:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 87
    color "#FFFFFF"

label init_question:
    show screen countdown with None
    #$ show_s("countdown")
    #show screen countdown with None
    call screen quiz_proper with dissolve

screen countdown():
    if timeout_label is not None:
        add "clock" xalign 0.85 yalign 0.85
        timer timeout action [SetVariable("timeout", 10), SetVariable("timeout_label", None), Show(timeout_label, transition=dissolve), SPlay("gameover"), Hide("countdown")]

screen quiz_proper:
    if not in_story:
        imagebutton auto "images/Button/pause_quiz_%s.png" action Hide("countdown"), Show("pause_quiz"): #hide the countdown for now
            align (0.86, 0.04)
            activate_sound "audio/click.ogg"

    frame:
        align (0.5, 0.15)
        xsize 1241
        yminimum 163
        background "#D9D9D9"

        $ number = question_num + 1

        text "[number]. " + questions[question_num]:
            font "Copperplate Gothic Bold Regular.ttf"
            align (0.5, 0.5)

    $ x = 0
    style_prefix "options"

    vbox:
        align (0.5, 0.5)
        spacing 20

        for option in options[question_num]:
            if x == 0:
                $ letter = "A"
            elif x == 1:
                $ letter = "B"
            elif x == 2:
                $ letter = "C"
            elif x == 3:
                $ letter = "D"

            textbutton "[letter]. " + option:
                action If(letters[question_num] == letter, (Show("right", transition=dissolve), SetVariable("score", score+1), SPlay("gamewin")), (Show("wrong", transition=dissolve), SPlay("gameover"))), Hide("countdown")
                    
            $ x += 1

style options_button_text:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    align (0.5, 0.5)
    size 50
    color "#ffffff"
    insensitive_color "#ffffff"
    hover_color "#b1e7f5"
    selected_color "#7ceafd"

screen pause_quiz:
    modal True
    add "halfblack"

    imagebutton auto "images/Button/pause_quiz_%s.png" action Show("countdown"), Hide("pause_quiz"):
        align (0.86, 0.04)
        activate_sound "audio/click.ogg"

    frame:
        align (0.82, 0.136)
        xysize (489, 421)
        background "#757274"

        vbox:
            align (0.5, 0.5)
            imagebutton auto "images/Button/continue_quiz_%s.png" action Show("countdown"), Hide("pause_quiz"):
                align (0.5, 0.5)
                activate_sound "audio/click.ogg"
            imagebutton auto "images/Button/exit_quiz_%s.png" action Hide("pause_quiz"), Hide("quiz_proper"), Show("quiz_list_screen", transition=dissolve):
                align (0.5, 0.5)
                yoffset 20
                activate_sound "audio/click.ogg"

screen right:
    modal True

    add "halfblack"
    if in_story:
        add "mc happy_uniform"
    else:
        add "mc_happy"

    button:
        xysize(1920,1080)
        action [Hide("right", transition=fade), Jump("next_question")]
        activate_sound "audio/click.ogg"

    frame:
        xysize (1920, 90)
        align (0.5, 0.8)
        background "gui/nvl.png"
        text "Your answer is {b}{color=#00008B}correct{/color}{/b}!" style "correct"

screen wrong:
    modal True

    add "halfblack"

    if in_story:
        add "mc sad_uniform"
    else:
        add "mc_sad"

    button:
        xysize(1920,1080)
        action [Hide("wrong", transition=fade), Jump("next_question")]
        activate_sound "audio/click.ogg"

    frame:
        xysize (1920, 90)
        align (0.5, 0.8)
        background "gui/nvl.png"
        text "Your answer is {b}{color=#FF0000}wrong{/color}{/b}." style "correct"

style correct:
    font "KronaOne-Regular.ttf"
    color "#303031"
    size 30
    xalign 0.5
    yalign 0.5

label next_question:
    $ question_num += 1

    #cheat
    if in_story and question_num == 10:
        jump cheat_quiz

    if question_num == len(questions):
        $ question_num = 0
        jump results
    
    $ timeout = 12 # Sets how long in seconds the user has to make a choice
    $ timeout_label = 'wrong' #sets the label that is automatically jumped to if the user makes no choice

    jump init_question 

label results:
    pause 1.0
    hide screen countdown

    $ total = len(quiz_data['questions'])

    python:
        L = learned
        if score/total >= 0.7:
            if in_story:
                mc_reac = "mc happy_uniform"
            else:
                mc_reac = "mc_happy"

            A = (L*(1-S)) / (L*(1-S) + (1-L)*G)
            L = A + (1-A)*T
            sndplay("Win")
        else:
            if in_story:
                mc_reac = "mc sad_uniform"
            else:
                mc_reac = "mc_sad"
            A = (L*S) / ((L*S) + (1-L)*(1-G))
            L = A + (1-A)*T
            sndplay("Lose")
        
    if in_story:
        $ global quiz_loc
        $ quiz_loc = "standard"

    $ quiz_data['records'].append(score)
    $ mastery = round(L * 100, 2)
    $ learned = L
    $ quiz_data['mastery'].append(mastery)
    $ quiz_data['learned'] = learned
    $ save_quiz_record()

    screen show_score:
        modal True
        image mc_reac:
            xalign 0.5

        button:
            xysize(1920,1080)
            activate_sound "audio/click.ogg"

            if in_story:
                action [Hide("show_score"), SetVariable("in_story", False), SetVariable("score", 0), SNDstop(), Jump("chapter_2")] keysym ["K_SPACE"]
            else:
                action [Hide("show_score"), SetVariable("score", 0), SNDstop(), Show("quiz_status", transition=dissolve)] keysym ["K_SPACE"]
        
        text "Your score is {b} [score] {/b}!" style "game_instruction"

    call screen show_score with dissolve