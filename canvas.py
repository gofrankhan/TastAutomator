import tkinter as tk
from tkinter import ttk
import os
from global_instance import *

class Canvas():

    def __init__(self, properties, *args, **kwargs):
        self.parent_frame = None
        self.canvas_frame = None
        self.my_canvas = None
        self.xscroll = None
        self.yscroll = None
        self.cards = []
        self.arrows = []
        self.cards_dict = {}
        self.var_dict = {}
        self.card_number = 0
        self.arrow_number = 0
        self.new_card = None
        self.select_x = 0
        self.select_y = 0
        self.normal_font = ("Normal")
        self.properties = properties
        variable_dict['prompt-assignment'] = "empty"

    def create_Ui(self, parent):
        self.parent_frame = parent
        self.canvas_frame = ttk.Frame(self.parent_frame, height = 950, width = 700)
        self.canvas_frame.pack(expand = True, fill = tk.BOTH, side = tk.TOP)
        self.my_canvas = tk.Canvas(self.canvas_frame, width = 750, height = 470, background = 'white', scrollregion = (0,0,2200, 4380))
        self.my_canvas.grid(row = 0, column = 0, columnspan=30, rowspan=30, sticky = 'nsew')

        self.xscroll = ttk.Scrollbar(self.canvas_frame, orient = tk.HORIZONTAL, command = self.my_canvas.xview)
        self.yscroll = ttk.Scrollbar(self.canvas_frame, orient = tk.VERTICAL, command = self.my_canvas.yview)
        self.my_canvas.config(xscrollcommand = self.xscroll.set, yscrollcommand = self.yscroll.set)
        self.xscroll.grid(row = 31, column = 0, columnspan = 30, sticky = 'ew')
        self.yscroll.grid(row = 1, column = 31,  rowspan = 30, sticky = 'ns')
        self.my_canvas.bind('<Button-3>', self.do_popup)

        self.right_click_menu = tk.Menu(self.my_canvas, bg="lightgrey", fg="black", tearoff=0)
        self.right_click_menu.add_command(label='Select', command=self.onclick)
        self.right_click_menu.add_command(label='Delete', command=self.delete)
        self.right_click_menu.add_command(label='Link', command=self.create_arrow)

    def create_arrow(self):
        self.arrow = 'arrow' + str(self.arrow_number)
        self.arrows.append(self.arrow)
        self.my_canvas.create_line(50,45, 200, 45, tags=[self.arrow])
        self.my_canvas.create_line(195,40, 200, 45, tags=[self.arrow])
        self.my_canvas.create_line(195,50, 200, 45, tags=[self.arrow])
        self.my_canvas.tag_lower(self.arrow)
        self.my_canvas.tag_bind(self.arrow, '<B1-Motion>', self.move1)
        self.my_canvas.tag_bind(self.arrow, '<ButtonPress-1>', self.savePosn)
        self.arrow_number  = self.arrow_number + 1

    def create_card(self, card_title, card_type):
        self.new_card = 'card' + str(self.card_number)
        self.cards.append(self.new_card)
        self.cards_dict[self.new_card] = card_title + card_type
        self.card_number += 1
        self.my_canvas.create_rectangle(50, 20, 200, 100, fill='#dfcdaa', tags=[self.new_card])
        self.my_canvas.create_line(50,45, 200, 45, tags=[self.new_card])
        self.my_canvas.create_text(55,40, text=card_title, anchor = 'sw', tags=[self.new_card])
        self.my_canvas.create_text(55,50, text="Details of the card \nIt may have \nmultiple lines", anchor = 'nw', tags=[self.new_card])
        #self.my_canvas.move(a, 20, 20)
        self.my_canvas.tag_bind(self.new_card, '<B1-Motion>', self.move)
        self.my_canvas.tag_bind(self.new_card, '<ButtonPress-1>', self.savePosn)
        if(card_title == 'Open URL' and card_type == 'web'):
            self.properties.open_url(self.new_card)
        elif(card_title == 'Close Browser'and card_type == 'web'):
            self.properties.close_browser(self.new_card)
        elif(card_title == 'Navigation'and card_type == 'web'):
            self.properties.navigation(self.new_card)
        elif(card_title == 'Switch To'and card_type == 'web'):
            self.properties.switch_to(self.new_card)
        elif(card_title == 'Drag And Drop'and card_type == 'web'):
            self.properties.drag_and_drop(self.new_card)
        elif(card_title == 'Click'and card_type == 'web'):
            self.properties.click(self.new_card)
        elif(card_title == 'Clear'and card_type == 'web'):
            self.properties.clear(self.new_card)
        elif(card_title == 'Read Text'and card_type == 'web'):
            self.properties.read_text(self.new_card)
        elif(card_title == "Input Text"and card_type == 'web'):
            self.properties.input_text(self.new_card)
        elif(card_title == "Select Option"and card_type == 'web'):
            self.properties.select_option(self.new_card)
        elif(card_title == "Message Box"and card_type == 'more'):
            self.properties.message_box(self.new_card)
        elif(card_title == "Open Workbook"and card_type == 'excel'):
            self.properties.excel_open(self.new_card)
        elif(card_title == "Create Workbook"and card_type == 'excel'):
            self.properties.excel_create(self.new_card)
        elif(card_title == "Delete Workbook"and card_type == 'excel'):
            self.properties.excel_delete_file(self.new_card)
        elif(card_title == "Create Worksheet"and card_type == 'excel'):
            self.properties.excel_create_worksheet(self.new_card)
        elif(card_title == "Delete Worksheet" and card_type == 'excel'):
            self.properties.excel_delete_worksheet(self.new_card)
        elif(card_title == "Set Value" and card_type == 'excel'):
            self.properties.excel_set_value(self.new_card)
        elif(card_title == "Get Value" and card_type == 'excel'):
            self.properties.excel_get_value(self.new_card)
        elif(card_title == "Set Formula" and card_type == 'excel'):
            self.properties.excel_set_formula(self.new_card)
        elif(card_title == "Merge Unmerge" and card_type == 'excel'):
            self.properties.excel_merge_unmerge(self.new_card)
        elif(card_title == "Copy Paste" and card_type == 'excel'):
            self.properties.excel_copy_paste(self.new_card)
        elif(card_title == "Save Workbook" and card_type == 'excel'):
            self.properties.excel_save_workbook(self.new_card)
        elif(card_title == "Create String" and card_type == 'string'):
            self.properties.create_variable(self.new_card, 'string')
        elif(card_title == "Create List" and card_type == 'list'):
            self.properties.create_variable(self.new_card, 'list')
        elif(card_title == "Create Dictioinary" and card_type == 'dictionary'):
            self.properties.create_variable(self.new_card, 'dictionary')
        elif(card_title == "Create Number" and card_type == 'number'):
            self.properties.create_variable(self.new_card, 'number')
        elif(card_title == "Create Boolean" and card_type == 'boolean'):
            self.properties.create_variable(self.new_card, 'boolean')
        elif(card_title == "Create Any" and card_type == 'any'):
            self.properties.create_variable(self.new_card, 'any')
        elif(card_title == "Get Element" and card_type == 'web'):
            self.properties.get_element(self.new_card)
        elif(card_title == "Get Elements" and card_type == 'web'):
            self.properties.get_elements(self.new_card)
        elif(card_title == "For Loop" and card_type == 'control'):
            self.properties.for_loop(self.new_card)
        elif(card_title == "For Each" and card_type == 'control'):
            self.properties.for_each(self.new_card)
        elif(card_title == "If" and card_type == 'control'):
            self.properties._if(self.new_card)
        elif(card_title == "Split" and card_type == 'string'):
            self.properties.split_string(self.new_card)
        elif(card_title == "Index" and card_type == 'string'):
            self.properties.manipulate_string(self.new_card, 'index')
        elif(card_title == "Count" and card_type == 'string'):
            self.properties.manipulate_string(self.new_card, 'count')
        elif(card_title == "Find" and card_type == 'string'):
            self.properties.manipulate_string(self.new_card, 'find')
        elif(card_title == "Strip" and card_type == 'string'):
            self.properties.manipulate_string(self.new_card, 'strip')
        elif(card_title == "LStrip" and card_type == 'string'):
            self.properties.manipulate_string(self.new_card, 'lstrip')
        elif(card_title == "RStrip" and card_type == 'string'):
            self.properties.manipulate_string(self.new_card, 'rstrip')
        elif(card_title == "Get Value" and card_type == 'list'):
            self.properties.list_get_value(self.new_card)
        elif(card_title == "Concate" and card_type == 'string'):
            self.properties.concate_string(self.new_card)
        elif(card_title  =="Increment" and card_type == "number"):
            self.properties.increment_decrement(self.new_card, 'increment')
        elif(card_title  =="Decrement" and card_type == "number"):
            self.properties.increment_decrement(self.new_card, 'decrement')


    def savePosn(self, event):
        self.lastx = event.x
        self.lasty = event.y

    def move(self, event):
        self.my_canvas.move(self.new_card, event.x-self.lastx, event.y-self.lasty)
        self.lastx = event.x
        self.lasty = event.y
    
    def move1(self, event):
        self.my_canvas.move(self.arrow, event.x-self.lastx, event.y-self.lasty)
        self.lastx = event.x
        self.lasty = event.y

    def onclick(self):
        self.my_canvas.itemconfig(self.new_card)
        if(self.cards_dict[self.new_card] == 'Open URLweb'):
            self.properties.open_url(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Close Browserweb'):
            self.properties.close_browser(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Navigationweb'):
            self.properties.navigation(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Switch Toweb'):
            self.properties.switch_to(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Drag And Dropweb'):
            self.properties.drag_and_drop(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Clickweb'):
            self.properties.click(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Clearweb'):
            self.properties.clear(self.new_card)
        elif(self.cards_dict[self.new_card] == 'Read Textweb'):
            self.properties.read_text(self.new_card)
        elif(self.cards_dict[self.new_card] == "Input Textweb"):
            self.properties.input_text(self.new_card)
        elif(self.cards_dict[self.new_card] == "Select Optionweb"):
            self.properties.select_option(self.new_card)
        elif(self.cards_dict[self.new_card] == "Message Boxmore"):
            self.properties.message_box(self.new_card)
        elif(self.cards_dict[self.new_card] == "Open Workbookexcel"):
            self.properties.excel_open(self.new_card)
        elif(self.cards_dict[self.new_card] == "Create Workbookexcel"):
            self.properties.excel_create(self.new_card)
        elif(self.cards_dict[self.new_card] == "Delete Workbookexcel"):
            self.properties.excel_delete_file(self.new_card)
        elif(self.cards_dict[self.new_card] == "Create Worksheetexcel"):
            self.properties.excel_create_worksheet(self.new_card)
        elif(self.cards_dict[self.new_card] == "Delete Worksheetexcel"):
            self.properties.excel_delete_worksheet(self.new_card)
        elif(self.cards_dict[self.new_card] == "Set Valueexcel"):
            self.properties.excel_set_value(self.new_card)
        elif(self.cards_dict[self.new_card] == "Get Valueexcel"):
            self.properties.excel_get_value(self.new_card)
        elif(self.cards_dict[self.new_card] == "Set Formulaexcel"):
            self.properties.excel_set_formula(self.new_card)
        elif(self.cards_dict[self.new_card] == "Merge Unmergeexcel"):
            self.properties.excel_merge_unmerge(self.new_card)
        elif(self.cards_dict[self.new_card] == "Copy Pasteexcel"):
            self.properties.excel_copy_paste(self.new_card)
        elif(self.cards_dict[self.new_card] == "Save Workbookexcel"):
            self.properties.excel_save_workbook(self.new_card)
        elif(self.cards_dict[self.new_card] == "Create Stringstring"):
            self.properties.create_variable(self.new_card, 'string')
        elif(self.cards_dict[self.new_card] == "Create Listlist"):
            self.properties.create_variable(self.new_card, 'list')
        elif(self.cards_dict[self.new_card] == "Create Dictionarydictionary"):
            self.properties.create_variable(self.new_card, 'dictionary')
        elif(self.cards_dict[self.new_card] == "Create Booleanboolean"):
            self.properties.create_variable(self.new_card, 'boolean')
        elif(self.cards_dict[self.new_card] == "Create Numbernumber"):
            self.properties.create_variable(self.new_card, 'number')
        elif(self.cards_dict[self.new_card] == "Create Anyany"):
            self.properties.create_string_variable(self.new_card)
        elif(self.cards_dict[self.new_card] == "Get Elementweb"):
            self.properties.get_element(self.new_card)
        elif(self.cards_dict[self.new_card] == "Get Elementsweb"):
            self.properties.get_elements(self.new_card)
        elif(self.cards_dict[self.new_card] == "For Loopcontrol"):
            self.properties.for_loop(self.new_card)
        elif(self.cards_dict[self.new_card] == "For Eachcontrol"):
            self.properties.for_each(self.new_card)
        elif(self.cards_dict[self.new_card] == "Ifcontrol"):
            self.properties._if(self.new_card)
        elif(self.cards_dict[self.new_card] == "Splitstring"):
            self.properties.split_string(self.new_card)
        elif(self.cards_dict[self.new_card] == "Indexstring"):
            self.properties.manipulate_string(self.new_card, "index")
        elif(self.cards_dict[self.new_card] == "Countstring"):
            self.properties.manipulate_string(self.new_card, "count")
        elif(self.cards_dict[self.new_card] == "Findstring"):
            self.properties.manipulate_string(self.new_card, "find")
        elif(self.cards_dict[self.new_card] == "Stripstring"):
            self.properties.manipulate_string(self.new_card, "strip")
        elif(self.cards_dict[self.new_card] == "LStripstring"):
            self.properties.manipulate_string(self.new_card, "lstrip")
        elif(self.cards_dict[self.new_card] == "RStripstring"):
            self.properties.manipulate_string(self.new_card, "rstrip")
        elif(self.cards_dict[self.new_card] =="Get Valuelist"):
            self.properties.list_get_value(self.new_card)
        elif(self.cards_dict[self.new_card] =="Concatestring"):
            self.properties.concate_string(self.new_card)
        elif(self.cards_dict[self.new_card] =="Incrementnumber"):
            self.properties.increment_decrement(self.new_card, 'increment')
        elif(self.cards_dict[self.new_card] =="Decrementnumber"):
            self.properties.increment_decrement(self.new_card, 'decrement')


    def do_popup(self, event):
        try:
            self.select_x , self.select_y = event.x, event.y
            self.right_click_menu.tk_popup(event.x_root, event.y_root)
            item = self.my_canvas.find_closest(event.x, event.y)
            tags = self.my_canvas.itemcget(item, "tags")
            self.new_card = tags
        finally:
            self.right_click_menu.grab_release()

    def delete(self):
        self.my_canvas.delete(self.new_card)
        self.cards.remove(self.new_card)
        file_path = my_path + "files\\"
        if(os.path.isfile(file_path + self.new_card + '.xml')):
            os.remove(file_path + self.new_card + '.xml')
        if(len(self.cards) == 0):
            self.properties.reset_all("Empty")

    def get_cards(self):
        return self.cards

    def get_card_dictionary(self):
        return self.cards_dict


        

