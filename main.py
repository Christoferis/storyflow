#storyflow a program to organize a dm quest or a choose your own adventure type story

import sys
import dearpygui.dearpygui as dpg
from windows import storyboard


#main loop
def main():
    #add viewport
    dpg.create_context()
    main_vp = dpg.create_viewport(title="storyflow")
    dpg.show_viewport()
    dpg.setup_dearpygui()


    #window that contains tabs
    with dpg.window() as stories:

        with dpg.table(header_row=False, borders_innerV=True, resizable=True) as ui:

            dpg.add_table_column(width_stretch=True, init_width_or_weight=0.25)
            dpg.add_table_column(width_stretch=True)

            with dpg.table_row():
                with dpg.tab_bar() as nodes:
                    with dpg.tab(label="Favorites"):
                        dpg.add_text("hey")
                        pass
                    
                    with dpg.tab(label="Nodes"):
                        dpg.add_text("hallo")
                        pass

                #main Tab
                with dpg.tab_bar() as storyboards:
                    dpg.add_tab_button(label="+", callback=lambda: storyboard(storyboards))
                    storyboard(storyboards)

                pass
        pass

    dpg.set_primary_window(window=stories, value=True)

    dpg.show_imgui_demo()

    dpg.start_dearpygui()
    dpg.destroy_context()

    sys.exit()
    pass


main()