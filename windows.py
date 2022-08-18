import dearpygui.dearpygui as dpg

storyboard_count = 0

def storyboard(parent):
    global storyboard_count

    with dpg.tab(parent=parent, label=f"story {storyboard_count}", closable=True):
        dpg.add_node_editor()
        storyboard_count += 1
