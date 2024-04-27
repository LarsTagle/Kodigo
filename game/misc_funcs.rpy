init -2 python:
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