init:
    $ base_path = ""
    $ quiz_title = f"Quiz {persistent.quiz_def_num}"

init python:
    import json
    import subprocess

    base_path = os.getcwd() #get working directory

    def get_path(relative_path):
        return os.path.join(base_path, relative_path)

    def init_json(): #file path
        global fp
        fp = get_path(f"kodigo/game/python/docs/{quiz_title}.json")

        init_data = {
            "notes": "",
            "sentences": [],
            "keywords": [],
            "answers": [],
            "questions": []
        }

        with open(fp, 'w') as file:
            json.dump(init_data, file)

    #check if text is uploaded
    def is_notes():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        if quiz["notes"]:
            return True

        return False

    #deletes json file if it exists
    def del_json():
        if os.path.exists(fp):
            os.remove(fp)

    # get_notes and get_keys can be combined
    def get_notes():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        if quiz["notes"]:
            return quiz["notes"]

        return None

    def get_keys():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        if quiz["keywords"]:
            return quiz["keywords"]

        return None

    def get_str(arr):
        if arr:
            str = ""
            for a in arr:
                str += a + ", "
            return str

        return None

screen create_quiz:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("create_quiz"), Jump("quit_warning")]:
        xalign 0.86
        yalign 0.04

    #get the notes if it exists
    $ notes = get_notes()
    $ keywords = get_str(get_keys())

    $ file_path = get_path(f"kodigo/game/python/docs/{quiz_title}.txt")

    $ file_path_keys = get_path(f"kodigo/game/python/docs/{quiz_title}_keys.json")

    $ file_path_mapped = get_path(f"kodigo/game/python/docs/{quiz_title}_mapped.json")

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

        if notes:
            vpgrid:
                cols 1
                scrollbars "vertical"
                spacing 5
                mousewheel True

                vbox:
                    text notes style "notes_style"
        else:
            ypadding 40
            xpadding 40
            text "Texts from the document will appear here." style "notes_style":
                xalign 0.5
                yalign 0.5

    if notes:
        imagebutton auto "images/Button/summarize_%s.png" action Jump("summarize"):
            xalign 0.28
            yalign 0.85
    if keywords:
        imagebutton auto "images/Button/edit_%s.png":# action Jump("edit_keywords"): skip this for now
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
                        text keywords:
                            font "KronaOne-Regular.ttf"
                            size 24
                            color "#303031"
            else:
                ypadding 40
                xpadding 40
                text "Keywords from the text will appear here." style "notes_style":
                    xalign 0.5
                    yalign 0.5

    hbox:
        xalign 0.690
        yalign 0.15

        text "[quiz_title]": #specify with a number later
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 70
            color "#FFFFFF"

        imagebutton auto "images/Button/edit_title_%s.png" action Jump("edit_title"):
            xoffset 40

    if not notes:
        imagebutton auto "images/Button/upload_%s.png" action Jump("upload_file"):
            xalign 0.75
            yalign 0.8
    else:
        imagebutton auto "images/Button/create_quiz_%s.png": #since we are skipping editting the keywords & texts, we proceed here next
            xalign 0.75
            yalign 0.8

label quit_warning:
    #checks if questions are generated
    if is_notes():
        $ show_s("create_quiz_dull")
        show halfblack
        call screen warning
    else:
        $ del_json()
        call screen custom_quizzes

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

                    imagebutton auto "images/Button/yes_%s.png" action [Hide("warning"), Function(set_bool, True), Jump("warning_2")]
                    imagebutton auto "images/Button/no_%s.png" action [Hide("warning"), Function(set_bool, False), Jump("warning_2")]

label warning_2:
    $ hide_s("create_quiz_dull")
    hide halfblack

    #if player wants to exit
    if bool:
        $ file_path = f"kodigo/game/python/docs/{quiz_title}.txt"
        $ file_path_json = f"kodigo/game/python/docs/{quiz_title}.json"
        $ file_path_keys = f"kodigo/game/python/docs/{quiz_title}_keys.json"

        if os.path.exists(file_path):
            $ os.remove(file_path) # remove notes
        if os.path.exists(file_path_json):
            $ os.remove(file_path_json)
        if os.path.exists(file_path_keys):
            $ os.remove(file_path_keys)
        call screen custom_quizzes with dissolve
    else:
        call screen create_quiz

label edit_title:
    $ show_s("create_quiz_dull")
    hide screen create_quiz

    python:
        old_fp = get_path(f"kodigo/game/python/docs/{quiz_title}.json")
        temp = renpy.input("Quiz name:", length=17)
        temp = temp.strip()
        new_fp = get_path(f"kodigo/game/python/docs/{temp}.json")

    screen duplicate:
        vbox:
            xalign 0.5
            yalign 0.5
            xsize 1000
            ysize 100
            spacing 5
            text "Can't have multiple quizzes with the same name.":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#999999"
                xalign 0.5
                yalign 0.5
            text "Try again.":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#999999"
                xalign 0.5
                yalign 0.5

    #duplicate name
    if os.path.exists(new_fp) and old_fp != new_fp:
        show screen duplicate
        pause 2.0
        hide screen duplicate
        $ hide_s("create_quiz_dull")
        call screen create_quiz
    elif os.path.exists(old_fp):
        $ os.rename(old_fp, new_fp)
        $ quiz_title = temp
        $ fp = get_path(f"kodigo/game/python/docs/{quiz_title}.json") #reset

    $ hide_s("create_quiz_dull")
    call screen create_quiz

label upload_file:
    $ show_s("create_quiz_dull")
    show halfblack
    hide screen create_quiz
    $ python_path = get_path(f"kodigo/game/python/Python311/python.exe")
    $ py_path = get_path(f"kodigo/game/python/upload_file.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    screen terminate_process:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("terminate_process"), Function(terminate, process)]:
            xalign 0.86
            yalign 0.04

    show screen terminate_process

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen processing
        pause 0.1

    screen processing:
        text "Processing document...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    hide screen processing

label get_sentences:
    #if uploading successful
    if is_notes():
        hide screen terminate_process
        $ notes = get_notes()
        $ py_path = get_path(f"kodigo/game/python/get_sentences.py")
        $ process = subprocess.Popen([python_path, py_path, quiz_title, notes], creationflags=subprocess.CREATE_NO_WINDOW)

        #might need to store this somewhere else for code minimization
        while not is_subprocess_finished(process):
            show screen extract_sent
            pause 0.1

        screen extract_sent:
            text "Extracting sentences...":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5

        #maybe we should let the user know how many sentences there is

        hide screen extract_sent
        jump get_keywords
    else:
        hide halfblack
        $ hide_s("create_quiz_dull")
        call screen create_quiz

screen create_quiz_dull:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    #get the notes if it exists
    $ notes = get_notes()
    $ keywords = get_str(get_keys())

    $ file_path = get_path(f"kodigo/game/python/docs/{quiz_title}.txt")

    $ file_path_keys = get_path(f"kodigo/game/python/docs/{quiz_title}_keys.json")

    $ file_path_mapped = get_path(f"kodigo/game/python/docs/{quiz_title}_mapped.json")

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

        if notes:
            vpgrid:
                cols 1
                scrollbars "vertical"
                spacing 5
                mousewheel True

                vbox:
                    text notes style "notes_style"
        else:
            ypadding 40
            xpadding 40
            text "Texts from the document will appear here." style "notes_style":
                xalign 0.5
                yalign 0.5

    if notes:
        imagebutton auto "images/Button/summarize_%s.png":
            xalign 0.28
            yalign 0.85
    if keywords:
        imagebutton auto "images/Button/edit_%s.png":# action Jump("edit_keywords"): skip this for now
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
                        text keywords:
                            font "KronaOne-Regular.ttf"
                            size 24
                            color "#303031"
            else:
                ypadding 40
                xpadding 40
                text "Keywords from the text will appear here." style "notes_style":
                    xalign 0.5
                    yalign 0.5

    hbox:
        xalign 0.690
        yalign 0.15

        text "[quiz_title]": #specify with a number later
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 70
            color "#FFFFFF"

        imagebutton auto "images/Button/edit_title_%s.png":
            xoffset 40

    if not notes:
        imagebutton auto "images/Button/upload_%s.png":
            xalign 0.75
            yalign 0.8
    else:
        imagebutton auto "images/Button/create_quiz_%s.png": #since we are skipping editting the keywords & texts, we proceed here next
            xalign 0.75
            yalign 0.8
