"""
todo:
    1.  have a screen for the user to be able to choose a bg or difficulty
    2. add a choice to skip cleaning
"""

screen dormicleaning_instructions:
    tag menu
    modal True
    add "bg roomnight"

    imagebutton auto "images/Button/exit_%s.png" action ShowMenu("minigame"):
        align (0.97, 0.06)
        activate_sound "audio/click.ogg"

    frame:
        xpadding 40
        ypadding 50
        align (0.5, 0.60)
        background "#D9D9D9"

        vbox:
            spacing 25

            text "Dormicleaning":
                style "minigame_title_font"
                color "#000000"
                align (0.5, 0.5)

            text "Objective: Find lost items in a dormitory room within a limited time.":
                color "#000000"
                font "Inter-Bold.ttf"
                size 40

            text "Gameplay:\n• Use your mouse to explore the dormitory room.\n• Click on the objects you believe match the descriptions provided at the bottom of the screen.\n• Click and drag to inspect different areas of the room for hidden items.\n• Utilize the hint system by clicking on the hint button if needed (this deducts points or time).\n• Progress through levels by successfully finding all the hidden items within the time limit.":
                color "#000000"
                font "Inter-Regular.ttf"
                size 32

            imagebutton auto "images/Button/play_%s.png" action SaveMNCallerScreen("dormicleaning_instructions"), Jump("init_dormicleaning"):
                align (0.5, 0.5)
                activate_sound "audio/click.ogg"

label init_dormicleaning:
    show screen dormicleaning with None
    call screen init_dc with dissolve

    screen init_dc:
        add "halfblack"

        button:
            xysize(1920,1080)
            action [Hide("init_dc"), SetVariable("dc_start", True)] keysym ["K_SPACE"]

            vbox:
                align (0.5, 0.5)
                spacing 5
                text "You need to collect all the items in" style "game_instruction"
                text "7 seconds. Let's begin!" style "game_instruction"

screen dormicleaning:
    add "bg room"

    for item, x, y in vars_needed:
        imagebutton:
            idle f"minigame/{item}.png"
            hover At(f"minigame/{item}.png", hovered)
            xpos x ypos y 
            focus_mask True
            mouse "hand"
            tooltip item
            action DCClick(item, x, y)
    
    if dc_start:
        # inventory frame
        frame:
            xysize (max_count * 150 + dc_xpadding *  2 + max_count * 10, 150 + dc_ypadding *  2 )
            # inventory position
            align (0.5, 0.06)
            background Frame(At("gui/frame.png", half_transparent) , 48 , 48 )

            hbox:
                align(0.1, 0.5)
                spacing 10
                # display collected items
                for item, x, y in vars_needed:
                    imagebutton:
                        idle f"minigame/inventory/{item}.png"
                        hover At(f"minigame/inventory/{item}.png", hovered)
                        focus_mask True
                        align (0.5, 0.5)
                        tooltip item
                        action NullAction()
                            
    # timer animation
    if dc_start and dc_time >  0 :

        timer dc_time *  0.6666 action SetVariable("dc_warning", True)

        # visualization of the timer as a bar
        bar:
            value AnimatedValue(old_value=1.0, value=0.0, range=1.0, delay=dc_time)

            # recolor and flicker the left bar bar,
            # when less than a third of the time is left
            if dc_warning:
                left_bar Frame(At("gui/bar/left.png" , paint2( "#e02" , "#e028" , 0.2 )), gui . bar_borders, tile = gui . bar_tile)

        # loss by timer
        timer dc_time repeat True action SetVariable("dc_start", False), SPlay("gameover"), Show("dc_result", transition=dissolve)

        # we've collected everything, let's leave (Return()() from def no longer works)
        if len(vars_needed) <  1 :
            timer 0.01 repeat True action SetVariable("dc_start", False), SPlay("gamewin"), Show("dc_result", transition=dissolve)

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip:
                    size 20

transform half_transparent:
    matrixcolor OpacityMatrix(0.5)

screen dc_result:
    modal True
    add "halfblack"
    
    $ uncollected = len(vars_needed)

    if uncollected <  1 :
        text "Yay! All items have been collected!" style "game_instruction"

        button:
            xysize(1920,1080)
            
            if in_story: 
                action [SetVariable("in_story", False), Hide("dormicleaning"), Hide("dc_result"), Jump("chapter1_1")] keysym ["K_SPACE"]
            else:
                action [Hide("dormicleaning"), Hide("dc_result"), Show(mn_caller_screen, transition=dissolve)] keysym ["K_SPACE"]

    else:
        vbox:
            align (0.5, 0.5)
            spacing 5
            text "GAME OVER" style "game_instruction"
            text "\nNo items left: [uncollected]." style "game_instruction"

        button:
            xysize(1920,1080)
            action [Hide("dc_result"), Jump("dc_retry")] keysym ["K_SPACE"]

label dc_retry:
    show screen dim with None
    hide screen dormicleaning with dissolve

    if in_story:
        menu:
            "Try Again":
                $ points += 1
                hide screen dim
                $ init_dc_vars()
                jump init_dormicleaning
            "Skip Cleaning":
                $ points -= 1
                hide screen dim
                show mc sleepy_casual with dissolve
                mc "I guess I’ll just go for a little campus tour first."
                hide mc
                jump chapter1_1
    else:
        menu:
            "Try Again":
                hide screen dim
                $ init_dc_vars()
                jump init_dormicleaning
            "Exit":
                hide screen dim
                with dissolve
                $ renpy.call_screen("%s"%(mn_caller_screen))
    
    screen dim:
        add "bg room"
        add "halfblack"

init -2 python:
    global coordinates, objects, domains, constraints, object_loc, object_coord

    object_coord = []
    object_loc = []

    coordinates = {
            "bed": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722]],
            "top_desk": [[375, 169]],
            "bottom_desk": [[428, 398], [545, 370]],
            "floor": [[159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970]],
            "chair": [[517, 597], [626, 633]]
            }

    objects = ["bag", "cap", "fan",  "clock", "laptop", "pillow", "shoe", "mug", "pen", "phone", "psp", "rice cooker"]

    domains = {
        "bag": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], #top desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970] #floor
                ], #everywhere except the chair and bottom desk
        "cap": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy
        "fan": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], #top desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597] #chair 
                ], #everywhere except bottom desk, allowed in one of the chair coordinates - 517, 597
        "clock": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy
        "laptop": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], #top desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597] #chair 
                ], #everywhere except bottom desk, allowed in one of the chair coordinates - 517, 597
        "pillow": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], #top desk
                [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [428, 398]], #bed floor upper desk, not allowed on = 159, 883
        "shoe": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy
        "mug": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy
        "pen": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy except only allowed in one coordinate on headboard - 829, 128
        "phone": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy except only allowed in one coordinate on headboard - 829, 128
        "psp": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], [626, 633] #chair
                ], #lucy
        "rice cooker": [[1046, 252], [1451, 436], [1565, 371], [1746, 418], [1271, 424], [1521, 535], [1721, 626], [973, 435], [1111, 528], [1335, 626], [1583, 722], #bed
                [375, 169], [428, 398], [545, 370], #top & bottom desk
                [159, 883], [354, 313], [512, 887], [733, 948], [845, 745], [789, 791], [960, 845], [834, 970], [984, 932], [1159, 970], #floor
                [517, 597], #chair
                ] #everywhere except bottom desk, allowed in one of the chair coordinates - 517, 597
    }
    
    #lambda x, y: x != y
    constraints = {
        "bag": lambda x: x not in (coordinates["chair"] or coordinates["bottom_desk"]), #everywhere except the chair and bottom desk
        "fan": lambda x: x not in coordinates["bottom_desk"] and x != [626, 633], #everywhere except bottom desk, allowed in one of the chair coordinates - 517, 597
        "laptop": lambda x: x not in coordinates["bottom_desk"] and x != [626, 633], #everywhere except bottom desk, allowed in one of the chair coordinates - 517, 597
        "pillow": lambda x: x in coordinates["bed"] + coordinates["floor"] + coordinates["top_desk"] and x != [159, 883] , #bed floor upper desk, not allowed on = 159, 883
        "pen": lambda x: x not in [[700, 149], [926, 108]], #lucy except only allowed in one coordinate on headboard - 829, 128
        "phone": lambda x: x not in [[700, 149], [926, 108]], #lucy except only allowed in one coordinate on headboard - 829, 128
        "rice cooker": lambda x: x not in coordinates["bottom_desk"] and x != [626, 633],  #everywhere except bottom desk, allowed in one of the chair coordinates - 517, 597
        "only_one": lambda x: x not in coordinates["top_desk"] if object_loc["pillow"] == "top_desk" else True
        }
    
    class CSP: 
        def __init__(self, variables, Domains,constraints): 
            self.variables = variables 
            self.domains = Domains 
            self.constraints = constraints 
            self.solution = None

        def solve(self): 
            assignment = {} 
            self.solution = self.backtrack(assignment) 
            return self.solution 

        def backtrack(self, assignment): 
            if len(assignment) == len(self.variables): 
                return assignment 
            
            var = self.select_unassigned_variable(assignment)
            
            for value in self.order_domain_values(var, assignment): 
                if self.is_consistent(var, value, assignment): 
                    object_coord.append(value)
                    self.save_loc(value)
                    assignment[var] = value 
                    result = self.backtrack(assignment) 
                    if result is not None: 
                        return result 
                    del assignment[var] 
            return None

        def select_unassigned_variable(self, assignment): 
            unassigned_vars = [var for var in self.variables if var not in assignment] 
            return min(unassigned_vars, key=lambda var: len(self.domains[var])) 

        def order_domain_values(self, var, assignment): 
            return self.domains[var] 
        
        #check if all in constraint(that_object) is all true? or just the variable
        def is_consistent(self, var, value, assignment): 
            if var in self.constraints and not self.constraints[var](value):
                return False
            elif value in object_coord: 
                return False
            elif self.check_loc(value) in object_loc:
                return False
            return True

        #check the location on the coordinate
        def check_loc(self, value):
            for key, points in coordinates.items():
                if value in points:
                    return key
            return None
        
        def save_loc(self, value):
            key = self.check_loc(value)
            if key not in object_loc:
                object_loc.append(key)

init python:
    dc_xpadding =  20
    dc_ypadding =  40

    def init_dc_vars():
        global vars_needed, max_count, dc_start, dc_time, dc_bar, dc_warning

        dc_start = False
        dc_warning = False
        dc_time = 7
        dc_bar =  100
        vars_needed = []
        objs = get_objects(5)
        coord = get_coordinates(objs)
        X = []
        Y = []

        for obj in objs:
            X.append(coord[obj][0])
            Y.append(coord[obj][1])

        for obj, x, y in zip(objs, X, Y):
            vars_needed.append((obj, x, y))

        max_count =  len(vars_needed)
        
    def get_objects(max):
        renpy.random.shuffle(objects)
        return objects[:max]

    def get_coordinates(variables):
        global object_coord, object_loc

        for key in domains:
            renpy.random.shuffle(domains[key])

        csp = CSP(variables, domains, constraints) 

        object_coord = []
        object_loc = []

        return csp.solve() 

    def dc_click(item, x, y):
        vars_needed.pop(vars_needed.index((item, x, y)))
        #store . hf_picked . append()
        splay("click")
        renpy.restart_interaction()

    DCClick = renpy.curry(dc_click)
