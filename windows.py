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

    with dpg.node(parent=editor, label="title") as node:
        hand = str(int(random() * 100))
        text = str(int(random() * 100))

        with dpg.node_attribute():
            print(node)
            txt = dpg.add_node_attribute(multiline=True, width=dpg.get_item_width(node), height=dpg.get_item_height(node), tag=text)

            def resizer():
                dpg.set_item_height(txt, dpg.get_item_height(node))
                dpg.set_item_width(txt, dpg.get_item_width(node))


            with dpg.item_handler_registry(hand):
                dpg.add_item_resize_handler(callback=resizer)

            #bind the thingy
            dpg.bind_item_handler_registry(item=text, handler_registry=hand)

def _set_current_active_storyboard(board):
    global current_storyboard
    current_storyboard = board
    pass

