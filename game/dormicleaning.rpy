screen dormicleaning_instructions:
    tag menu
    add "bg roomnight"

    imagebutton auto "images/Button/exit_%s.png" action ShowMenu("minigame"):
        xalign 0.97
        yalign 0.06

    frame:
        xpadding 40
        ypadding 50
        xalign 0.5
        yalign 0.60
        background "#D9D9D9"

        vbox:
            spacing 25

            text "Dormicleaning":
                style "minigame_title_font"
                color "#000000"
                xalign 0.5
                yalign 0.5

            text "Objective: Find lost items in a dormitory room within a limited time.":
                color "#000000"
                font "Inter-Bold.ttf"
                size 40

            text "Gameplay:\n• Use your mouse to explore the dormitory room.\n• Click on the objects you believe match the descriptions provided at the bottom of the screen.\n• Click and drag to inspect different areas of the room for hidden items.\n• Utilize the hint system by clicking on the hint button if needed (this deducts points or time).\n• Progress through levels by successfully finding all the hidden items within the time limit.":
                color "#000000"
                font "Inter-Regular.ttf"
                size 32

            imagebutton auto "images/Button/play_%s.png" action ShowMenu("dormicleaning"):
                xalign 0.5
                yalign 0.5


label dormicleaning:
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ hf_init( "bg room" , 5 ,
        ( "clock" , 425 , 380 , _( "Clock" )),
        ( "laptop" , 240 , 60 , _( "Laptop" )),
        ( "pillow" , 990 , 220 , _( "Pillow" )),
        ( "shoe" , 1100 , 890 , _( "Shoe" )),
        ( "backpack" , 200 , 760  , _( "Backpack" )),
         # OPTIONAL PARAMETERS:
        # enable cursor change when hovering
        mouse = True ,
         # enable inventory and remove found items from it
        inventory = False ,
         # disable hints
        hint = True ,
         # turn on item illumination when hovering
        hover = brightness( 0.05),
         # reduce the size of inventory cells so that they do not interfere with collecting items
        w = 200 ,
        h = 200
    )

    with fade
    $ hf_bg()
    with dissolve

    centered "{size=+24}You need to collect all the items in 7 seconds.\nLet's begin!"

    $ hf_start()

    $ renpy.pause(1, hard=True)

    if hf_return == 0:
        centered "{size=+24}Уay! All items have been collected!"
    else:
        centered "{size=+24}GAME OVER\nNo items left: [hf_return]."

    menu:
        "Try Again":
            jump dormicleaning

        "Exit":
            pass

    $ hf_hide()
    with dissolve

    if in_story:
        $ in_story = False
        jump chapter1_1
    else:
        call screen minigame()

init 1 :
    # define the game background, game time in seconds
    # and set the game parameters - sprites and position for collected items
    $ hf_init( "bg room" , 5 ,
        ( "clock" , 0 , 0 , _( "Clock" )),
        ( "laptop" , 111 , 560 , _( "Laptop" )),
        ( "pillow" , 700 , 615 , _( "Pillow" )),
        ( "shoe" , 1813 , 161 , _( "Shoe" )),
        ( "backpack" , 355 , 240 , _( "Backpack" )),
         # OPTIONAL PARAMETERS:
        # enable cursor change when hovering
        mouse = True ,
         # enable inventory and remove found items from it
        inventory = False ,
         # disable hints
        hint = False ,
         # turn on item illumination when hovering
        hover = brightness( 0.05),
         # reduce the size of inventory cells so that they do not interfere with collecting items
        w = 200 ,
        h = 200
    )

# then the game will be called:
    # $ hf_start()

    # the number of uncollected items will be in hf_return

    # transform to move the tooltip
    transform hf_hint_at():
        anchor( .5 , 1.25 )
        function hf_hint_at_f

    # style for the hint
    style hint_style is frame:
         # the yellow background is stretched to fit the text
        background Frame( "#fe9" , 0 , 0 )
         # padding from the edges to the text
        xpadding 20
        ypadding 15

    # style for hint text
    style hint_style_text is text:
        color "#014"
        outlines []

init -2 python:
    def images_auto(folders=["images"]):
        config.automatic_images_minimum_components = 1
        config.automatic_images = [' ', '_', '/']
        config.automatic_images_strip = folders

init python:
    # automatic declaration of sprites (including webp)
    images_auto()

    # cursors
    config . mouse = {
         "hand" : [( "images/c/hand1.png" , 2 , 10 ),
        ( "images/c/hand1.png" , 2 , 10 ), ( "images/c/hand1.png" , 2 , 10 ),
        ( "images/c/hand1.png" , 2 , 10 ), ( "images/c/hand2.png" , 2 , 10 ),
        ( "images/c/hand2.png" , 2 , 10 ), ( "images/c/hand3.png" , 2 , 10 ),
        ( "images/c/hand3.png" , 2 , 10 ), ( "images/c/hand2.png" , 2 , 10 ),
        ( "images/c/hand2.png" , 2 , 10 )],
        "finger" : [( "images/c/finger.png" , 2 , 10 )]}

    # mouse coordinates
    def  hf_hint_at_f (trans, st, at):
        trans . pos = renpy . get_mouse_pos()
        return  0

# SETTINGS
    # whether the cursor should change when hovering
    hf_mouse =  True

    # whether to display a hint
    hf_hint =  False

    # True - found items are added to inventory
    # False - found items disappear from inventory
    # None - inventory is not displayed
    hf_inventory =  None

    # transform for highlighting on hover
    # could be, for example, brightness(.05)
    hf_hover =  None

    # name of the folder with game sprites in the images directory plus a space
    hf_dir =  "minigame"

    # sizes of items in inventory
    hf_w, hf_h =  300 , 300

    # timebar sizes
    hf_t_w, hf_t_h =  1040 , 32

    # indentation of items from inventory edges
    hf_xpadding =  20
    hf_ypadding =  40

    # inventory window position
    hf_xalign =  0.5
    hf_yalign =  0.05

    # timebar position
    hf_t_xalign = 0.5
    hf_t_yalign = 0.01

# INTERNAL VARIABLES
    # time for which items need to be collected
    hf_time =  10

    # time to reset for animation
    hf_bar =  100

    # game mode (False - background mode)
    hf_game_mode =  False

    # items to find
    hf_needed = []

    # items that have already been found
    hf_picked = []

    # game background
    hf_back =  "black"

    # whether the timebar needs to be repainted (a quarter of the time remains)
    hf_warning =  False

    # number of uncollected items
    hf_return =  0

    # initial number of items
    hf_max_count =  0

    # game initialization
    def  hf_init (bg, time, * args, ** kwargs):
        global hf_needed, hf_picked, hf_back, hf_time, hf_bar, hf_max_count
        # reset lists and variables
        hf_needed = []
        hf_picked = []
        hf_back = bg
        hf_time = 7
        hf_bar =  100
        # add items to the list that need to be found
        for item, x, y, h in args:
            hf_needed . append((item, x, y, h))
        hf_max_count =  len (hf_needed)
         # apply optional game parameters
        # essentially change the values ​​of similar variables,
        # but they must start with hf_
        for k, v in kwargs . items():
            kk =  "hf_"  + k
            if kk in  globals () . keys():
                globals ()[kk] = kwargs . get(k)

    # show the game as a background on the master layer
    def  hf_bg ():
        store . hf_game_mode =  False
        show_s( "HiddenFolks" )

    # hide the game background
    # but first show if the game screen is hidden
    def  hf_hide ():
        hf_bg()
        renpy . with_statement( None )
        hide_s( "HiddenFolks" )

    # start the game
    # if some effect is specified, then first show the game with it
    def  hf_start (effect = None ):
        store . hf_game_mode =  False
        store . hf_warning =  False
        hf_bg()
        renpy . with_statement(effect)
        store . hf_game_mode =  True
        store . hf_return =  len (hf_needed)
        renpy . call_screen( "HiddenFolks" )
        hf_bg()

    # click on an item (move it to inventory or remove it from there)
    def  hf_click (item, x, y, h):
        store . hf_picked . append(store . hf_needed . pop(hf_needed . index((item, x, y, h))))
        splay( "click" )
        renpy . restart_interaction()
        # remains to build
        store . hf_return =  len (hf_needed)
    HFClick = renpy . curry(hf_click)

    # change the color of the timer
    # or start an animation of decreasing time
    def  hf_go (warning = False ):
        if warning:
            # change the color
            store . hf_warning =  True
        else :
            # start the animation
            store . hf_bar =  0
        renpy . restart_interaction()
    HFGo = renpy . curry(hf_go)

    # get a sprite for inventory
    def  hf_isprite (item):
         # if there is the desired item in the inventory folder,
        # then take it, otherwise - what is on the screen
        i = hf_dir +  " inventory "  + item
        if has_image(i):
            item = i
        # get the sprite size of the item
        w, h = get_size(item)
        # coefficients for zoom
        zoom =  1
        # if the item is larger than the cell, calculate a new zoom
        if w > hf_w or h > hf_h:
            # on the larger side
            if w > h :
                zoom = hf_w / w
            else :
                zoom = hf_h / h
        # return the sprite fit into the inventory cell size
        return Transform(item, zoom = zoom)

    # hint text
    hf_hint_text =  ""

    # change the hint text
    def  hf_set_hint (t = "" ):
        if hf_hint and hf_hint_text != t:
            store . hf_hint_text = t
            renpy . restart_interaction()
    SetHint = renpy . curry(hf_set_hint)

screen HiddenFolks():
    # game background
    add hf_back

    # all items on the screen
    for i, x, y, h in hf_needed:

        $ item = hf_dir +  " "  + i
        # button item
        imagebutton:
            style "empty"
            # item sprite
            idle item
            # position of the object (coordinates of its center)
            pos(x, y)
            # hover over a pixel
            focus_mask True
            # all actions only in game mode
            if hf_game_mode:

                # change the cursor if necessary
                if hf_mouse:
                    mouse "hand"

                # if hover selection is enabled
                if  not hf_hover is  None :
                     # if there is an image for the selected object, then display it
                    if has_image(item +  " hover" ):
                        hover item +  "hover"
                    # otherwise highlight with the transform specified in the settings
                    else :
                        hover At(item, hf_hover)

                # change the tooltip text on hover
                hovered SetHint(h)
                unhovered SetHint()

                # click processing
                action HFClick(i, x, y, h)

    # timer animation
    if hf_game_mode and hf_time >  0 :
        # activation of the timer
        timer 0.01 action HFGo()

        # timer for repainting the bar (one third of the total time)
        timer hf_time *  0.6666 action HFGo( True )

        # visualization of the timer as a bar
        bar:
            # position and size of the timebar
            align(hf_t_xalign, hf_t_yalign)
            xysize(hf_t_w, hf_t_h)
            value AnimatedValue(hf_bar, 100 , hf_time)

            # recolor and flicker the left bar bar,
            # when less than a third of the time is left
            if hf_warning:
                left_bar Frame(At( "gui/bar/left.png" , paint2( "#e02" , "#e028" , 0.2 )), gui . bar_borders, tile = gui . bar_tile)

        # loss by timer
        timer hf_time repeat True action SetHint(), SPlay( "gameover" ), Return("dormicleaning")

        # we've collected everything, let's leave (Return()() from def no longer works)
        if hf_return <  1 :
            timer 0.01 repeat True action SetHint(), SPlay( "gamewin" ), Return("dormicleaning")

        # inventory
        if  not hf_inventory is  None :
             # inventory frame
            frame:
                style "empty"
                xysize (hf_max_count * hf_w + hf_xpadding *  2 , hf_h + hf_ypadding *  2 )
                 # inventory position
                align(hf_xalign, hf_yalign)
                background Frame( "framei" , 48 , 48 )
                 # container for items
                hbox:
                    align( 0.5 , 0.5 )
                     # display collected items
                    if hf_inventory:
                         for item, x, y, h in hf_picked:
                             # xysize(hf_w, hf_h)
                            imagebutton idle hf_isprite(item) align( 0.5 , 0.5 ):
                                 # hover per pixel
                                focus_mask True
                                action NullAction()
                                if hf_game_mode:
                                     # change the cursor if necessary
                                    if hf_mouse:
                                        mouse "hand"
                                    # change the tooltip text when hovering the cursor
                                    hovered SetHint(h)
                                    unhovered SetHint()
                    # or display the items that remain to be collected
                    else :
                         for item, x, y, h in hf_needed:
                            imagebutton idle hf_isprite(item) align( 0.5 , 0.5 ):
                                 # pixel targeting
                                focus_mask True
                                action NullAction()
                                if hf_game_mode:
                                     # change the cursor if necessary
                                    if hf_mouse:
                                        mouse "hand"
                                    # change the tooltip text when hovering the cursor
                                    hovered SetHint(h)
                                    unhovered SetHint()

    # if necessary, display a hint
    if hf_hint and hf_hint_text:
        frame:
            style "hint_style"
            text hf_hint_text style "hint_style_text" align( 0.5 , 0.5 )
            at hf_hint_at()
