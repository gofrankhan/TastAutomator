from tkinter import *
from tkinter import ttk

from selenium.webdriver.remote import command, switch_to
from global_instance import *
import xml.etree.ElementTree as xml
from readfilesxml import ReadFileFromXML
from my_variables import MyVariables

class Properties(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent , *args, **kwargs)
        self.parent_frame = parent
        self.path = my_path + "\\files"
        self.lbl_empty = Label(self.parent_frame, text = "Emply", height = 10, padx = 10, pady = 10)
        self.lbl_empty.grid(row = 0, column = 0, columnspan = 2 , padx = 10, pady = 10)
        self.read_file_from_xml = ReadFileFromXML()

    def reset_all(self, nameText):
        for widget in self.parent_frame.winfo_children():
            widget.destroy()
        self.lbl_empty = Label(self.parent_frame, text = nameText, height = 10)
        self.lbl_empty.grid(row = 0, column = 0, columnspan = 2, sticky=NW)
    
    def save_excel_open(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        location = xml.Element('location')
        filename = xml.Element('filename')
        session.text = self.entry_session.get()
        location.text = self.entry_location.get()
        filename.text = self.entry_filename.get()
        action = xml.Element('action')
        action.text = "excel_open"
        root.append(action)
        root.append(session)
        root.append(location)
        root.append(filename)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def excel_open(self, new_card):
        self.reset_all('Open Workbook')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_location = Label(self.parent_frame, text="Location:")
        self.entry_location = Entry(self.parent_frame, width = 30)

        self.lbl_filename = Label(self.parent_frame, text="File Name:")
        self.entry_filename= Entry(self.parent_frame, width = 30)

        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_location.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_location.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_filename.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_filename.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_open(new_card))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)

        session, location, filename = self.read_file_from_xml.read_xml_excel_open(new_card)
        self.entry_session.insert(0, session)
        self.entry_location.insert(0, location)
        self.entry_filename.insert(0, filename)
    
    def save_excel_create(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        location = xml.Element('location')
        filename = xml.Element('filename')
        session.text = self.entry_session.get()
        location.text = self.entry_location.get()
        filename.text = self.entry_filename.get()
        action = xml.Element('action')
        action.text = "excel_create"
        root.append(action)
        root.append(session)
        root.append(location)
        root.append(filename)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)


    def excel_create(self, new_card):
        self.reset_all('Create Workbook')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_location = Label(self.parent_frame, text="Location:")
        self.entry_location = Entry(self.parent_frame, width = 30)

        self.lbl_filename = Label(self.parent_frame, text="File Name:")
        self.entry_filename= Entry(self.parent_frame, width = 30)

        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_location.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_location.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_filename.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_filename.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_create(new_card))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)
        session, location, filename = self.read_file_from_xml.read_xml_excel_create(new_card)
        self.entry_session.insert(0, session)
        self.entry_location.insert(0, location)
        self.entry_filename.insert(0, filename)
    
    def save_excel_delete_file(self, new_card):

        root = xml.Element('root')
        location = xml.Element('location')
        filename = xml.Element('filename')
        location.text = self.entry_location.get()
        filename.text = self.entry_filename.get()
        action = xml.Element('action')
        action.text = "excel_delete_file"
        root.append(action)
        root.append(location)
        root.append(filename)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def excel_delete_file(self, new_card):
        self.reset_all('Delete Workbook')

        self.lbl_location = Label(self.parent_frame, text="Location:")
        self.entry_location = Entry(self.parent_frame, width = 30)

        self.lbl_filename = Label(self.parent_frame, text="File Name:")
        self.entry_filename= Entry(self.parent_frame, width = 30)

        self.lbl_location.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_location.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_filename.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_filename.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_delete_file(new_card))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)

        location, filename = self.read_file_from_xml.read_xml_excel_delete_file(new_card)
        self.entry_location.insert(0, location)
        self.entry_filename.insert(0, filename)
    
    def save_excel_create_worksheet(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        sheetname = xml.Element('sheetname')
        position = xml.Element('position')
        value = xml.Element('value')
        session.text = self.entry_session.get()
        sheetname.text = self.entry_sheet_name.get()
        if(self.var_sheet_position.get() == 'default'):
            position.text = self.var_sheet_position.get()
            value.text = '0'
        else:
            position.text = self.var_sheet_position.get()
            value.text = self.entry_sheet_position.get()
        action = xml.Element('action')
        action.text = "excel_create_worksheet"
        root.append(action)
        root.append(session)
        root.append(sheetname)
        root.append(position)
        root.append(value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    
    def excel_create_worksheet(self, new_card):
        self.reset_all('Create Worksheet')

        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session  = Entry(self.parent_frame, width = 30)
        self.lbl_session .grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_sheet_name = Label(self.parent_frame, text="Sheet Name:")
        self.entry_sheet_name  = Entry(self.parent_frame, width = 30)
        self.lbl_sheet_name .grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_name.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)

        self.var_sheet_position = StringVar()
        self.my_sheet_position_end = Checkbutton(self.parent_frame, text="Default[END]", variable=self.var_sheet_position, onvalue="default", offvalue="off", anchor = 'w')
        self.my_sheet_position_end.deselect()
        self.my_sheet_position_end.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)

        self.my_sheet_position = Checkbutton(self.parent_frame, text="Enter Position:", variable=self.var_sheet_position, onvalue="positional", offvalue="off", anchor = 'w')
        self.my_sheet_position.deselect()
        self.entry_sheet_position = Entry(self.parent_frame, width = 30)
        self.my_sheet_position.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_position.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_create_worksheet(new_card))
        btn_save.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=W)

        session, sheetname, position, value = self.read_file_from_xml.read_xml_excel_create_worksheet(new_card)
        self.entry_session.insert(0, session)
        self.entry_sheet_name.insert(0, sheetname)
        if(position == 'default'):
            self.my_sheet_position_end.select()
        elif(position == 'positional'):
            self.my_sheet_position.select()
            self.entry_sheet_position.insert(0, value)
    
    def save_excel_delete_worksheet(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        sheetname = xml.Element('sheetname')
        session.text = self.entry_session.get()
        sheetname.text = self.entry_sheet_name.get()
        action = xml.Element('action')
        action.text = "excel_delete_worksheet"
        root.append(action)
        root.append(session)
        root.append(sheetname)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def excel_delete_worksheet(self, new_card):
        self.reset_all('Delete Worksheet')

        self.lbl_session = Label(self.parent_frame, text="Session:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_sheet_name = Label(self.parent_frame, text="Sheet Name:")
        self.entry_sheet_name= Entry(self.parent_frame, width = 30)

        self.lbl_session.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_sheet_name.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_name.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_delete_worksheet(new_card))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)

        session, sheetname = self.read_file_from_xml.read_xml_excel_delete_worksheet(new_card)
        self.entry_session.insert(0, session)
        self.entry_sheet_name.insert(0, sheetname)

    def save_excel_save_workbook(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        location = xml.Element('location')
        filename = xml.Element('filename')
        session.text = self.entry_session.get()
        location.text = self.entry_location.get()
        filename.text = self.entry_filename.get()
        action = xml.Element('action')
        action.text = "excel_save_workbook"
        root.append(action)
        root.append(session)
        root.append(location)
        root.append(filename)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def excel_save_workbook(self, new_card):
        self.reset_all('Save Workbook')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_location = Label(self.parent_frame, text="Location:")
        self.entry_location = Entry(self.parent_frame, width = 30)

        self.lbl_filename = Label(self.parent_frame, text="File Name:")
        self.entry_filename= Entry(self.parent_frame, width = 30)

        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_location.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_location.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_filename.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_filename.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_save_workbook(new_card))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)

        session, location, filename = self.read_file_from_xml.read_xml_excel_save_workbook(new_card)
        self.entry_session.insert(0, session)
        self.entry_location.insert(0, location)
        self.entry_filename.insert(0, filename)


    def save_excel_set_value(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        sheetname = xml.Element('sheetname')
        cell = xml.Element('cell')
        value = xml.Element('value')
        session.text = self.entry_session.get()
        sheetname.text = self.entry_sheet_name.get()
        cell.text = self.my_var_cell.get()
        value.text = self.my_var_value.get()
        action = xml.Element('action')
        action.text = "excel_set_value"
        root.append(action)
        root.append(session)
        root.append(sheetname)
        root.append(cell)
        root.append(value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def excel_set_value(self, new_card):
        self.reset_all('Set Value')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_sheet_name = Label(self.parent_frame, text="Sheet Name:")
        self.entry_sheet_name = Entry(self.parent_frame, width = 30)

        self.lbl_value = Label(self.parent_frame, text="Value:")
        self.my_var_value= StringVar()
        self.my_combo_value = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_value)
        self.my_combo_value['values'] = tuple(variable_dict.keys())
        self.my_combo_value.current(0)

        self.lbl_cell = Label(self.parent_frame, text="Cell:")
        self.my_var_cell= StringVar()
        self.my_combo_cell = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_cell)
        self.my_combo_cell['values'] = tuple(variable_dict.keys())
        self.my_combo_cell.current(0)

        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_sheet_name.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_name.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_value.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_value.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_cell.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_cell.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_set_value(new_card))
        btn_save.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=W)

        session, sheetname, cell, value = self.read_file_from_xml.read_xml_excel_set_value(new_card)
        self.entry_session.insert(0, session)
        self.entry_sheet_name.insert(0, sheetname)
        if(value != ""):
            self.my_combo_value.set(value)
        if(cell  != ""):
            self.my_combo_cell.set(cell)
    
    def save_excel_set_formula(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        sheetname = xml.Element('sheetname')
        cell = xml.Element('cell')
        formula = xml.Element('formula')
        session.text = self.entry_session.get()
        sheetname.text = self.entry_sheet_name.get()
        cell.text = self.entry_cell.get()
        formula.text = self.entry_formula.get()
        action = xml.Element('action')
        action.text = "excel_set_formula"
        root.append(action)
        root.append(session)
        root.append(sheetname)
        root.append(cell)
        root.append(formula)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    
    def excel_set_formula(self, new_card):
        self.reset_all('Set Formula')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_sheet_name = Label(self.parent_frame, text="Sheet Name:")
        self.entry_sheet_name = Entry(self.parent_frame, width = 30)

        self.lbl_formula = Label(self.parent_frame, text="Formula:")
        self.entry_formula = Entry(self.parent_frame, width = 30)

        self.lbl_cell = Label(self.parent_frame, text="Cell:")
        self.entry_cell = Entry(self.parent_frame, width = 30)


        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_sheet_name.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_name.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_formula.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_formula.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_cell.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_cell.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_set_formula(new_card))
        btn_save.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=W)

        session, sheetname, cell, formula = self.read_file_from_xml.read_xml_excel_set_formula(new_card)
        self.entry_session.insert(0, session)
        self.entry_sheet_name.insert(0, sheetname)
        self.entry_cell.insert(0, cell)
        self.entry_formula.insert(0, formula)
    
    def save_excel_merge_unmerge(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        sheetname = xml.Element('sheetname')
        merge_unmerge = xml.Element('merge_unmerge')
        from_cell = xml.Element('from_cell')
        to_cell = xml.Element('to_cell')
        session.text = self.entry_session.get()
        sheetname.text = self.entry_sheet_name.get()
        if(self.var_merge_unmerge.get() == 'merge'):
            merge_unmerge.text = 'merge'
        elif(self.var_merge_unmerge.get() == 'unmerge'):
            merge_unmerge.text = 'unmerge'
        from_cell.text = self.entry_from_cell.get()
        to_cell.text = self.entry_to_cell.get()
        action = xml.Element('action')
        action.text = "excel_merge_unmerge"
        root.append(action)
        root.append(session)
        root.append(sheetname)
        root.append(merge_unmerge)
        root.append(from_cell)
        root.append(to_cell)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    
    def excel_merge_unmerge(self, new_card):
        self.reset_all('Merge Unmerge')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_sheet_name = Label(self.parent_frame, text="Sheet Name:")
        self.entry_sheet_name = Entry(self.parent_frame, width = 30)

        self.var_merge_unmerge = StringVar()
        self.my_merge = Checkbutton(self.parent_frame, text="Merge", variable=self.var_merge_unmerge, onvalue="merge", offvalue="off", anchor = 'w')
        self.my_merge.deselect()
        self.my_unmerge = Checkbutton(self.parent_frame, text="Unmerge", variable=self.var_merge_unmerge, onvalue="unmerge", offvalue="off", anchor = 'w')
        self.my_unmerge.deselect()

        self.lbl_from_cell = Label(self.parent_frame, text="From Cell:")
        self.entry_from_cell = Entry(self.parent_frame, width = 30)

        self.lbl_to_cell = Label(self.parent_frame, text="To Cell:")
        self.entry_to_cell = Entry(self.parent_frame, width = 30)


        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_sheet_name.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_name.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.my_merge.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_unmerge.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_from_cell.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_from_cell.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_to_cell.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_to_cell.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_merge_unmerge(new_card))
        btn_save.grid(row = 9, column = 0, padx = 10, pady = 10, sticky=W)

        session, sheetname, merge_unmerge, from_cell, to_cell = self.read_file_from_xml.read_xml_excel_merge_unmerge(new_card)
        self.entry_session.insert(0, session)
        self.entry_sheet_name.insert(0, sheetname)
        if(merge_unmerge == "merge"):
            self.my_merge.select()
        elif(merge_unmerge == "unmerge"):
            self.my_unmerge.select()
        self.entry_from_cell.insert(0, from_cell)
        self.entry_to_cell.insert(0, to_cell)

    def save_excel_copy_paste(self, new_card):

        root = xml.Element('root')
        copy_session = xml.Element('copy_session')
        copy_sheetname = xml.Element('copy_sheetname')
        copy_start = xml.Element('copy_start')
        copy_end = xml.Element('copy_end')
        paste_session = xml.Element('paste_session')
        paste_sheetname = xml.Element('paste_sheetname')
        paste_start = xml.Element('paste_start')
        paste_end = xml.Element('paste_end')
        copy_session.text = self.entry_copy_session.get()
        copy_sheetname.text = self.entry_copy_sheet_name.get()
        copy_start.text = self.entry_copy_start.get()
        copy_end.text = self.entry_copy_end.get()
        paste_session.text = self.entry_paste_session.get()
        paste_sheetname.text = self.entry_paste_sheet_name.get()
        paste_start.text = self.entry_paste_start.get()
        paste_end.text = self.entry_paste_end.get()
        action = xml.Element('action')
        action.text = "excel_copy_paste"
        root.append(action)
        root.append(copy_session)
        root.append(copy_sheetname)
        root.append(copy_start)
        root.append(copy_end)
        root.append(paste_session)
        root.append(paste_sheetname)
        root.append(paste_start)
        root.append(paste_end)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def excel_copy_paste(self, new_card):
        self.reset_all('Copy Paste')
        self.lbl_copy_session = Label(self.parent_frame, text="Copy Session Name:")
        self.entry_copy_session = Entry(self.parent_frame, width = 30)

        self.lbl_copy_sheet_name = Label(self.parent_frame, text="Copy Sheet Name:")
        self.entry_copy_sheet_name = Entry(self.parent_frame, width = 30)

        self.lbl_copy_start = Label(self.parent_frame, text="Copy Start:")
        self.entry_copy_start = Entry(self.parent_frame, width = 30)

        self.lbl_copy_end = Label(self.parent_frame, text="Copy End:")
        self.entry_copy_end = Entry(self.parent_frame, width = 30)

        self.lbl_paste_session = Label(self.parent_frame, text="Paste Session Name:")
        self.entry_paste_session = Entry(self.parent_frame, width = 30)

        self.lbl_paste_sheet_name = Label(self.parent_frame, text="Paste Sheet Name:")
        self.entry_paste_sheet_name = Entry(self.parent_frame, width = 30)

        self.lbl_paste_start = Label(self.parent_frame, text="Paste Start:")
        self.entry_paste_start = Entry(self.parent_frame, width = 30)

        self.lbl_paste_end = Label(self.parent_frame, text="Paste End:")
        self.entry_paste_end = Entry(self.parent_frame, width = 30)


        self.lbl_copy_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_copy_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_copy_sheet_name.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_copy_sheet_name.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_copy_start.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_copy_start.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_copy_end.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_copy_end.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_paste_session.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_paste_session.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_paste_sheet_name.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_paste_sheet_name.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_paste_start.grid(row = 7, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_paste_start.grid(row = 7, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_paste_end.grid(row = 8, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_paste_end.grid(row = 8, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_copy_paste(new_card))
        btn_save.grid(row = 9, column = 0, padx = 10, pady = 10, sticky=W)

        copy_session, copy_sheetname, copy_start, copy_end, paste_session, paste_sheetname, paste_start, paste_end = self.read_file_from_xml.read_xml_excel_copy_paste(new_card)
        self.entry_copy_session.insert(0, copy_session)
        self.entry_copy_sheet_name.insert(0, copy_sheetname)
        self.entry_copy_start.insert(0, copy_start)
        self.entry_copy_end.insert(0, copy_end)
        self.entry_paste_session.insert(0, paste_session)
        self.entry_paste_sheet_name.insert(0, paste_sheetname)
        self.entry_paste_start.insert(0, paste_start)
        self.entry_paste_end.insert(0, paste_end)

    def save_excel_get_value(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        sheetname = xml.Element('sheetname')
        cell = xml.Element('cell')
        save_to = xml.Element('variable')
        session.text = self.entry_session.get()
        sheetname.text = self.entry_sheet_name.get()
        cell.text = self.entry_cell.get()
        save_to.text = self.myVar.get()
        action = xml.Element('action')
        action.text = "excel_get_value"
        root.append(action)
        root.append(session)
        root.append(sheetname)
        root.append(cell)
        root.append(save_to)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    
    def excel_get_value(self, new_card):
        self.reset_all('Get Value')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_sheet_name = Label(self.parent_frame, text="Sheet Name:")
        self.entry_sheet_name = Entry(self.parent_frame, width = 30)

        self.lbl_cell = Label(self.parent_frame, text="Cell:")
        self.entry_cell = Entry(self.parent_frame, width = 30)

        self.lbl_save_to = Label(self.parent_frame, text="Save To:")
        self.myVar = StringVar()
        self.my_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.myVar)
        self.my_variable['values'] = ('prompt-assignment')
        self.my_variable.current(0)


        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_sheet_name.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_sheet_name.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_cell.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_cell.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_save_to.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_variable.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_excel_get_value(new_card))
        btn_save.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=W)

        session, sheetname, cell, save_to = self.read_file_from_xml.read_xml_excel_get_value(new_card)
        self.entry_session.insert(0, session)
        self.entry_sheet_name.insert(0, sheetname)
        self.entry_cell.insert(0, cell)
        self.my_variable.set(save_to)

    
    def save_open_url(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        link = xml.Element('link')
        browser = xml.Element('browser')
        session.text = self.entry_session.get()
        link.text = self.entry_link.get()
        browser.text = self.clicked.get()
        action = xml.Element('action')
        action.text = "openurl"
        root.append(action)
        root.append(session)
        root.append(link)
        root.append(browser)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def open_url(self, new_card):
        self.reset_all('Open Url')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)

        self.lbl_link = Label(self.parent_frame, text="URL:")
        self.entry_link = Entry(self.parent_frame, width = 30)

        options = [
            "Google Chrome",
            "Mozilla Firefox",
            "Internet Explorer",
            "Microsoft Edge"
        ]

        self.clicked = StringVar()
        self.clicked.set(options[0])

        self.lbl_browser = Label(self.parent_frame, text="Select Browser:")
        self.entry_browser= OptionMenu(self.parent_frame, self.clicked, *options)  

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_open_url(new_card))

        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=W)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=W)
        self.lbl_link.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=W)
        self.entry_link.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=W)
        self.lbl_browser.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=W)
        self.entry_browser.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=W)
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)
        url, browser, session = self.read_file_from_xml.read_xml_open_url(new_card)
        self.entry_link.insert(0, url)
        self.entry_session.insert(0, session)
        self.clicked.set(browser)

    def save_close_browser(self, new_card):

        root = xml.Element('root')
        session = xml.Element('session')
        session.text = self.entry_session.get()
        action = xml.Element('action')
        action.text = "close_browser"
        root.append(action)
        root.append(session)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def close_browser(self, new_card):
        self.reset_all('Close Browser')
        self.lbl_session = Label(self.parent_frame, text="Session Name:")
        self.entry_session = Entry(self.parent_frame, width = 30)
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_close_browser(new_card))

        self.lbl_session.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=W)
        self.entry_session.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=W)
        btn_save.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=W)

        session = self.read_file_from_xml.read_xml_close_browser(new_card)
        self.entry_session.insert(0, session)

    def save_navigation(self, new_card):

        root = xml.Element('root')
        navigation = xml.Element('navigation')
        navigation.text = self.var_navigation.get()
        action = xml.Element('action')
        action.text = "navigation"
        root.append(action)
        root.append(navigation)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def navigation(self, new_card):
        self.reset_all('Navigation')
        self.var_navigation = StringVar()
        self.my_check_navigation_forword = Checkbutton(self.parent_frame, text="Forward", variable=self.var_navigation, onvalue="forward", offvalue="off", anchor = 'w')
        self.my_check_navigation_forword.deselect()
        self.my_check_navigation_back = Checkbutton(self.parent_frame, text="Back", variable=self.var_navigation, onvalue="back", offvalue="off", anchor = 'w')
        self.my_check_navigation_back.deselect()
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_navigation(new_card))

        self.my_check_navigation_forword.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=W)
        self.my_check_navigation_back.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=W)
        btn_save.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=W)

        navigation = self.read_file_from_xml.read_xml_navigation(new_card)
        if(navigation == 'forward'):
            self.my_check_navigation_forword.select()
        elif(navigation == 'back'):
            self.my_check_navigation_back.select()
        
    def save_switch_to(self, new_card):

        root = xml.Element('root')
        switch_to = xml.Element('switch_to')
        switch_to.text = self.var_switch_to.get()
        value = xml.Element('value')
        value.text = 'null'
        if(self.var_switch_to.get() == 'window'):
            value.text = self.entry_switch_to_window.get()
        if(self.var_switch_to.get() == 'frame'):
            value.text = self.entry_switch_to_frame.get()
        action = xml.Element('action')
        action.text = "switch_to"
        root.append(action)
        root.append(switch_to)
        root.append(value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def switch_to(self, new_card):
        self.reset_all('Switch To')
        self.var_switch_to = StringVar()
        self.my_check_switch_to_window = Checkbutton(self.parent_frame, command = self.activateSwitchTo, text="Window", variable=self.var_switch_to, onvalue="window", offvalue="off", anchor = 'w')
        self.my_check_switch_to_window.deselect()
        self.entry_switch_to_window = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_switch_to_window.grid(row = 1, column = 0, padx = 10, sticky=NW)
        self.entry_switch_to_window.grid(row = 1, column = 1, padx = 10, sticky=NW)
        self.my_check_switch_to_frame  = Checkbutton(self.parent_frame, command = self.activateSwitchTo, text="Frame", variable=self.var_switch_to, onvalue="frame", offvalue="off", anchor = 'w')
        self.my_check_switch_to_frame.deselect()
        self.entry_switch_to_frame = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_switch_to_frame.grid(row = 2, column = 0, padx = 10, sticky=NW)
        self.entry_switch_to_frame.grid(row = 2, column = 1, padx = 10, sticky=NW)
        self.my_check_switch_to_parent = Checkbutton(self.parent_frame, command = self.activateSwitchTo,  text="Parent", variable=self.var_switch_to, onvalue="parent", offvalue="off", anchor = 'w')
        self.my_check_switch_to_parent.deselect()
        self.my_check_switch_to_parent.grid(row = 3, column = 0, padx = 10, sticky=NW)
        self.my_check_switch_to_alert = Checkbutton(self.parent_frame, command = self.activateSwitchTo,  text="Alert", variable=self.var_switch_to, onvalue="alert", offvalue="off", anchor = 'w')
        self.my_check_switch_to_alert.deselect()
        self.my_check_switch_to_alert.grid(row = 4, column = 0, padx = 10, sticky=NW)
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_switch_to(new_card))
        btn_save.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=W)

        switch_to, value = self.read_file_from_xml.read_xml_switch_to(new_card)
        if(switch_to == 'window'):
            self.my_check_switch_to_window.select()
            self.entry_switch_to_window.config(state=NORMAL)
            self.entry_switch_to_window.insert(0, value)
        elif(switch_to == 'frame'):
            self.my_check_switch_to_frame.select()
            self.entry_switch_to_frame.config(state=NORMAL)
            self.entry_switch_to_frame.insert(0, value)
        elif(switch_to == 'parent'):
            self.my_check_switch_to_parent.select()
        elif(switch_to == 'alert'):
            self.my_check_switch_to_alert.select()

    def save_click(self, new_card):
        root = xml.Element('root')
        action = xml.Element('action')
        action.text = "click"
        root.append(action)
        locator_value = self.save_check_box()
        locator_name = xml.Element('locator_name')
        locator_name.text = self.var_locator.get()
        root.append(locator_name)
        root.append(locator_value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    

    def click(self, new_card):
        self.reset_all('Click')

        self.create_input_ui(1)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_click(new_card))
        btn_save.grid(row = 10, column = 0, padx = 10, pady = 10, sticky=W)
    
        locator_name, locator_value = self.read_file_from_xml.read_xml_click(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
    
    def save_clear(self, new_card):
        root = xml.Element('root')
        action = xml.Element('action')
        action.text = "clear"
        root.append(action)
        locator_value = self.save_check_box()
        locator_name = xml.Element('locator_name')
        locator_name.text = self.var_locator.get()
        root.append(locator_name)
        root.append(locator_value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def clear(self, new_card):
        self.reset_all('Clear')

        self.create_input_ui(1)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_clear(new_card))
        btn_save.grid(row = 10, column = 0, padx = 10, pady = 10, sticky=W)
    
        locator_name, locator_value, = self.read_file_from_xml.read_xml_clear(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
    
    def save_read_text(self, new_card, name):

        root = xml.Element('root')
        save_to = xml.Element('variable')
        save_to.text = self.myVar.get()
        action = xml.Element('action')
        action.text = name
        root.append(action)
        locator_value = self.save_check_box()
        locator_name = xml.Element('locator_name')
        locator_name.text = self.var_locator.get()
        root.append(locator_name)
        root.append(locator_value)
        root.append(save_to)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def read_text(self, new_card):
        self.reset_all('Read Text')

        self.create_input_ui(1)

        self.lbl_save_to = Label(self.parent_frame, text="Save To:")
        self.myVar = StringVar()
        self.my_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.myVar)
        self.my_variable['values'] = tuple(variable_dict.keys())
        self.my_variable.current(0)
        
        self.lbl_save_to.grid(row = 10, column = 0, padx = 10, pady = 10, sticky=W)
        self.my_variable.grid(row = 10, column= 1, padx = 10, pady = 10, sticky=W)
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_read_text(new_card, 'readtext'))
        btn_save.grid(row = 11, column = 0, padx = 10, pady = 10, sticky=W)
        locator_name, locator_value, _variable = self.read_file_from_xml.read_xml_read_text(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
        if(_variable != ""):
            self.my_variable.set(_variable)


    def get_element(self, new_card):
        self.reset_all('Get Element')

        self.create_input_ui(1)

        self.my_check_element.grid_forget()
        self.my_combo_element.grid_forget()

        self.lbl_save_to = Label(self.parent_frame, text="Save To:")
        self.myVar = StringVar()
        self.my_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.myVar)
        self.my_variable['values'] = tuple(variable_dict.keys())
        self.my_variable.current(0)
        
        self.lbl_save_to.grid(row = 9, column = 0, padx = 10, pady = 10, sticky=W)
        self.my_variable.grid(row = 9, column= 1, padx = 10, pady = 10, sticky=W)
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_read_text(new_card, 'get_element'))
        btn_save.grid(row = 10, column = 0, padx = 10, pady = 10, sticky=W)
        locator_name, locator_value = self.read_file_from_xml.read_xml_read_text(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)

    def get_elements(self, new_card):
        self.reset_all('Get Elements')

        self.create_input_ui(1)

        self.my_check_element.grid_forget()
        self.my_combo_element.grid_forget()

        self.lbl_save_to = Label(self.parent_frame, text="Save To:")
        self.myVar = StringVar()
        self.my_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.myVar)
        self.my_variable['values'] = tuple(variable_dict.keys())
        self.my_variable.current(0)
        
        self.lbl_save_to.grid(row = 9, column = 0, padx = 10, pady = 10, sticky=W)
        self.my_variable.grid(row = 9, column= 1, padx = 10, pady = 10, sticky=W)
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_read_text(new_card, 'get_elements'))
        btn_save.grid(row = 10, column = 0, padx = 10, pady = 10, sticky=W)
        locator_name, locator_value = self.read_file_from_xml.read_xml_read_text(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
    
    def save_message_box(self, new_card):

        root = xml.Element('root')
        variable_msg = xml.Element('variable')
        variable_msg.text = self.myVarMsg.get()
        action = xml.Element('action')
        action.text = "messagebox"
        root.append(action)
        root.append(variable_msg)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def message_box(self, new_card):
        self.reset_all('Message Box')

        self.myVarMsg = StringVar()
        self.my_variable_msg = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.myVarMsg)
        self.my_variable_msg['values'] = tuple(variable_dict.keys())
        self.my_variable_msg.current(0)
        self.lbl_variable = Label(self.parent_frame, text="Variable:")
        self.lbl_variable.grid(row = 1, column= 0, padx = 10, pady = 10)
        self.my_variable_msg.grid(row = 1, column= 1, padx = 10, pady = 10)
        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_message_box(new_card))
        btn_save.grid(row = 2, column = 0, padx = 10, pady = 10)
        _variable = self.read_file_from_xml.read_xml_message_box(new_card)
        if(_variable != ""):
            self.my_variable_msg.set(_variable)

    def save_input_text(self, new_card):

        root = xml.Element('root')
        action = xml.Element('action')
        action.text = "inputtext"
        root.append(action)
        locator_value = self.save_check_box()
        locator_name = xml.Element('locator_name')
        locator_name.text = self.var_locator.get()
        root.append(locator_name)
        root.append(locator_value)
        value = xml.Element('value')
        value.text = self.entry_value.get()
        root.append(value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    
    def input_text(self, new_card):
        self.reset_all('Input Text')

        self.create_input_ui(1)

        self.lbl_value = Label(self.parent_frame, text="Value:")
        self.entry_value = Entry(self.parent_frame, width = 30)
        self.lbl_value.grid(row = 10, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_value.grid(row = 10, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_input_text(new_card))
        btn_save.grid(row = 11, column = 0, padx = 10, pady = 10, sticky=NW)

        locator_name, locator_value, value = self.read_file_from_xml.read_xml_input_text(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
        self.entry_value.insert(0, value)

    def save_split_string(self, new_card, work):

        root = xml.Element('root')
        action = xml.Element('action')
        action.text = work
        root.append(action)
        variable1 = xml.Element('variable1')
        variable1.text = self.my_var_split_string_variable.get()
        variable2 = xml.Element('variable2')
        variable2.text = self.my_var_split_string_list.get()
        root.append(variable1)
        root.append(variable2)
        if(work == 'split_string' or work == 'list_get_value'):
            delimiter = xml.Element('delimiter')
            delimiter.text = self.entry_string_delimiter.get()
            root.append(delimiter)
        
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def save_concate_string(self, new_card):
        root = xml.Element('root')
        action = xml.Element('action')
        action.text = "concate_string"
        root.append(action)
        string1 = xml.Element('string1')
        string1.text = self.my_var_concate_string_1.get()
        string2 = xml.Element('string2')
        string2.text = self.my_var_concate_string_2.get()
        root.append(string1)
        root.append(string2)
        save_to = xml.Element('save_to')
        save_to.text = self.my_var_concate_save_to.get()
        root.append(save_to)
        
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def split_string(self, new_card):
        self.reset_all('Split String')

        self.lbl_string_variable = Label(self.parent_frame, text="String Variable:")
        self.my_var_split_string_variable = StringVar()
        self.my_combo_split_string_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_split_string_variable)
        self.my_combo_split_string_variable['values'] = tuple(variable_dict.keys())
        self.my_combo_split_string_variable.current(0)
        self.lbl_string_variable.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_split_string_variable.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_string_list = Label(self.parent_frame, text="String List:")
        self.my_var_split_string_list = StringVar()
        self.my_combo_split_string_list = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_split_string_list)
        self.my_combo_split_string_list['values'] = tuple(variable_dict.keys())
        self.my_combo_split_string_list.current(0)
        self.lbl_string_list.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_split_string_list.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_string_delimiter = Label(self.parent_frame, text="Delimiter:")
        self.entry_string_delimiter = Entry(self.parent_frame, width = 30)
        self.lbl_string_delimiter.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_string_delimiter.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_split_string(new_card, 'split_string'))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)

        string_variable, string_list, delimiter = self.read_file_from_xml.read_xml_split_string(new_card)
        if(string_variable !=""):
            self.my_combo_split_string_variable.set(string_variable)
        if(string_list != ""):
            self.my_combo_split_string_list.set(string_list)
        self.entry_string_delimiter.insert(0, delimiter)
    
    def manipulate_string(self, new_card, name):
        self.reset_all(name)

        self.lbl_string_variable = Label(self.parent_frame, text="Source String:")
        self.my_var_split_string_variable = StringVar()
        self.my_combo_split_string_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_split_string_variable)
        self.my_combo_split_string_variable['values'] = tuple(variable_dict.keys())
        self.my_combo_split_string_variable.current(0)
        self.lbl_string_variable.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_split_string_variable.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_string_list = Label(self.parent_frame, text="Destination String:")
        self.my_var_split_string_list = StringVar()
        self.my_combo_split_string_list = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_split_string_list)
        self.my_combo_split_string_list['values'] = tuple(variable_dict.keys())
        self.my_combo_split_string_list.current(0)
        self.lbl_string_list.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_split_string_list.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_split_string(new_card, name))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)

        source_string, destination_string = self.read_file_from_xml.read_xml_manipulate_string(new_card)
        if(source_string !=""):
            self.my_combo_split_string_variable.set(source_string)
        if(destination_string != ""):
            self.my_combo_split_string_list.set(destination_string)

    def concate_string(self, new_card):
        self.reset_all("Concate String")

        self.lbl_concate_string_1 = Label(self.parent_frame, text="String 1:")
        self.my_var_concate_string_1 = StringVar()
        self.my_combo_concate_string_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_concate_string_1)
        self.my_combo_concate_string_1['values'] = tuple(variable_dict.keys())
        self.my_combo_concate_string_1.current(0)
        self.lbl_concate_string_1.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_concate_string_1.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_concate_string_2 = Label(self.parent_frame, text="String 2:")
        self.my_var_concate_string_2 = StringVar()
        self.my_combo_concate_string_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_concate_string_2)
        self.my_combo_concate_string_2['values'] = tuple(variable_dict.keys())
        self.my_combo_concate_string_2.current(0)
        self.lbl_concate_string_2.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_concate_string_2.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_concate_save_to = Label(self.parent_frame, text="Save To:")
        self.my_var_concate_save_to = StringVar()
        self.my_combo_concate_save_to = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_concate_save_to)
        self.my_combo_concate_save_to['values'] = tuple(variable_dict.keys())
        self.my_combo_concate_save_to.current(0)
        self.lbl_concate_save_to.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_concate_save_to.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_concate_string(new_card))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)

        string_1, string_2, save_to = self.read_file_from_xml.read_xml_concate_string(new_card)
        if(string_1 !=""):
            self.my_combo_concate_string_1.set(string_1)
        if(string_2 !=""):
            self.my_combo_concate_string_2.set(string_2)
        if(save_to != ""):
            self.my_combo_concate_save_to.set(save_to)
    
    def save_increment_decrement(self, new_card, opt_type):
        root = xml.Element('root')
        action = xml.Element('action')
        action.text = opt_type
        root.append(action)
        _variable = xml.Element('_variable')
        _variable.text = self.my_var_variable.get()
        _variable_by = xml.Element('_variable_by')
        _variable_by.text = self.entry_variable_by.get()
        root.append(_variable)
        root.append(_variable_by)
        save_to = xml.Element('save_to')
        save_to.text = self.my_var_save_to.get()
        root.append(save_to)
        
        tree = xml.ElementTree(root)
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)


    def increment_decrement(self, new_card, opt_type):
        self.reset_all(opt_type)

        self.lbl_variable = Label(self.parent_frame, text="Variable :")
        self.my_var_variable = StringVar()
        self.my_combo_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_variable)
        self.my_combo_variable['values'] = tuple(variable_dict.keys())
        self.my_combo_variable.current(0)
        self.lbl_variable.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_variable.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_opt_type= Label(self.parent_frame, text= opt_type + " by:")
        self.entry_variable_by = Entry(self.parent_frame, width = 26)
        self.lbl_opt_type.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_variable_by.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)


        self.lbl_save_to = Label(self.parent_frame, text="Save To:")
        self.my_var_save_to = StringVar()
        self.my_combo_save_to = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_save_to)
        self.my_combo_save_to['values'] = tuple(variable_dict.keys())
        self.my_combo_save_to.current(0)
        self.lbl_save_to.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_save_to.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_increment_decrement(new_card, opt_type))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)

        _variable, _variable_by, save_to = self.read_file_from_xml.read_xml_increment_decrement(new_card)
        if(_variable !=""):
            self.my_combo_variable.set(_variable)
        self.entry_variable_by.insert(0, _variable_by)
        if(save_to != ""):
            self.my_combo_save_to.set(save_to)


    def list_get_value(self, new_card):
        self.reset_all("Get Value")

        self.lbl_string_variable = Label(self.parent_frame, text="String Variable:")
        self.my_var_split_string_variable = StringVar()
        self.my_combo_split_string_variable = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_split_string_variable)
        self.my_combo_split_string_variable['values'] = tuple(variable_dict.keys())
        self.my_combo_split_string_variable.current(0)
        self.lbl_string_variable.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_split_string_variable.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_string_list = Label(self.parent_frame, text="String List:")
        self.my_var_split_string_list = StringVar()
        self.my_combo_split_string_list = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_split_string_list)
        self.my_combo_split_string_list['values'] = tuple(variable_dict.keys())
        self.my_combo_split_string_list.current(0)
        self.lbl_string_list.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_split_string_list.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_string_delimiter = Label(self.parent_frame, text="Index:")
        self.entry_string_delimiter = Entry(self.parent_frame, width = 30)
        self.lbl_string_delimiter.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_string_delimiter.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_split_string(new_card, 'list_get_value'))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)

        string_variable, string_list, delimiter = self.read_file_from_xml.read_xml_split_string(new_card)
        if(string_variable !=""):
            self.my_combo_split_string_variable.set(string_variable)
        if(string_list != ""):
            self.my_combo_split_string_list.set(string_list)
        self.entry_string_delimiter.insert(0, delimiter)


    def save_for_loop(self, new_card, action_name):

        root = xml.Element('root')
        action = xml.Element('action')
        action.text = action_name
        root.append(action)
        init_variable = xml.Element('init_variable')
        condition_for = xml.Element('condition_for')
        condition = xml.Element('condition')
        variable1 = xml.Element('variable1')
        variable2 = xml.Element('variable2')
        init_variable.text = self.my_for_loop_init.get()
        condition_for.text = self.my_var_combo_condition_for.get()
        condition.text = self.my_var_combo_condition.get()
        variable1.text = self.my_var_str_1.get()
        variable2.text = self.my_var_str_2.get()
        root.append(init_variable)
        root.append(condition_for)
        root.append(condition)
        root.append(variable1)
        root.append(variable2)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    def add_2_string(self, event):
        str_list = ['Greater Then', 'Less Then', 'Equal To', 'Greater Then Equal', 'Less Then Equal', 'Ends With', 'Starts With', 'Not In', 'Substring']
        if(self.my_combo_condition.get() in str_list):
            self.lbl_str_1 = Label(self.parent_frame, text="String 1:")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_2 = Label(self.parent_frame, text="String 2:")
            self.my_var_str_2 = StringVar()
            self.my_combo_str_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_2)
            self.my_combo_str_2['values'] = tuple(variable_dict.keys())
            self.my_combo_str_2.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.lbl_str_2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)
        else:
            self.lbl_str_1 = Label(self.parent_frame, text="String:   ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.empty_label_1 = Label(self.parent_frame, text="", width=50)
            self.empty_label_1.grid(row = 6, column = 0, padx = 10, pady = 10, columnspan=2, sticky=NW)
    
    def add_2_number(self, event):
        str_list = ['Greater Then', 'Less Then', 'Equal To', 'Greater Then Equal', 'Less Then Equal']
        if(self.my_combo_condition.get() in str_list):
            self.lbl_str_1 = Label(self.parent_frame, text="Number 1:")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_2 = Label(self.parent_frame, text="Number 2:")
            self.my_var_str_2 = StringVar()
            self.my_combo_str_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_2)
            self.my_combo_str_2['values'] = tuple(variable_dict.keys())
            self.my_combo_str_2.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.lbl_str_2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)


    def add_2_boolean(self, event):
        str_list = ['Equal To', 'Not Equal']
        if(self.my_combo_condition.get() in str_list):
            self.lbl_str_1 = Label(self.parent_frame, text="Variable 1:   ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_2 = Label(self.parent_frame, text="Variable 2:   ")
            self.my_var_str_2 = StringVar()
            self.my_combo_str_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_2)
            self.my_combo_str_2['values'] = tuple(variable_dict.keys())
            self.my_combo_str_2.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.lbl_str_2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)
        else:
            self.lbl_str_1 = Label(self.parent_frame, text="Variable:   ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.empty_label_1 = Label(self.parent_frame, text="", width=50)
            self.empty_label_1.grid(row = 6, column = 0, padx = 10, pady = 10, columnspan=2, sticky=NW)

    def add_2_list(self, event):
        str_list = ['In', 'Not In']
        if(self.my_combo_condition.get() in str_list):
            self.lbl_str_1 = Label(self.parent_frame, text="Variable:      ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_2 = Label(self.parent_frame, text="List:            ")
            self.my_var_str_2 = StringVar()
            self.my_combo_str_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_2)
            self.my_combo_str_2['values'] = tuple(variable_dict.keys())
            self.my_combo_str_2.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.lbl_str_2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)
        else:
            self.lbl_str_1 = Label(self.parent_frame, text="List:         ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.empty_label_1 = Label(self.parent_frame, text="", width=50)
            self.empty_label_1.grid(row = 6, column = 0, padx = 10, pady = 10, columnspan=2, sticky=NW)
    
    def add_2_dictionary(self, event):
        str_list = ['Key Exist', 'Key Not Exist']
        if(self.my_combo_condition.get() in str_list):
            self.lbl_str_1 = Label(self.parent_frame, text="Key:             ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_2 = Label(self.parent_frame, text="Dictionary:        ")
            self.my_var_str_2 = StringVar()
            self.my_combo_str_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_2)
            self.my_combo_str_2['values'] = tuple(variable_dict.keys())
            self.my_combo_str_2.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.lbl_str_2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)
        else:
            self.lbl_str_1 = Label(self.parent_frame, text="Dictionary:      ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.empty_label_1 = Label(self.parent_frame, text="", width=50)
            self.empty_label_1.grid(row = 6, column = 0, padx = 10, pady = 10, columnspan=2, sticky=NW)


    def add_2_web(self, event):
        str_list = ['Element To Be Clickable', 'Element To Be Selected', 'Presence Of Element', 'Visibility of Element']
        str_list2 = ['Title Is','Title Contains', 'Url Is', 'Url Contains']
        str_list3 = ['Presence of Text in Element']
        if(self.my_combo_condition.get() in str_list3):
            self.lbl_str_1 = Label(self.parent_frame, text="Text:             ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_2 = Label(self.parent_frame, text="Element:        ")
            self.my_var_str_2 = StringVar()
            self.my_combo_str_2 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_2)
            self.my_combo_str_2['values'] = tuple(variable_dict.keys())
            self.my_combo_str_2.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.lbl_str_2.grid(row = 6, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_2.grid(row = 6, column = 1, padx = 10, pady = 10, sticky=NW)
        elif(self.my_combo_condition.get() in str_list2):
            self.lbl_str_1 = Label(self.parent_frame, text="Input:          ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.empty_label_1 = Label(self.parent_frame, text="", width=50)
            self.empty_label_1.grid(row = 6, column = 0, padx = 10, pady = 10, columnspan=2, sticky=NW)
        elif(self.my_combo_condition.get() in str_list):
            self.lbl_str_1 = Label(self.parent_frame, text="Element:          ")
            self.my_var_str_1 = StringVar()
            self.my_combo_str_1 = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_str_1)
            self.my_combo_str_1['values'] = tuple(variable_dict.keys())
            self.my_combo_str_1.current(0)
            self.lbl_str_1.grid(row = 5, column = 0, padx = 10, pady = 10, sticky=NW)
            self.my_combo_str_1.grid(row = 5, column = 1, padx = 10, pady = 10, sticky=NW)
            self.empty_label_1 = Label(self.parent_frame, text="", width=50)
            self.empty_label_1.grid(row = 6, column = 0, padx = 10, pady = 10, columnspan=2, sticky=NW)
    
    def update_conditions(self, event):
        if(self.my_var_combo_condition_for.get() == 'String'):
            self.my_combo_condition['values'] = self.string_list
            self.my_combo_condition.current(0)
            self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_string)
        elif(self.my_var_combo_condition_for.get() == 'Number'):
            self.my_combo_condition['values'] = self.number_list
            self.my_combo_condition.current(0)
            self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_number)
        elif(self.my_var_combo_condition_for.get() == 'Boolean'):
            self.my_combo_condition['values'] = self.boolean_list
            self.my_combo_condition.current(0)
            self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_boolean)
        elif(self.my_var_combo_condition_for.get() == 'List'):
            self.my_combo_condition['values'] = self.list_list
            self.my_combo_condition.current(0)
            self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_list)
        elif(self.my_var_combo_condition_for.get() == 'Dictionary'):
            self.my_combo_condition['values'] = self.dictionary_list
            self.my_combo_condition.current(0)
            self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_dictionary)
        elif(self.my_var_combo_condition_for.get() == 'Web'):
            self.my_combo_condition['values'] = self.web_list
            self.my_combo_condition.current(0)
            self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_web)

    def for_loop(self, new_card):
        self.reset_all('For Loop')

        self.lbl_init_variable = Label(self.parent_frame, text="Init Variable:")

        self.my_for_loop_init = StringVar()
        self.my_combo_for_loop_init = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_for_loop_init)
        self.my_combo_for_loop_init['values'] = tuple(variable_dict.keys())
        self.my_combo_for_loop_init.current(0)
        self.lbl_init_variable.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_for_loop_init.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)

        self.lbl_condition_details = Label(self.parent_frame, text="Condition Details:")
        self.lbl_condition_for = Label(self.parent_frame, text="Condition For:")

        self.my_var_combo_condition_for = StringVar()
        self.my_combo_condition_for = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_combo_condition_for)
        self.my_combo_condition_for['values'] = ('String', 'Number', 'Boolean', 'List', 'Dictionary', 'Web', 'Excel')
        self.my_combo_condition_for.current(0)
        
        self.lbl_condition_details.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.lbl_condition_for.grid(row = 3, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_condition_for.grid(row = 3, column = 1, padx = 10, pady = 10, sticky=NW)

        self.string_list = ('Greater Then', 'Less Then', 'Equal To', 'Substring', 'Starts With', 'Ends With', 'Not In', 'IsEmpty', 'IsNumber', 'IsAlpha', 'IsTitle', 'IsUpper', 'IsLower')
        self.number_list = ('Greater Then', 'Less Then', 'Equal To', 'Not Equal', 'Greater Then Equal', 'Less Then Equal')
        self.boolean_list = ('IsTrue', 'IsFalse', 'Equal To', 'Not Equal')
        self.list_list = ('In', 'Not In', 'IsEmpty')
        self.dictionary_list = ('Key Exist', 'Key Not Exist', 'IsEmpty')
        self.web_list = ('Element To Be Clickable', 'Element To Be Selected', 'Presence Of Element', 'Visibility of Element', 'Title Is','Title Contains', 'Url Is', 'Url Contains', 'Presence of Text in Element')

        self.lbl_condition = Label(self.parent_frame, text="Condition:")
        self.my_var_combo_condition = StringVar()
        self.my_combo_condition = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_var_combo_condition)
        self.my_combo_condition['values'] = self.string_list
        self.my_combo_condition.current(0)
        self.my_combo_condition_for.bind('<<ComboboxSelected>>', self.update_conditions)
        self.my_combo_condition.bind('<<ComboboxSelected>>', self.add_2_string)
        self.lbl_condition.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=NW)
        self.my_combo_condition.grid(row = 4, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_for_loop(new_card, 'for_loop'))
        btn_save.grid(row = 7, column = 0, padx = 10, pady = 10, sticky=NW)

        #locator_name, locator_value, value = self.read_file_from_xml.read_xml_input_text(new_card)
        #self.deselect_locator_checkbox(locator_name, locator_value)
        #self.entry_value.insert(0, value)

    def save_select_option(self, new_card):
        root = xml.Element('root')
        locator_name = None
        locator_value = None
        select_by_name = None
        select_by_value = None

        locator_value = self.save_check_box()

        if(self.var_select_by.get() == 'index'):
            select_by_value = xml.Element('select_by_value')
            select_by_value.text = self.entry_select_by_index.get()
        elif(self.var_select_by.get() == 'value'):
            select_by_value = xml.Element('select_by_value')
            select_by_value.text = self.entry_select_by_value.get()
        elif(self.var_select_by.get() == 'visible_text'):
            select_by_value = xml.Element('select_by_value')
            select_by_value.text = self.entry_select_by_visible_text.get()
        elif(self.var_select_by.get() == 'deselect_all'):
            select_by_value = xml.Element('select_by_value')
            select_by_value.text = 'deselect_all'
        
        action = xml.Element('action')
        action.text = "select_option"
        locator_name = xml.Element('locator_name')
        locator_name.text = self.var_locator.get()
        select_by_name = xml.Element('select_by_name')
        select_by_name.text = self.var_select_by.get()
        root.append(action)
        root.append(locator_name)
        root.append(locator_value)
        root.append(select_by_name)
        root.append(select_by_value)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)

    
    def select_option(self, new_card):
        self.reset_all('Select Option')

        self.create_input_ui(1)
        row_index = 10

        self.lbl_select_by = Label(self.parent_frame, text="Select By:")
        self.lbl_select_by.grid(row = row_index, column = 0, padx = 10, sticky=NW)
        
        self.var_select_by = StringVar()
        self.my_select_by_visible_text = Checkbutton(self.parent_frame, command = self.activateSelectBy, text="Visible Text", variable=self.var_select_by, onvalue="visible_text", offvalue="off", anchor = 'w')
        self.my_select_by_visible_text.deselect()
        self.entry_select_by_visible_text = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_select_by_visible_text.grid(row = row_index + 1, column = 0, padx = 10, sticky=NW)
        self.entry_select_by_visible_text.grid(row = row_index + 1, column = 1, padx = 10, sticky=NW)

        self.my_select_by_index = Checkbutton(self.parent_frame, command = self.activateSelectBy, text="Index", variable=self.var_select_by, onvalue="index", offvalue="off", anchor = 'w')
        self.my_select_by_index.deselect()
        self.entry_select_by_index = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_select_by_index.grid(row = row_index + 2, column = 0, padx = 10, sticky=NW)
        self.entry_select_by_index.grid(row = row_index + 2, column = 1, padx = 10, sticky=NW)

        self.my_select_by_value = Checkbutton(self.parent_frame, command = self.activateSelectBy, text="Value", variable=self.var_select_by, onvalue="value", offvalue="off", anchor = 'w')
        self.my_select_by_value.deselect()
        self.entry_select_by_value = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_select_by_value.grid(row = row_index + 3, column = 0, padx = 10, sticky=NW)
        self.entry_select_by_value.grid(row = row_index + 3, column = 1, padx = 10, sticky=NW)

        self.my_deselect_all = Checkbutton(self.parent_frame, command = self.activateSelectBy, text="Deselect All", variable=self.var_select_by, onvalue="deselect_all", offvalue="off", anchor = 'w')
        self.my_deselect_all.deselect()
        self.my_deselect_all.grid(row = row_index + 4, column = 0, padx = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_select_option(new_card))
        btn_save.grid(row = row_index + 5, column = 0, padx = 10, pady = 10, sticky=NW)

        locator_name, locator_value, select_by_name, select_by_value = self.read_file_from_xml.read_xml_select_option(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
        self.deselect_select_by_checkbox(select_by_name, select_by_value)

    def save_drag_and_drop(self, new_card):
        root = xml.Element('root')
        locator_name = None
        locator_value = None
        locator_name_target = None
        locator_value_target = None

        locator_value = self.save_check_box()
        locator_value_target = self.save_check_box_target()
        
        action = xml.Element('action')
        action.text = "drag_and_drop"
        locator_name = xml.Element('locator_name')
        locator_name.text = self.var_locator.get()
        locator_name_target = xml.Element('locator_name_target')
        locator_name_target.text = self.var_locator_target.get()
        root.append(action)
        root.append(locator_name)
        root.append(locator_value)
        root.append(locator_name_target)
        root.append(locator_value_target)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
    
    def drag_and_drop(self, new_card):
        self.reset_all('Drag And Drop')

        self.lbl_select_by = Label(self.parent_frame, text="Source:")
        self.lbl_select_by.grid(row = 1, column = 0, padx = 10, sticky=NW)

        self.create_input_ui(2)

        self.lbl_select_by = Label(self.parent_frame, text="Target :")
        self.lbl_select_by.grid(row = 11, column = 0, padx = 10, sticky=NW)

        row_start = 12
        self.var_locator_target = StringVar()
        self.my_check_xpath_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="xPath", variable=self.var_locator_target, onvalue="xpath", offvalue="off", anchor = 'w')
        #self.my_check_xpath.deselect()
        self.entry_xpath_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_xpath_target.grid(row = row_start, column = 0, padx = 10, sticky=NW)
        self.entry_xpath_target.grid(row = row_start, column = 1, padx = 10, sticky=NW)

        self.my_check_name_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="Name", variable=self.var_locator_target, onvalue="name", offvalue="off", anchor = 'w')
        #self.my_check_name.deselect()
        self.entry_name_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_name_target.grid(row = row_start + 1, column = 0, padx = 10, sticky=NW)
        self.entry_name_target.grid(row = row_start + 1, column = 1, padx = 10, sticky=NW)

        self.my_check_id_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="ID", variable=self.var_locator_target, onvalue="id", offvalue="off", anchor = 'w')
        #self.my_check_id.deselect()
        self.entry_id_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_id_target.grid(row = row_start + 2, column = 0, padx = 10, sticky=NW)
        self.entry_id_target.grid(row = row_start + 2, column = 1, padx = 10, sticky=NW)

        self.my_check_class_name_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="Class Name", variable=self.var_locator_target, onvalue="class_name", offvalue="off", anchor = 'w')
        #self.my_check_class_name.deselect()
        self.entry_class_name_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_class_name_target.grid(row = row_start + 3, column = 0, padx = 10, sticky=NW)
        self.entry_class_name_target.grid(row = row_start + 3, column = 1, padx = 10, sticky=NW)

        self.my_check_tag_name_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="Tag Name", variable=self.var_locator_target, onvalue="tag_name", offvalue="off", anchor = 'w')
        #self.my_check_tag_name.deselect()
        self.entry_tag_name_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_tag_name_target.grid(row = row_start + 4, column = 0, padx = 10,  sticky=NW)
        self.entry_tag_name_target.grid(row = row_start + 4, column = 1, padx = 10, sticky=NW)

        self.my_check_css_selector_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="CSS Selector", variable=self.var_locator_target, onvalue="css_selector", offvalue="off")
        #self.my_check_css_selector.deselect()
        self.entry_css_selector_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_css_selector_target.grid(row = row_start + 5, column = 0, padx = 10,  sticky=NW)
        self.entry_css_selector_target.grid(row = row_start + 5, column = 1, padx = 10, sticky=NW)

        self.my_check_link_text_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="Link Text", variable=self.var_locator_target, onvalue="link_text", offvalue="off" , anchor = 'w')
        #self.my_check_link_text.deselect()
        self.entry_link_text_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_link_text_target.grid(row = row_start + 6, column = 0, padx = 10, sticky=NW)
        self.entry_link_text_target.grid(row = row_start + 6, column = 1, padx = 10, sticky=NW)

        self.my_check_partial_link_text_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="Partial Link Text", variable=self.var_locator_target, onvalue="partial_link_text", offvalue="off", anchor = 'w')
        self.my_check_partial_link_text_target.deselect()
        self.entry_partial_link_text_target = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_partial_link_text_target.grid(row = row_start + 7, column = 0, padx = 10, sticky=NW)
        self.entry_partial_link_text_target.grid(row = row_start + 7, column = 1, padx = 10, sticky=NW)

        self.my_check_element_target = Checkbutton(self.parent_frame, command = self.activateEntryTarget, text="Element", variable=self.var_locator_target, onvalue="element", offvalue="off", anchor = 'w')
        self.my_check_element_target.deselect()
        self.my_element_target = StringVar()
        self.my_combo_element_target = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_element_target, state='disabled')
        self.my_combo_element_target['values'] = tuple(variable_dict.keys())
        self.my_combo_element_target.current(0)
        self.my_check_element_target.grid(row = row_start + 8, column = 0, padx = 10, sticky=NW)
        self.my_combo_element_target.grid(row = row_start + 8, column = 1, padx = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_drag_and_drop(new_card))
        btn_save.grid(row = row_start + 9, column = 0, padx = 10, pady = 10, sticky=NW)

        locator_name, locator_value, locator_name_target, locator_value_target = self.read_file_from_xml.read_xml_drag_and_drop(new_card)
        self.deselect_locator_checkbox(locator_name, locator_value)
        self.deselect_locator_checkbox_target(locator_name_target, locator_value_target)
    
    
    def activateSelectBy(self):
        self.entry_select_by_index.config(state=DISABLED)
        self.entry_select_by_value.config(state=DISABLED)
        self.entry_select_by_visible_text.config(state=DISABLED)
        if(self.var_select_by.get() == 'index'):
            self.entry_select_by_index.config(state=NORMAL)
        if(self.var_select_by.get() == 'value'):
            self.entry_select_by_value.config(state=NORMAL)
        if(self.var_select_by.get() == 'visible_text'):
            self.entry_select_by_visible_text.config(state=NORMAL)

    def activateSwitchTo(self):
        self.entry_switch_to_window.config(state=DISABLED)
        self.entry_switch_to_frame.config(state=DISABLED)
        if(self.var_switch_to.get() == 'window'):
            self.entry_switch_to_window.config(state=NORMAL)
        if(self.var_switch_to.get() == 'frame'):
            self.entry_switch_to_frame.config(state=NORMAL)

    def create_input_ui(self, row_start):

        self.var_locator = StringVar()
        self.my_check_xpath = Checkbutton(self.parent_frame, command = self.activateEntry, text="xPath", variable=self.var_locator, onvalue="xpath", offvalue="off", anchor = 'w')
        #self.my_check_xpath.deselect()
        self.entry_xpath = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_xpath.grid(row = row_start, column = 0, padx = 10, sticky=NW)
        self.entry_xpath.grid(row = row_start, column = 1, padx = 10, sticky=NW)

        self.my_check_name = Checkbutton(self.parent_frame, command = self.activateEntry, text="Name", variable=self.var_locator, onvalue="name", offvalue="off", anchor = 'w')
        #self.my_check_name.deselect()
        self.entry_name = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_name.grid(row = row_start + 1, column = 0, padx = 10, sticky=NW)
        self.entry_name.grid(row = row_start + 1, column = 1, padx = 10, sticky=NW)

        self.my_check_id = Checkbutton(self.parent_frame, command = self.activateEntry, text="ID", variable=self.var_locator, onvalue="id", offvalue="off", anchor = 'w')
        #self.my_check_id.deselect()
        self.entry_id = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_id.grid(row = row_start + 2, column = 0, padx = 10, sticky=NW)
        self.entry_id.grid(row = row_start + 2, column = 1, padx = 10, sticky=NW)

        self.my_check_class_name = Checkbutton(self.parent_frame, command = self.activateEntry, text="Class Name", variable=self.var_locator, onvalue="class_name", offvalue="off", anchor = 'w')
        #self.my_check_class_name.deselect()
        self.entry_class_name = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_class_name.grid(row = row_start + 3, column = 0, padx = 10, sticky=NW)
        self.entry_class_name.grid(row = row_start + 3, column = 1, padx = 10, sticky=NW)

        self.my_check_tag_name = Checkbutton(self.parent_frame, command = self.activateEntry, text="Tag Name", variable=self.var_locator, onvalue="tag_name", offvalue="off", anchor = 'w')
        #self.my_check_tag_name.deselect()
        self.entry_tag_name = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_tag_name.grid(row = row_start + 4, column = 0, padx = 10,  sticky=NW)
        self.entry_tag_name.grid(row = row_start + 4, column = 1, padx = 10, sticky=NW)

        self.my_check_css_selector = Checkbutton(self.parent_frame, command = self.activateEntry, text="CSS Selector", variable=self.var_locator, onvalue="css_selector", offvalue="off")
        #self.my_check_css_selector.deselect()
        self.entry_css_selector = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_css_selector.grid(row = row_start + 5, column = 0, padx = 10,  sticky=NW)
        self.entry_css_selector.grid(row = row_start + 5, column = 1, padx = 10, sticky=NW)

        self.my_check_link_text = Checkbutton(self.parent_frame, command = self.activateEntry, text="Link Text", variable=self.var_locator, onvalue="link_text", offvalue="off" , anchor = 'w')
        #self.my_check_link_text.deselect()
        self.entry_link_text = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_link_text.grid(row = row_start + 6, column = 0, padx = 10, sticky=NW)
        self.entry_link_text.grid(row = row_start + 6, column = 1, padx = 10, sticky=NW)

        self.my_check_partial_link_text = Checkbutton(self.parent_frame, command = self.activateEntry, text="Partial Link Text", variable=self.var_locator, onvalue="partial_link_text", offvalue="off", anchor = 'w')
        self.my_check_partial_link_text.deselect()
        self.entry_partial_link_text = Entry(self.parent_frame, width = 30, state='disabled')
        self.my_check_partial_link_text.grid(row = row_start + 7, column = 0, padx = 10, sticky=NW)
        self.entry_partial_link_text.grid(row = row_start + 7, column = 1, padx = 10, sticky=NW)

        self.my_check_element = Checkbutton(self.parent_frame, command = self.activateEntry, text="Element", variable=self.var_locator, onvalue="element", offvalue="off", anchor = 'w')
        self.my_check_element.deselect()
        self.my_element = StringVar()
        self.my_combo_element = ttk.Combobox(self.parent_frame, width = 26, textvariable = self.my_element, state='disabled')
        self.my_combo_element['values'] = tuple(variable_dict.keys())
        self.my_combo_element.current(0)
        self.my_check_element.grid(row = row_start + 8, column = 0, padx = 10, sticky=NW)
        self.my_combo_element.grid(row = row_start + 8, column = 1, padx = 10, sticky=NW)

    def activateEntry(self):
        self.entry_xpath.config(state=DISABLED)
        self.entry_id.config(state=DISABLED)
        self.entry_name.config(state=DISABLED)
        self.entry_tag_name.config(state=DISABLED)
        self.entry_class_name.config(state=DISABLED)
        self.entry_css_selector.config(state=DISABLED)
        self.entry_link_text.config(state=DISABLED)
        self.entry_partial_link_text.config(state=DISABLED)
        self.my_combo_element.config(state=DISABLED)
        if(self.var_locator.get() == 'xpath'):
            self.entry_xpath.config(state=NORMAL)
        if(self.var_locator.get() == 'id'):
            self.entry_id.config(state=NORMAL)
        if(self.var_locator.get() == 'name'):
            self.entry_name.config(state=NORMAL)
        if(self.var_locator.get() == 'tag_name'):
            self.entry_tag_name.config(state=NORMAL)
        if(self.var_locator.get() == 'class_name'):
            self.entry_class_name.config(state=NORMAL)
        if(self.var_locator.get() == 'link_text'):
            self.entry_link_text.config(state=NORMAL)
        if(self.var_locator.get() == 'partial_link_text'):
            self.entry_partial_link_text.config(state=NORMAL)
        if(self.var_locator.get() == 'css_selector'):
            self.entry_css_selector.config(state=NORMAL)
        if(self.var_locator.get() == 'element'):
            self.my_combo_element.config(state=NORMAL)

    def activateEntryTarget(self):
        self.entry_xpath_target.config(state=DISABLED)
        self.entry_id_target.config(state=DISABLED)
        self.entry_name_target.config(state=DISABLED)
        self.entry_tag_name_target.config(state=DISABLED)
        self.entry_class_name_target.config(state=DISABLED)
        self.entry_css_selector_target.config(state=DISABLED)
        self.entry_link_text_target.config(state=DISABLED)
        self.entry_partial_link_text_target.config(state=DISABLED)
        self.my_combo_element_target.config(state=DISABLED)
        if(self.var_locator_target.get() == 'xpath'):
            self.entry_xpath_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'id'):
            self.entry_id_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'name'):
            self.entry_name_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'tag_name'):
            self.entry_tag_name_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'class_name'):
            self.entry_class_name_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'link_text'):
            self.entry_link_text_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'partial_link_text'):
            self.entry_partial_link_text_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'css_selector'):
            self.entry_css_selector_target.config(state=NORMAL)
        if(self.var_locator_target.get() == 'element'):
            self.my_combo_element_target.config(state=NORMAL)

    def update_create_ui(self):
        pass

    def deselect_locator_checkbox(self, locator_name, locator_value):
        if(locator_name == 'xpath'):
            self.my_check_xpath.select()
            self.entry_xpath.config(state=NORMAL)
            self.entry_xpath.insert(0, locator_value)
        elif(locator_name == 'id'):
            self.my_check_id.select()
            self.entry_id.config(state=NORMAL)
            self.entry_id.insert(0, locator_value)
        elif(locator_name == 'name'):
            self.my_check_name.select()
            self.entry_name.config(state=NORMAL)
            self.entry_name.insert(0, locator_value)
        elif(locator_name == 'class_name'):
            self.my_check_class_name.select()
            self.entry_class_name.config(state=NORMAL)
            self.entry_class_name.insert(0, locator_value)
        elif(locator_name == 'tag_name'):
            self.my_check_tag_name.select()
            self.entry_tag_name.config(state=NORMAL)
            self.entry_tag_name.insert(0, locator_value)
        elif(locator_name == 'css_selector'):
            self.my_check_css_selector.select()
            self.entry_css_selector.config(state=NORMAL)
            self.entry_css_selector.insert(0, locator_value)
        elif(locator_name == 'link_text'):
            self.my_check_link_text.select()
            self.entry_link_text.config(state=NORMAL)
            self.entry_link_text.insert(0, locator_value)
        elif(locator_name == 'partial_link_text'):
            self.my_check_partial_link_text.select()
            self.entry_partial_link_text.config(state=NORMAL)
            self.entry_partial_link_text.insert(0, locator_value)
        elif(locator_name == 'element'):
            self.my_check_element.select()
            self.my_combo_element.config(state=NORMAL)
            self.my_combo_element.insert(0, locator_value)

    def deselect_locator_checkbox_target(self, locator_name_target, locator_value_target):
        if(locator_name_target == 'xpath'):
            self.my_check_xpath_target.select()
            self.entry_xpath_target.config(state=NORMAL)
            self.entry_xpath_target.insert(0, locator_value_target)
        elif(locator_name_target == 'id'):
            self.my_check_id_target.select()
            self.entry_id_target.config(state=NORMAL)
            self.entry_id_target.insert(0, locator_value_target)
        elif(locator_name_target == 'name'):
            self.my_check_name_target.select()
            self.entry_name_target.config(state=NORMAL)
            self.entry_name_target.insert(0, locator_value_target)
        elif(locator_name_target == 'class_name'):
            self.my_check_class_name_target.select()
            self.entry_class_name_target.config(state=NORMAL)
            self.entry_class_name_target.insert(0, locator_value_target)
        elif(locator_name_target == 'tag_name'):
            self.my_check_tag_name_target.select()
            self.entry_tag_name_target.config(state=NORMAL)
            self.entry_tag_name_target.insert(0, locator_value_target)
        elif(locator_name_target == 'css_selector'):
            self.my_check_css_selector_target.select()
            self.entry_css_selector_target.config(state=NORMAL)
            self.entry_css_selector_target.insert(0, locator_value_target)
        elif(locator_name_target == 'link_text'):
            self.my_check_link_text_target.select()
            self.entry_link_text_target.config(state=NORMAL)
            self.entry_link_text_target.insert(0, locator_value_target)
        elif(locator_name_target == 'partial_link_text'):
            self.my_check_partial_link_text_target.select()
            self.entry_partial_link_text_target.config(state=NORMAL)
            self.entry_partial_link_text_target.insert(0, locator_value_target)
        elif(locator_name_target == 'element'):
            self.my_check_element_target.select()
            self.my_combo_element_target.config(state=NORMAL)
            self.my_combo_element_target.insert(0, locator_value_target)
    
    def deselect_select_by_checkbox(self, select_by_name, select_by_value):
        if(select_by_name == 'index'):
            self.my_select_by_index.select()
            self.entry_select_by_index.config(state=NORMAL)
            self.entry_select_by_index.insert(0, select_by_value)
        elif(select_by_name == 'value'):
            self.my_select_by_value.select()
            self.entry_select_by_value.config(state=NORMAL)
            self.entry_select_by_value.insert(0, select_by_value)
        elif(select_by_name == 'visible_text'):
            self.my_select_by_visible_text.select()
            self.entry_select_by_visible_text.config(state=NORMAL)
            self.entry_select_by_visible_text.insert(0, select_by_value)
        elif(select_by_name == 'deselect_all'):
            self.my_deselect_all.select()

    def save_check_box(self):
        locator_value = xml.Element('locator_value')
        if(self.var_locator.get() == "xpath"):
            locator_value.text = self.entry_xpath.get()
        elif(self.var_locator.get() == "id"):
            locator_value.text = self.entry_id.get()
        elif(self.var_locator.get() == "name"):
            locator_value.text = self.entry_name.get()
        elif(self.var_locator.get() == "class_name"):
            locator_value.text = self.entry_class_name.get()
        elif(self.var_locator.get() == "tag_name"):
            locator_value.text = self.entry_tag_name.get()
        elif(self.var_locator.get() == "css_selector"):
            locator_value.text = self.entry_css_selector.get()
        elif(self.var_locator.get() == "link_text"):
            locator_value.text = self.entry_link_text.get()
        elif(self.var_locator.get() == "partial_link_text"):
            locator_value.text = self.entry_partial_link_text.get()
        elif(self.var_locator.get() == "element"):
            locator_value.text = self.my_combo_element.get()
        return locator_value

    def save_check_box_target(self):
        locator_value_target = xml.Element('locator_value_target')
        if(self.var_locator_target.get() == "xpath"):
            locator_value_target.text = self.entry_xpath_target.get()
        elif(self.var_locator_target.get() == "id"):
            locator_value_target.text = self.entry_id_target.get()
        elif(self.var_locator_target.get() == "name"):
            locator_value_target.text = self.entry_name_target.get()
        elif(self.var_locator_target.get() == "class_name"):
            locator_value_target.text = self.entry_class_name_target.get()
        elif(self.var_locator_target.get() == "tag_name"):
            locator_value_target.text = self.entry_tag_name_target.get()
        elif(self.var_locator_target.get() == "css_selector"):
            locator_value_target.text = self.entry_css_selector_target.get()
        elif(self.var_locator_target.get() == "link_text"):
            locator_value_target.text = self.entry_link_text_target.get()
        elif(self.var_locator_target.get() == "partial_link_text"):
            locator_value_target.text = self.entry_partial_link_text_target.get()
        elif(self.var_locator_target.get() == "element"):
            locator_value_target.text = self.my_combo_element_target.get()
        return locator_value_target

    def save_create_variable(self, new_card, type_name):
        root = xml.Element('root')
        variable_name = xml.Element('variable_name')
        variable_value = xml.Element('variable_value')
        _type = xml.Element('type')
        variable_name.text = self.entry_variable_name.get()
        variable_value.text = self.entry_variable_value.get()
        _type.text = type_name
        MyVariables.create_variable(self.entry_variable_name.get(), self.entry_variable_value.get(), type_name)
        action = xml.Element('action')
        action.text = "create_variable"
        root.append(action)
        root.append(variable_name)
        root.append(variable_value)
        root.append(_type)
        tree = xml.ElementTree(root)
        
        from xml.dom import minidom
        save_path_file = self.path + "\\" + new_card + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)


    def create_variable(self, new_card, type_name):
        self.reset_all("Create Variable")

        self.lbl_variable_name = Label(self.parent_frame, text="Variable Name:")
        self.entry_variable_name = Entry(self.parent_frame, width = 30)

        self.lbl_variable_value = Label(self.parent_frame, text="Initial Value:")
        self.entry_variable_value = Entry(self.parent_frame, width = 30)

        self.lbl_variable_name.grid(row = 1, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_variable_name.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NW)
        self.lbl_variable_value.grid(row = 2, column = 0, padx = 10, pady = 10, sticky=NW)
        self.entry_variable_value.grid(row = 2, column = 1, padx = 10, pady = 10, sticky=NW)

        btn_save = Button(self.parent_frame, text="Save", command = lambda: self.save_create_variable(new_card, type_name))
        btn_save.grid(row = 4, column = 0, padx = 10, pady = 10, sticky=W)

        variable_name, variable_value = self.read_file_from_xml.read_xml_create_variable(new_card)
        self.entry_variable_name.insert(0, variable_name)
        self.entry_variable_value.insert(0, variable_value)