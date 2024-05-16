"""
todo:
    1. have a screen for the user to be able to choose a bg or difficulty
    2. add a choice to skip cleaning
    3. to fix the objects glitching, we can separate them in each screen call and hide it if it's clicked. no modal true
"""

screen dormicleaning_instructions:
    tag minigame
    modal True
    
    add "bg roomnight"

    imagebutton auto "images/Button/exit_%s.png" action ShowMenu("minigame") keysym ['K_ESCAPE']:
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

#screen choose_difficulty:

label init_dormicleaning:
    show screen dormicleaning with None
    call screen init_dc with dissolve

    screen init_dc:
        add "halfblack"

        #button for exit
        button:
            xysize(0, 0)
            action [Hide("init_dc"), Hide("dormicleaning"), Show(mn_caller_screen, transition=dissolve)] keysym ['K_ESCAPE']

        button:
            xysize(1920,1080)
            action [Hide("init_dc"), SetVariable("dc_start", True)] keysym ["K_SPACE"]

            vbox:
                align (0.5, 0.5)
                spacing 5
                text "You need to collect all the items in" style "game_instruction"
                text "7 seconds. Let's begin!" style "game_instruction"

screen dormicleaning:
    tag minigame
    add "bg room"

    #button for exit
    button:
        xysize(0, 0)
        action [Hide("init_dc"), Hide("dormicleaning"), Show(mn_caller_screen, transition=dissolve)] keysym ['K_ESCAPE']

    for item, x, y in vars_needed:
        imagebutton:
            idle f"minigame/{item}.png"
            #hover At(f"minigame/{item}.png", hovered)
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
                action [Hide("dormicleaning"), Hide("dc_result"), InitDC(5), Show(mn_caller_screen, transition=dissolve)] keysym ["K_SPACE"]

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
                $ init_dc_vars(5)
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
                $ init_dc_vars(5)
                jump init_dormicleaning
            "Exit":
                hide screen dim
                with dissolve
                $ init_dc_vars(5)
                $ renpy.call_screen("%s"%(mn_caller_screen))
    
    screen dim:
        add "bg room"
        add "halfblack"

init -2 python:
    global coordinates, objects, domains, constraints, locations

    coordinates = [[[1046, 252], [1045, 291], [1021, 351], [1046, 325], [1072, 423], [1023, 399], [1046, 272], [1075, 414], [1074, 374], [1091, 392], [1126, 310]], [[1311, 346], [1331, 384], [1384, 457], [1384, 432], [1414, 493], [1382, 486], [1343, 346], [1411, 504], [1416, 470], [1442, 499], [1496, 506]],
                    [[1602, 432], [1639, 429], [1705, 607], [1635, 435], [1635, 477], [1649, 454], [1674, 540], [1656, 551], [1658, 566]], #bed
                    [[828, 680], [806, 710], [803, 743], [831, 713], [848, 780], [811, 771], [846, 673], [873, 804], [874, 793], [845, 745]], #floor
                    [[390, 85], [389, 70], [379, 129], [373, 166], [386, 153], [416, 232], [396, 225], [411, 242], [414, 242], [382, 190], [418, 242]], [[416, 398], [427, 414], [438, 392], [441, 414]], [[541, 367], [555, 378], [571, 370], [585, 365]],  #desk
                    [[479, 498], [482, 516], [527, 587], [520, 585], [520, 607], [528, 587], [479, 569], [524, 581]]] #chair

    locations = {"bed" : [[1046, 252], [1045, 291], [1021, 351], [1046, 325], [1311, 346], [1331, 384], [1384, 457], [1384, 432], [1072, 423], [1414, 493], [1023, 399], [1382, 486], [1046, 272], [1343, 346], [1075, 414], [1411, 504], [1074, 374], [1416, 470], [1091, 392], [1442, 499], 
                        [1602, 432], [1639, 429], [1126, 310], [1496, 506], [1705, 607], [1635, 435], [1635, 477], [1649, 454], [1674, 540], [1656, 551], [1658, 566]],
                "floor" : [[828, 680], [806, 710], [803, 743], [831, 713], [848, 780], [811, 771], [846, 673], [873, 804], [874, 793], [845, 745]],
                "desk" : [[390, 85], [389, 70], [379, 129], [373, 166], [386, 153], [416, 232], [396, 225], [411, 242], [414, 242], [382, 190], [416, 398], [427, 414], [438, 392], [541, 367], [555, 378], [571, 370], [418, 242], [441, 414], [585, 365]],
                "chair" : [[479, 498], [482, 516], [527, 587], [520, 585], [520, 607], [528, 587], [479, 569], [524, 581]]}

    objects = ["pillow", "rice cooker", "laptop", "fan", "cap", "shoe", "bag", "clock", "psp", "phone", "mug", "pen"]

    domains = {"pillow" : [[1046, 252], [1311, 346], [828, 680], [389, 70], [1602, 432]],
                "rice cooker" : [[1045, 291], [1331, 384], [806, 710], [379, 129], [1635, 435]],
                "laptop" : [[1021, 351], [1384, 457], [803, 743], [373, 166], [482, 516], [1635, 477]],
                "fan" : [[1046, 325], [1384, 432], [831, 713], [386, 153], [479, 498], [1649, 454]],
                "cap" : [[1072, 423], [1414, 493], [848, 780], [416, 232], [416, 398], [541, 367], [528, 587], [1674, 540]],
                "shoe" : [[1023, 399], [1382, 486], [811, 771], [396, 225], [479, 569], [1656, 551]],
                "bag" : [[1046, 272], [1343, 346], [846, 673], [390, 85], [1639, 429]],
                "clock" : [[1075, 414], [1411, 504], [873, 804], [411, 242], [427, 414], [555, 378], [520, 585], [1658, 566]],
                "psp" : [[1075, 414], [1411, 504], [873, 804], [411, 242], [427, 414], [555, 378], [520, 585], [1658, 566]], #clock and psp have the same coordinates
                "phone" : [[1074, 374], [1416, 470], [382, 190]],
                "mug" : [[1091, 392], [1442, 499], [874, 793], [414, 242], [438, 392], [571, 370], [524, 581]],
                "pen" : [[1126, 310], [1496, 506], [1705, 607], [845, 745], [520, 607], [418, 242], [441, 414], [585, 365]]
                }

    constraints = [lambda i, value, list: value in list[i], 
                    {"bed" : lambda max, max_assigned: max_assigned["bed"] < max * 0.4, 
                    "floor" : lambda max, max_assigned: max_assigned["floor"] < max * 0.28,
                    "desk" : lambda max, max_assigned: max_assigned["desk"] < max * 0.17,
                    "chair" : lambda max, max_assigned: max_assigned["chair"] < max * 0.15
                    }]

    class CSP: 
        def __init__(self, variables, domains, constraints, m): 
            self.variables = variables
            self.domains = domains 
            self.constraints = constraints 
            self.assigned = []
            self.max_assigned = {"bed" : 0,
                                "floor" : 0,
                                "desk" : 0,
                                "chair" : 0}
            self.max = m
            self.solution = None

        def solve(self): 
            assignment = {} 
            self.solution = self.backtrack(assignment) 
            return self.solution 

        def backtrack(self, assignment): 
            if len(assignment) == len(self.variables): 
                return assignment 
            
            var = self.select_unassigned_variable(assignment)
            
            for value in self.order_domain_values(var): 
                if self.is_consistent(value): 
                    assignment[var] = value 
                    result = self.backtrack(assignment) 
                    if result is not None: 
                        return result 
                    del assignment[var] 
            return None

        def select_unassigned_variable(self, assignment): 
            unassigned_vars = [var for var in self.variables if var not in assignment] 
            return min(unassigned_vars, key=lambda var: len(self.domains[var])) 

        def order_domain_values(self, var): 
            renpy.random.shuffle(self.domains[var]) 
            return self.domains[var]
        
        def is_consistent(self, value): 
            for i in range(len(self.assigned)):
                if self.constraints[0](i, value, self.assigned):
                    return False
                
            for loc in locations:
                if value in locations[loc]:
                    if self.constraints[1][loc](self.max, self.max_assigned):
                        self.max_assigned[loc] += 1
                    else:
                        return False

            #add it to the assigned when consistent
            for x in coordinates:
                if value in x:
                    self.assigned.append(x)

            return True

init python:
    dc_xpadding =  20
    dc_ypadding =  40

    def init_dc_vars(m):
        global vars_needed, max_count, dc_start, dc_time, dc_bar, dc_warning

        dc_start = False
        dc_warning = False
        dc_time = 7
        dc_bar =  100
        vars_needed = []
        objs, coord = get_coordinates(m)
        X = []
        Y = []

        for obj in objs:
            X.append(coord[obj][0])
            Y.append(coord[obj][1])

        for obj, x, y in zip(objs, X, Y):
            vars_needed.append((obj, x, y))

        max_count =  len(vars_needed)
    InitDC = renpy.curry(init_dc_vars)
        
    def get_objects(m):
        renpy.random.shuffle(objects)
        return objects[:m]

    def get_coordinates(m): 
        while True:
            renpy.random.shuffle(objects)
            variables = objects[:m]
            csp = CSP(variables, domains, constraints, m)
            solution = csp.solve() 
            if solution != None:
                break
        
        return variables, solution

    def dc_click(item, x, y):
        vars_needed.pop(vars_needed.index((item, x, y)))
        #store . hf_picked . append()
        splay("click")
        renpy.restart_interaction()

    DCClick = renpy.curry(dc_click)
