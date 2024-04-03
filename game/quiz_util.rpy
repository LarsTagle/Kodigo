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
            xalign 0.73  
            yalign 0.144
            xsize 600
            ysize 60  
            background "#ffffff00"

            input value title length 15 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 57
                color "#FFFFFF"
                xalign 1.0
                yalign 0.15

        imagebutton auto "images/Button/pen_%s.png" action [Hide("input_title"), Jump("edit_title_2")]:
            xalign 0.85
            yalign 0.134

    else:
        hbox:
            xalign 0.5
            yalign 0.1
            input value title length 18 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- ":
                xalign 0.5
                yalign 0.1
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 150
                color "#FFFFFF"
            imagebutton auto "images/Button/edit_title_%s.png" action [Hide("input_title"), Jump("edit_title_2")]:
                xoffset 40
                yoffset 45

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

screen input_keys:
    imagebutton auto "images/Button/edit_%s.png":
        xalign 0.85
        yalign 0.5

    vbox:
        xalign 0.737
        yalign 0.4

        text "Keywords":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 48
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

        frame:
            xalign 0.25
            yalign 0.5
            xsize 400
            ysize 400
            background "#D9D9D9"
            yoffset 30

            if keywords:
                vpgrid:
                    cols 1
                    scrollbars "vertical"
                    spacing 5
                    mousewheel True

                    vbox:
                        xsize 370
                        ysize 390
                        input value keys length 6262 allow "abcdefghijklmnopqrstuvwxyz, " multiline True:
                            font "KronaOne-Regular.ttf"
                            size 24
                            color "#303031"

label edit_keywords:
    $ keywords = get_str(get_keys())
    $ in_edit_keywords = True
    $ show_s("preprocess_text_dull")
    call screen input_keys
    $ in_edit_keywords = False
    call screen preprocess_text

screen save_quiz_dull:
    add "bg quiz main"

    $ questions, answers = get_quiz()

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    if not in_edit_title:
        hbox:
            xalign 0.5
            yalign 0.1
            text "[quiz_title]": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 150
                color "#FFFFFF"

            imagebutton auto "images/Button/edit_title_%s.png":
                xoffset 40
                yoffset 45

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


screen preprocess_text_dull:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    #get the notes if it exists
    $ notes = get_notes()
    $ keywords = get_str(get_keys())

    text "Notes":
        font "Copperplate Gothic Thirty-Three Regular.otf"
        size 48
        color "#FFFFFF"
        xalign 0.324
        yalign 0.15

    frame:
        xalign 0.25
        yalign 0.5
        xsize 600
        ysize 600
        background "#D9D9D9"

        vpgrid:
            cols 1
            scrollbars "vertical"
            spacing 5
            mousewheel True

            vbox:
                xsize 570
                ysize 590
                if notes:
                    text notes style "notes"
                else:
                    text "Texts from the document will appear here." style "notes"

    if notes:
        imagebutton auto "images/Button/summarize_%s.png":
            xalign 0.28
            yalign 0.85

    if not in_edit_keywords:
        if keywords:
            imagebutton auto "images/Button/edit_%s.png":
                xalign 0.85
                yalign 0.5

        vbox:
            xalign 0.737
            yalign 0.4

            text "Keywords":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 48
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5

            frame:
                xalign 0.25
                yalign 0.5
                xsize 400
                ysize 400
                background "#D9D9D9"
                yoffset 30

                vpgrid:
                    cols 1
                    scrollbars "vertical"
                    spacing 5
                    mousewheel True

                    vbox:
                        xsize 370
                        ysize 390
                        if keywords:
                            text keywords:
                                font "KronaOne-Regular.ttf"
                                size 24
                                color "#303031"
                        else:
                            text "Keywords from the text will appear here." style "notes"
    if not in_edit_title:
        frame: 
            xalign 0.73  
            yalign 0.144
            xsize 600
            ysize 60  
            background "#ffffff00"
            
            text "[quiz_title]": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 57
                color "#FFFFFF"
                xalign 1.0
                yalign 0.15

        imagebutton auto "images/Button/pen_%s.png":
            xalign 0.85
            yalign 0.134

    if not notes:
        imagebutton auto "images/Button/upload_%s.png":
            xalign 0.75
            yalign 0.8
    else:
        imagebutton auto "images/Button/create_quiz_%s.png": #since we are skipping editting the keywords & texts, we proceed here next
            xalign 0.75
            yalign 0.8
