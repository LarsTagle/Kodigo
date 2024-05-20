#to do next:
#try another preprocessing method for pdf texts, else just remove that all together.

#error found
#handle when keywords failed to extract

#reset this after creation for less processing
define persistent.quiz_def_num = 1 #changes if the player want to save "Quiz 1", "Quiz 2" etc

init:
    $ quiz_title = f"Quiz {persistent.quiz_def_num}"
    $ edit_quiz = False
    $ quiz_type = "Multiple Choices"

init python:
    import json
    import subprocess
    import shutil

    base_path = os.getcwd() #get working directory

    def get_path(relative_path):
        return os.path.join(base_path, relative_path)

    def terminate(process):
        process.terminate()

    def is_subprocess_finished(process):
        return process.poll() is not None

    def init_json(): #file path
        edit_quiz = False
        global fp
        fp = get_path(f"kodigo/game/python/temp/{quiz_title}.json")

        #delete all the uncreated quizzes files in temp
        folder_path = get_path("kodigo/game/python/temp/")
        # Get a list of all files in the folder
        files = os.listdir(folder_path)
        # Iterate through the list of files and delete each one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)

        #start again
        init_data = {
            "notes": "",
            "sentences": [],
            "ranked_sentences": [],
            "keywords": [],
            "answers": [],
            "questions": [],
            "type": "",
            "records": [],
            "mastery": [],
            "learned": 0.1
        }

        #set default type
        global quiz_type
        quiz_type = "Multiple Choices"
        
        init_data["type"] = quiz_type

        with open(fp, 'w') as file:
            json.dump(init_data, file)
    
    #if just editting a quiz then copy it to temp then edit there
    def copy_json():
        global fp 

        with open(get_path(f"kodigo/game/python/quizzes/{quiz_loc}/{current_quiz}.json") , 'r') as file:
            quiz = json.load(file)
        
        fp = get_path(f"kodigo/game/python/temp/{quiz_title}.json")

        with open(fp, 'w') as file:
            json.dump(quiz, file)
    CopyJson = renpy.curry(copy_json)

    #check if text is uploaded
    def is_notes():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        if quiz["notes"] == "not supported":
            return "not supported"
        elif quiz["notes"] or quiz["sentences"]:
            return True

        return False

    def get_answers():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        return quiz["answers"]
    
    def get_sentences():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        return quiz["sentences"]

    #deletes json file if it exists
    def del_json():
        if os.path.exists(fp):
            os.remove(fp)

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

    def get_quiz():
        with open(fp, 'r') as file:
            quiz = json.load(file)
        questions = quiz["questions"]
        answers = quiz["answers"]
        return questions, answers
    
    def set_type(type):
        global quiz_type
        quiz_type = type 

        with open(fp, 'r') as file:
            quiz = json.load(file)
        
        quiz["type"] = type

        with open(fp, 'w') as file:
            json.dump(quiz, file)
    
    def type_choices():
        choices = ["Multiple Choices", "Identification", "Mixed"]
        ch = []
        ch.append(quiz_type)

        for choice in choices:
            if choice not in ch:
                ch.append(choice) 
        
        return ch

    def is_type_set():
        with open(fp, 'r') as file:
            quiz = json.load(file)

        if quiz["type"]:
            return True

        return False

    def save():
        #add the quiz in the list
        quiz_list["custom"].append(quiz_title)
        with open(list_path, 'w') as file:
            json.dump(quiz_list, file)
        #move it to the right folder
        destination = get_path("kodigo/game/python/quizzes/custom/")
        shutil.copy(fp, destination)

    def reset_quiz_title():
        if f"Quiz {persistent.quiz_def_num}" == quiz_title:
            persistent.quiz_def_num += 1
    
    def reset_title():
        quiz_title = f"Quiz {persistent.quiz_def_num}" #reset
        new_title = quiz_title

    #for text input defs
    def store_sentence(sent):
        with open(fp, 'r') as file:
            quiz = json.load(file)
        
        if edit_sentence:
            quiz["sentences"][edit_sentence_index] = sent
            quiz["answers"][edit_sentence_index] = ""
            with open(fp, 'w') as file:
                json.dump(quiz, file)
        else:
            quiz["sentences"].append(sent)
            quiz["answers"].append("")
            with open(fp, 'w') as file:
                json.dump(quiz, file)

            #call a subprocess to get the answer
            py_path = get_path(f"kodigo/game/python/keywords.py")
            subprocess.Popen([python_path, py_path, quiz_title, "last"], creationflags=subprocess.CREATE_NO_WINDOW)

init 1:
    $ python_path = get_path("Python311/python.exe")

screen preprocess_text:
    tag minigame
    add "bg quiz main"

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Function(set_in_save, False), Hide("preprocess_text"), Jump("quit_warning")] keysym ['K_ESCAPE']:
        xalign 0.86
        yalign 0.04

    frame:
        xalign 0.5
        yalign 0.1
        xsize 1500
        ysize 135
        background "#ffffff00"

        hbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            text "[quiz_title]": #specify with a number later
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 80
                color "#FFFFFF"

            imagebutton auto "images/Button/pen_%s.png" action [Function(set_in_save, False), Jump("edit_title")]:
                yoffset 5

    #get the notes and keywords if they exists
    #$ notes = get_notes()
    $ answers = get_answers()

    if answers:
        $ highlighted_sentences = get_boldened_notes()
        $ sentences = get_sentences()
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
                for i in range(len(sentences)+1):
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

                                if i != len(sentences):
                                    vbox: 
                                        xsize 1000
                                        if answers: 
                                            text highlighted_sentences[i] style "notes"
                                        else:
                                            text sentences[i] style "notes"
                                    vbox:
                                        xalign 1.0 
                                        yalign 0.5
                                        spacing 5

                                        if answers and answers[i]:
                                            imagebutton auto "images/Button/edit_text_%s.png" action [SetVariable("current_text", sentences[i]), SetVariable("edit_sentence", True), SetVariable("edit_sentence_index", i), Show("input_text")]
                                            imagebutton auto "images/Button/edit_icon_%s.png" action [Function(set_old_key, answers, i), ShowMenu("input_keys", sentences, answers, i)]
                                        else:
                                            imagebutton auto "images/Button/edit_text_%s.png" action [SetVariable("current_text", sentences[i]), SetVariable("edit_sentence", True), SetVariable("edit_sentence_index", i), Show("input_text")]
                                            imagebutton auto "images/Button/edit_icon_%s.png" action [Function(set_old_key, answers, i), ShowMenu("input_keys", sentences, answers, i)]

                                else:          
                                    vbox: 
                                        xsize 1000
                                        text "Add another sentence..." style "notes"
                                    vbox:
                                        xalign 1.0 
                                        yalign 0.5
                                        spacing 5
                                        imagebutton auto "images/Button/edit_text_%s.png" action Show("input_text")                        
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
                        vbox:
                            xalign 1.0 
                            yalign 0.5
                            spacing 5
                            imagebutton auto "images/Button/edit_text_%s.png" action Show("input_text")

    if answers and answers[-1] != "":
        imagebutton auto "images/Button/create_quiz_%s.png" action [Hide("preprocess_text"), Jump("genarating_quiz")]: 
            align (0.95, 0.984)
    else:
        imagebutton auto "images/Button/upload_%s.png" action Jump("upload_file"):
            align (0.95, 0.984)

label upload_file:
    $ show_s("preprocess_text_dull")
    hide screen preprocess_text

    $ py_path = get_path(f"kodigo/game/python/upload_file.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    screen terminate_process:
        imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("terminate_process"), Function(terminate, process)] keysym ['K_ESCAPE']:
            xalign 0.86
            yalign 0.04

    show screen terminate_process

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen uploading
        pause 0.1

    screen uploading:
        add "halfblack"
        text "Uploading document...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    hide screen uploading

    screen not_supported:
        add "halfblack"
        frame:
            align (0.5, 0.5)
            xysize(450, 300)
            vbox:
                spacing 80
                frame:
                    xfill True
                    ysize 50
                    background "#0b5fbed8"
                    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Hide("not_supported"), Show("preprocess_text")]:
                        xalign 1.0
                
                text "File type not supported.":
                    size 30
                    color "#303031"
                    xalign 0.5
                    yalign 0.5

    if not is_notes():
        call screen preprocess_text
    elif is_notes() == "not supported":
        call screen not_supported

    jump get_sentences

#asks the player if they want to summarize first or have user input for keywords
label ask_player:
    call screen ask

    screen ask:
        add "halfblack"
        style_prefix "yes_or_no"

        frame:
            align (0.5, 0.5)
            xysize(600, 350)
            vbox:
                spacing 50
                frame:
                    xfill True
                    ysize 50
                    background "#0b5fbed8"
                    imagebutton auto "images/Button/info_icon_%s.png" action NullAction():
                        tooltip "Summarizing improves keyword accuracy."
                        align(1.0, 0.5)
                text "Summarize text before extracting keywords?":
                    size 30
                    color "#303031"
                    xalign 0.5
                    yalign 0.5

                hbox:
                    align(0.5, 0.5)
                    spacing 40

                    frame:
                        background "#0b5fbed8"
                        textbutton "YES" action [Hide("ask"), Jump("summarize")]

                    frame:
                        background "#D3D3D3"
                        textbutton "NO" action [Hide("ask"), Jump("get_keywords")]
        
        $ tooltip = GetTooltip()

        if tooltip:

            nearrect:
                focus "tooltip"
                prefer_top True

                frame:
                    xalign 0.5
                    text tooltip:
                        size 20
    
style yes_or_no_button_text:
    font "fonts/Inter-Bold.ttf"
    color "#ffffff"
    hover_color "#ccc9c9"
    selected_color "#d3d0cf"
    size 25

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
            add "halfblack"
            text "Extracting sentences...":
                font "Copperplate Gothic Thirty-Three Regular.otf"
                size 60
                color "#FFFFFF"
                xalign 0.5
                yalign 0.5

        #maybe we should let the user know how many sentences there is
        hide screen extract_sent
        #call screen preprocess_text
        jump ask_player
    else:
        hide halfblack
        $ hide_s("preprocess_text_dull")
        call screen preprocess_text

label get_keywords:
    $ py_path = get_path(f"kodigo/game/python/keywords.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title, "bulk"], creationflags=subprocess.CREATE_NO_WINDOW)

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen extracting_keys
        pause 0.1

    screen extracting_keys:
        add "halfblack"
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
        hide screen preprocess_text

        $ notes = get_notes()
        $ py_path = get_path(f"kodigo/game/python/summarize.py")
        $ process = subprocess.Popen([python_path, py_path, quiz_title, notes], creationflags=subprocess.CREATE_NO_WINDOW)

        #Check if the subprocess has finished
        while not is_subprocess_finished(process):
            show screen summarizing
            pause 0.1

        screen summarizing:
            add "halfblack"
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
    hide screen preprocess_text

    #$ py_path = get_path(f"kodigo/game/python/fill_in_blanks.py")
    $ py_path = get_path(f"kodigo/game/python/gen_questions.py")
    $ process = subprocess.Popen([python_path, py_path, quiz_title], creationflags=subprocess.CREATE_NO_WINDOW)

    #Check if the subprocess has finished
    while not is_subprocess_finished(process):
        show screen generating
        pause 0.1
    
    screen generating:
        add "halfblack"
        text "Generating quiz...":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5
    
    hide screen generating

    screen success:
        tag minigame
        add "halfblack"

        button:
            xysize(1920,1080)
            action [Function(hide_s, "preprocess_text_dull"), Show("save_quiz", transition=dissolve)] keysym ['K_SPACE', 'K_ESCAPE']  

        text "Quiz successfully generated!":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

    call screen success

screen save_quiz():
    tag minigame
    add "bg quiz main"

    $ questions, answers = get_quiz()

    imagebutton auto "images/Minigames Menu/exit_%s.png" action [Function(set_in_save, True), Jump("quit_warning")] keysym ['K_ESCAPE']:
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

            imagebutton auto "images/Button/pen_%s.png" action [Function(set_in_save, True), Jump("edit_title")]:
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
                xfill True
                yfill True
                vbox:
                    xfill True
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

                imagebutton auto "images/Button/down_%s.png" action Show("choose_type"):
                    align (0.5, 0.5)

        if is_type_set():
            imagebutton auto "images/Button/save_quiz_%s.png" action [Function(reset_quiz_title), Function(save), Jump("confirm_save")]:
                xalign 0.5
                yalign 0.5
                yoffset 200
        else:
            imagebutton auto "images/Button/save_quiz_%s.png":
                xalign 0.5
                yalign 0.5
                yoffset 200

screen choose_type:
    modal True

    $ choices = type_choices()

    style_prefix "quiz_type"

    frame:
        xysize (380, 150)
        xpadding 14
        ypadding 11
        xalign 0.786
        yalign 0.52
        background Frame("images/Minigames Menu/round_frame.png")

        vbox:
            xalign 0.0
            spacing 1
            hbox:
                align (0.5, 0.5)
                spacing 5
                textbutton quiz_type action [Function(set_type, choices[0]), Hide("choose_type")]:
                    align (0.5, 0.5)

                imagebutton auto "images/Button/down_%s.png" action Hide("choose_type"):
                    align (0.5, 0.5)

            textbutton f"{choices[1]}" action [Function(set_type, choices[1]), Hide("choose_type")]
            textbutton f"{choices[2]}" action [Function(set_type, choices[2]), Hide("choose_type")]

style quiz_type_button_text:
    font "KronaOne-Regular.ttf"
    bold True
    size 24
    color "#303031"
    hover_color "#606064"
    selected_color "#585655"

label confirm_save:
    hide screen save_quiz
    $ show_s("save_quiz_dull")

    call screen saved

    screen saved:
        tag minigame
        add "halfblack"

        button:
            xysize(1920,1080)
            action [Hide("saved"), Function(hide_s, "save_quiz_dull"), Function(reset_title), Show(mn_caller_screen, transition=dissolve)] keysym ['K_ESCAPE']

        text "Quiz save successfully!":
            font "Copperplate Gothic Thirty-Three Regular.otf"
            size 60
            color "#FFFFFF"
            xalign 0.5
            yalign 0.5

style q_and_a:
    font "KronaOne-Regular.ttf"
    size 24
    color "#303031"