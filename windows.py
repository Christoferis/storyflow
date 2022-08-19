import dearpygui.dearpygui as dpg

storyboard_count = 0
current_storyboard = 33

def storyboard(parent):
    global storyboard_count

    with dpg.tab(parent=parent, label=f"story {storyboard_count}", closable=True):
        dpg.add_node_editor()
        storyboard_count += 1


def create_standard_node():
    global current_storyboard
    editor = dpg.get_item_children(current_storyboard)[1][0]

    print(editor)
    dpg.add_node(parent=editor)


def _set_current_active_storyboard(board):
    global current_storyboard
    current_storyboard = board
    pass
