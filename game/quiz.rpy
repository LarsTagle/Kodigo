"""
things to fix:
    1. polish quiz ui
    2. integrate ai
    3. fix assets
    4. add toolkits
    5. add comments
    6. if possible, add mini text editor
"""

#back to status quo, error in mapping sentence

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
        quiz_loc  = type

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

        for i in range(len(questions)):
            choices = random.sample(quiz_data["answers"], 3)
            if answers[i] in choices:
                choices.remove(answers[i])
                while True:
                    choice = random.sample(quiz_data["answers"], 1)
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

    def get_words(answers):
        keywords = []
        for a in answers:
            if " " in a:
                keys = a.split(" ")
                for k in keys:
                    if k not in keywords:
                        keywords.append(k)
            elif a not in keywords:
                keywords.append(a)

        return keywords

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
        xalign 0.97
        yalign 0.06

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
                xalign 0.5
                yalign 0.5

screen program_quiz_protocol():
    tag menu
    add "bg quiz main"

    $ get_quiz_list()

    add "quiz title":
        yalign 0.2
        xalign 0.5

    imagebutton auto "images/Minigames Menu/exit_%s.png" action ShowMenu("minigame"):
        xalign 0.86
        yalign 0.04

    imagebutton auto "images/Button/standard_quiz_%s.png" action [Function(set_quiz_loc, "standard"), ShowMenu("quiz_list_screen")]:
        yalign 0.55
        xalign 0.5
    imagebutton auto "images/Button/custom_quiz_%s.png"action [Function(set_quiz_loc, "custom"), ShowMenu("quiz_list_screen")]:
        yalign 0.7
        xalign 0.5

screen quiz_list_screen:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("custom_quizzes"), ShowMenu("program_quiz_protocol")]:
        xalign 0.86
        yalign 0.04

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
        xalign 0.199
        yalign 0.0341

    #ui is temporary
    if quiz_list[quiz_loc]:
        vpgrid:
            cols 3
            scrollbars "vertical"
            mousewheel True
            xalign 0.5
            yalign 0.44
            spacing 20
            xsize 1449
            ysize 740
            yfill True
            for quiz in quiz_list[quiz_loc]:
                #frame within a frame to add space away from the scrollbar
                frame:
                    xpadding 40
                    ypadding 40
                    xsize 420
                    ysize 232
                    background "#f7f2f200"
                    frame:
                        xalign 0.5
                        yalign 0.5
                        xpadding 40
                        ypadding 40
                        xsize 400
                        ysize 212
                        background "#D9D9D9"
                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 6
                            text quiz style "title"
                            imagebutton auto "images/Button/quiz_play_%s.png" xalign 0.5 yalign 0.5 action [Function(set_quiz, quiz), Jump("init_quiz")]
                            imagebutton auto "images/Button/status_%s.png" xalign 0.5 yalign 0.5 action [Function(set_quiz, quiz), Show("quiz_status")]
                            imagebutton auto "images/Button/notes_%s.png" xalign 0.5 yalign 0.5 action [Function(set_quiz, quiz), Show("display_notes")]
    else:
        frame:
            xsize 1449
            ysize 740
            align (0.64, 0.5)
            background "#d9d9d900"
            text empty_list:
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#FFFFFF"

    if quiz_loc == "custom":
        imagebutton auto "images/Button/create_quiz_%s.png" action [Function(init_json), ShowMenu("preprocess_text")]:
            xalign 0.95
            yalign 0.984

style title:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 30
    color "#000000"
    xalign 0.5
    yalign 0.5    

#probobaly better if we separate it by sentences via bullets
screen display_notes:
    add "bg quiz main"

    $ notes = quiz_data["notes"]

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("display_notes"), ShowMenu("quiz_list_screen")]:
        xalign 0.86
        yalign 0.04

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    frame:
        xalign 0.523
        yalign 0.55
        xsize 1263
        ysize 626
        background "#D9D9D9"

        vpgrid:
            cols 1
            scrollbars "vertical"
            spacing 5
            mousewheel True

            vbox:
                text notes style "notes"

    imagebutton auto "images/Button/play_%s.png" action [Hide("display_notes"), Jump("init_quiz")]:
        xalign 0.98
        yalign 0.98

style notes:
    font "KronaOne-Regular.ttf"
    justify True
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
        xalign 0.86
        yalign 0.04

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    text "Mastery":
        font "Copperplate Gothic Bold Regular.ttf"
        size 40
        color "#FFFFFF"
        xalign 0.5
        yalign 0.3

    text "[mastery]%":
        font "Copperplate Gothic Bold Regular.ttf"
        size 30
        color "#FFFFFF"
        xalign 0.5
        yalign 0.38

    imagebutton auto "images/Button/retry_%s.png" action [Hide("quiz_status"), Call("init_quiz")]:
        xalign 0.5
        yalign 0.5

    imagebutton auto "images/Button/pass_attempts_%s.png" action [Hide("quiz_status"), ShowMenu("scoreboard")]:
        xalign 0.5
        yalign 0.65

screen scoreboard:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("scoreboard"), ShowMenu("quiz_list_screen")]: #don't know yet
        xalign 0.86
        yalign 0.04

    text current_quiz:
        font "Copperplate Gothic Bold Regular.ttf"
        size 50
        color "#FFFFFF"
        xalign 0.5
        yalign 0.15

    text "Passed Attempts":
        font "Copperplate Gothic Bold Regular.ttf"
        size 40
        color "#FFFFFF"
        xalign 0.5
        yalign 0.25

    vpgrid:
        cols 1
        mousewheel True
        scrollbars "vertical"
        xalign 0.5
        yalign 0.5
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
        xalign 0.5
        yalign 0.8
        yoffset 20

    imagebutton auto "images/Button/play_%s.png" action [Hide("scoreboard"), Jump("init_quiz")]:
        xalign 0.98
        yalign 0.98

style status:
    font "Copperplate Gothic Bold Regular.ttf"
    size 30
    color "#FFFFFF"

label init_quiz:
    $ time = 12
    $ question_num = 0

    screen ready_set:
        add "bg quiz main"
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("ready"), ShowMenu("quiz_list_screen")]:
            xalign 0.86
            yalign 0.04

        text "READY...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("ready"), Show("one")]

    screen one:
        add "bg quiz main"
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("one"), ShowMenu("quiz_list_screen")]:
            xalign 0.86
            yalign 0.04

        text "1...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("one"), Show("two")]

    screen two:
        add "bg quiz main"
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("two"), ShowMenu("quiz_list_screen")]:
            xalign 0.86
            yalign 0.04

        text "2...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("two"), Show("three")]

    screen three:
        add "bg quiz main"
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("three"), ShowMenu("quiz_list_screen")]:
            xalign 0.86
            yalign 0.04

        text "3...":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("three"), Show("go")]

    screen go:
        add "bg quiz main"
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("go"), ShowMenu("quiz_list_screen")]:
            xalign 0.86
            yalign 0.04

        text "GO!":
            style "init_quiz_font"
            xalign 0.5
            yalign 0.48

        timer 1.0 action [Hide("go"), Jump("init_question")]

    call screen ready_set with dissolve

style init_quiz_font:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 87
    color "#FFFFFF"

label init_question:
    $ show_s("countdown")
    #show screen countdown with None
    call screen quiz_proper with dissolve

screen countdown():
    add "bg quiz main"
    
    if timeout_label is not None:
        add "clock" xalign 0.85 yalign 0.85
        timer timeout action [SetVariable("timeout", 10), SetVariable("timeout_label", None), Jump(timeout_label)]

## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True
"""
screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    $ current_time = int(time)
    image "images/Minigames Menu/timer/[current_time].png" xalign 0.85 yalign 0.85
    """
"""
python:
    while time >= 0:
        process = subprocess.Popen([python_path, py_path, str(time)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, creationflags=subprocess.CREATE_NO_WINDOW)
        stdout_data, _ = process.communicate()
        t = int(stdout_data.decode())
        time -= 1
"""

screen quiz_proper:
    imagebutton auto "images/Button/pause_quiz_%s.png" action Jump("pause_quiz"):
        xalign 0.86
        yalign 0.04

    frame:
        xalign 0.5
        yalign 0.15
        xsize 1241
        yminimum 163
        background "#D9D9D9"

        $ number = question_num + 1

        text "[number]. " + questions[question_num]:
            font "Copperplate Gothic Bold Regular.ttf"
            xalign 0.5
            yalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(letters[question_num] == 'A', Jump("right"), Jump("wrong")):
        yalign 0.39
        xalign 0.5

    text "A. " + options[question_num][0]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.4
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(letters[question_num] == 'B', Jump("right"), Jump("wrong")):
        yalign 0.5
        xalign 0.5

    text "B. " + options[question_num][1]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.5
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(letters[question_num] == 'C', Jump("right"), Jump("wrong")):
        yalign 0.612
        xalign 0.5

    text "C. " + options[question_num][2]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.6
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png" action If(letters[question_num] == 'D', Jump("right"), Jump("wrong")):
        yalign 0.712
        xalign 0.5

    text "D. " + options[question_num][3]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.7
        xalign 0.5

label pause_quiz:
    hide screen quiz_proper
    #hide screen countdown
    $ hide_s("countdown")
    $ show_s("question_dull")

    call screen paused_menu

    screen paused_menu:
        add "halfblack"

        imagebutton auto "images/Button/pause_quiz_%s.png" action Jump("continue_quiz"):
            xalign 0.86
            yalign 0.04
        frame:
            xalign 0.82
            yalign 0.136
            xsize 489
            ysize 421
            background "#757274"

            vbox:
                xalign 0.5
                yalign 0.5
                imagebutton auto "images/Button/continue_quiz_%s.png" action Jump("continue_quiz"):
                    xalign 0.5
                    yalign 0.5
                imagebutton auto "images/Button/exit_quiz_%s.png" action Jump("exit_quiz"):
                    xalign 0.5
                    yalign 0.5
                    yoffset 20

label continue_quiz:
    hide paused_menu
    $ hide_s("question_dull")
    jump init_question

label exit_quiz:
    hide paused_menu
    $ hide_s("question_dull")
    call screen quiz_list_screen

screen show_correction(is_correct):
    if is_correct:
        $ mc_reac = "mc_happy"
        $ answer_is = "Your answer is {b}{color=#00008B}correct{/color}{/b}!"

        button:
            xysize(1920,1080)
            action Jump("next_question")#[Hide("show_correction"), Jump("next_question")]
    else:
        $ mc_reac = "mc_sad"
        $ answer_is = "Your answer is {b}{color=#FF0000}wrong{/color}{/b}."

        button:
            xysize(1920,1080)
            action [Hide("show_correction"), Show("show_answer")]

    add "halfblack"
    add mc_reac

    frame:
        xsize 1920
        ysize 90
        xalign 0.5
        yalign 0.8
        background "gui/nvl.png"
        text answer_is style "correct"

screen show_answer:
    add "halfblack"
    add "mc_sad"

    button:
        xysize(1920,1080)
        action [Hide("show_answer"), Jump("next_question")]

    $ letter = letters[question_num]
    $ answer = answers[question_num]

    frame:
        xsize 1920
        ysize 90
        xalign 0.5
        yalign 0.8
        background "gui/nvl.png" 
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            text "The correct answer is " style "correct"
            text "{b}{color=#FF0000}[letter]. [answer]{/color}{/b}." style "correct"

style correct:
    font "KronaOne-Regular.ttf"
    color "#303031"
    size 30
    xalign 0.5
    yalign 0.5

label right:  
    hide screen quiz_proper
    #hide screen countdown
    $ hide_s("countdown")
    $ show_s("question_dull")

    $ score += 1

    call screen show_correction (True) with dissolve
    jump next_question

label wrong:
    hide screen quiz_proper
    #hide screen countdown
    $ hide_s("countdown")
    $ show_s("question_dull")

    call screen show_correction (False) with dissolve
    jump next_question


label next_question:
    $ question_num += 1

    #cheat
    if in_story and question_num == 10:
        $ hide_s("question_dull")
        jump cheat_quiz

    if question_num == len(questions):
        $ question_num = 0
        jump results
    
    $ timeout = 12 # Sets how long in seconds the user has to make a choice
    $ timeout_label = 'wrong' #sets the label that is automatically jumped to if the user makes no choice

    $ hide_s("question_dull")
    jump init_question 

label results:
    hide screen countdown
    $ hide_s("question_dull")
    "Your score is {b} [score] {/b}!"

    python:
        L = learned
        if score/15 >= 0.7:
            A = (L*(1-S)) / (L*(1-S) + (1-L)*G)
            L = A + (1-A)*T
        else:
            A = (L*S) / ((L*S) + (1-L)*(1-G))
            L = A + (1-A)*T

    if in_story:
        $ global quiz_loc
        $ quiz_loc = "standard"

    $ quiz_data['records'].append(score)
    $ score = 0
    $ mastery = round(L * 100, 2)
    $ learned = L
    $ quiz_data['mastery'].append(mastery)
    $ quiz_data['learned'] = learned
    $ save_quiz_record()

    #this need's to be put in quiz_status instead
    if in_story:
        $ in_story = False
        jump chapter_2

    call screen quiz_status

screen question_dull:
    add "bg quiz main"
    $ timeout = 12 # Sets how long in seconds the user has to make a choice
    $ timeout_label = 'wrong' #sets the label that is automatically jumped to if the user makes no choice

    imagebutton auto "images/Button/pause_quiz_%s.png":
        xalign 0.86
        yalign 0.04

    frame:
        xalign 0.5
        yalign 0.15
        xsize 1241
        ysize 163
        background "#D9D9D9"

        $ number = question_num + 1

        text "[number]. " + questions[question_num]:
            font "Copperplate Gothic Bold Regular.ttf"
            xalign 0.5
            yalign 0.5

    style_prefix "mytext"

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.39
        xalign 0.5

    text "A. " + options[question_num][0]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.4
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.5
        xalign 0.5

    text "B. " + options[question_num][1]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.5
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.612
        xalign 0.5

    text "C. " + options[question_num][2]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.6
        xalign 0.5

    imagebutton auto "images/Button/choice_%s.png":
        yalign 0.712
        xalign 0.5

    text "D. " + options[question_num][3]:
        font "Copperplate Gothic Thirty-Three Regular.otf"
        yalign 0.7
        xalign 0.5