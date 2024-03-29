#summarization working
#keywords extraction working
#sentence mapping working
#question generation working

""" In order to minimize processing time:
    1. In the case that player chooses mixed type of quiz:
        a. only 1/4 of the sentences get generated as questions, all would have multiple choices. (this is the most processing heavy)
        b. 2/4 of it, it would be fill in the blanks, with:
            i. 1/2 would be multiple questions.
            ii. 1/2 would have multiple choices.
        c. the last 1/4 would either be T/F questions or choose from a box. (since idk and don't have a code yet for T/F questions let's just do the latter)
    2. User chooses all multiple choices:
        a. 1/4 of the sentences get generated as questions. (we can't just do all since it really is that long as shit time to process)
        b. fill in the blanks
    3. Still don't know how to choose which sentences get turned to questions. (aiming for the most intelligible questions.)
"""

""" Preexisting issues/errors in the code:
    1. Handle the uncreated json files. (either with adding a function to get app to ask the player to exit or not (like in story mode) just don't know at which part of the code that is
    2. Errors of unhidden bgs.
    3. Add condition on the code for the cheating.
    4. etc

"""
#there's an issue with sentence mapping
#though you should probably work on thdcbvvvvvvvvvvvvv whatever do what you pls
init:
    $ base_path = ""
    $ quiz_title = f"Quiz {persistent.quiz_def_num}"

init python:
    import json
    import subprocess

    base_path = os.getcwd() #get working directory
    global python_path

    def get_path(relative_path):
        return os.path.join(base_path, relative_path)

    def init_json(): #file path
        global fp
        fp = get_path(f"kodigo/game/python/docs/{quiz_title}.json")

        init_data = {
            "notes": "",
            "sentences": [],
            "ranked_sentences": [],
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

    def get_sents_len():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        sentences = quiz["sentences"]

        return len(sentences)

    def set_in_save(bool):
        global in_save
        in_save = bool

init 1:
    $ python_path = get_path("Python311/python.exe")

screen preprocess_text:
    tag menu
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("preprocess_text"), Jump("quit_warning")]:
        xalign 0.86
        yalign 0.04

    #get the notes and keywords if they exists
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

        vpgrid:
            cols 1
            scrollbars "vertical"
            spacing 5
            mousewheel True

            vbox:
                xsize 570
                ysize 590
                if notes:
                    text notes style "notes_style"
                else:
                    text "Texts from the document will appear here." style "notes_style"

    if notes:
        imagebutton auto "images/Button/summarize_%s.png" action Jump("summarize"):
            xalign 0.28
            yalign 0.85
    if keywords:
        imagebutton auto "images/Button/edit_%s.png" action Jump("edit_keywords"): #skip this for now
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
                        text "Keywords from the text will appear here." style "notes_style"
    hbox:
        xalign 0.690
        yalign 0.15

        text "[quiz_title]": #specify with a number later
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 70
            color "#FFFFFF"

        imagebutton auto "images/Button/edit_title_%s.png" action [Function(set_in_save, False), Jump("edit_title")]:
            xoffset 40

    if not keywords:
        imagebutton auto "images/Button/upload_%s.png" action Jump("upload_file"):
            xalign 0.75
            yalign 0.8
    else:
        imagebutton auto "images/Button/create_quiz_%s.png" action [Hide("preprocess_text"), Jump("genarating_quiz")]: #since we are skipping editting the keywords & texts, we proceed here next
            xalign 0.75
            yalign 0.8

label upload_file:
    $ show_s("preprocess_text_dull")
    show halfblack
    hide screen preprocess_text

    $ py_path = get_path(f"kodigo/game/python/upload_file.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    screen terminate_process:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("terminate_process"), Function(terminate, process)]:
            xalign 0.86
            yalign 0.04

    show screen terminate_process

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen uploading
        pause 0.1

    screen uploading:
        text "Uploading document...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    hide screen uploading
    jump get_sentences

#asks the player if they want to summarize first or have user input for keywords
label ask_player:
    call screen ask

    screen ask:
        frame:
            xalign 0.5
            yalign 0.5
            xpadding 40
            ypadding 40
            xsize 600
            ysize 450
            background "#D9D9D9"

            vbox:
                text "Would you like to summarize the text first before keywords extraction?":
                    font "Copperplate Gothic Thirty-Three Regular.otf"
                    size 50
                    color "#303031"
                    xalign 0.5
                    yalign 0.5

                hbox:
                    xalign 0.5
                    yalign 0.5
                    yoffset 60
                    spacing 40

                    imagebutton auto "images/Button/yes_%s.png" action [Hide("ask"), Jump("summarize")]
                    imagebutton auto "images/Button/no_%s.png" action [Hide("ask"), Jump("get_keywords")]

#should ask question first before proceeding
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
        jump ask_player
    else:
        hide halfblack
        $ hide_s("preprocess_text_dull")
        call screen preprocess_text

label get_keywords:
    $ py_path = get_path(f"kodigo/game/python/keywords.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen extracting_keys
        pause 0.1

    screen extracting_keys:
        text "Extracting keywords...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    hide screen extracting_keys
    jump mapping_sentences

#can do this earlier so the processing for getting the quiz proper wouldn't be so big
#also to highlight/bolden the keywords.
#ALSO there should be a case for multiple keywords per sentence???? don't know how to do that
label mapping_sentences:
    $ py_path = get_path(f"kodigo/game/python/map_sentences.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    while not is_subprocess_finished(process):
        pause 0.1

    hide halfblack
    $ hide_s("preprocess_text_dull")
    call screen preprocess_text

label summarize:
    #I'll add the condition or screen for if < 15
    if get_sents_len() < 15:
        call screen preprocess_text
    else:
        $ show_s("preprocess_text_dull")
        show halfblack
        hide screen preprocess_text

        $ notes = get_notes()
        $ py_path = get_path(f"kodigo/game/python/summarize.py")
        $ process = subprocess.Popen([python_path, py_path, quiz_title, notes], creationflags=subprocess.CREATE_NO_WINDOW)

        #Check if the subprocess has finished
        while not is_subprocess_finished(process):
            show screen summarizing
            pause 0.1

        screen summarizing:
            text "Summarizing...":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5
        hide screen summarizing
        jump get_keywords

label genarating_quiz:
    $ show_s("preprocess_text_dull")
    show halfblack
    hide screen preprocess_text

    $ py_path = get_path(f"kodigo/game/python/fill_in_blanks.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        pause 0.1

    screen success:
        text "Quiz successfully generated!":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    show screen success
    pause 2.0
    show halfblack
    hide screen success
    $ hide_s("preprocess_text_dull")
    call screen save_quiz

screen save_quiz:
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png":
        xalign 0.86
        yalign 0.04

    hbox:
        xalign 0.5
        yalign 0.1
        text "[quiz_title]": #specify with a number later
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 150
            color "#FFFFFF"

        imagebutton auto "images/Button/edit_title_%s.png" action [Function(set_in_save, True), Jump("edit_title")]:
            xoffset 40
            yoffset 45

    vbox:
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 40
            text "Questions": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 70
                color "#FFFFFF"
            text "Answers": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 70
                color "#FFFFFF"
