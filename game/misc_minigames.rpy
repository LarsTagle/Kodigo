"""
to add next:
1. depends on the direction:
    a. do the second round of sewing opposite it.
    b. it should end at the index at the opposite end of the beginning of the first sewing.
    c. restart the timer.
2. fix ui:
    a. after the dot has clicked, if it's adjacent dot is also clicked, replace the dot with a thread.
    b. would need to create new images for that I guess.
"""

init python:
    global start_sew
    dot_pos = [[996, 228], [1055, 261], [1115, 304], [1181, 321], [1232, 354], [1247, 406], [1232, 464], [1232, 523],
                [1247, 583], [1247, 643], [1196, 676], [1130, 693], [1070, 740], [1011, 786], [952, 757], [894, 724],
                [829, 691], [764, 660], [749, 583], [764, 506], [749, 439], [749, 374], [799, 337], [864, 304], [930, 261]]
    
    def init_sewing_vars():
        global sew_direction, pos_clicked, hint_time, start_sew, dot_idle, sewn_dots, sewing_time, sewing_bar, sewing_warning
        pos_clicked = []

        for i in range(len(dot_pos)):
            pos_clicked.append(None)

        start_sew = True
        sew_direction = None
        hint_time = 3
        sewn_dots = 0
        dot_idle = "minigame/dot.png"
        sewing_time = 25
        sewing_bar = 100
        sewing_warning = False

    def dot_clicked(i):
        pos_clicked[i] = True
        

transform hovered:
    matrixcolor BrightnessMatrix(0.2)

label init_sewing:
    $ init_sewing_vars()

    $ show_s("sewing_game")
    show halfblack
    with dissolve

    screen init_sewing_screen:
        modal True

        button:
            xysize(1920,1080)
            action [Hide("init_sewing_screen"), Function(hide_s, "sewing_game"), Show("sewing_game"), Show("sewing_timer")]
        
        text "Click each dots to sew it!" style "game_instruction"

    call screen init_sewing_screen with dissolve

screen reset_hint_timer:
    timer 3.0 action [SetVariable("dot_idle", "hint_dot"), Hide("reset_hint_timer")]

screen sewing_timer:
    # timer animation
    if sewing_time >  0 :
        #timer to change the color of bar
        timer sewing_time *  0.6666 action SetVariable("sewing_warning", True)

        # visualization of the timer as a bar
        bar:
            # position and size of the timebar
            align(0.5, 0.05)
            xysize(1040 , 35)
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=sewing_time)

            # recolor and flicker the left bar bar,
            # when less than a third of the time is left
            if sewing_warning:
                left_bar Frame(At( "gui/bar/left.png" , paint2( "#e02" , "#e028" , 0.2 )), gui . bar_borders, tile = gui . bar_tile)

        # loss by timer
        timer sewing_time repeat True action [SPlay( "gameover" ), Return("loss")]

        if sewn_dots == len(dot_pos):
            timer 0.01 repeat True action [SPlay( "gamewin" ), Hide("sewing_timer")]

screen sewing_game:
    add "bg sewing"
    image "images/minigame/BUseal.png" align (0.55, 0.5)
    
    if sewn_dots < len(dot_pos):
        for i in range(len(dot_pos)):
            $ j, k = dot_pos[i]
            imagebutton:
                if pos_clicked[i]:
                    idle "minigame/dot_b.png"
                else:
                    idle "minigame/dot.png"
                hover "dot_hover"
                mouse "needle"
                activate_sound "audio/click.ogg"
                xpos j ypos k

                #if game just starting
                if start_sew:
                    idle dot_idle
                    action [SetVariable("start_sew", False), SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
                #if sew_direction is not yet set
                elif sew_direction == None:
                    #if previous dot already clicked, and current dot is not clicked
                    if pos_clicked[i-1] and pos_clicked[i] == None:
                        idle dot_idle
                        action [SetVariable("sew_direction", "clockwise"), SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
                    #if the next dot won't cause index out of range and is already clicked, and current dot is not clicked
                    elif i+1 < len(dot_pos) and pos_clicked[i+1] and pos_clicked[i] == None:
                        idle dot_idle
                        action [SetVariable("sew_direction", "counter_clockwise"), SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
                    #if dot is the last index, and first that is already clicked, and current dot is not yet clicked
                    elif i == len(dot_pos)-1 and pos_clicked[0] and pos_clicked[i] == None:
                        idle dot_idle
                        action [SetVariable("sew_direction", "counter_clockwise"), SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
                #if clockwise and previous dot is already clicked and current is not yet clicked
                elif sew_direction == "clockwise" and pos_clicked[i-1] and pos_clicked[i] == None:
                    idle dot_idle
                    action [SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
                #if next dot won't cause any index out of range and is already clicked, and current is not yet clicked
                elif i+1 < len(dot_pos) and sew_direction == "counter_clockwise" and pos_clicked[i+1] and pos_clicked[i] == None:
                    idle dot_idle
                    action [SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
                elif sew_direction == "counter_clockwise" and i == len(dot_pos)-1 and pos_clicked[0] and pos_clicked[i] == None:
                    idle dot_idle
                    action [SetVariable("sewn_dots", sewn_dots+1), SetVariable("dot_idle", "minigame/dot.png"), Function(dot_clicked, i), Show("reset_hint_timer")]
            
        timer 3.0 action SetVariable("dot_idle", "hint_dot")
    else:
        add "halfblack"

        button:
            xysize(1920,1080)
            action [Hide("sewing_game"), Hide("reset_hint_timer"), Jump("chapter1_3")]
        
        text "Sewing completed!" style "game_instruction"

label loss:
    hide screen sewing_timer
    hide screen sewing_game 
    "you LOSSED!"
    jump chapter1_3
            
image dot_hover:
    "minigame/dot.png"
    hovered

image hint_dot:
    "minigame/dot.png"
    pause 0.3
    "dot_hover"
    pause 0.2
    repeat

style game_instruction:
    font "Copperplate Gothic Thirty-Three Regular.otf"
    size 80
    color "#FFFFFF"
    xalign 0.5
    yalign 0.5
