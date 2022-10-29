import dearpygui.dearpygui as dpg
from random import random

storyboard_count = 0
current_storyboard = 35

def storyboard(parent):
    global storyboard_count

    with dpg.tab(parent=parent, label=f"story {storyboard_count}", closable=True) as t:
        dpg.add_node_editor()
        storyboard_count += 1
    
    return t

def create_standard_node():
    global current_storyboard
    editor = dpg.get_item_children(current_storyboard)[1][0]

    with dpg.node(parent=editor, label="Node 1"):        
        hand = str(int(random() * 100))
        text = str(int(random() * 100))

        with dpg.node_attribute(label="Node A1"):
            dpg.add_input_text(width=150, height=600)


def _set_current_active_storyboard(board):
    #rework as the thing keeps crashing at first startup -> try to remove this context thingy
    global current_storyboard
    current_storyboard = board
    pass

