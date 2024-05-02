#fix editting to dissallow empty text field
define title = VariableInputValue(variable = "new_title", returnable = True)
define key = VariableInputValue(variable = "change_key", returnable = True)
define new_text = VariableInputValue(variable = "current_text", returnable = True)

init:
    $ new_title = quiz_title
    $ current_text = ""
    $ edit_sentence = False
    $ edit_sentence_index = None

init python:
    global in_edit_title, in_edit_keywords
    in_edit_title = False
    in_edit_keywords = False
    global keywords

    def set_old_key(answers, i):
        global change_key
        global index 
        change_key = answers[i]
        index = i
    
    def reset_key(i):
        with open(fp, 'r') as file:
            quiz = json.load(file)
        
        if change_key.lower() in quiz["sentences"][i].lower():
            quiz["answers"][index] = change_key

        with open(fp, 'w') as file:
            json.dump(quiz, file)

label quit_warning:
    #checks if questions are generated
    if is_notes():
        if not in_save:
            $ show_s("preprocess_text_dull")
        else: 
            $ show_s("save_quiz_dull")
        
        call screen warning
    else:
        $ del_json()
        $ quiz_title = f"Quiz {persistent.quiz_def_num}" #resets
        $ renpy.call_screen("%s"%(mn_caller_screen))

    screen warning:
        add "halfblack"
        style_prefix "yes_or_no"

        if not in_save:
            $ verb = "creating"
        else:
            $ verb = "saving"

        frame:
            align (0.5, 0.5)
            xysize(450, 390)

            vbox:
                spacing 50
                frame:
                    xfill True
                    ysize 50
                    background "#0b5fbed8"
                    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("warning"), Function(set_bool, False), Jump("warning_2")] keysym ['K_ESCAPE']:
                        xalign 1.0

                text f"Are you sure you want to exit before [verb] '{quiz_title}'?":
                    size 30
                    color "#303031"
                    xalign 0.5
                    yalign 0.5

                hbox:
                    align(0.5, 0.5)
                    spacing 40

                    frame:
                        background "#0b5fbed8"
                        textbutton "YES" action [Hide("warning"), Function(set_bool, True), Jump("warning_2")]

                    frame:
                        background "#D3D3D3"
                        textbutton "NO" action [Hide("warning"), Function(set_bool, False), Jump("warning_2")]

label warning_2:
    if not in_save:
        $ hide_s("preprocess_text_dull")
        #if player wants to exit
        if bool:
            $ del_json()
            $ quiz_title = f"Quiz {persistent.quiz_def_num}" #resets

            #reset fp
            if edit_quiz:
                $ fp = get_path(f"kodigo/game/python/quizzes/{quiz_loc}/{current_quiz}.json") 
                
            $ renpy.call_screen("%s"%(mn_caller_screen))
        else:
            call screen preprocess_text
    else:
        $ hide_s("save_quiz_dull")
        if bool:
            call screen preprocess_text
        else:
            call screen save_quiz

screen input_title:
    if not in_save:
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
                    default_focus True

                imagebutton auto "images/Button/pen_%s.png" action [Hide("input_title"), Jump("edit_title_2")]:
                    yoffset 5
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
        action [Hide("empty"), Call("exit_edit", temp)] keysym ['K_ESCAPE']

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
        action [Hide("duplicate"), Call("exit_edit", temp)] keysym ['K_ESCAPE']

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

screen input_keys(sentences, answers, i):
    modal True
    add "halfblack"

    $ old = answers[i]
    style_prefix "enter"

    frame:
        xysize(500, 400)
        align(0.5, 0.5)
        vbox:
            spacing 1
            frame:
                xfill True
                ysize 50
                background "#0b5fbed8"
                imagebutton auto "images/Minigames Menu/exit_%s.png" action Hide("input_keys") keysym ['K_ESCAPE']:
                    xalign 1.0
            frame:
                xfill True
                ysize 150
                vbox:
                    xfill True
                    spacing 40
                    text "Original keyword:" style "notes"
                    text "{b}[old]{/b}" style "notes" color "#007FFF":
                        align(0.3, 0.5)
            frame: 
                xfill True
                yfill True
                vbox:
                    xfill True
                    spacing 40
                    text "New keyword:" style "notes"
                    input value key length 40 allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789- " style "notes" color "#007FFF":
                        align(0.3, 0.5)
                        default_focus True
                        copypaste True
                        bold True
                textbutton "ENTER" action [Function(reset_key, i), Hide("input_keys")] keysym ["K_RETURN", "K_KP_ENTER"]:
                    align (1.0, 1.0)

screen input_text:
    modal True
    add "halfblack"

    frame:
        xysize(800, 400)
        align(0.5, 0.5)
        vbox:
            spacing 1
            frame:
                xfill True
                ysize 50
                background "#0b5fbed8"
                imagebutton auto "images/Minigames Menu/exit_%s.png" action [SetVariable("current_text", ""), Hide("input_text")] keysym ['K_ESCAPE']:
                    xalign 1.0
                imagebutton auto "images/Button/info_icon_%s.png" action NullAction():
                    tooltip "One sentence will do."
                    align(0.0, 0.5)
            frame: 
                xfill True
                yfill True
                ypadding 20
                xpadding 20

                style_prefix "enter"
                
                if current_text == "":
                    text "Paste a text here.":
                        size 30
                        color "#303031a1"
                        align(0.0, 0.0)
                vbox:
                    xfill True
                    yfill True
                    spacing 40
                    input value new_text length 256:
                        size 30
                        color "#303031"
                        align(0.0, 0.0)
                        default_focus True
                        caret_blink True
                        copypaste True
                        multiline True
                if edit_sentence:
                    textbutton "ENTER" action [Function(store_sentence, current_text), SetVariable("edit_sentence", False), SetVariable("current_text", ""), Hide("input_text")] keysym ["K_RETURN", "K_KP_ENTER"]:
                        align(1.0, 1.0)
                else:
                    textbutton "ENTER" action [Function(store_sentence, current_text), SetVariable("current_text", ""), Hide("input_text")] keysym ["K_RETURN", "K_KP_ENTER"]:
                        align(1.0, 1.0)
    
    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                xalign 0.5
                text tooltip:
                    size 20

style enter_button_text:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 40

screen preprocess_text_dull:
    add "bg quiz main"

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

                imagebutton auto "images/Button/pen_%s.png" action [Function(set_in_save, False), Jump("edit_title")]:
                    yoffset 5


    #get the notes and keywords if they exists
    #$ notes = get_notes()
    
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
        
    vbox:
        align (0.8, 0.5)
        spacing 20

        text "Quiz Type": #specify with a number later
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 50
            color "#FFFFFF"
            align (0.5, 0.5)

        frame:
            xysize (380, 70)
            align (0.5, 0.5)
            background Frame("images/Minigames Menu/round_frame.png")
            
            hbox:
                align (0.5, 0.5)
                spacing 10
                text quiz_type:
                    font "KronaOne-Regular.ttf"
                    bold True
                    size 24
                    color "#303031"
                    align (0.5, 0.5)

                imagebutton auto "images/Button/down_%s.png":
                    align (0.5, 0.5)

        imagebutton auto "images/Button/save_quiz_%s.png":
            xalign 0.5
            yalign 0.5
            yoffset 200