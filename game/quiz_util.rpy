#fix editting to dissallow empty text field
define title = VariableInputValue(variable = "new_title", returnable = True)
define keys = VariableInputValue(variable = "keywords", returnable = True)

init:
    $ new_title = quiz_title

init python:
    global in_edit_title
    global in_edit_keywords
    in_edit_title = False
    in_edit_keywords = False
    global keywords

label quit_warning:
    #checks if questions are generated
    if is_notes():
        $ show_s("preprocess_text_dull")
        show halfblack
        call screen warning
    else:
        $ del_json()
        $ quiz_title = f"Quiz {persistent.quiz_def_num}" #resets
        call screen quiz_list_screen

    screen warning:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            xsize 450
            ysize 420
            background "#D9D9D9"

            vbox:
                xalign 0.5
                yalign 0.5

                text f"'{quiz_title}' is not yet created.":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 50
                    color "#303031"
                    xalign 0.5
                    yalign 0.5
                text "Would you like to exit?":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 30
                    color "#303031"
                    yoffset 10

                hbox:
                    xalign 0.5
                    yalign 0.5
                    yoffset 50
                    spacing 40

                    imagebutton auto "images/Button/yes_%s.png" action [Hide("warning"), Function(set_bool, True), Jump("warning_2")] #Function(set_bool, True) apparently was not necessary tangina
                    imagebutton auto "images/Button/no_%s.png" action [Hide("warning"), Function(set_bool, False), Jump("warning_2")]

label warning_2:
    $ hide_s("preprocess_text_dull")
    hide halfblack

    #if player wants to exit
    if bool:
        call screen quiz_list_screen with dissolve
    else:
        call screen preprocess_text

screen input_title:
    if not in_save:
        frame: 
            xalign 0.76
            yalign 0.144
            xsize 650
            ysize 85  
            background "#ffffff00"
            
            hbox: 
                xalign 0.5
                yalign 0.5 
                input value title length 15 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 57
                    color "#FFFFFF"
                    xalign 0.5
                    yalign 0.5 

                imagebutton auto "images/Button/pen_%s.png" action [Hide("input_title"), Jump("edit_title_2")]:
                    yalign 0.1
    else:
        frame:
            xalign 0.5
            yalign 0.1
            xsize 1200
            ysize 135
            background "#ffffff00"

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 5
                input value title length 15 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 100
                    color "#FFFFFF"

                imagebutton auto "images/Button/pen_%s.png" action [Hide("input_title"), Jump("edit_title_2")]:
                    yoffset 5

label edit_title:
    $ in_edit_title = True

    if in_save:
        hide screen save_quiz
        $ show_s("save_quiz_dull")
    else:
        hide screen preprocess_text
        $ show_s("preprocess_text_dull")
    call screen input_title

label edit_title_2:
    #like if the quiz is in custom
    $ old_fp = get_path(f"kodigo/game/python/quizzes/custom/{quiz_title}.json")
    $ new_fp = get_path(f"kodigo/game/python/quizzes/custom/{new_title}.json") #idrk

    if new_title == "":
        $ in_edit_title = False
        $ temp = quiz_title
        $ quiz_title = new_title
        call screen empty (temp)
    elif os.path.exists(new_fp) and old_fp != new_fp: #duplicate name
        $ in_edit_title = False
        $ temp = quiz_title
        $ quiz_title = new_title
        call screen duplicate (temp)
    elif os.path.exists(fp):
        $ os.rename(fp, get_path(f"kodigo/game/python/temp/{new_title}.json"))
        $ quiz_title = new_title
        $ fp = get_path(f"kodigo/game/python/temp/{quiz_title}.json") #reset

    $ in_edit_title = False 

    if in_save:
        $ hide_s("save_quiz_dull")
        call screen save_quiz
    else:
        $ hide_s("preprocess_text_dull")
        call screen preprocess_text
        
screen empty(temp):
    add "halfblack"

    button:
        xysize(1920,1080)
        action [Hide("empty"), Call("exit_edit", temp)]

    vbox:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 100
        spacing 5
        text "Name can't be empty.":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5
        text "Try again.":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

screen duplicate(temp):
    add "halfblack"
    
    button:
        xysize(1920,1080)
        action [Hide("duplicate"), Call("exit_edit", temp)]

    vbox:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 100
        spacing 5
        text "Can't have multiple quizzes with the same name.":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5
        text "Try again.":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5
       
label exit_edit(temp):
    $ quiz_title = temp
    $ new_title = quiz_title
    if in_save:
        $ hide_s("save_quiz_dull")
        call screen save_quiz
    else:
        $ hide_s("preprocess_text_dull")
        call screen preprocess_text

screen input_keys(j):
    $ answers = get_answers()

    if answers:
        $ sentences = get_boldened_notes()
    else:
        $ sentences = get_sentences()

    text "Notes":
        font "Copperplate Gothic Thirty-Three Regular.otf"
        size 48
        color "#FFFFFF"
        xalign 0.22
        yalign 0.2

    if sentences:
        viewport:
            scrollbars "vertical"
            mousewheel True
            xalign 0.5
            yalign 0.6
            xsize 1220
            ysize 650

            vbox:
                spacing 30
                for i in range(len(sentences)):
                    frame:
                        xpadding 10
                        xsize 1220
                        background "#f7f2f200"
                        vbox:
                            spacing 10
                            frame:
                                xalign 0.5
                                yalign 0.5
                                xpadding 40
                                ypadding 40
                                xsize 1150
                                background "#D9D9D9"
                                hbox:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 1070
                                    spacing 10
                                    vbox: 
                                        xsize 1000
                                        text sentences[i] style "notes"
                                    imagebutton auto "images/Button/edit_icon_%s.png": 
                                        xalign 1.0 
                                        yalign 0.5
                            if i == j:
                                frame:
                                    xalign 0.5
                                    yalign 0.5
                                    xpadding 40
                                    ypadding 40
                                    xsize 1150
                                    background "#D9D9D9"
                                    text "try"


label edit_keys(sentences, keywords, i):
    $ in_edit_keywords = True
    $ show_s("preprocess_text_dull")
    call screen input_keys (i)
    "[sentences]"
    "[keywords]"

screen preprocess_text_dull:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    frame:
        xalign 0.5
        yalign 0.1
        xsize 1200
        ysize 135
        background "#ffffff00"

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            text "[quiz_title]": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 100
                color "#FFFFFF"

            imagebutton auto "images/Button/pen_%s.png": 
                yoffset 5

    #get the notes and keywords if they exists
    #$ notes = get_notes()
    
    $ answers = get_answers()

    if answers:
        $ sentences = get_boldened_notes()
    else:
        $ sentences = get_sentences()

    if not in_edit_keywords:
        text "Notes":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 48
            color "#FFFFFF"
            xalign 0.22
            yalign 0.2
    
        if sentences:
            viewport:
                scrollbars "vertical"
                mousewheel True
                xalign 0.5
                yalign 0.6
                xsize 1220
                ysize 650

                vbox:
                    spacing 30
                    for i in range(len(sentences)):
                        frame:
                            xpadding 10
                            xsize 1220
                            background "#f7f2f200"
                            frame:
                                xalign 0.5
                                yalign 0.5
                                xpadding 40
                                ypadding 40
                                xsize 1150
                                background "#D9D9D9"
                                hbox:
                                    xalign 0.5
                                    yalign 0.5
                                    xsize 1070
                                    spacing 10
                                    vbox: 
                                        xsize 1000
                                        text sentences[i] style "notes"
                                    imagebutton auto "images/Button/edit_icon_%s.png": 
                                        xalign 1.0 
                                        yalign 0.5
        else:
            viewport:
                scrollbars "vertical"
                mousewheel True
                xalign 0.5
                yalign 0.6
                xsize 1220
                ysize 650

                frame:
                    xpadding 10
                    xsize 1220
                    background "#f7f2f200"
                    frame:
                        xalign 0.5
                        yalign 0.5
                        xpadding 40
                        ypadding 40
                        xsize 1150
                        background "#D9D9D9"
                        hbox:
                            xalign 0.5
                            yalign 0.5
                            xsize 1070
                            spacing 10
                            vbox: 
                                xsize 1000
                                text "Sentences will appear {b}{color=#007FFF}here{/color}{/b}..." style "notes"
                            imagebutton auto "images/Button/edit_icon_%s.png":
                                xalign 1.0 
                                yalign 0.5

    if not answers:
        imagebutton auto "images/Button/upload_%s.png":
            xalign 0.95
            yalign 0.984
    else:
        imagebutton auto "images/Button/create_quiz_%s.png": 
            xalign 0.95
            yalign 0.984

screen save_quiz_dull:
    add "bg quiz main"

    $ questions, answers = get_quiz()

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    if not in_edit_title:
        frame:
            xalign 0.5
            yalign 0.1
            xsize 1200
            ysize 135
            background "#ffffff00"

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 5
                text "[quiz_title]": #specify with a number later
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 100
                    color "#FFFFFF"

                imagebutton auto "images/Button/pen_%s.png":
                    yoffset 5

    vbox:
        xsize 750
        ysize 550
        xalign 0.30
        yalign 0.55
        spacing 20
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 40
            text "Questions and Answers": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 50
                color "#FFFFFF"
        #fix this later
        frame:
            xsize 700
            ysize 600
            background "#D9D9D9"
            vpgrid:
                cols 1
                spacing 20
                scrollbars "vertical"
                mousewheel True
                vbox:
                    spacing 5
                    for i in range(len(questions)):
                        $ question = questions[i]
                        $ answer = answers[i]
                        text "Question: [question]" style "q_and_a"
                        text "Answer: [answer]" style "q_and_a"
                        text "\n"
        
    #this is temporary!
    #Mixed should be the default
    vbox:
        xalign 0.8
        yalign 0.5
        spacing 20
        frame:
            xsize 337
            ysize 200
            xalign 0.5
            yalign 0.5
            background "#D9D9D9"
            vbox:
                spacing 5
                textbutton "Mulitple Choices" style "q_and_a"
                textbutton "Identification" style "q_and_a" 
                textbutton "Mixed" style "q_and_a"

        imagebutton auto "images/Button/save_quiz_%s.png":
            xalign 0.5
            yalign 0.5