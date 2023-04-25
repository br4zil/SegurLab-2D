# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init:
    $ import random
    
init python:

    def find_question(name, list_of_objects):
        for object in list_of_objects:
            name_of_object, question = object
            if name_of_object == name:
                result = question
                
        return result
        
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

style checkbox_button:
    xysize (50, 50)
    background Solid("#ff0000") # Unchecked FF0000
    hover_background Solid("#ffff00") # Unchecked Hovered (I usually increase brightness of the image by 15% unsing im. matrix manipulators)
    insensitive_background Solid("#d3d3d3") # Disabled (May not be required, I usually use im.Sepia() for images)
    selected_idle_background Solid("#00ff00") # Checked
    selected_hover_background Solid("#00ff11") # Checked Hovered

screen countdown_no_bar:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve # This is the timer bar.

default timeout = 90.0
default timeout_label = None
default persistent.timed_choices = True
default disable_button = False

define answer = "NONE"
define end_result_screen = "NONE"

screen tutorial:
    imagemap:
       ground "tutorial.png" xalign 0.5 yalign 0.5
       hotspot ((58, 62, 1804, 949)) action Jump("questions_loop")
screen Azul01:
    imagemap:
       ground "Azul01.png" xalign 0.5 yalign 0.5
       imagebutton:
            idle "check3_idle.png"
            if disable_button == False:
                hover "box4.png"
            selected_idle "box4.png"
            selected_hover "box4.png"
            focus_mask None
            xpos 600
            ypos 550
            action SetVariable("answer","A"), Return()
       imagebutton:
            idle "check3_idle.png"
            if disable_button == False:
                hover "box4.png"
            selected_hover "box4.png"
            selected_idle "box4.png"
            focus_mask None
            xpos 600
            ypos 760
            action SetVariable("answer","B"),Return() 
       imagebutton:
            idle "check3_idle.png"
            if disable_button == False:
                hover "box4.png"
            selected_idle "box4.png"    
            selected_hover "box4.png"
            focus_mask None
            xpos 1020
            ypos 550
            action SetVariable("answer","C"),Return() 
       imagebutton:
            idle "check3_idle.png"
            if disable_button == False:
                hover "box4.png"
            selected_hover "box4.png"
            selected_idle "box4.png"
            focus_mask None
            xpos 1020
            ypos 760
            action SetVariable("answer","D"),Return()      

    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
       
screen Azul02:
    imagemap:
       ground "Azul02.png" xalign 0.5 yalign 0.5
       hotspot (1088, 606, 422, 59) action SetVariable("answer","A"), Return()
       hotspot (1097, 693, 412, 39) action SetVariable("answer","B"), Return()
       hotspot (1094, 764, 414, 48) action SetVariable("answer","C"), Return()
       hotspot (1094, 838, 422, 43) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle "check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()         
    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
       
screen Azul03:
    imagemap:
       ground "Azul03.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
            hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Azul04:
    imagemap:
       ground "Azul04.png" xalign 0.5 yalign 0.5
       hotspot (1088, 606, 422, 59) action SetVariable("answer","A"), Return()
       hotspot (1097, 693, 412, 39) action SetVariable("answer","B"), Return()
       hotspot (1094, 764, 414, 48) action SetVariable("answer","C"), Return()
       hotspot (1094, 838, 422, 43) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()         
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Azul05:
    imagemap:
       ground "Azul05.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Azul06:
    imagemap:
       ground "Azul06.png" xalign 0.5 yalign 0.5
       hotspot (1088, 606, 422, 59) action SetVariable("answer","A"), Return()
       hotspot (1097, 693, 412, 39) action SetVariable("answer","B"), Return()
       hotspot (1094, 764, 414, 48) action SetVariable("answer","C"), Return()
       hotspot (1094, 838, 422, 43) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()         
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Azul07:
    imagemap:
       ground "Azul07.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Azul08:
    imagemap:
       ground "Azul08.png" xalign 0.5 yalign 0.5
       hotspot (1088, 606, 422, 59) action SetVariable("answer","A"), Return()
       hotspot (1097, 693, 412, 39) action SetVariable("answer","B"), Return()
       hotspot (1094, 764, 414, 48) action SetVariable("answer","C"), Return()
       hotspot (1094, 838, 422, 43) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()         
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Azul09:
    imagemap:
       ground "Azul09.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Azul10:
    imagemap:
       ground "Azul10.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
#VERMELHOS
       
screen Red01:
    imagemap:
       ground "Red01.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Red02:
    imagemap:
       ground "Red02.png" xalign 0.5 yalign 0.5
       hotspot (878, 622, 415, 36) action SetVariable("answer","A"), Return()
       hotspot (882, 694, 510, 38) action SetVariable("answer","B"), Return()
       hotspot (885, 768, 883, 34) action SetVariable("answer","C"), Return()
       hotspot (882, 842, 675, 32) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()                
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Red03:
    imagemap:
       ground "Red03.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Red04:
    imagemap:
       ground "Red04.png" xalign 0.5 yalign 0.5
       hotspot (1004, 623, 550, 35) action SetVariable("answer","A"), Return()
       hotspot (1012, 698, 333, 31) action SetVariable("answer","B"), Return()
       hotspot (1010, 766, 483, 38) action SetVariable("answer","C"), Return()
       hotspot (1010, 841, 399, 32) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()                
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Red05:
    imagemap:
       ground "Red05.png" xalign 0.5 yalign 0.5
       hotspot (1133, 621, 127, 37) action SetVariable("answer","A"), Return()
       hotspot (1134, 693, 151, 41) action SetVariable("answer","B"), Return()
       hotspot (1138, 768, 175, 37) action SetVariable("answer","C"), Return()
       hotspot (1136, 842, 162, 40) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 820
        action SetVariable("answer","D"),Return()             
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Red06:
    imagemap:
       ground "Red06.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Red07:
    imagemap:
       ground "Red07.png" xalign 0.5 yalign 0.5
       hotspot (1125, 626, 136, 35) action SetVariable("answer","A"), Return()
       hotspot (1121, 698, 200, 38) action SetVariable("answer","B"), Return()
       hotspot (1124, 764, 158, 46) action SetVariable("answer","C"), Return()
       hotspot (1125, 836, 89, 45) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 820
        action SetVariable("answer","D"),Return()   
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Red08:
    imagemap:
       ground "Red08.png" xalign 0.5 yalign 0.5
       hotspot (1157, 622, 137, 36) action SetVariable("answer","A"), Return()
       hotspot (1162, 694, 132, 34) action SetVariable("answer","B"), Return()
       hotspot (1162, 768, 134, 33) action SetVariable("answer","C"), Return()
       hotspot (1162, 844, 131, 30) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 820
        action SetVariable("answer","D"),Return()       
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Red09:
    imagemap:
       ground "Red09.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    

    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Red10:
    imagemap:
       ground "Red10.png" xalign 0.5 yalign 0.5
       hotspot (884, 625, 402, 37) action SetVariable("answer","A"), Return()
       hotspot (884, 692, 493, 41) action SetVariable("answer","B"), Return()
       hotspot (885, 770, 543, 35) action SetVariable("answer","C"), Return()
       hotspot (881, 840, 709, 34) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "check2"
        selected_hover "check2"
        selected_idle"check2"
        focus_mask None
        xpos 850
        ypos 820
        action SetVariable("answer","D"),Return()         
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()           
# VERDES!

screen Verde01:
    imagemap:
       ground "Verde01.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Verde02:
    imagemap:
       ground "Verde02.png" xalign 0.5 yalign 0.5
       hotspot (1080, 626, 265, 42) action SetVariable("answer","A"), Return()
       hotspot (1081, 702, 144, 34) action SetVariable("answer","B"), Return()
       hotspot (1080, 772, 184, 38) action SetVariable("answer","C"), Return()
       hotspot (1081, 846, 216, 34) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 820
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Verde03:
    imagemap:
       ground "Verde03.png" xalign 0.5 yalign 0.5
       hotspot (625, 564, 259, 174) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Verde04:
    imagemap:
       ground "Verde04.png" xalign 0.5 yalign 0.5
       hotspot (1081, 629, 261, 36) action SetVariable("answer","A"), Return()
       hotspot (1085, 702, 140, 34) action SetVariable("answer","B"), Return()
       hotspot (1084, 776, 180, 33) action SetVariable("answer","C"), Return()
       hotspot (1082, 849, 216, 33) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 820
        action SetVariable("answer","D"),Return()     
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
screen Verde05:
    imagemap:
       ground "Verde05.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Verde06:
    imagemap:
       ground "Verde06.png" xalign 0.5 yalign 0.5
       hotspot (1081, 630, 137, 34) action SetVariable("answer","A"), Return()
       hotspot (1084, 701, 144, 35) action SetVariable("answer","B"), Return()
       hotspot (1082, 772, 140, 40) action SetVariable("answer","C"), Return()
       hotspot (1081, 845, 141, 43) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 600
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 675
        action SetVariable("answer","B"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 750
        action SetVariable("answer","C"),Return()
    imagebutton:
        idle "check_idle.png"
        if disable_button == False:
           hover "box5.png"
        selected_hover "box5.png"
        selected_idle "box5.png"
        focus_mask None
        xpos 1050
        ypos 820
        action SetVariable("answer","D"),Return() 
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
##ROXOS###

screen Roxo01:
    imagemap:
       ground "Roxo01.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()       
screen Roxo02:
    imagemap:
       ground "Roxo02.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()           
screen Roxo03:
    imagemap:
       ground "Roxo03.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()           
screen Roxo04:
    imagemap:
       ground "Roxo04.png" xalign 0.5 yalign 0.5
       hotspot (630, 569, 254, 169) action SetVariable("answer","A"), Return()
       hotspot (630, 781, 252, 172) action SetVariable("answer","B"), Return()
       hotspot (1049, 564, 261, 177) action SetVariable("answer","C"), Return()
       hotspot (1050, 782, 254, 168) action SetVariable("answer","D"), Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 550
        action SetVariable("answer","A"),Return()
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 600
        ypos 760
        action SetVariable("answer","B"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 550
        action SetVariable("answer","C"),Return() 
    imagebutton:
        idle "check3_idle.png"
        if disable_button == False:
           hover "box4.png"
        selected_idle "box4.png"
        selected_hover "box4.png"
        focus_mask None
        xpos 1020
        ypos 760
        action SetVariable("answer","D"),Return()    
    if persistent.timed_choices:

        bar:
            xalign 0.5
            xpos 1550
            ypos 930
            xsize 400
            value AnimatedValue(old_value=0.0, value=1.0, range=1.0, delay=timeout)

        timer timeout action SetVariable("answer","timeout"), Return()
       
define v = Character("Vegeta")
show layer card_layer:
    xalign 2.5 yalign 0.5 rotate 180

init:
    $ timer_range = 0
    $ timer_jump = 0




# The game starts here.

label pause:
    $ renpy.pause ()
    jump pause

label splashscreen:
    scene black
    with Pause(1)

    show apre with dissolve
    with Pause(20)

    hide apre with dissolve
    with Pause(1)
    
    show titleb3 with dissolve:
        xalign 0.5 yalign 0.5
    with Pause(10)
    hide titleb3 with dissolve

    return

label start:
#resize da UI:
    image check2:
        "check2.png"
    image checkbox:
        "box.png"
        zoom 0.05
    image vcheckbox:
        "vbox.png"
        zoom 0.05
    
    $ answered = 0
    $ renpy.block_rollback()
    $ easy_list = ["Azul01","Azul02", "Azul03","Verde01", "Verde02", "Roxo01", "Red01", "Red02", "Red03"]
    $ medium_list = ["Azul04","Azul05","Azul06","Verde03","Verde04", "Roxo02","Red04","Red05","Red06"]
    $ hard_list = ["Roxo03","Roxo04","Verde05","Verde06","Red07","Red08","Red09","Red10","Azul07","Azul08","Azul09","Azul10"]
    $ all_list =["Roxo01", "Roxo02", "Roxo03","Roxo04","Verde01", "Verde02", "Verde03","Verde04","Verde05","Verde06","Red01", "Red02", "Red03","Red04","Red05","Red06","Red07","Red08","Red09","Red10", "Azul01", "Azul02", "Azul03","Azul04","Azul05","Azul06","Azul07","Azul08","Azul09","Azul10"]
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    $ score = 0
    $ nrquestoes = 0
    $ totalquestions = len(easy_list) + len(medium_list) + len(hard_list)
    scene chemp
    #show z2
    #jump pause
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show screen tutorial
    jump pause
label questions_loop:
    $ answer = "NONE"
    $ disable_button = False
    hide screen tutorial
    if not easy_list == []:
        $ random_jump_target = random.choice(easy_list)
        $ easy_list.remove(random_jump_target)
        $ renpy.call(random_jump_target)
    elif not medium_list == []:
        $ random_jump_target = random.choice(medium_list)
        $ medium_list.remove(random_jump_target)
        $ renpy.call(random_jump_target)
    elif not hard_list == []:
        $ random_jump_target = random.choice(hard_list)
        $ hard_list.remove(random_jump_target)
        $ renpy.call(random_jump_target)
    "Você acertou [nrquestoes] de [totalquestions] questões e seu score final é [score]. Clique para continuar."
    "Fim da Demonstração!"
    $ MainMenu(confirm=False)()
#########CARTÕES#############


#AZUL 01#
label Azul01:
    call screen Azul01 with dissolve
    show screen Azul01
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 
 
    else:
        "Errada! Clique para continuar."
    hide screen Azul01 with dissolve
    jump questions_loop
    
#AZUL 02#
label Azul02:
    call screen Azul02 with dissolve
    show screen Azul02
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "B":
        $ score = score + 10
        $ nrquestoes = nrquestoes + 1 
        "Correta! Seu score atual é : [score]. Clique para continuar."

    else:
        "Errada! Clique para continuar."
    hide screen Azul02 with dissolve
    jump questions_loop

    
#AZUL 03#

label Azul03:
    call screen Azul03 with dissolve
    show screen Azul03
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul03 with dissolve
    jump questions_loop

#AZUL 04#
label Azul04:
    call screen Azul04 with dissolve
    show screen Azul04
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul04 with dissolve
    jump questions_loop
    
#AZUL 05#

label Azul05:
    call screen Azul05 with dissolve
    show screen Azul05
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "A":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul05 with dissolve
    jump questions_loop
    
#AZUL 06#

label Azul06:
    call screen Azul06 with dissolve
    show screen Azul06
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "C":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul06 with dissolve
    jump questions_loop

#AZUL 07
label Azul07:
    call screen Azul07 with dissolve
    show screen Azul07
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "A":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul07 with dissolve
    jump questions_loop

#AZUL 08

label Azul08:
    call screen Azul08 with dissolve
    show screen Azul08
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul08 with dissolve
    jump questions_loop

    
#AZUL 09#

label Azul09:
    call screen Azul09 with dissolve
    show screen Azul09
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "C":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul09 with dissolve
    jump questions_loop

#AZUL 10#

label Azul10:
    call screen Azul10 with dissolve
    show screen Azul10
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "C":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Azul10 with dissolve
    jump questions_loop

    
#Red 01#
label Red01:
    call screen Red01 with dissolve
    show screen Red01
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red01 with dissolve
    jump questions_loop

    
#Red 02#
label Red02:
    call screen Red02 with dissolve
    show screen Red02
    
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"    
    if answer == "C":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 
    else:
        "Errada! Clique para continuar."
    hide screen Red02 with dissolve
    jump questions_loop

    
#Red 03#

label Red03:
    call screen Red03 with dissolve
    show screen Red03
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red03 with dissolve
    jump questions_loop


#Red 04#
label Red04:
    call screen Red04 with dissolve
    show screen Red04
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red04 with dissolve
    jump questions_loop

    
#Red 05#

label Red05:
    call screen Red05 with dissolve
    show screen Red05
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red05 with dissolve
    jump questions_loop

    
#Red 06#

label Red06:
    call screen Red06 with dissolve
    show screen Red06
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red06 with dissolve
    jump questions_loop


#Red 07
label Red07:
    call screen Red07 with dissolve
    show screen Red07
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "A":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red07 with dissolve
    jump questions_loop

    
#Red 08

label Red08:
    call screen Red08 with dissolve
    show screen Red08
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red08 with dissolve
    jump questions_loop
    
#Red 09#

label Red09:
    call screen Red09 with dissolve
    show screen Red09
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red09 with dissolve
    jump questions_loop

#Red 10#

label Red10:
    call screen Red10 with dissolve
    show screen Red10
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Red10 with dissolve
    jump questions_loop
    
#VERDES

#Verde 01
label Verde01:
    call screen Verde01 with dissolve
    show screen Verde01
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "A":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Verde01 with dissolve
    jump questions_loop
    
#Verde 02
label Verde02:
    call screen Verde02 with dissolve
    show screen Verde02
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "A":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Verde02 with dissolve
    jump questions_loop

    
#Verde 03#

label Verde03:
    call screen Verde03 with dissolve
    show screen Verde03
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Verde03 with dissolve
    jump questions_loop

    
#Verde 04#

label Verde04:
    call screen Verde04 with dissolve
    show screen Verde04
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Verde04 with dissolve
    jump questions_loop


#Verde 05#

label Verde05:
    call screen Verde05 with dissolve
    show screen Verde05
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Verde05 with dissolve
    jump questions_loop

#Verde 06#

label Verde06:
    call screen Verde06 with dissolve
    show screen Verde06
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Verde06 with dissolve
    jump questions_loop

#CARTOES ROXOS"

#Roxo 01

label Roxo01:
    call screen Roxo01 with dissolve
    show screen Roxo01
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "A":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Roxo01 with dissolve
    jump questions_loop

#Roxo 02

label Roxo02:
    call screen Roxo02 with dissolve
    show screen Roxo02
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "D":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Roxo02 with dissolve
    jump questions_loop

#Roxo 03

label Roxo03:
    call screen Roxo03 with dissolve
    show screen Roxo03
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "B":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Roxo03 with dissolve
    jump questions_loop
    
#Roxo 04
label Roxo04:
    call screen Roxo04 with dissolve
    show screen Roxo04
    $ disable_button = True
    if answer =="timeout":
        "Tempo Limite Atingido!"
    if answer == "C":
        $ score = score + 10
        "Correta! Seu score atual é : [score]. Clique para continuar."
        $ nrquestoes = nrquestoes + 1 

    else:
        "Errada! Clique para continuar."
    hide screen Roxo04 with dissolve
    jump questions_loop

label start2:
# INTERFACE RESCALE
    $ b1_zoom = 0.2
    $ b1_yalign = 0.996
    $ b1_xalign = 0.99
    image b1:
        "b1.png"
        zoom b1_zoom
    image b2:
        "b2.png"
        zoom b1_zoom
    $ frame_yalign = 1.0
    $ frame_xalign = 1.0
    image frame:
        "frame.png"
    
# inicialização
    $ game2_answer_list = []
    $ score = 0
    $ nrtelas = 0
    $ screen_count = 5
    $ total_acertos = 0
    $ total_riscos = 0
    $ total_score = 0
    #define gui.text_color = '#000000'
    scene chemp #
    default option1 = False                
    default option2 = False
    default option3 = False                
    default option4 = False
    $ screen_list = ["screen01", "screen02", "screen03","screen04","screen05"]
    $ text_list = []
    $ chosen_list = []
    $ answer_list = []
    #$ question_list = [("boneco01","Boneco 1 Apareceu?", True),("boneco02","Boneco 2 Apareceu?", True), ("boneco03","Boneco 3 Apareceu?", True),("boneco04","Boneco 4 Apareceu?", True), ("boneco05","Boneco 5 Apareceu?", True), ("boneco06","Boneco 6 Apareceu?", True)]
    #$ personagem_list = ["boneco01","boneco02", "boneco03","boneco04", "boneco05", "boneco06"]
    #$ coord_list = [
    $ personagem_count = 4
    #hide chemp
    #scene branco
    show instru with dissolve:
        xalign 0.5 yalign 0.5
    $ renpy.pause ()
    hide instru
    $ time = 1000
    $ timer_range = 5
    $ timer_jump = 'menu1_end'
    show img482:
        #zoom 1.0
        xalign 0.5 yalign 0.5
    #show screen countdown
    $ bottom_choice = False
    
# List of Chosen Characters to show in the Hidden Object Game

label telas_loop:
    if not screen_list == []:
        $ random_jump_target = random.choice(screen_list)
        $ screen_list.remove(random_jump_target)
        $ chosen_list.append(random_jump_target)
        $ screen_count = screen_count - 1
        $ nrtelas = nrtelas + 1
        $ renpy.scene()
        show img482:
            xalign 0.5 yalign 0.5 
        $ renpy.call(random_jump_target)
    "Fim de Jogo! Seu Total de acertos foi de [total_acertos] de [total_riscos], com o score final de [total_score]"
    $ MainMenu(confirm=False)()

label screen01:
    $ score = 0
    $ game2_acertos = 0
    $ results_counter = 0
    $ max_riscos = 4
    $ game2_answer_list = []
    $ erros = 0
# experimento_pequeno
    $ experimento_pequeno_yalign = 0.7
    $ experimento_pequeno_xalign = 0.3 
    $ experimento_pequeno_zoom = 0.22
    image experimento_pequeno: 
        "experimento.png"
        zoom experimento_pequeno_zoom
    image experimento_pequeno_r: 
        "experimento_r.png"        
        zoom experimento_pequeno_zoom
    $ experimento_pequeno_var = True
    $ game2_answer_list.append ("experimento_pequeno_var")
    $ game2_answer_list.append (experimento_pequeno_var)   
#mochila_grande
    $ mochila_grande_yalign = 0.7
    $ mochila_grande_xalign = 0.05 
    $ mochila_grande_zoom = 0.5    
    image mochila_grande: 
        "mochila.png"
        zoom mochila_grande_zoom
    image mochila_grande_r: 
        "mochila_r.png"
        zoom mochila_grande_zoom
    image mochila_grande_pro: 
        "mochila_pro.png"
        zoom mochila_grande_zoom
    image mochila_grande_rpro: 
        "mochila_rpro.png"
        zoom mochila_grande_zoom
    image mochila_grande_mold_s: 
        "mochila_mold_s.png"
        zoom mochila_grande_zoom
    image mochila_grande_mold_i: 
        "mochila_mold_i.png"
        zoom mochila_grande_zoom   
    $ mochila_grande_var = True
    $ game2_answer_list.append ("mochila_grande_var")
    $ game2_answer_list.append (mochila_grande_var)           
#sem_ocolus
    $ sem_ocolus_xalign = 0.35
    $ sem_ocolus_yalign = 0.44
    $ sem_ocolus_zoom = 0.75       
    image sem_ocolus: 
        "boneco_b.png"
        zoom sem_ocolus_zoom
    image sem_ocolus_r: 
        "boneco_b_r.png"
        zoom sem_ocolus_zoom
    image sem_ocolus_pro: 
        "boneco_b_pro.png"
        zoom sem_ocolus_zoom
    image sem_ocolus_rpro: 
        "boneco_b_rpro.png"
        zoom sem_ocolus_zoom
    image sem_ocolus_mold_s: 
        "boneco_b_mold_s.png"
        zoom sem_ocolus_zoom
    image sem_ocolus_mold_i: 
        "boneco_b_mold_i.png"
        zoom sem_ocolus_zoom        
    $ sem_ocolus_var = True
    $ game2_answer_list.append ("sem_ocolus_var")
    $ game2_answer_list.append (sem_ocolus_var)           
#boneco_c
    $ boneco_c_xalign = 0.69
    $ boneco_c_yalign = 0.35 
    $ boneco_c_zoom = 0.7   
    image boneco_c: 
        "boneco_c.png"
        zoom boneco_c_zoom
    image boneco_c_r: 
        "boneco_c_r.png"
        zoom boneco_c_zoom
    image boneco_c_pro: 
        "boneco_c_pro.png"
        zoom boneco_c_zoom
    image boneco_c_rpro: 
        "boneco_c_rpro.png"
        zoom boneco_c_zoom
    image boneco_c_mold_s: 
        "boneco_c_mold_s.png"
        zoom boneco_c_zoom
    image boneco_c_mold_i: 
        "boneco_c_mold_i.png"
        zoom boneco_c_zoom
                                        
    $ boneco_c_var = True
    $ game2_answer_list.append ("boneco_c_var")
    $ game2_answer_list.append (boneco_c_var)           
#Cientista
    $ Cientista_xalign = 0.745
    $ Cientista_yalign = 1.47
    $ Cientista_zoom = 0.75    
    image Cientista: 
        "Cientista.png"
        zoom Cientista_zoom
    image Cientista_r: 
        "Cientista_r.png"
        zoom Cientista_zoom        
    $ Cientista_var = True
    $ game2_answer_list.append ("Cientista_var")
    $ game2_answer_list.append (Cientista_var)           
#lixeira
    $ lixeira_yalign = 0.37
    $ lixeira_xalign = 0.22
    $ lixeira_zoom = 0.35    
    image lixeira: 
        "lixeira.png"
        zoom lixeira_zoom 
    image lixeira_r: 
        "lixeira_r.png"
        zoom lixeira_zoom         
    $ lixeira_var = True
    $ game2_answer_list.append ("lixeira_var")
    $ game2_answer_list.append (lixeira_var)           
#costas
    $ costas_yalign = -0.1
    $ costas_xalign = 0.13
    $ costas_zoom = 0.8
    image costas: 
        "costas.png"
        zoom costas_zoom
    image costas_r: 
        "costas_r.png"
        zoom costas_zoom
    image costas_pro: 
        "costas_pro.png"
        zoom costas_zoom 
    image costas_rpro: 
        "costas_rpro.png"
        zoom costas_zoom 
    image costas_mold_s: 
        "costas_mold_s.png"
        zoom costas_zoom 
    image costas_mold_i: 
        "costas_mold_i.png"
        zoom costas_zoom         
    $ costas_var = True
    $ game2_answer_list.append ("costas_var")
    $ game2_answer_list.append (costas_var)           
# luva_caindo
    $ luva_caindo_yalign = 0.25
    $ luva_caindo_xalign = 0.22
    $ luva_caindo_zoom = 0.22
    image luva_caindo: 
        "luva_caindo.png"
        zoom luva_caindo_zoom 
    image luva_caindo_r: 
        "luva_caindo_r.png"
        zoom luva_caindo_zoom 
    image luva_caindo_pro: 
        "luva_caindo_pro.png"
        zoom luva_caindo_zoom 
    image luva_caindo_rpro: 
        "luva_caindo_rpro.png"
        zoom luva_caindo_zoom 
    image luva_caindo_mold_s: 
        "luva_caindo_mold_s.png"
        zoom luva_caindo_zoom 
    image luva_caindo_mold_i: 
        "luva_caindo_mold_i.png"
        zoom luva_caindo_zoom 
                                                
    $ luva_caindo_var = True
    $ game2_answer_list.append ("luva_caindo_var")
    $ game2_answer_list.append (luva_caindo_var)           
#frasco_capela
    $ frasco_capela_xalign = 0.80
    $ frasco_capela_yalign = 0.26
    $ frasco_capela_zoom = 0.35
    image frasco_capela: 
        "frasco_capela.png"
        zoom frasco_capela_zoom
    image frasco_capela_r: 
        "frasco_capela_r.png"
        zoom frasco_capela_zoom         
    $ frasco_capela_var = True
    $ game2_answer_list.append ("frasco_capela_var")
    $ game2_answer_list.append (frasco_capela_var)           

        
    call screen game2_hiddenobject with dissolve
    jump end_result_screen

screen game2_hiddenobject:
    imagebutton:
        idle "frasco_capela"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("frasco_capela_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("frasco_capela_var") + 1] == False)
        hover "frasco_capela_r"
        selected_idle "frasco_capela_r" 
        xalign frasco_capela_xalign
        yalign frasco_capela_yalign

    imagebutton:
        idle "lixeira"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("lixeira_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("lixeira_var") + 1] == False)
        hover "lixeira_r"
        selected_idle "lixeira_r" 
        yalign lixeira_yalign
        xalign lixeira_xalign
        
    imagebutton:
        idle "luva_caindo"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("luva_caindo_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("luva_caindo_var") + 1] == False)
        hover "luva_caindo_r"
        selected_idle "luva_caindo_r" 
        yalign luva_caindo_yalign
        xalign luva_caindo_xalign        
        
    imagebutton:
        idle "costas"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("costas_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("costas_var") + 1] == False)
        hover "costas_r"
        selected_idle "costas_r" 
        yalign costas_yalign
        xalign costas_xalign

    imagebutton:
        idle "sem_ocolus"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("sem_ocolus_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("sem_ocolus_var") + 1] == False)
        hover "sem_ocolus_r"
        selected_idle "sem_ocolus_r" 
        xalign sem_ocolus_xalign
        yalign sem_ocolus_yalign

    imagebutton:
        idle "experimento_pequeno"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("experimento_pequeno_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("experimento_pequeno_var") + 1] == False)
        hover "experimento_pequeno_r"
        selected_idle "experimento_pequeno_r" 
        yalign experimento_pequeno_yalign
        xalign experimento_pequeno_xalign

    imagebutton:
        idle "mochila_grande"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("mochila_grande_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("mochila_grande_var") + 1] == False)
        hover "mochila_grande_r"
        selected_idle "mochila_grande_r" 
        yalign mochila_grande_yalign
        xalign mochila_grande_xalign

    imagebutton:
        idle "boneco_c"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("boneco_c_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("boneco_c_var") + 1] == False)
        hover "boneco_c_r"
        selected_idle "boneco_c_r" 
        xalign boneco_c_xalign
        yalign boneco_c_yalign

    imagebutton:
        idle "Cientista"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("Cientista_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("Cientista_var") + 1] == False)
        hover "Cientista_r"
        selected_idle "Cientista_r" 
        xalign Cientista_xalign
        yalign Cientista_yalign
    
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action With(dissolve), Return()

label end_result_screen:
    $ erros = 0
    $ score = 0
    $ game2_acertos = 0
    $ results_counter = 0
    while (results_counter < len(game2_answer_list)):
        if (game2_answer_list[results_counter] == "frasco_capela_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show frasco_capela_r:
                    yalign frasco_capela_yalign
                    xalign frasco_capela_xalign
            else:
                show frasco_capela:
                    yalign frasco_capela_yalign
                    xalign frasco_capela_xalign
        if (game2_answer_list[results_counter] == "lixeira_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show lixeira_r:
                    yalign lixeira_yalign
                    xalign lixeira_xalign
            else:
                show lixeira:
                    yalign lixeira_yalign
                    xalign lixeira_xalign             
        if (game2_answer_list[results_counter] == "luva_caindo_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show luva_caindo_rpro behind costas,costas_r,costas_pro,costas_rpro:
                    yalign luva_caindo_yalign
                    xalign luva_caindo_xalign
            else:
                show luva_caindo_pro behind costas,costas_r,costas_pro,costas_rpro:
                    yalign luva_caindo_yalign
                    xalign luva_caindo_xalign
        if (game2_answer_list[results_counter] == "costas_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show costas_rpro:
                    yalign costas_yalign
                    xalign costas_xalign
            else:
                show costas_pro:
                    yalign costas_yalign
                    xalign costas_xalign
        if (game2_answer_list[results_counter] == "sem_ocolus_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show sem_ocolus_rpro behind experimento_pequeno, experimento_pequeno_r:
                    yalign sem_ocolus_yalign
                    xalign sem_ocolus_xalign
            else:
                show sem_ocolus_pro behind experimento_pequeno, experimento_pequeno_r:
                    yalign sem_ocolus_yalign
                    xalign sem_ocolus_xalign
        if (game2_answer_list[results_counter] == "experimento_pequeno_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show experimento_pequeno_r:
                    yalign experimento_pequeno_yalign
                    xalign experimento_pequeno_xalign
            else:
                show experimento_pequeno:
                    yalign experimento_pequeno_yalign
                    xalign experimento_pequeno_xalign
        if (game2_answer_list[results_counter] == "mochila_grande_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show mochila_grande_rpro:
                    yalign mochila_grande_yalign
                    xalign mochila_grande_xalign
                    
            else:
                show mochila_grande_pro:
                    yalign mochila_grande_yalign
                    xalign mochila_grande_xalign
                    
        if (game2_answer_list[results_counter] == "boneco_c_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show boneco_c_rpro:
                    yalign boneco_c_yalign
                    xalign boneco_c_xalign
                    
            else:
                show boneco_c_pro:
                    yalign boneco_c_yalign
                    xalign boneco_c_xalign
                                        
                    
        if (game2_answer_list[results_counter] == "Cientista_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show Cientista_r:
                    yalign Cientista_yalign
                    xalign Cientista_xalign
            else:
                show Cientista:
                    yalign Cientista_yalign
                    xalign Cientista_xalign
        $ results_counter = results_counter + 1
    
    $ proceed_flag = False
    $ review_answer = "NONE"
    $ score_points = score * 15
    $ total_acertos = total_acertos + score
    $ total_riscos = total_riscos + max_riscos
    $ total_score = total_acertos + score_points
    if (erros == 0):
        "Você indentificou [score] de [max_riscos] riscos! Seu score final é [score_points]. Clique para continuar."
    if (erros > 0):
        "Você indentificou [score] de [max_riscos] riscos, porém [erros] items foram erroneamente marcados! Seu score final é [score_points]. Clique para continuar."
    while (proceed_flag == False):
        "Clique nos items que representam riscos para maiores informações. Senão clique no botão verde novamente para ir para o proximo nivel"
        call screen review_screens with dissolve
        if (review_answer == "mochila_grande"):
            "Mochila na mesa apresenta risco de contaminação, tanto de agentes externos quanto internos! Mochilas, bolsas e afins devem estar longe de areas de risco, como armarios ou cabides apropriados."
        if (review_answer == "sem_ocolus"):
            "Esta aluna não está utilizando proteção ocular, pondo em risco sua visão!"
        if (review_answer == "boneco_c"):
            "Este aluno está se agachando no chão do laboratório, colocando-se em risco devido a residuos presentes no chão"
        if (review_answer == "costas"):
            "Este aluno está se desfazendo de suas luvas de forma errada!"
        if (review_answer == "luva_caindo"):
            "As luvas devem ser descartadas no local apropriado e não na lixeira comum!"            
        $ review_answer = "NONE"
    jump telas_loop
    
screen review_screens:
        
    imagebutton:
        idle "mochila_grande_mold_i"
        focus_mask None
        action SetVariable("review_answer","mochila_grande"),Return()
        selected (review_answer == "mochila_grande")
        hover "mochila_grande_mold_s"
        selected_idle "mochila_grande_mold_s"          
        yalign mochila_grande_yalign
        xalign mochila_grande_xalign
        
    imagebutton:
        idle "sem_ocolus_mold_i"
        focus_mask None
        action SetVariable("review_answer","sem_ocolus"),Return()
        selected (review_answer == "sem_ocolus")
        hover "sem_ocolus_mold_s"
        selected_idle "sem_ocolus_mold_s"          
        yalign sem_ocolus_yalign
        xalign sem_ocolus_xalign

    imagebutton:
        idle "boneco_c_mold_i"
        focus_mask None
        action SetVariable("review_answer","boneco_c"),Return()
        selected (review_answer == "boneco_c")
        hover "boneco_c_mold_s"
        selected_idle "boneco_c_mold_s"          
        yalign boneco_c_yalign
        xalign boneco_c_xalign

    imagebutton:
        idle "costas_mold_i"
        focus_mask None
        action SetVariable("review_answer","costas"),Return()
        selected (review_answer == "costas")
        hover "costas_mold_s"
        selected_idle "costas_mold_s"          
        yalign costas_yalign
        xalign costas_xalign         

    imagebutton:
        idle "luva_caindo_mold_i"
        focus_mask None
        action SetVariable("review_answer","luva_caindo"),Return()
        selected (review_answer == "luva_caindo")
        hover "luva_caindo_mold_s"
        selected_idle "luva_caindo_mold_s"          
        yalign luva_caindo_yalign
        xalign luva_caindo_xalign 
        
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action SetVariable("proceed_flag",True), Return()    


label screen02:
    $ score = 0
    $ game2_answer_list = []
    $ max_riscos = 3
    $ erros = 0
    
#EXPERIMENTO_2
    $ experimento_2_zoom = 0.22
    $ experimento_2_xalign = 0.5
    $ experimento_2_yalign = 0.7 
    image experimento_2: 
        "experimento.png"
        zoom experimento_2_zoom
    image experimento_2_r: 
        "experimento_r.png"
        zoom experimento_2_zoom
    $ experimento_2_var = True
    $ game2_answer_list.append ("experimento_2_var")
    $ game2_answer_list.append (experimento_2_var)   
#tresfrascos
    $ tresfrascos_zoom = 0.65
    $ tresfrascos_xalign = 0.25
    $ tresfrascos_yalign = 0.75
    image tresfrascos: 
        "tresfrascos.png"
        zoom tresfrascos_zoom
    image tresfrascos_r: 
        "tresfrascos_r.png"
        zoom tresfrascos_zoom
    $ tresfrascos_var = True
    $ game2_answer_list.append ("tresfrascos_var")
    $ game2_answer_list.append (tresfrascos_var)           
#frasco_toxico
    $ frasco_toxico_zoom = 0.45
    $ frasco_toxico_xalign = 0.1
    $ frasco_toxico_yalign = 0.77
    image frasco_toxico: 
        "frasco_toxico.png"
        zoom frasco_toxico_zoom
    image frasco_toxico_r: 
        "frasco_toxico_r.png"
        zoom frasco_toxico_zoom
    image frasco_toxico_pro: 
        "frasco_toxico_pro.png"
        zoom frasco_toxico_zoom
    image frasco_toxico_rpro: 
        "frasco_toxico_rpro.png"
        zoom frasco_toxico_zoom
    image frasco_toxico_mold_s: 
        "frasco_toxico_mold_s.png"
        zoom frasco_toxico_zoom
    image frasco_toxico_mold_i: 
        "frasco_toxico_mold_i.png"
        zoom frasco_toxico_zoom        
    $ frasco_toxico_var = True
    $ game2_answer_list.append ("frasco_toxico_var")
    $ game2_answer_list.append (frasco_toxico_var)           
#cara_livro
    $ cara_livro_zoom = 0.7
    $ cara_livro_xalign = 0.05
    $ cara_livro_yalign = 0.45
    image cara_livro: 
        "cara_livro.png"
        zoom cara_livro_zoom
    image cara_livro_r: 
        "cara_livro_r.png"
        zoom cara_livro_zoom        
    $ cara_livro_var = True
    $ game2_answer_list.append ("cara_livro_var")
    $ game2_answer_list.append (cara_livro_var)           
#cabelo_solto
    $ cabelo_solto_zoom = 0.7 
    $ cabelo_solto_xalign = 0.35
    $ cabelo_solto_yalign = 0.44
    image cabelo_solto: 
        "cabelo_solto.png"
        zoom cabelo_solto_zoom
    image cabelo_solto_r: 
        "cabelo_solto_r.png"
        zoom cabelo_solto_zoom
    image cabelo_solto_pro: 
        "cabelo_solto_pro.png"
        zoom cabelo_solto_zoom
    image cabelo_solto_rpro: 
        "cabelo_solto_rpro.png"
        zoom cabelo_solto_zoom
    image cabelo_solto_mold_s: 
        "cabelo_solto_mold_s.png"
        zoom cabelo_solto_zoom
    image cabelo_solto_mold_i: 
        "cabelo_solto_mold_i.png"
        zoom cabelo_solto_zoom          
    $ cabelo_solto_var = True
    $ game2_answer_list.append ("cabelo_solto_var")
    $ game2_answer_list.append (cabelo_solto_var)   
#cadeirante
    $ cadeirante_zoom = 0.88
    $ cadeirante_xalign = 0.69
    $ cadeirante_yalign = 0.30
    image cadeirante: 
        "cadeirante.png"
        zoom cadeirante_zoom
    image cadeirante_r: 
        "cadeirante_r.png"
        zoom cadeirante_zoom        
    $ cadeirante_var = True
    $ game2_answer_list.append ("cadeirante_var")
    $ game2_answer_list.append (cadeirante_var)           
#inventario
    $ inventario_xalign = 0.22
    $ inventario_yalign = -0.02
    image inventario: 
        "inventario.png"   
    image inventario_r: 
        "inventario_r.png"          
    $ inventario_var = True
    $ game2_answer_list.append ("inventario_var")
    $ game2_answer_list.append (inventario_var)           
#garrafa_quebrada
    $ garrafa_quebrada_zoom = 0.3
    $ garrafa_quebrada_xalign = 0.845
    $ garrafa_quebrada_yalign = 0.31
    image garrafa_quebrada: 
        "garrafa_quebrada.png"
        zoom garrafa_quebrada_zoom
    image garrafa_quebrada_r: 
        "garrafa_quebrada_r.png"
        zoom garrafa_quebrada_zoom 
    image garrafa_quebrada_pro: 
        "garrafa_quebrada_pro.png"
        zoom garrafa_quebrada_zoom
    image garrafa_quebrada_rpro: 
        "garrafa_quebrada_rpro.png"
        zoom garrafa_quebrada_zoom
    image garrafa_quebrada_mold_s: 
        "garrafa_quebrada_mold_s.png"
        zoom garrafa_quebrada_zoom
    image garrafa_quebrada_mold_i: 
        "garrafa_quebrada_mold_i.png"
        zoom garrafa_quebrada_zoom        
    $ garrafa_quebrada_var = True
    $ game2_answer_list.append ("garrafa_quebrada_var")
    $ game2_answer_list.append (garrafa_quebrada_var)           

        
    call screen game2_hiddenobject02 with dissolve
    jump end_result_screen_2

screen game2_hiddenobject02:

    imagebutton:
        idle "garrafa_quebrada"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("garrafa_quebrada_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("garrafa_quebrada_var") + 1] == False)
        hover "garrafa_quebrada_r"
        selected_idle "garrafa_quebrada_r" 
        xalign garrafa_quebrada_xalign
        yalign garrafa_quebrada_yalign

    imagebutton:
        idle "inventario"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("inventario_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("inventario_var") + 1] == False)
        hover "inventario_r"
        selected_idle "inventario_r" 
        yalign inventario_yalign
        xalign inventario_xalign

    imagebutton:
        idle "cabelo_solto"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("cabelo_solto_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("cabelo_solto_var") + 1] == False)
        hover "cabelo_solto_r"
        selected_idle "cabelo_solto_r" 
        xalign cabelo_solto_xalign
        yalign cabelo_solto_yalign
        
    imagebutton:
        idle "tresfrascos"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("tresfrascos_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("tresfrascos_var") + 1] == False)
        hover "tresfrascos_r"
        selected_idle "tresfrascos_r" 
        yalign tresfrascos_yalign
        xalign tresfrascos_xalign

    imagebutton:
        idle "cara_livro"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("cara_livro_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("cara_livro_var") + 1] == False)
        hover "cara_livro_r"
        selected_idle "cara_livro_r" 
        yalign cara_livro_yalign
        xalign cara_livro_xalign

    imagebutton:
        idle "frasco_toxico"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("frasco_toxico_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("frasco_toxico_var") + 1] == False)
        hover "frasco_toxico_r"
        selected_idle "frasco_toxico_r" 
        yalign frasco_toxico_yalign
        xalign frasco_toxico_xalign

    imagebutton:
        idle "cadeirante"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("cadeirante_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("cadeirante_var") + 1] == False)
        hover "cadeirante_r"
        selected_idle "cadeirante_r" 
        xalign cadeirante_xalign
        yalign cadeirante_yalign

    imagebutton:
        idle "experimento_2"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("experimento_2_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("experimento_2_var") + 1] == False)
        hover "experimento_2_r"
        selected_idle "experimento_2_r" 
        yalign experimento_2_yalign
        xalign experimento_2_xalign
    
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action With(dissolve), Return()

label end_result_screen_2:
    $ score = 0
    $ game2_acertos = 0
    $ results_counter = 0
    while (results_counter < len(game2_answer_list)):
        if (game2_answer_list[results_counter] == "experimento_2_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show experimento_2_r:
                    yalign experimento_2_yalign
                    xalign experimento_2_xalign
            else:
                show experimento_2:
                    yalign experimento_2_yalign
                    xalign experimento_2_xalign
        if (game2_answer_list[results_counter] == "tresfrascos_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show tresfrascos_r:
                    yalign tresfrascos_yalign
                    xalign tresfrascos_xalign
            else:
                show tresfrascos:
                    yalign tresfrascos_yalign
                    xalign tresfrascos_xalign             
        if (game2_answer_list[results_counter] == "frasco_toxico_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show frasco_toxico_rpro:
                    yalign frasco_toxico_yalign
                    xalign frasco_toxico_xalign
            else:
                show frasco_toxico_pro:
                    yalign frasco_toxico_yalign
                    xalign frasco_toxico_xalign
        if (game2_answer_list[results_counter] == "cara_livro_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show cara_livro_r behind frasco_toxico,frasco_toxico_r,frasco_toxico_pro,frasco_toxico_rpro:
                    yalign cara_livro_yalign
                    xalign cara_livro_xalign
            else:
                show cara_livro behind frasco_toxico, frasco_toxico_r,frasco_toxico_pro,frasco_toxico_rpro:
                    yalign cara_livro_yalign
                    xalign cara_livro_xalign
        if (game2_answer_list[results_counter] == "cadeirante_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show cadeirante_r:
                    yalign cadeirante_yalign
                    xalign cadeirante_xalign
            else:
                show cadeirante:
                    yalign cadeirante_yalign
                    xalign cadeirante_xalign
        if (game2_answer_list[results_counter] == "garrafa_quebrada_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show garrafa_quebrada_rpro:
                    yalign garrafa_quebrada_yalign
                    xalign garrafa_quebrada_xalign
            else:
                show garrafa_quebrada_pro:
                    yalign garrafa_quebrada_yalign
                    xalign garrafa_quebrada_xalign
        if (game2_answer_list[results_counter] == "cabelo_solto_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show cabelo_solto_rpro:
                    yalign cabelo_solto_yalign
                    xalign cabelo_solto_xalign
                    
            else:
                show cabelo_solto_pro:
                    yalign cabelo_solto_yalign
                    xalign cabelo_solto_xalign
                    
        if (game2_answer_list[results_counter] == "inventario_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show inventario_r:
                    yalign inventario_yalign
                    xalign inventario_xalign
            else:
                show inventario:
                    yalign inventario_yalign
                    xalign inventario_xalign
        $ results_counter = results_counter + 1
    
    $ proceed_flag = False
    $ review_answer = "NONE"
    $ score_points = score * 15
    $ total_acertos = total_acertos + score
    $ total_riscos = total_riscos + max_riscos
    $ total_score = total_acertos + score_points
    if (erros == 0):
        "Você indentificou [score] de [max_riscos] riscos! Seu score final é [score_points]. Clique para continuar."
    if (erros > 0):
        "Você indentificou [score] de [max_riscos] riscos, porém [erros] items foram erroneamente marcados! Seu score final é [score_points]. Clique para continuar."
    while (proceed_flag == False):
        "Clique nos items que representam riscos para maiores informações. Senão clique no botão verde novamente para ir para o proximo nivel"
        call screen review_screens2 with dissolve
        if (review_answer == "garrafa_quebrada"):
            "Uma recepiente de vidro se encontra quebrado, ele deverá ser apropriadamente recolhido e descartado o quanto antes!"
        if (review_answer == "cabelo_solto"):
            "Esta aluno está de cabelo long e solto, pondo-a em risco devido a possiveis materiais que seu cabelo poderá entrar em contato"
        if (review_answer == "frasco_toxico"):
            "Esté frasco contem elementos toxicos, ele não deve ser manipulado fora da capela!"
        $ review_answer = "NONE"
    jump telas_loop
    
screen review_screens2:
        
    imagebutton:
        idle "garrafa_quebrada_mold_i"
        focus_mask None
        action SetVariable("review_answer","garrafa_quebrada"),Return()
        selected (review_answer == "garrafa_quebrada")
        hover "garrafa_quebrada_mold_s"
        selected_idle "garrafa_quebrada_mold_s"          
        yalign garrafa_quebrada_yalign
        xalign garrafa_quebrada_xalign
        
    imagebutton:
        idle "cabelo_solto_mold_i"
        focus_mask None
        action SetVariable("review_answer","cabelo_solto"),Return()
        selected (review_answer == "cabelo_solto")
        hover "cabelo_solto_mold_s"
        selected_idle "cabelo_solto_mold_s"          
        yalign cabelo_solto_yalign
        xalign cabelo_solto_xalign

    imagebutton:
        idle "frasco_toxico_mold_i"
        focus_mask None
        action SetVariable("review_answer","frasco_toxico"),Return()
        selected (review_answer == "frasco_toxico")
        hover "frasco_toxico_mold_s"
        selected_idle "frasco_toxico_mold_s"          
        yalign frasco_toxico_yalign
        xalign frasco_toxico_xalign      
        
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action SetVariable("proceed_flag",True), Return()    

label screen03:
#Initializing
    $ score = 0
    $ game2_answer_list = []
    $ max_riscos = 4
    $ erros = 0

#MOCHILA
    $ mochila_zoom = 0.3
    $ mochila_xalign = 0.22
    $ mochila_yalign = 0.35
    image mochila: 
        "mochila.png"
        zoom mochila_zoom
    image mochila_r: 
        "mochila_r.png"
        zoom mochila_zoom
    image mochila_pro: 
        "mochila_pro.png"
        zoom mochila_zoom 
    image mochila_rpro: 
        "mochila_rpro.png"
        zoom mochila_zoom   
    image mochila_mold_s:
        "mochila_mold_s.png"
        zoom mochila_zoom
    image mochila_mold_i:
        "mochila_mold_i.png"
        zoom mochila_zoom
    $ mochila_var = True
    $ game2_answer_list.append ("mochila_var")
    $ game2_answer_list.append (mochila_var)           
#microscopio
    $ microscopio_zoom = 0.8
    $ microscopio_yalign = 0.7
    $ microscopio_xalign = 0.6         
    image microscopio:
        "microscopio.png"
        zoom microscopio_zoom
    image microscopio_r:
        "microscopio_r.png"
        zoom microscopio_zoom
    $ microscopio_var = True
    $ game2_answer_list.append ("microscopio_var")
    $ game2_answer_list.append (microscopio_var)        
#carvalho
    $ carvalho_zoom = 0.65
    $ carvalho_xalign = 0.65
    $ carvalho_yalign = 0.01 
    image carvalho: 
        "carvalho.png"
        zoom carvalho_zoom
    image carvalho_r: 
        "carvalho_r.png"
        zoom carvalho_zoom
    $ carvalho_var = True
    $ game2_answer_list.append ("carvalho_var")
    $ game2_answer_list.append (carvalho_var) 
#rachado
    $ rachado_xalign = 0.35
    $ rachado_yalign = 0.75        
    image rachado: 
        "rachado.png"
    image rachado_r: 
        "rachado_r.png"
    image rachado_pro: 
        "rachado_pro.png"
    image rachado_rpro: 
        "rachado_rpro.png"
    image rachado_mold_s: 
        "rachado_mold_s.png"
    image rachado_mold_i: 
        "rachado_mold_i.png"
    $ rachado_var = True
    $ game2_answer_list.append ("rachado_var")
    $ game2_answer_list.append (rachado_var) 
 
#livro_2
    $ livro_2_zoom = 0.4
    $ livro_2_xalign = 0.15
    $ livro_2_yalign = 0.78
    image livro_2: 
        "livro.png"
        zoom livro_2_zoom   
    image livro_2_r: 
        "livro_r.png"
        zoom livro_2_zoom  
    $ livro_2_var = True
    $ game2_answer_list.append ("livro_2_var")
    $ game2_answer_list.append (livro_2_var) 
        
#vidro_verde
    $ vidro_verde_zoom = 0.65
    $ vidro_verde_yalign = 0.7
    $ vidro_verde_xalign = 0.45
    image vidro_verde: 
        "vidro_verde.png"
        zoom vidro_verde_zoom
    image vidro_verde_r: 
        "vidro_verde_r.png"
        zoom vidro_verde_zoom
    $ vidro_verde_var = True
    $ game2_answer_list.append ("vidro_verde_var")
    $ game2_answer_list.append (vidro_verde_var) 
#cafe
    $ cafe_zoom = 0.5
    $ cafe_xalign = 0.15
    $ cafe_yalign = 0.48
    image cafe: 
        "cafe.png"
        zoom cafe_zoom
    image cafe_r: 
        "cafe_r.png"
        zoom cafe_zoom
    image cafe_pro: 
        "cafe_pro.png"
        zoom cafe_zoom
    image cafe_rpro: 
        "cafe_rpro.png"
        zoom cafe_zoom
    image cafe_mold_s: 
        "cafe_mold_s.png"
        zoom cafe_zoom
    image cafe_mold_i: 
        "cafe_mold_i.png"
        zoom cafe_zoom
    $ cafe_var = True
    $ game2_answer_list.append ("cafe_var")
    $ game2_answer_list.append (cafe_var) 
# celular
    $ celular_zoom = 0.75
    $ celular_xalign = 0.45 
    $ celular_yalign = 0.40      
    image celular: 
        "celular.png"
        zoom celular_zoom
    image celular_r: 
        "celular_r.png"
        zoom celular_zoom 
    image celular_pro: 
        "celular_pro.png"
        zoom celular_zoom 
    image celular_rpro: 
        "celular_rpro.png"
        zoom celular_zoom 
    image celular_mold_s: 
        "celular_mold_s.png"
        zoom celular_zoom 
    image celular_mold_i: 
        "celular_mold_i.png"
        zoom celular_zoom
    $ celular_var = True
    $ game2_answer_list.append ("celular_var")
    $ game2_answer_list.append (celular_var)         
        
    call screen game2_hiddenobject03 with dissolve
    jump end_result_screen_3

screen game2_hiddenobject03:

    imagebutton:
        idle "carvalho"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("carvalho_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("carvalho_var") + 1] == False)
        hover "carvalho_r"
        selected_idle "carvalho_r"  
        xalign carvalho_xalign
        yalign carvalho_yalign      

    imagebutton:
        idle "microscopio"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("microscopio_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("microscopio_var") + 1] == False)
        hover "microscopio_r"
        selected_idle "microscopio_r"  
        yalign microscopio_yalign
        xalign microscopio_xalign

    imagebutton:
        idle "mochila"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("mochila_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("mochila_var") + 1] == False)
        hover "mochila_r"
        selected_idle "mochila_r"  
        yalign mochila_yalign
        xalign mochila_xalign

    imagebutton:
        idle "celular"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("celular_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("celular_var") + 1] == False)
        hover "celular_r"
        selected_idle "celular_r"  
        xalign celular_xalign
        yalign celular_yalign

    imagebutton:
        idle "rachado"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("rachado_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("rachado_var") + 1] == False)
        hover "rachado_r"
        selected_idle "rachado_r"  
        yalign rachado_yalign
        xalign rachado_xalign   

    imagebutton:
        idle "cafe"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("cafe_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("cafe_var") + 1] == False)
        hover "cafe_r"
        selected_idle "cafe_r"  
        yalign cafe_yalign
        xalign cafe_xalign     

    imagebutton:
        idle "vidro_verde"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("vidro_verde_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("vidro_verde_var") + 1] == False)
        hover "vidro_verde_r"
        selected_idle "vidro_verde_r"  
        yalign vidro_verde_yalign
        xalign vidro_verde_xalign
        
    imagebutton:
        idle "livro_2"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("livro_2_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("livro_2_var") + 1] == False)
        hover "livro_2_r"
        selected_idle "livro_2_r"  
        yalign livro_2_yalign
        xalign livro_2_xalign     
    
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action With(dissolve), Return()
        
label end_result_screen_3:
    $ score = 0
    $ game2_acertos = 0
    $ results_counter = 0
    while (results_counter < len(game2_answer_list)):
        if (game2_answer_list[results_counter] == "carvalho_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show carvalho_r behind microscopio, microscopio_r:
                    yalign carvalho_yalign
                    xalign carvalho_xalign
            else:
                show carvalho behind microscopio, microscopio_r:
                    yalign carvalho_yalign
                    xalign carvalho_xalign
        if (game2_answer_list[results_counter] == "microscopio_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show microscopio_r:
                    yalign microscopio_yalign
                    xalign microscopio_xalign
            else:
                show microscopio:
                    yalign microscopio_yalign
                    xalign microscopio_xalign             
        if (game2_answer_list[results_counter] == "mochila_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show mochila_rpro:
                    yalign mochila_yalign
                    xalign mochila_xalign
            else:
                show mochila_pro:
                    yalign mochila_yalign
                    xalign mochila_xalign
        if (game2_answer_list[results_counter] == "livro_2_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show livro_2_r:
                    yalign livro_2_yalign
                    xalign livro_2_xalign
            else:
                show livro_2:
                    yalign livro_2_yalign
                    xalign livro_2_xalign
        if (game2_answer_list[results_counter] == "vidro_verde_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show vidro_verde_r:
                    yalign vidro_verde_yalign
                    xalign vidro_verde_xalign
            else:
                show vidro_verde:
                    yalign vidro_verde_yalign
                    xalign vidro_verde_xalign
        if (game2_answer_list[results_counter] == "cafe_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show cafe_rpro:
                    yalign cafe_yalign
                    xalign cafe_xalign
            else:
                show cafe_pro:
                    yalign cafe_yalign
                    xalign cafe_xalign
        if (game2_answer_list[results_counter] == "celular_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show celular_rpro behind vidro_verde,vidro_verde_r:
                    yalign celular_yalign
                    xalign celular_xalign
                    
            else:
                show celular_pro behind vidro_verde,vidro_verde_r:
                    yalign celular_yalign
                    xalign celular_xalign
                    
        if (game2_answer_list[results_counter] == "rachado_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show rachado_rpro:
                    yalign rachado_yalign
                    xalign rachado_xalign
            else:
                show rachado_pro:
                    yalign rachado_yalign
                    xalign rachado_xalign
        $ results_counter = results_counter + 1
    
    $ proceed_flag = False
    $ review_answer = "NONE"
    $ score_points = score * 15
    $ total_acertos = total_acertos + score
    $ total_riscos = total_riscos + max_riscos
    $ total_score = total_acertos + score_points
    if (erros == 0):
        "Você indentificou [score] de [max_riscos] riscos! Seu score final é [score_points]. Clique para continuar."
    if (erros > 0):
        "Você indentificou [score] de [max_riscos] riscos, porém [erros] items foram erroneamente marcados! Seu score final é [score_points]. Clique para continuar."
    while (proceed_flag == False):
        "Clique nos items que representam riscos para maiores informações. Senão clique no botão verde novamente para ir para o proximo nivel"
        call screen review_screens3 with dissolve
        if (review_answer == "celular"):
            "Este aluno está utilizando o celunar durante o manuseio ativo de substancias, faceis distrações aqui o colocam em risco!"
        if (review_answer == "rachado"):
            "Esta vidraça está rachada, mesmo que não há vazamentos ela já apresenta um risco para qualquer outra manipulação e não deve ser utilizada!"
        if (review_answer == "cafe"):
            "Esta aluna está tomando café durante uma participação ativa de manipulação. O risco aqui é ainda maior, pois pode ocorrer ingestão de substancias perigosas!"
        if (review_answer == "mochila"):
            "Mochila no chão apresenta risco de contaminação, tanto de agentes externos quanto internos!Mochilas, bolsas e afins devem estar longe de areas de risco, como armarios ou cabides apropriados."
        $ review_answer = "NONE"
    jump telas_loop
    
screen review_screens3:
        
    imagebutton:
        idle "celular_mold_i"
        focus_mask None
        action SetVariable("review_answer","celular"),Return()
        selected (review_answer == "celular")
        hover "celular_mold_s"
        selected_idle "celular_mold_s"          
        yalign celular_yalign
        xalign celular_xalign
        
    imagebutton:
        idle "rachado_mold_i"
        focus_mask None
        action SetVariable("review_answer","rachado"),Return()
        selected (review_answer == "rachado")
        hover "rachado_mold_s"
        selected_idle "rachado_mold_s"          
        yalign rachado_yalign
        xalign rachado_xalign

    imagebutton:
        idle "cafe_mold_i"
        focus_mask None
        action SetVariable("review_answer","cafe"),Return()
        selected (review_answer == "cafe")
        hover "cafe_mold_s"
        selected_idle "cafe_mold_s"          
        yalign cafe_yalign
        xalign cafe_xalign

    imagebutton:
        idle "mochila_mold_i"
        focus_mask None
        action SetVariable("review_answer","mochila"),Return()
        selected (review_answer == "mochila")
        hover "mochila_mold_s"
        selected_idle "mochila_mold_s"          
        yalign mochila_yalign
        xalign mochila_xalign        
        
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action SetVariable("proceed_flag",True), Return()        

label screen04:
#Initializing
    $ score = 0
    $ game2_answer_list = []
    $ max_riscos = 5
    $ erros = 0
    
# PAR LUVAS
    $ par_luvas_zoom = 0.6
    $ par_luvas_yalign = 0.8
    $ par_luvas_xalign = 0.05  
    image par_luvas: 
        "par_luvas.png"
        zoom par_luvas_zoom           
    image par_luvas_r: 
        "par_luvas_r.png"
        zoom par_luvas_zoom 
    image par_luvas_pro: 
        "par_luvas_pro.png"
        zoom par_luvas_zoom 
    image par_luvas_rpro: 
        "par_luvas_rpro.png"
        zoom par_luvas_zoom
    image par_luvas_mold_i: 
        "par_luvas_mold_i.png"
        zoom par_luvas_zoom
    image par_luvas_mold_s: 
        "par_luvas_mold_s.png"
        zoom par_luvas_zoom         
    $ par_luvas_var = True
    $ game2_answer_list.append ("par_luvas_var")
    $ game2_answer_list.append (par_luvas_var)    

# Frasco Acima
    $ frasco_acima_zoom = 1.10
    $ frasco_acima_yalign = 0.01
    $ frasco_acima_xalign = 0.65
    image frasco_acima: 
        "frasco_acima.png"
        zoom frasco_acima_zoom
    image frasco_acima_r: 
        "frasco_acima_r.png"
        zoom frasco_acima_zoom
    image frasco_acima_pro: 
        "frasco_acima_pro.png"
        zoom frasco_acima_zoom
    image frasco_acima_rpro: 
        "frasco_acima_rpro.png"
        zoom frasco_acima_zoom
    image frasco_acima_mold_i: 
        "frasco_acima_mold_i.png"
        zoom frasco_acima_zoom 
    image frasco_acima_mold_s: 
        "frasco_acima_mold_s.png"
        zoom frasco_acima_zoom         
    $ frasco_acima_var = True
    $ game2_answer_list.append ("frasco_acima_var")
    $ game2_answer_list.append (frasco_acima_var)
# LIVRO
       
    $ livro_zoom = 0.4 
    $ livro_yalign = 0.75
    $ livro_xalign = 0.15 
    image livro: 
        "livro.png"
        zoom livro_zoom             
    image livro_r: 
        "livro_r.png"
        zoom livro_zoom
    $ livro_var = True
    $ game2_answer_list.append ("livro_var")
    $ game2_answer_list.append (livro_var)    

# SEM LUVAS
    $ sem_luvas_zoom = 0.45   
    $ sem_luvas_yalign = 0.48
    $ sem_luvas_xalign = 0.15      
    image sem_luvas: 
        "sem_luvas.png"
        zoom sem_luvas_zoom    
    image sem_luvas_r: 
        "sem_luvas_r.png"
        zoom sem_luvas_zoom
    image sem_luvas_pro: 
        "sem_luvas_pro.png"
        zoom sem_luvas_zoom
    image sem_luvas_rpro: 
        "sem_luvas_rpro.png"
        zoom sem_luvas_zoom
    image sem_luvas_mold_i: 
        "sem_luvas_mold_i.png"
        zoom sem_luvas_zoom 
    image sem_luvas_mold_s: 
        "sem_luvas_mold_s.png"
        zoom sem_luvas_zoom 
    $ sem_luvas_var = True
    $ game2_answer_list.append ("sem_luvas_var")
    $ game2_answer_list.append (sem_luvas_var)        

#DR BROWN
    $ drbrown_zoom = 0.70  
    $ drbrown_yalign = 0.33
    $ drbrown_xalign = 0.55  
    image drbrown: 
        "drbrown.png"
        zoom drbrown_zoom    
    image drbrown_r:
        "drbrown_r.png"
        zoom drbrown_zoom
    $ drbrown_var = True
    $ game2_answer_list.append ("drbrown_var")   
    $ game2_answer_list.append (drbrown_var)

#LIVROS XICARA
    $ livros_xicara_zoom = 0.4   
    $ livros_xicara_yalign = 0.80
    $ livros_xicara_xalign = 0.3    
    image livros_xicara:
        "livros_xicara.png"
        zoom livros_xicara_zoom 
    image livros_xicara_r: 
        "livros_xicara_r.png"
        zoom livros_xicara_zoom
    image livros_xicara_pro:
        "livros_xicara_pro.png"
        zoom livros_xicara_zoom
    image livros_xicara_rpro:
        "livros_xicara_rpro.png"
        zoom livros_xicara_zoom
    image livros_xicara_mold_i: 
        "livros_xicara_mold_i.png"
        zoom livros_xicara_zoom 
    image livros_xicara_mold_s: 
        "livros_xicara_mold_s.png"
        zoom livros_xicara_zoom 
    $ livros_xicara_var = True
    $ game2_answer_list.append ("livros_xicara_var")
    $ game2_answer_list.append (livros_xicara_var)        
# EXPERIMENTO
    $ experimento_zoom = 0.28   
    $ experimento_yalign = 0.73
    $ experimento_xalign = 0.54      
    image experimento:
        "experimento.png"
        zoom experimento_zoom
    image experimento_r: 
        "experimento_r.png"
        zoom experimento_zoom
    $ experimento_var = True
    $ game2_answer_list.append ("experimento_var")
    $ game2_answer_list.append (experimento_var)        
#AGUA CHAO
    $ agua_chao_zoom = 0.8  
    $ agua_chao_yalign = 0.54
    $ agua_chao_xalign = 0.42   
    image agua_chao:
        "agua_chao.png"
        zoom agua_chao_zoom
    image agua_chao_r:
        "agua_chao_r.png"
        zoom agua_chao_zoom
    image agua_chao_pro:
        "agua_chao_pro.png"
        zoom agua_chao_zoom
    image agua_chao_rpro:
        "agua_chao_rpro.png"
        zoom agua_chao_zoom
    image agua_chao_mold_i: 
        "agua_chao_mold_i.png"
        zoom agua_chao_zoom 
    image agua_chao_mold_s: 
        "agua_chao_mold_s.png"
        zoom agua_chao_zoom 
    $ agua_chao_var = True
    $ game2_answer_list.append ("agua_chao_var")
    $ game2_answer_list.append (agua_chao_var)    
    
    call screen game2_hiddenobject04 with dissolve
    jump end_result_screen_4

screen game2_hiddenobject04:
    
    imagebutton:
        idle "agua_chao"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("agua_chao_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("agua_chao_var") + 1] == False)
        hover "agua_chao_r"
        selected_idle "agua_chao_r"  
        yalign agua_chao_yalign
        xalign agua_chao_xalign
    
   # $ frasco_acima_var = True
   # $ game2_answer_list.append (frasco_acima_var)
   # $ gabarito_list.append (False)
    imagebutton:
        idle "frasco_acima"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("frasco_acima_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("frasco_acima_var") + 1] == False)
        hover "frasco_acima_r"
        selected_idle "frasco_acima_r"        
        xalign frasco_acima_xalign
        yalign frasco_acima_yalign

   # $ drbrownvar = True
   # $ game2_answer_list.append (drbrownvar)
   # $ gabarito_list.append (True)
    imagebutton:
        idle "drbrown"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("drbrown_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("drbrown_var") + 1] == False)
        hover "drbrown_r"
        selected_idle "drbrown_r"        
        xalign drbrown_xalign
        yalign drbrown_yalign
    #$ index_counter = index_counter + 1
    
    imagebutton:
        idle "livros_xicara"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("livros_xicara_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("livros_xicara_var") + 1] == False)
        hover "livros_xicara_r"
        selected_idle "livros_xicara_r"          
        yalign livros_xicara_yalign
        xalign livros_xicara_xalign

    imagebutton:
        idle "sem_luvas"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("sem_luvas_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("sem_luvas_var") + 1] == False)
        hover "sem_luvas_r"
        selected_idle "sem_luvas_r"          
        yalign sem_luvas_yalign
        xalign sem_luvas_xalign

    imagebutton:
        idle "par_luvas"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("par_luvas_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("par_luvas_var") + 1] == False)
        hover "par_luvas_r"
        selected_idle "par_luvas_r"  
        yalign par_luvas_yalign
        xalign par_luvas_xalign       

    imagebutton:
        idle "experimento"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("experimento_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("experimento_var") + 1] == False)
        hover "experimento_r"
        selected_idle "experimento_r"  
        yalign experimento_yalign
        xalign experimento_xalign
    imagebutton:
        idle "livro"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("livro_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("livro_var") + 1] == False)
        hover "livro_r"
        selected_idle "livro_r"  
        yalign livro_yalign
        xalign livro_xalign    

    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action With(dissolve), Return()
        
label end_result_screen_4:
    $ score = 0
    $ game2_acertos = 0
    $ results_counter = 0
    while (results_counter < len(game2_answer_list)):
        if (game2_answer_list[results_counter] == "livro_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show livro_r:
                    yalign livro_yalign
                    xalign livro_xalign
            else:
                show livro:
                    yalign livro_yalign
                    xalign livro_xalign
        if (game2_answer_list[results_counter] == "experimento_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show experimento_r:
                    yalign experimento_yalign
                    xalign experimento_xalign
            else:
                show experimento:
                    yalign experimento_yalign
                    xalign experimento_xalign             
        if (game2_answer_list[results_counter] == "par_luvas_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show par_luvas_rpro:
                    yalign par_luvas_yalign
                    xalign par_luvas_xalign
            else:
                show par_luvas_pro:
                    yalign par_luvas_yalign
                    xalign par_luvas_xalign
        if (game2_answer_list[results_counter] == "sem_luvas_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show sem_luvas_rpro behind livro, livro_r:
                    yalign sem_luvas_yalign
                    xalign sem_luvas_xalign
            else:
                show sem_luvas_pro behind livro, livro_r:
                    yalign sem_luvas_yalign
                    xalign sem_luvas_xalign                
        if (game2_answer_list[results_counter] == "livros_xicara_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show livros_xicara_rpro:
                    yalign livros_xicara_yalign
                    xalign livros_xicara_xalign
            else:
                show livros_xicara_pro:
                    yalign livros_xicara_yalign
                    xalign livros_xicara_xalign
        if (game2_answer_list[results_counter] == "drbrown_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show drbrown_r:
                    yalign drbrown_yalign
                    xalign drbrown_xalign
            else:
                show drbrown:
                    yalign drbrown_yalign
                    xalign drbrown_xalign          
        if (game2_answer_list[results_counter] == "frasco_acima_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show frasco_acima_rpro:
                    yalign frasco_acima_yalign
                    xalign frasco_acima_xalign
            else:
                show frasco_acima_pro:
                    yalign frasco_acima_yalign
                    xalign frasco_acima_xalign
        if (game2_answer_list[results_counter] == "agua_chao_var"):
            hide agua_chao
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show agua_chao_rpro behind drbrown, drbrown_r:
                    yalign agua_chao_yalign
                    xalign agua_chao_xalign
            else:
                show agua_chao_pro behind drbrown, drbrown_r:
                    yalign agua_chao_yalign
                    xalign agua_chao_xalign             
        $ results_counter = results_counter + 1
    
    $ proceed_flag = False
    $ review_answer = "NONE"
    $ score_points = score * 15
    $ total_acertos = total_acertos + score
    $ total_riscos = total_riscos + max_riscos
    $ total_score = total_acertos + score_points
    if (erros == 0):
        "Você indentificou [score] de [max_riscos] riscos! Seu score final é [score_points]. Clique para continuar."
    if (erros > 0):
        "Você indentificou [score] de [max_riscos] riscos, porém [erros] items foram erroneamente marcados! Seu score final é [score_points]. Clique para continuar."
    while (proceed_flag == False):
        "Clique nos items que representam riscos para maiores informações. Senão clique no botão verde novamente para ir para o proximo nivel"
        call screen review_screens4 with dissolve
        if (review_answer == "agua_chao"):
            "Um derramamento está ocorrendo aqui! Ele deverá identificado e tratado!"
        if (review_answer == "frasco_acima"):
            "Este aluno está manipulando a vidraça de forma completamente indevida! A manipulção deve ser feita na mesa e em pleno campo de visão, evitando acidentes!"
        if (review_answer == "livros_xicara"):
            "Além do risco da má organização, há uma xicara de café equilibrada em cima, aumentando o risco!"
        if (review_answer == "sem_luvas"):
            "Esta aluna não está usando seu EPI devidamente, Observe a falta de luvas!"
        if (review_answer == "par_luvas"):
            "Este par de luvas foi descartado indevidamente, ele deve ser colocado no local de descarte apropriado, evitando contaminações"  
        $ review_answer = "NONE"
    jump telas_loop
    
screen review_screens4:

    imagebutton:
        idle "livros_xicara_mold_i"
        focus_mask None
        action SetVariable("review_answer","livros_xicara"),Return()
        selected (review_answer == "livros_xicara")
        hover "livros_xicara_mold_s"
        selected_idle "livros_xicara_mold_s"          
        yalign livros_xicara_yalign
        xalign livros_xicara_xalign

    imagebutton:
        idle "sem_luvas_mold_i"
        focus_mask None
        action SetVariable("review_answer","sem_luvas"),Return()
        selected (review_answer == "sem_luvas")
        hover "sem_luvas_mold_s"
        selected_idle "sem_luvas_mold_s"          
        yalign sem_luvas_yalign
        xalign sem_luvas_xalign

    imagebutton:
        idle "par_luvas_mold_i"
        focus_mask None
        action SetVariable("review_answer","par_luvas"),Return()
        selected (review_answer == "par_luvas")
        hover "par_luvas_mold_s"
        selected_idle "par_luvas_mold_s"  
        yalign par_luvas_yalign
        xalign par_luvas_xalign
        
    imagebutton:
        idle "frasco_acima_mold_i"
        focus_mask None
        action SetVariable("review_answer","frasco_acima"),Return()
        selected (review_answer == "frasco_acima")
        hover "frasco_acima_mold_s"
        selected_idle "frasco_acima_mold_s"  
        yalign frasco_acima_yalign
        xalign frasco_acima_xalign  
        
    imagebutton:
        idle "agua_chao_mold_i"
        focus_mask None
        action SetVariable("review_answer","agua_chao"),Return()
        selected (review_answer == "agua_chao")
        hover "agua_chao_mold_s"
        selected_idle "agua_chao_mold_s"  
        yalign agua_chao_yalign
        xalign agua_chao_xalign  
        
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action SetVariable("proceed_flag",True), Return()
    
label screen05:

    $ score = 0
    $ game2_answer_list = []
    $ max_riscos = 4
    $ erros = 0
#mulher_lixo
    $ mulher_lixo_zoom = 0.7
    $ mulher_lixo_yalign = -0.05
    $ mulher_lixo_xalign = 0.10
    image mulher_lixo:    
        "mulher_lixo.png"
        zoom mulher_lixo_zoom
    image mulher_lixo_r: 
        "mulher_lixo_r.png"
        zoom mulher_lixo_zoom
    $ mulher_lixo_var = True
    $ game2_answer_list.append ("mulher_lixo_var")
    $ game2_answer_list.append (mulher_lixo_var)
#hamburger
    $ hamburger_zoom = 0.3
    $ hamburger_yalign = 0.8
    $ hamburger_xalign = 0.05     
    image hamburger: 
        "hamburger.png"
        zoom hamburger_zoom
    image hamburger_r: 
        "hamburger_r.png"
        zoom hamburger_zoom
    image hamburger_pro: 
        "hamburger_pro.png"
        zoom hamburger_zoom
    image hamburger_rpro: 
        "hamburger_rpro.png"
        zoom hamburger_zoom
    image hamburger_mold_i: 
        "hamburger_mold_i.png"
        zoom hamburger_zoom
    image hamburger_mold_s: 
        "hamburger_mold_s.png"
        zoom hamburger_zoom        
    $ hamburger_var = True
    $ game2_answer_list.append ("hamburger_var")
    $ game2_answer_list.append (hamburger_var)
#rick
    $ rick_zoom = 0.9
    $ rick_xalign = 0.65
    $ rick_yalign = 0.01         
    image rick: 
        "rick.png"
        zoom rick_zoom
    image rick_r: 
        "rick_r.png"
        zoom rick_zoom
    $ rick_var = True
    $ game2_answer_list.append ("rick_var")
    $ game2_answer_list.append (rick_var)
#coposbecker
    $ coposbecker_zoom = 1.2
    $ coposbecker_yalign = 0.8
    $ coposbecker_xalign = 0.3        
    image coposbecker: 
        "coposbecker.png"
        zoom coposbecker_zoom
    image coposbecker_r: 
        "coposbecker_r.png"
        zoom coposbecker_zoom
    $ coposbecker_var = True
    $ game2_answer_list.append ("coposbecker_var")
    $ game2_answer_list.append (coposbecker_var)
#lixeira2
    $ lixeira2_zoom = 0.35
    $ lixeira2_yalign = 0.37
    $ lixeira2_xalign = 0.22       
    image lixeira2: 
        "lixeira.png"
        zoom lixeira2_zoom
    image lixeira2_r: 
        "lixeira_r.png"
        zoom lixeira2_zoom
    $ lixeira2_var = True
    $ game2_answer_list.append ("lixeira2_var")
    $ game2_answer_list.append (lixeira2_var)        
#cara_dois_copos
    $ cara_dois_copos_zoom = 0.8
    $ cara_dois_copos_xalign = 0.34
    $ cara_dois_copos_yalign = 0.35        
    image cara_dois_copos: 
        "cara_dois_copos.png"
        zoom cara_dois_copos_zoom
    image cara_dois_copos_r: 
        "cara_dois_copos_r.png"
        zoom cara_dois_copos_zoom
    $ cara_dois_copos_var = True
    $ game2_answer_list.append ("cara_dois_copos_var")
    $ game2_answer_list.append (cara_dois_copos_var)
#vidro_amarelo
    $ vidro_amarelo_zoom = 0.3
    $ vidro_amarelo_yalign = 0.78
    $ vidro_amarelo_xalign = 0.49        
    image vidro_amarelo:
        "vidro_amarelo.png"
        zoom vidro_amarelo_zoom
    image vidro_amarelo_r: 
        "vidro_amarelo_r.png"
        zoom vidro_amarelo_zoom
    $ vidro_amarelo_var = True
    $ game2_answer_list.append ("vidro_amarelo_var")
    $ game2_answer_list.append (vidro_amarelo_var)        
#porta_ensaio
    $ porta_ensaio_zoom = 1.20
    $ porta_ensaio_yalign = 0.75
    $ porta_ensaio_xalign = 0.59         
    image porta_ensaio:
        "porta_ensaio.png"
        zoom porta_ensaio_zoom
    image porta_ensaio_r: 
        "porta_ensaio_r.png"
        zoom porta_ensaio_zoom
    $ porta_ensaio_var = True
    $ game2_answer_list.append ("porta_ensaio_var")
    $ game2_answer_list.append (porta_ensaio_var)
#frasco_derramado
    $ frasco_derramado_zoom = 0.55
    $ frasco_derramado_xalign = 0.838
    $ frasco_derramado_yalign = 0.29        
    image frasco_derramado:
        "frasco_derramado.png"
        zoom frasco_derramado_zoom
    image frasco_derramado_r: 
        "frasco_derramado_r.png"
        zoom frasco_derramado_zoom
    image frasco_derramado_pro: 
        "frasco_derramado_pro.png"
        zoom frasco_derramado_zoom
    image frasco_derramado_rpro: 
        "frasco_derramado_rpro.png"
        zoom frasco_derramado_zoom
    image frasco_derramado_mold_i: 
        "frasco_derramado_mold_i.png"
        zoom frasco_derramado_zoom
    image frasco_derramado_mold_s: 
        "frasco_derramado_mold_s.png"
        zoom frasco_derramado_zoom 
    $ frasco_derramado_var = True
    $ game2_answer_list.append ("frasco_derramado_var")
    $ game2_answer_list.append (frasco_derramado_var)
#livro2
    $ livro2_zoom = 0.48
    $ livro2_yalign = 0.75
    $ livro2_xalign = 0.42
    image livro2: 
        "livro.png"
        zoom livro2_zoom
    image livro2_r: 
        "livro_r.png"
        zoom livro2_zoom
    $ livro2_var = True
    $ game2_answer_list.append ("livro2_var")
    $ game2_answer_list.append (livro2_var)
#agua_mesa
    $ agua_mesa_yalign = 1.03
    $ agua_mesa_xalign = 0.15        
    image agua_mesa:
        "agua_mesa.png"
    image agua_mesa_r: 
        "agua_mesa_r.png"
    image agua_mesa_pro: 
        "agua_mesa_pro.png"
    image agua_mesa_rpro: 
        "agua_mesa_rpro.png"
    image agua_mesa_mold_i: 
        "agua_mesa_mold_i.png"
    image agua_mesa_mold_s: 
        "agua_mesa_mold_s.png"        
    $ agua_mesa_var = True
    $ game2_answer_list.append ("agua_mesa_var")
    $ game2_answer_list.append (agua_mesa_var)
#garrafa_quebrada2
    $ garrafa_quebrada2_zoom = 0.5
    $ garrafa_quebrada2_yalign = 0.82
    $ garrafa_quebrada2_xalign = 0.19        
    image garrafa_quebrada2:
        "garrafa_quebrada2.png"
        zoom garrafa_quebrada2_zoom
    image garrafa_quebrada2_r: 
        "garrafa_quebrada2_r.png"
        zoom garrafa_quebrada2_zoom
    image garrafa_quebrada2_pro: 
        "garrafa_quebrada2_pro.png"
        zoom garrafa_quebrada2_zoom
    image garrafa_quebrada2_rpro: 
        "garrafa_quebrada2_rpro.png"
        zoom garrafa_quebrada2_zoom
    image garrafa_quebrada2_mold_i: 
        "garrafa_quebrada2_mold_i.png"
        zoom garrafa_quebrada2_zoom
    image garrafa_quebrada2_mold_s: 
        "garrafa_quebrada2_mold_s.png"
        zoom garrafa_quebrada2_zoom        
    $ garrafa_quebrada2_var = True
    $ game2_answer_list.append ("garrafa_quebrada2_var")
    $ game2_answer_list.append (garrafa_quebrada2_var)

    call screen game2_hiddenobject05 with dissolve
    jump end_result_screen_5
    
screen game2_hiddenobject05:
    imagebutton:
        idle "frasco_derramado"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("frasco_derramado_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("frasco_derramado_var") + 1] == False)
        hover "frasco_derramado_r"
        selected_idle "frasco_derramado_r" 
        xalign frasco_derramado_xalign
        yalign frasco_derramado_yalign
    
    imagebutton:
        idle "mulher_lixo"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("mulher_lixo_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("mulher_lixo_var") + 1] == False)
        hover "mulher_lixo_r"
        selected_idle "mulher_lixo_r"
        yalign mulher_lixo_yalign
        xalign mulher_lixo_xalign

    imagebutton:
        idle "rick"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("rick_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("rick_var") + 1] == False)
        hover "rick_r"
        selected_idle "rick_r" 
        xalign rick_xalign
        yalign rick_yalign

    imagebutton:
        idle "cara_dois_copos"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("cara_dois_copos_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("cara_dois_copos_var") + 1] == False)
        hover "cara_dois_copos_r"
        selected_idle "cara_dois_copos_r" 
        xalign cara_dois_copos_xalign
        yalign cara_dois_copos_yalign
        
    imagebutton:
        idle "agua_mesa"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("agua_mesa_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("agua_mesa_var") + 1] == False)
        hover "agua_mesa_r"
        selected_idle "agua_mesa_r" 
        yalign agua_mesa_yalign
        xalign agua_mesa_xalign 

    imagebutton:
        idle "garrafa_quebrada2"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("garrafa_quebrada2_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("garrafa_quebrada2_var") + 1] == False)
        hover "garrafa_quebrada2_r"
        selected_idle "garrafa_quebrada2_r" 
        yalign garrafa_quebrada2_yalign
        xalign garrafa_quebrada2_xalign

    imagebutton:
        idle "lixeira2"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("lixeira2_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("lixeira2_var") + 1] == False)
        hover "lixeira2_r"
        selected_idle "lixeira2_r" 
        yalign lixeira2_yalign
        xalign lixeira2_xalign

    imagebutton:
        idle "hamburger"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("hamburger_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("hamburger_var") + 1] == False)
        hover "hamburger_r"
        selected_idle "hamburger_r" 
        yalign hamburger_yalign
        xalign hamburger_xalign

    imagebutton:
        idle "porta_ensaio"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("porta_ensaio_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("porta_ensaio_var") + 1] == False)
        hover "porta_ensaio_r"
        selected_idle "porta_ensaio_r" 
        yalign porta_ensaio_yalign
        xalign porta_ensaio_xalign
    imagebutton:
        idle "coposbecker"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("coposbecker_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("coposbecker_var") + 1] == False)
        hover "coposbecker_r"
        selected_idle "coposbecker_r" 
        yalign coposbecker_yalign
        xalign coposbecker_xalign

    imagebutton:
        idle "livro2"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("livro2_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("livro2_var") + 1] == False)
        hover "livro2_r"
        selected_idle "livro2_r" 
        yalign livro2_yalign
        xalign livro2_xalign
    imagebutton:
        idle "vidro_amarelo"
        focus_mask True
        action ToggleDict(game2_answer_list, game2_answer_list.index("vidro_amarelo_var") + 1)
        selected (game2_answer_list[game2_answer_list.index("vidro_amarelo_var") + 1] == False)
        hover "vidro_amarelo_r"
        selected_idle "vidro_amarelo_r" 
        yalign vidro_amarelo_yalign
        xalign vidro_amarelo_xalign
        
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action With(dissolve), Return()
        

label end_result_screen_5:
    $ score = 0
    $ game2_acertos = 0
    $ results_counter = 0
    while (results_counter < len(game2_answer_list)):
        if (game2_answer_list[results_counter] == "mulher_lixo_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show mulher_lixo_r:
                    yalign mulher_lixo_yalign
                    xalign mulher_lixo_xalign
            else:
                show mulher_lixo:
                    yalign mulher_lixo_yalign
                    xalign mulher_lixo_xalign
        if (game2_answer_list[results_counter] == "rick_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show rick_r:
                    yalign rick_yalign
                    xalign rick_xalign
            else:
                show rick:
                    yalign rick_yalign
                    xalign rick_xalign             
        if (game2_answer_list[results_counter] == "hamburger_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show hamburger_rpro:
                    yalign hamburger_yalign
                    xalign hamburger_xalign
            else:
                show hamburger_pro:
                    yalign hamburger_yalign
                    xalign hamburger_xalign
        if (game2_answer_list[results_counter] == "lixeira2_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show lixeira2_r:
                    yalign lixeira2_yalign
                    xalign lixeira2_xalign
            else:
                show lixeira2:
                    yalign lixeira2_yalign
                    xalign lixeira2_xalign                
        if (game2_answer_list[results_counter] == "cara_dois_copos_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show cara_dois_copos_r:
                    yalign cara_dois_copos_yalign
                    xalign cara_dois_copos_xalign
            else:
                show cara_dois_copos:
                    yalign cara_dois_copos_yalign
                    xalign cara_dois_copos_xalign
        if (game2_answer_list[results_counter] == "coposbecker_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show coposbecker_r:
                    yalign coposbecker_yalign
                    xalign coposbecker_xalign
            else:
                show coposbecker:
                    yalign coposbecker_yalign
                    xalign coposbecker_xalign          
        if (game2_answer_list[results_counter] == "vidro_amarelo_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show vidro_amarelo_r:
                    yalign vidro_amarelo_yalign
                    xalign vidro_amarelo_xalign
            else:
                show vidro_amarelo:
                    yalign vidro_amarelo_yalign
                    xalign vidro_amarelo_xalign
        if (game2_answer_list[results_counter] == "porta_ensaio_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show porta_ensaio_r:
                    yalign porta_ensaio_yalign
                    xalign porta_ensaio_xalign
            else:
                show porta_ensaio:
                    yalign porta_ensaio_yalign
                    xalign porta_ensaio_xalign
        if (game2_answer_list[results_counter] == "livro2_var"):
            if (game2_answer_list[results_counter + 1] == False):
                $ erros = erros + 1
                show livro2_r behind vidro_amarelo:
                    yalign livro2_yalign
                    xalign livro2_xalign
            else:
                show livro2 behind vidro_amarelo:
                    yalign livro2_yalign
                    xalign livro2_xalign
        if (game2_answer_list[results_counter] == "frasco_derramado_var"):
            hide agua_chao
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show frasco_derramado_rpro:
                    yalign frasco_derramado_yalign
                    xalign frasco_derramado_xalign
            else:
                show frasco_derramado_pro:
                    yalign frasco_derramado_yalign
                    xalign frasco_derramado_xalign
        if (game2_answer_list[results_counter] == "agua_mesa_var"):
            hide agua_chao
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show agua_mesa_rpro:
                    yalign agua_mesa_yalign
                    xalign agua_mesa_xalign
                    
            else:
                show agua_mesa_pro:
                    yalign agua_mesa_yalign
                    xalign agua_mesa_xalign
                    
        if (game2_answer_list[results_counter] == "garrafa_quebrada2_var"):
            hide agua_chao
            if (game2_answer_list[results_counter + 1] == False):
                $ score = score + 1
                show garrafa_quebrada2_rpro:
                    yalign garrafa_quebrada2_yalign
                    xalign garrafa_quebrada2_xalign
            else:
                show garrafa_quebrada2_pro:
                    yalign garrafa_quebrada2_yalign
                    xalign garrafa_quebrada2_xalign
        $ results_counter = results_counter + 1
    
    $ proceed_flag = False
    $ review_answer = "NONE"
    $ score_points = score * 15
    $ total_acertos = total_acertos + score
    $ total_riscos = total_riscos + max_riscos
    $ total_score = total_acertos + score_points
    if (erros == 0):
        "Você indentificou [score] de [max_riscos] riscos! Seu score final é [score_points]. Clique para continuar."
    if (erros > 0):
        "Você indentificou [score] de [max_riscos] riscos, porém [erros] items foram erroneamente marcados! Seu score final é [score_points]. Clique para continuar."
    while (proceed_flag == False):
        "Clique nos items que representam riscos para maiores informações. Senão clique no botão verde novamente para ir para o proximo nivel"
        call screen review_screens5 with dissolve
        if (review_answer == "hamburger"):
            "Alimentos e bebidas na mesa de manipulação é uma alto risco para qualquer pessoa que os ingerir, evite se alimentar no ambiente laboratorial!"
        if (review_answer == "frasco_derramado"):
            "Ocorreu um derramamento na capela, ele deve ser tratado devidamente, com atenção ao seu possivel risco durante esse tratamento!"
        if (review_answer == "agua_mesa"):
            "Esta agua escorreu pela mesa, uma limpeza devida é necessaria!"
        if (review_answer == "garrafa_quebrada2"):
            "Esta vidraça quebrada deve ser devidamente removida da mesa de manipulação!"
        $ review_answer = "NONE"
    jump telas_loop
    
screen review_screens5:

    imagebutton:
        idle "hamburger_mold_i"
        focus_mask None
        action SetVariable("review_answer","hamburger"),Return()
        selected (review_answer == "hamburger")
        hover "hamburger_mold_s"
        selected_idle "hamburger_mold_s"          
        yalign hamburger_yalign
        xalign hamburger_xalign

    imagebutton:
        idle "agua_mesa_mold_i"
        focus_mask None
        action SetVariable("review_answer","agua_mesa"),Return()
        selected (review_answer == "agua_mesa")
        hover "agua_mesa_mold_s"
        selected_idle "agua_mesa_mold_s"          
        yalign agua_mesa_yalign
        xalign agua_mesa_xalign        

    imagebutton:
        idle "garrafa_quebrada2_mold_i"
        focus_mask None
        action SetVariable("review_answer","garrafa_quebrada2"),Return()
        selected (review_answer == "garrafa_quebrada2")
        hover "garrafa_quebrada2_mold_s"
        selected_idle "garrafa_quebrada2_mold_s"          
        yalign garrafa_quebrada2_yalign
        xalign garrafa_quebrada2_xalign

    imagebutton:
        idle "frasco_derramado_mold_i"
        focus_mask None
        action SetVariable("review_answer","frasco_derramado"),Return()
        selected (review_answer == "frasco_derramado")
        hover "frasco_derramado_mold_s"
        selected_idle "frasco_derramado_mold_s"          
        yalign frasco_derramado_yalign
        xalign frasco_derramado_xalign
        
    image "frame":
        xalign frame_xalign
        yalign frame_yalign
    
    imagebutton:
        idle "b1"
        hover "b2"
        xalign b1_xalign
        yalign b1_yalign
        action SetVariable("proceed_flag",True), Return()
            
#label generate_scene_loop:
#    if not personagem_count == 0:
#        $ random_jump_target = random.choice(personagem_list)
#        $ personagem_list.remove(random_jump_target)
#        $ chosen_list.append(random_jump_target)
#        $ personagem_count = personagem_count - 1
#        $ nrquestoes = nrquestoes + 1
#        $ renpy.call(random_jump_target)
    #menu:
    #    "Continuar":
    #        hide screen countdown
     #       jump menu1_end
            

#jump menu1_end

screen game2_checkboxscreen():
    imagemap:
       ground "z2.png" xalign 0.5 yalign 0.5
    vpgrid:
        area (98, 516, 1726, 461)
        align (-0.5, 0.5)
        cols 2
        spacing 5
        draggable True
        mousewheel True
        ysize 1000
        xsize 1000

        #scrollbars "vertical"
        #side_xalign 0.5
        for i in range(1, 5):
            vbox:
                
                #spacing 15
                anchor (0.5, 0.5)
                align (0.5, 0.5)
                if i ==1:
                    button:
                        style "checkbox_button"
                        action ToggleVariable("option1")
                    text "[text_list[0]]" xpos 55 ypos -40
                if i ==2:
                    button:
                        style "checkbox_button"
                        action ToggleVariable("option2")
                    text "[text_list[1]]" xpos 55 ypos -40    
                if i ==3:
                    button:
                        style "checkbox_button"
                        action ToggleVariable("option3")
                    text "[text_list[2]]" xpos 55 ypos -40    
                if i ==4:
                    button:
                        style "checkbox_button"
                        action ToggleVariable("option4")  
                    text "[text_list[3]]" xpos 55 ypos -40    
    button:
        align (0.5, 0.5)
        xpos 0.5 ypos 0.5
        textbutton "Confirmar Respostas" action Return()
    
label boneco01:
    show boneco01:
        zoom 0.4
        xalign 0.5 yalign 0.5
    jump generate_scene_loop
label boneco02:
    show boneco02:
        zoom 0.4
        xalign 0.7 yalign 0.5
    jump generate_scene_loop
label boneco03:
    show boneco03:
        zoom 0.4
        xalign 0.2 yalign 0.5
    jump generate_scene_loop
label boneco04:
    show boneco04:
        zoom 0.4
        xalign 0.1 yalign 0.5
    jump generate_scene_loop
label boneco05:
    show boneco05:
        zoom 0.4
        xalign 0.3 yalign 0.5
    jump generate_scene_loop
label boneco06:
    show boneco06:
        zoom 0.4
        xalign 0.8 yalign 0.5
    jump generate_scene_loop   

label timer_fim:
    hide instru
    hide erros
    "Agora informe os procedimentos e erros encontrados"
    
label menu1_end:
    hide instru
    hide erros
    hide boneco01
    hide boneco02
    hide boneco03
    hide boneco04
    hide boneco05
    hide boneco06
    
    python:
        for items, list in enumerate(chosen_list):
            for a_tuple, tuple in enumerate(question_list):
                current_tuple = question_list[a_tuple]
                if chosen_list[items] == current_tuple[0]:
                    text_list.append(current_tuple[1])
                    answer_list.append(current_tuple[2])
    call screen game2_checkboxscreen
    if option1 == answer_list[0]:
        $ score = score + 1
    if option2 == answer_list[1]:
        $ score = score + 1
    if option3 == answer_list[2]:
        $ score = score + 1
    if option4 == answer_list[3]:
        $ score = score + 1  
    "Você acertou [score] de [nrquestoes] questões e seu score final é [score]. Clique para continuar."
    $ MainMenu(confirm=False)()
    # This ends the game.
