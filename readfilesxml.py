from tkinter import Variable
from xml.dom import minidom
import os.path
from global_instance import *

# parse an xml file by name
class ReadFileFromXML():
    def __init__(self, *args, **kwargs):
        self.file_path = my_path + "files\\"

    def read_xml_open_url(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            url = mydoc.getElementsByTagName('link')
            browser = mydoc.getElementsByTagName('browser')
            session = mydoc.getElementsByTagName('session')
            return url[0].firstChild.data, browser[0].firstChild.data, session[0].firstChild.data    
        return "", "Google Chrome", ""

    def read_xml_close_browser(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            return session[0].firstChild.data    
        return ""
    def read_xml_navigation(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            navigation = mydoc.getElementsByTagName('navigation')
            return navigation[0].firstChild.data    
        return ""
    
    def read_xml_switch_to(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            switch_to = mydoc.getElementsByTagName('switch_to')
            value = mydoc.getElementsByTagName('value')
            return switch_to[0].firstChild.data, value[0].firstChild.data 
        return "", ""

    def read_xml_click(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            locator_name = mydoc.getElementsByTagName('locator_name')
            locator_value = mydoc.getElementsByTagName('locator_value')
            return locator_name[0].firstChild.data, locator_value[0].firstChild.data
        return "", ""

    def read_xml_clear(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            locator_name = mydoc.getElementsByTagName('locator_name')
            locator_value = mydoc.getElementsByTagName('locator_value')
            return locator_name[0].firstChild.data, locator_value[0].firstChild.data
        return "", "" 

    def read_xml_read_text(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            locator_name = mydoc.getElementsByTagName('locator_name')
            locator_value = mydoc.getElementsByTagName('locator_value')
            _variable = mydoc.getElementsByTagName('variable')
            return locator_name[0].firstChild.data, locator_value[0].firstChild.data, _variable[0].firstChild.data
        return "", "", ""
    
    def read_xml_message_box(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            _variable = mydoc.getElementsByTagName('variable')
            return _variable[0].firstChild.data
        return ""

    def read_xml_input_text(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            locator_name = mydoc.getElementsByTagName('locator_name')
            locator_value = mydoc.getElementsByTagName('locator_value')
            value = mydoc.getElementsByTagName('value')
            return locator_name[0].firstChild.data, locator_value[0].firstChild.data, value[0].firstChild.data
        return "", "", ""

    def read_xml_excel_open(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            location = mydoc.getElementsByTagName('location')
            filename = mydoc.getElementsByTagName('filename')
            return session[0].firstChild.data, location[0].firstChild.data, filename[0].firstChild.data    
        return "", "", "" 

    def read_xml_excel_create(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            location = mydoc.getElementsByTagName('location')
            filename = mydoc.getElementsByTagName('filename')
            return session[0].firstChild.data, location[0].firstChild.data, filename[0].firstChild.data    
        return "", "", "" 
    
    def read_xml_excel_delete_file(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            location = mydoc.getElementsByTagName('location')
            filename = mydoc.getElementsByTagName('filename')
            return location[0].firstChild.data, filename[0].firstChild.data    
        return "", ""

    def read_xml_excel_create_worksheet(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            sheetname = mydoc.getElementsByTagName('sheetname')
            position = mydoc.getElementsByTagName('position')
            value = mydoc.getElementsByTagName('value')
            return session[0].firstChild.data, sheetname[0].firstChild.data, position[0].firstChild.data, value[0].firstChild.data     
        return "", "", "", ""

    def read_xml_excel_delete_worksheet(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            sheetname = mydoc.getElementsByTagName('sheetname')
            return session[0].firstChild.data, sheetname[0].firstChild.data 
        return "", ""

    def read_xml_excel_save_workbook(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            location = mydoc.getElementsByTagName('location')
            filename = mydoc.getElementsByTagName('filename')
            return session[0].firstChild.data, location[0].firstChild.data, filename[0].firstChild.data
        return "", "", ""

    def read_xml_excel_set_value(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            sheetname = mydoc.getElementsByTagName('sheetname')
            cell = mydoc.getElementsByTagName('cell')
            value = mydoc.getElementsByTagName('value')
            return session[0].firstChild.data, sheetname[0].firstChild.data, cell[0].firstChild.data, value[0].firstChild.data
        return "", "", "", ""
    
    def read_xml_excel_set_formula(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            sheetname = mydoc.getElementsByTagName('sheetname')
            cell = mydoc.getElementsByTagName('cell')
            formula = mydoc.getElementsByTagName('formula')
            return session[0].firstChild.data, sheetname[0].firstChild.data, cell[0].firstChild.data, formula[0].firstChild.data
        return "", "", "", ""

    def read_xml_excel_get_value(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            sheetname = mydoc.getElementsByTagName('sheetname')
            cell = mydoc.getElementsByTagName('cell')
            save_to = mydoc.getElementsByTagName('variable')
            return session[0].firstChild.data, sheetname[0].firstChild.data, cell[0].firstChild.data, save_to[0].firstChild.data
        return "", "", "", ""

    def read_xml_excel_merge_unmerge(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            session = mydoc.getElementsByTagName('session')
            sheetname = mydoc.getElementsByTagName('sheetname')
            merge_unmerge = mydoc.getElementsByTagName('merge_unmerge')
            from_cell = mydoc.getElementsByTagName('from_cell')
            to_cell = mydoc.getElementsByTagName('from_cell')
            return session[0].firstChild.data, sheetname[0].firstChild.data, merge_unmerge[0].firstChild.data, from_cell[0].firstChild.data, to_cell[0].firstChild.data
        return "", "", "", "", ""

    def read_xml_excel_copy_paste(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            copy_session = mydoc.getElementsByTagName('copy_session')
            copy_sheetname = mydoc.getElementsByTagName('copy_sheetname')
            copy_start = mydoc.getElementsByTagName('copy_start')
            copy_end = mydoc.getElementsByTagName('copy_end')
            paste_session = mydoc.getElementsByTagName('paste_session')
            paste_sheetname = mydoc.getElementsByTagName('paste_sheetname')
            paste_start = mydoc.getElementsByTagName('paste_start')
            paste_end = mydoc.getElementsByTagName('paste_end')
            return copy_session[0].firstChild.data, copy_sheetname[0].firstChild.data, copy_start[0].firstChild.data, copy_end[0].firstChild.data, paste_session[0].firstChild.data, paste_sheetname[0].firstChild.data, paste_start[0].firstChild.data, paste_end[0].firstChild.data
        return "", "", "", "", "", "", "", ""
    
    def read_xml_select_option(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            locator_name = mydoc.getElementsByTagName('locator_name')
            locator_value = mydoc.getElementsByTagName('locator_value')
            select_by_name = mydoc.getElementsByTagName('select_by_name')
            select_by_value = mydoc.getElementsByTagName('select_by_value')
            return locator_name[0].firstChild.data, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data
        return "", "", "", ""
    
    def read_xml_drag_and_drop(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            locator_name = mydoc.getElementsByTagName('locator_name')
            locator_value = mydoc.getElementsByTagName('locator_value')
            locator_name_target = mydoc.getElementsByTagName('locator_name_target')
            locator_value_target = mydoc.getElementsByTagName('locator_value_target')
            return locator_name[0].firstChild.data, locator_value[0].firstChild.data, locator_name_target[0].firstChild.data, locator_value_target[0].firstChild.data
        return "", "", "", ""

    def read_xml_create_variable(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            variable_name = mydoc.getElementsByTagName('variable_name')
            variable_value = mydoc.getElementsByTagName('variable_value')
            return variable_name[0].firstChild.data, variable_value[0].firstChild.data
        return "", ""

    def read_xml_split_string(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            variable1 = mydoc.getElementsByTagName('variable1')
            variable2 = mydoc.getElementsByTagName('variable2')
            delimiter = mydoc.getElementsByTagName('delimiter')
            return variable1[0].firstChild.data, variable2[0].firstChild.data, delimiter[0].firstChild.data
        return "", "", ""
    
    def read_xml_manipulate_string(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            variable1 = mydoc.getElementsByTagName('variable1')
            variable2 = mydoc.getElementsByTagName('variable2')
            return variable1[0].firstChild.data, variable2[0].firstChild.data
        return "", ""

    def read_xml_concate_string(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            string1 = mydoc.getElementsByTagName('string1')
            string2 = mydoc.getElementsByTagName('string2')
            save_to = mydoc.getElementsByTagName('save_to')
            return string1[0].firstChild.data, string2[0].firstChild.data, save_to[0].firstChild.data
        return "", "", ""

    def read_xml_increment_decrement(self, new_card):
        path = self.file_path + new_card + '.xml'
        if(os.path.isfile(path)):
            mydoc = minidom.parse(path)
            item = mydoc.getElementsByTagName('root')
            _variable = mydoc.getElementsByTagName('_variable')
            _variable_by = mydoc.getElementsByTagName('_variable_by')
            save_to = mydoc.getElementsByTagName('save_to')
            return _variable[0].firstChild.data, _variable_by[0].firstChild.data, save_to[0].firstChild.data
        return "", "", ""
                                                                   
        

