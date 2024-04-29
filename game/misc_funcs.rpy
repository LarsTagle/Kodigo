init -2 python:
    global caller_screen, mn_caller_screen
    caller_screen = "main_menu"
    mn_caller_screen = "quiz_list_screen"
    #start music or playlist
    def mplay(mname, fadein=1, fadeout=1, loop=True, channel="music", ext="ogg"):
        list = []
        mname = make_list(mname)
        for i in mname:
            list.append(music_dir + "/" + i + "." + ext)
        renpy.music.play(list, channel=channel, loop=loop, fadein=fadein, fadeout=fadeout)

    #play sound
    def sndplay(mname, fadein=0, fadeout=0, channel="sound", ext="ogg", audio_dir=audio_dir):
        if mname:
            mname = make_list(mname)
            lst = []
            for i in mname:
                lst.append(audio_dir + "/" + i + "." + ext)
            renpy.play(lst, channel=channel, fadein=fadein, fadeout=fadeout)

    #play audio for an audio channel that supports multi-threading
    def splay(mname, fadein=0, fadeout=0, channel=config.play_channel, ext="ogg", audio_dir=audio_dir):
        if mname:
            mname = make_list(mname)
            lst = []
            for i in mname:
                lst.append(audio_dir + "/" + i + "." + ext)
            renpy.play(lst, channel=channel, fadein=fadein, fadeout=fadeout)
    
    #stop sound
    def sndstop(fadeout=0, channel='sound'):
        renpy.music.stop(channel=channel, fadeout=fadeout)

    SPlay = renpy.curry(splay)
    SNDstop = renpy.curry(sndstop)
    MPlay = renpy.curry(mplay)

    #save current screen, for outer
    def save_caller_screen(screen):
        global caller_screen
        caller_screen = screen
    SaveCallerScreen = renpy.curry(save_caller_screen)

    #save current screen, for quiz_game
    def save_mn_caller_screen(screen):
        global mn_caller_screen
        mn_caller_screen = screen
    SaveMNCallerScreen = renpy.curry(save_mn_caller_screen)

init python:
    # cursors
    config . mouse = {
        "hand" : [( "images/mouse/hand1.png" , 2 , 10 ),
                ( "images/mouse/hand1.png" , 2 , 10 ), 
                ( "images/mouse/hand1.png" , 2 , 10 ),
                ( "images/mouse/hand1.png" , 2 , 10 ), 
                ( "images/mouse/hand2.png" , 2 , 10 ),
                ( "images/mouse/hand2.png" , 2 , 10 ), 
                ( "images/mouse/hand3.png" , 2 , 10 ),
                ( "images/mouse/hand3.png" , 2 , 10 ), 
                ( "images/mouse/hand2.png" , 2 , 10 ),
                ( "images/mouse/hand2.png" , 2 , 10 )],
        "finger" : [( "images/mouse/finger.png" , 2 , 10 )],
        "needle" : [("images/mouse/needle_1.png", 0, 194),
                ("images/mouse/needle_1.png", 0, 194), 
                ("images/mouse/needle_1.png", 0, 194),
                ("images/mouse/needle_1.png", 0, 194),
                ("images/mouse/needle_2.png", 0, 194),
                ("images/mouse/needle_2.png", 0, 194),
                ("images/mouse/needle_3.png", 0, 194),
                ("images/mouse/needle_3.png", 0, 194),
                ("images/mouse/needle_2.png", 0, 194),
                ("images/mouse/needle_2.png", 0, 194)],
        "needle_opposite" : [("images/mouse/needle_opposite_1.png", 107, 0),
                ("images/mouse/needle_opposite_1.png", 107, 0), 
                ("images/mouse/needle_opposite_1.png", 107, 0),
                ("images/mouse/needle_opposite_1.png", 107, 0), 
                ("images/mouse/needle_opposite_2.png", 107, 0),
                ("images/mouse/needle_opposite_2.png", 107, 0), 
                ("images/mouse/needle_opposite_3.png", 107, 0),
                ("images/mouse/needle_opposite_3.png", 107, 0), 
                ("images/mouse/needle_opposite_2.png", 107, 0),
                ("images/mouse/needle_opposite_2.png", 107, 0)]}
    