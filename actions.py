import tkinter as tk
from tkinter import ttk
from typing import Text

class Actions(ttk.Frame):
    def __init__(self, parent, canvas, properties, *args, **kwargs):
        ttk.Frame.__init__(self, parent , *args, **kwargs)
        self.parent_frame = parent
        self.my_canvas = canvas
        self.properties = properties

        self.tabControl = ttk.Notebook(self.parent_frame, height = 360)

        self.web_tab = ttk.Frame(self.tabControl)
        self.window_tab = ttk.Frame(self.tabControl)
        self.excel_tab = ttk.Frame(self.tabControl)
        self.control_tab = ttk.Frame(self.tabControl)
        self.variable_tab = ttk.Notebook(self.tabControl)
        self.more_tab = ttk.Frame(self.tabControl)

        self.variable_string = ttk.Frame(self.variable_tab)
        self.variable_list = ttk.Frame(self.variable_tab)
        self.variable_dict = ttk.Frame(self.variable_tab)
        self.variable_boolean = ttk.Frame(self.variable_tab)
        self.variable_number = ttk.Frame(self.variable_tab)
        self.variable_any = ttk.Frame(self.variable_tab)

        self.tabControl.add(self.web_tab, text="Web")
        self.tabControl.add(self.window_tab, text="Window")
        self.tabControl.add(self.excel_tab, text="Excel")
        self.tabControl.add(self.control_tab, text="Control")
        self.tabControl.add(self.variable_tab, text="Variables")
        self.tabControl.add(self.more_tab, text="More")
        self.tabControl.pack(expand = 1, fill = tk.BOTH)

        self.variable_tab.add(self.variable_string, text="String")
        self.variable_tab.add(self.variable_number, text="Number")
        self.variable_tab.add(self.variable_boolean, text="Boolean")
        self.variable_tab.add(self.variable_list, text="List")
        self.variable_tab.add(self.variable_dict, text="Dictionary")
        self.variable_tab.add(self.variable_any, text="Any")

        #Actions for excel automation

        btn_create_workbook = tk.Button(self.excel_tab, text="Create Workbook", command=lambda : self.my_canvas.create_card('Create Workbook', 'excel'))
        btn_create_workbook.pack(anchor = 'nw')

        btn_open_workbook = tk.Button(self.excel_tab, text="Open Workbook", command=lambda : self.my_canvas.create_card('Open Workbook', 'excel'))
        btn_open_workbook.pack(anchor = 'nw')

        btn_delete_workbook = tk.Button(self.excel_tab, text="Delete Workbook", command=lambda : self.my_canvas.create_card('Delete Workbook', 'excel'))
        btn_delete_workbook.pack(anchor = 'nw')

        btn_create_worksheet = tk.Button(self.excel_tab, text="Create Worksheet", command=lambda : self.my_canvas.create_card('Create Worksheet', 'excel'))
        btn_create_worksheet.pack(anchor = 'nw')

        btn_delete_worksheet = tk.Button(self.excel_tab, text="Delete Worksheet", command=lambda : self.my_canvas.create_card('Delete Worksheet', 'excel'))
        btn_delete_worksheet.pack(anchor = 'nw')

        btn_save_workbook = tk.Button(self.excel_tab, text="Save Workbook", command=lambda : self.my_canvas.create_card('Save Workbook', 'excel'))
        btn_save_workbook.pack(anchor = 'nw')

        btn_set_cell_value = tk.Button(self.excel_tab, text="Set Value", command=lambda : self.my_canvas.create_card('Set Value', 'excel'))
        btn_set_cell_value.pack(anchor = 'nw')

        btn_get_cell_value = tk.Button(self.excel_tab, text="Get Value", command=lambda : self.my_canvas.create_card('Get Value', 'excel'))
        btn_get_cell_value.pack(anchor = 'nw')

        btn_set_cell_formula = tk.Button(self.excel_tab, text="Set Formula", command=lambda : self.my_canvas.create_card('Set Formula', 'excel'))
        btn_set_cell_formula.pack(anchor = 'nw')

        btn_merge_unmerge = tk.Button(self.excel_tab, text="Merge/Unmerge", command=lambda : self.my_canvas.create_card('Merge Unmerge', 'excel'))
        btn_merge_unmerge.pack(anchor = 'nw')

        btn_copy_paste = tk.Button(self.excel_tab, text="Copy Paste", command=lambda : self.my_canvas.create_card('Copy Paste', 'excel'))
        btn_copy_paste.pack(anchor = 'nw')

        btn_select_cell = tk.Button(self.excel_tab, text="Select Cell/Row/Column", command=lambda : self.my_canvas.create_card('Select Cell/Row/Column', 'excel'))
        btn_select_cell.pack(anchor = 'nw')

        btn_delete_cell = tk.Button(self.excel_tab, text="Delete Cell/Row/Column", command=lambda : self.my_canvas.create_card('Delete Cell/Row/Column', 'excel'))
        btn_delete_cell.pack(anchor = 'nw')

        btn_read_cell = tk.Button(self.excel_tab, text="Hide Cell/Row/Column", command=lambda : self.my_canvas.create_card('Read Cell/Row/Column', 'excel'))
        btn_read_cell.pack(anchor = 'nw')

        btn_find_cell = tk.Button(self.excel_tab, text="Find", command=lambda : self.my_canvas.create_card('Find', 'excel'))
        btn_find_cell.pack(anchor = 'nw')


        #Actions for Web automation
        btn_open_web = tk.Button(self.web_tab, text="Open URL", command= lambda : self.my_canvas.create_card('Open URL', 'web'))
        btn_open_web.pack(anchor = 'nw')

        btn_close_browser = tk.Button(self.web_tab, text="Close Browser", command= lambda : self.my_canvas.create_card('Close Browser', 'web'))
        btn_close_browser.pack(anchor = 'nw')

        btn_click_web = tk.Button(self.web_tab, text="Click", command=lambda : self.my_canvas.create_card('Click', 'web'))
        btn_click_web.pack(anchor = 'nw')

        btn_input_text_web = tk.Button(self.web_tab, text="Input Text", command=lambda : self.my_canvas.create_card('Input Text', 'web'))
        btn_input_text_web.pack(anchor = 'nw')

        btn_input_text_web = tk.Button(self.web_tab, text="Read Text", command=lambda : self.my_canvas.create_card('Read Text', 'web'))
        btn_input_text_web.pack(anchor = 'nw')

        btn_clear_web = tk.Button(self.web_tab, text="Clear", command=lambda : self.my_canvas.create_card('Clear', 'web'))
        btn_clear_web.pack(anchor = 'nw')

        btn_select_web = tk.Button(self.web_tab, text="Select", command=lambda : self.my_canvas.create_card('Select Option', 'web'))
        btn_select_web.pack(anchor = 'nw')

        btn_switch_to_web = tk.Button(self.web_tab, text="Switch To", command=lambda : self.my_canvas.create_card('Switch To', 'web'))
        btn_switch_to_web.pack(anchor = 'nw')

        btn_navigation_web = tk.Button(self.web_tab, text="Navigation", command=lambda : self.my_canvas.create_card('Navigation', 'web'))
        btn_navigation_web.pack(anchor = 'nw')

        btn_get_element_web = tk.Button(self.web_tab, text="Get Element", command=lambda : self.my_canvas.create_card('Get Element', 'web'))
        btn_get_element_web.pack(anchor = 'nw')

        btn_get_elements_web = tk.Button(self.web_tab, text="Get Elements", command=lambda : self.my_canvas.create_card('Get Elements', 'web'))
        btn_get_elements_web.pack(anchor = 'nw')

        btn_dragdrop_web = tk.Button(self.web_tab, text="Drag and Drop", command=lambda : self.my_canvas.create_card('Drag And Drop', 'web'))
        btn_dragdrop_web.pack(anchor = 'nw')

        #Actions for Desktop automation
        btn_open_desktop = tk.Button(self.window_tab, text="Open Application", command= lambda : self.my_canvas.create_card('Open Application', 'desktop'))
        btn_open_desktop.pack(anchor = 'nw')

        btn_close_application = tk.Button(self.window_tab, text="Close Application", command= lambda : self.my_canvas.create_card('Close Application', 'desktop'))
        btn_close_application.pack(anchor = 'nw')

        btn_click_desktop = tk.Button(self.window_tab, text="Click", command=lambda : self.my_canvas.create_card('Click', 'desktop'))
        btn_click_desktop.pack(anchor = 'nw')

        btn_input_text_desktop = tk.Button(self.window_tab, text="Enter", command=lambda : self.my_canvas.create_card('Input Text', 'desktop'))
        btn_input_text_desktop.pack(anchor = 'nw')

        btn_input_text_desktop = tk.Button(self.window_tab, text="Read", command=lambda : self.my_canvas.create_card('Read Text', 'desktop'))
        btn_input_text_desktop.pack(anchor = 'nw')

        btn_clear_desktop = tk.Button(self.window_tab, text="Clear", command=lambda : self.my_canvas.create_card('Clear', 'desktop'))
        btn_clear_desktop.pack(anchor = 'nw')

        btn_select_desktop = tk.Button(self.window_tab, text="Select", command=lambda : self.my_canvas.create_card('Select Option', 'desktop'))
        btn_select_desktop.pack(anchor = 'nw')

        btn_navigation_desktop = tk.Button(self.window_tab, text="Navigation", command=lambda : self.my_canvas.create_card('Navigation', 'desktop'))
        btn_navigation_desktop.pack(anchor = 'nw')

        btn_dragdrop_desktop = tk.Button(self.window_tab, text="Drag and Drop", command=lambda : self.my_canvas.create_card('Drag And Drop', 'desktop'))
        btn_dragdrop_desktop.pack(anchor = 'nw')

        btn_switch_to_desktop = tk.Button(self.window_tab, text="Switch To", command=lambda : self.my_canvas.create_card('Switch To', 'desktop'))
        btn_switch_to_desktop.pack(anchor = 'nw')


        #Actions for Control automation
        btn_for_loop_ctl = tk.Button(self.control_tab, text="For Loop", command=lambda : self.my_canvas.create_card('For Loop', 'control'))
        btn_for_loop_ctl.pack(anchor = 'nw')

        btn_while_loop_ctl = tk.Button(self.control_tab, text="While Loop", command=lambda : self.my_canvas.create_card('While Loop', 'control'))
        btn_while_loop_ctl.pack(anchor = 'nw')

        btn_for_each_ctl = tk.Button(self.control_tab, text="For Each", command=lambda : self.my_canvas.create_card('For Each', 'control'))
        btn_for_each_ctl.pack(anchor = 'nw')

        btn_if_ctl = tk.Button(self.control_tab, text="If", command=lambda : self.my_canvas.create_card('Tf', 'control'))
        btn_if_ctl.pack(anchor = 'nw')

        btn_if_else_ctl = tk.Button(self.control_tab, text="If Else", command=lambda : self.my_canvas.create_card('If Else', 'control'))
        btn_if_else_ctl.pack(anchor = 'nw')

        btn_else_ctl = tk.Button(self.control_tab, text="Else", command=lambda : self.my_canvas.create_card('Else', 'control'))
        btn_else_ctl.pack(anchor = 'nw')

        btn_break_ctl = tk.Button(self.control_tab, text="Break", command=lambda : self.my_canvas.create_card('Break', 'control'))
        btn_break_ctl.pack(anchor = 'nw')

        btn_continue_ctl = tk.Button(self.control_tab, text="Continue", command=lambda : self.my_canvas.create_card('Continue', 'control'))
        btn_continue_ctl.pack(anchor = 'nw')

        btn_wait_ctl = tk.Button(self.control_tab, text="Wait", command=lambda : self.my_canvas.create_card('Wait', 'control'))
        btn_wait_ctl.pack(anchor = 'nw')

        btn_delay_ctl = tk.Button(self.control_tab, text="Delay", command=lambda : self.my_canvas.create_card('Delay', 'control'))
        btn_delay_ctl.pack(anchor = 'nw')

        #Actions for More automation
        btn_keystroke_more = tk.Button(self.more_tab, text="Key Stroke", command=lambda : self.my_canvas.create_card('Key Stroke', 'more'))
        btn_keystroke_more.pack(anchor = 'nw')

        btn_messagebox_more = tk.Button(self.more_tab, text="Message Box", command=lambda : self.my_canvas.create_card('Message Box', 'more'))
        btn_messagebox_more.pack(anchor = 'nw')

        btn_leftclick_more = tk.Button(self.more_tab, text="Left Click", command=lambda : self.my_canvas.create_card('Left Click', 'more'))
        btn_leftclick_more.pack(anchor = 'nw')

        btn_rightclick_more = tk.Button(self.more_tab, text="Right Click", command=lambda : self.my_canvas.create_card('Right Click', 'more'))
        btn_rightclick_more.pack(anchor = 'nw')

        btn_scroll_more = tk.Button(self.more_tab, text="Scroll", command=lambda : self.my_canvas.create_card('Scroll', 'more'))
        btn_scroll_more.pack(anchor = 'nw')

        #Actions for More automation
        btn_create_dictionary = tk.Button(self.variable_dict, text="Create Dictionary", command=lambda : self.my_canvas.create_card('Create Dictionary', 'dictionary'))
        btn_create_dictionary.pack(anchor = 'nw')

        btn_assign_dict = tk.Button(self.variable_dict, text="Assign", command=lambda : self.my_canvas.create_card('Assign', 'dictionary'))
        btn_assign_dict.pack(anchor = 'nw')

        btn_get_dict = tk.Button(self.variable_dict, text="Get Value", command=lambda : self.my_canvas.create_card('Get Value', 'dictionary'))
        btn_get_dict.pack(anchor = 'nw')

        btn_items_dict = tk.Button(self.variable_dict, text="Get Items", command=lambda : self.my_canvas.create_card('Get Items', 'dictionary'))
        btn_items_dict.pack(anchor = 'nw')

        btn_keys_dict = tk.Button(self.variable_dict, text="Get Keys", command=lambda : self.my_canvas.create_card('Get Keys', 'dictionary'))
        btn_keys_dict.pack(anchor = 'nw')

        btn_values_dict = tk.Button(self.variable_dict, text="Get Values", command=lambda : self.my_canvas.create_card('Get Values', 'dictionary'))
        btn_values_dict.pack(anchor = 'nw')

        btn_clear_dict = tk.Button(self.variable_dict, text="Clear", command=lambda : self.my_canvas.create_card('Clear', 'dictionary'))
        btn_clear_dict.pack(anchor = 'nw')

        btn_pop_dict = tk.Button(self.variable_dict, text="Pop", command=lambda : self.my_canvas.create_card('Pop', 'dictionary'))
        btn_pop_dict.pack(anchor = 'nw')

        btn_update_dict = tk.Button(self.variable_dict, text="Update", command=lambda : self.my_canvas.create_card('Update', 'dictionary'))
        btn_update_dict.pack(anchor = 'nw')

        btn_copy_dict = tk.Button(self.variable_dict, text="Copy", command=lambda : self.my_canvas.create_card('Copy', 'dictionary'))
        btn_copy_dict.pack(anchor = 'nw')

        #Actions for More automation
        btn_create_list = tk.Button(self.variable_list, text="Create List", command=lambda : self.my_canvas.create_card('Create List', 'list'))
        btn_create_list.pack(anchor = 'nw')
        
        btn_assign_list = tk.Button(self.variable_list, text="Assign", command=lambda : self.my_canvas.create_card('Assign', 'list'))
        btn_assign_list.pack(anchor = 'nw')

        btn_get_list = tk.Button(self.variable_list, text="Get", command=lambda : self.my_canvas.create_card('Get Value', 'list'))
        btn_get_list.pack(anchor = 'nw')

        btn_length_list = tk.Button(self.variable_list, text="Length", command=lambda : self.my_canvas.create_card('Length', 'list'))
        btn_length_list.pack(anchor = 'nw')

        btn_append_list = tk.Button(self.variable_list, text="Append", command=lambda : self.my_canvas.create_card('Append', 'list'))
        btn_append_list.pack(anchor = 'nw')

        btn_extend_list = tk.Button(self.variable_list, text="Extend", command=lambda : self.my_canvas.create_card('Extend', 'list'))
        btn_extend_list.pack(anchor = 'nw')

        btn_remove_list = tk.Button(self.variable_list, text="Remove", command=lambda : self.my_canvas.create_card('Remove', 'list'))
        btn_remove_list.pack(anchor = 'nw')

        btn_pop_list = tk.Button(self.variable_list, text="Pop", command=lambda : self.my_canvas.create_card('Pop', 'list'))
        btn_pop_list.pack(anchor = 'nw')

        btn_clear_list = tk.Button(self.variable_list, text="Clear", command=lambda : self.my_canvas.create_card('Clear', 'list'))
        btn_clear_list.pack(anchor = 'nw')

        btn_index_list = tk.Button(self.variable_list, text="Index", command=lambda : self.my_canvas.create_card('Index', 'list'))
        btn_index_list.pack(anchor = 'nw')

        btn_count_list = tk.Button(self.variable_list, text="Count", command=lambda : self.my_canvas.create_card('Count', 'list'))
        btn_count_list.pack(anchor = 'nw')

        btn_sort_list = tk.Button(self.variable_list, text="Sort", command=lambda : self.my_canvas.create_card('Sort', 'list'))
        btn_sort_list.pack(anchor = 'nw')

        btn_reverse_list = tk.Button(self.variable_list, text="Reverse", command=lambda : self.my_canvas.create_card('Reverse', 'list'))
        btn_reverse_list.pack(anchor = 'nw')

        btn_copy_list = tk.Button(self.variable_list, text="Copy", command=lambda : self.my_canvas.create_card('Copy', 'list'))
        btn_copy_list.pack(anchor = 'nw')

        #Actions for More automation
        btn_create_string = tk.Button(self.variable_string, text="Create String", command=lambda : self.my_canvas.create_card('Create String', 'string'))
        btn_create_string.pack(anchor = 'nw')

        btn_assign_string = tk.Button(self.variable_string, text="Assign", command=lambda : self.my_canvas.create_card('Assign', 'string'))
        btn_assign_string.pack(anchor = 'nw')

        btn_capitalize_string = tk.Button(self.variable_string, text="Capitalize", command=lambda : self.my_canvas.create_card('Capitalize', 'string'))
        btn_capitalize_string.pack(anchor = 'nw')
    
        btn_concate_string = tk.Button(self.variable_string, text="Concate", command=lambda : self.my_canvas.create_card('Concate', 'string'))
        btn_concate_string.pack(anchor = 'nw')

        btn_upper_string = tk.Button(self.variable_string, text="Upper", command=lambda : self.my_canvas.create_card('Upper', 'string'))
        btn_upper_string.pack(anchor = 'nw')

        btn_lower_string = tk.Button(self.variable_string, text="Lower", command=lambda : self.my_canvas.create_card('Lower', 'string'))
        btn_lower_string.pack(anchor = 'nw')

        btn_title_string = tk.Button(self.variable_string, text="Title", command=lambda : self.my_canvas.create_card('Title', 'string'))
        btn_title_string.pack(anchor = 'nw')

        btn_length_string = tk.Button(self.variable_string, text="Length", command=lambda : self.my_canvas.create_card('Length', 'string'))
        btn_length_string.pack(anchor = 'nw')

        btn_find_string = tk.Button(self.variable_string, text="Find", command=lambda : self.my_canvas.create_card('Find', 'string'))
        btn_find_string.pack(anchor = 'nw')

        btn_index_string = tk.Button(self.variable_string, text="Index", command=lambda : self.my_canvas.create_card('Index', 'string'))
        btn_index_string.pack(anchor = 'nw')

        btn_count_string = tk.Button(self.variable_string, text="Count", command=lambda : self.my_canvas.create_card('Count', 'string'))
        btn_count_string.pack(anchor = 'nw')

        btn_split_string = tk.Button(self.variable_string, text="Split", command=lambda : self.my_canvas.create_card('Split', 'string'))
        btn_split_string.pack(anchor = 'nw')

        btn_strip_string = tk.Button(self.variable_string, text="Strip", command=lambda : self.my_canvas.create_card('Strip', 'string'))
        btn_strip_string.pack(anchor = 'nw')

        btn_lstrip_string = tk.Button(self.variable_string, text="LStrip", command=lambda : self.my_canvas.create_card('LStrip', 'string'))
        btn_lstrip_string.pack(anchor = 'nw')

        btn_rstrip_string = tk.Button(self.variable_string, text="RStrip", command=lambda : self.my_canvas.create_card('RStrip', 'string'))
        btn_rstrip_string.pack(anchor = 'nw')

        #Geting variable 
        btn_create_number = tk.Button(self.variable_number, text="Create Number", command=lambda : self.my_canvas.create_card('Create Number', 'number'))
        btn_create_number.pack(anchor = 'nw')

        btn_assign_number = tk.Button(self.variable_number, text="Assign", command=lambda : self.my_canvas.create_card('Assign', 'number'))
        btn_assign_number.pack(anchor = 'nw')

        btn_increment_number = tk.Button(self.variable_number, text="Increment", command=lambda : self.my_canvas.create_card('Increment', 'number'))
        btn_increment_number.pack(anchor = 'nw')

        btn_decrement_number = tk.Button(self.variable_number, text="Decrement", command=lambda : self.my_canvas.create_card('Decrement', 'number'))
        btn_decrement_number.pack(anchor = 'nw')

        btn_create_boolean = tk.Button(self.variable_boolean, text="Create Boolean", command=lambda : self.my_canvas.create_card('Create Boolean', 'any'))
        btn_create_boolean.pack(anchor = 'nw')

        btn_assign_boolean = tk.Button(self.variable_boolean, text="Assign", command=lambda : self.my_canvas.create_card('Assign', 'any'))
        btn_assign_boolean.pack(anchor = 'nw')

        btn_toggle_boolean = tk.Button(self.variable_boolean, text="Toggle", command=lambda : self.my_canvas.create_card('Toggle', 'any'))
        btn_toggle_boolean.pack(anchor = 'nw')

        btn_create_any = tk.Button(self.variable_any, text="Create Any", command=lambda : self.my_canvas.create_card('Create Any', 'any'))
        btn_create_any.pack(anchor = 'nw')
    
    
