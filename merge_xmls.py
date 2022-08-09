from tkinter import Variable
from xml.dom import minidom
import xml.etree.ElementTree as xml
import os.path
from canvas import Canvas
from global_instance import *

class merge_xmls():
    def __init__(self, canvas, *args, **kwargs):
        self.file_path = my_path
        self.canvas = canvas
        self.cards = self.canvas.get_cards()
    
    def read_xmls(self):
        root = xml.Element('root')
        for card in self.cards:
            path = self.file_path +'files\\'+ card + '.xml'
            if(os.path.isfile(path)):
                mydoc = minidom.parse(path)
                item = mydoc.getElementsByTagName('action')
                if(item[0].firstChild.data == "openurl"):
                    url_data = mydoc.getElementsByTagName('link')
                    browser_data = mydoc.getElementsByTagName('browser')
                    session_data = mydoc.getElementsByTagName('session')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    link = xml.Element('url')
                    browser = xml.Element('browser')
                    action.set('type', 'openurl')
                    session.text = session_data[0].firstChild.data
                    link.text = url_data[0].firstChild.data
                    browser.text = browser_data[0].firstChild.data
                    action.append(session)
                    action.append(link)
                    action.append(browser)
                    root.append(action)
                if(item[0].firstChild.data == "close_browser"):
                    session_data = mydoc.getElementsByTagName('session')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    action.set('type', 'close_browser')
                    session.text = session_data[0].firstChild.data
                    action.append(session)
                    root.append(action)
                if(item[0].firstChild.data == "navigation"):
                    navigation_data = mydoc.getElementsByTagName('navigation')
                    action = xml.Element('Action')
                    navigation = xml.Element('navigation')
                    action.set('type', 'navigation')
                    navigation.text = navigation_data[0].firstChild.data
                    action.append(navigation)
                    root.append(action)
                if(item[0].firstChild.data == "click"):
                    action = xml.Element('Action')
                    action.set('type', 'click')
                    locator_name_data = mydoc.getElementsByTagName('locator_name')
                    locator_value_data = mydoc.getElementsByTagName('locator_value')
                    locator_name = xml.Element('locator_name')
                    locator_value = xml.Element('locator_value')
                    locator_name.text = locator_name_data[0].firstChild.data
                    locator_value.text = locator_value_data[0].firstChild.data
                    action.append(locator_name)
                    action.append(locator_value)
                    root.append(action)
                if(item[0].firstChild.data == "clear"):
                    action = xml.Element('Action')
                    action.set('type', 'clear')
                    locator_name_data = mydoc.getElementsByTagName('locator_name')
                    locator_value_data = mydoc.getElementsByTagName('locator_value')
                    locator_name = xml.Element('locator_name')
                    locator_value = xml.Element('locator_value')
                    locator_name.text = locator_name_data[0].firstChild.data
                    locator_value.text = locator_value_data[0].firstChild.data
                    action.append(locator_name)
                    action.append(locator_value)
                    root.append(action)
                if(item[0].firstChild.data == "readtext" or item[0].firstChild.data == "get_element" or item[0].firstChild.data == "get_elements"):
                    variable_data = mydoc.getElementsByTagName('variable')
                    action = xml.Element('Action')
                    variable_name = xml.Element('variable')
                    variable_name.text = variable_data[0].firstChild.data
                    if(item[0].firstChild.data == "readtext"):
                        action.set('type', 'readtext')
                    elif(item[0].firstChild.data == "get_element"):
                        action.set('type', 'get_element')
                    elif(item[0].firstChild.data == "get_elements"):
                        action.set('type', 'get_elements')
                    locator_name_data = mydoc.getElementsByTagName('locator_name')
                    locator_value_data = mydoc.getElementsByTagName('locator_value')
                    locator_name = xml.Element('locator_name')
                    locator_value = xml.Element('locator_value')
                    locator_name.text = locator_name_data[0].firstChild.data
                    locator_value.text = locator_value_data[0].firstChild.data
                    action.append(locator_name)
                    action.append(locator_value)
                    action.append(variable_name)
                    root.append(action)
                if(item[0].firstChild.data == "inputtext"):
                    value_data = mydoc.getElementsByTagName('value')
                    action = xml.Element('Action')
                    value = xml.Element('value')
                    value.text = value_data[0].firstChild.data
                    action.set('type', 'inputtext')
                    locator_name_data = mydoc.getElementsByTagName('locator_name')
                    locator_value_data = mydoc.getElementsByTagName('locator_value')
                    locator_name = xml.Element('locator_name')
                    locator_value = xml.Element('locator_value')
                    locator_name.text = locator_name_data[0].firstChild.data
                    locator_value.text = locator_value_data[0].firstChild.data
                    action.append(locator_name)
                    action.append(locator_value)
                    action.append(value)
                    root.append(action)
                if(item[0].firstChild.data == "select_option"):
                    action = xml.Element('Action')
                    action.set('type', 'select_option')
                    locator_name_data = mydoc.getElementsByTagName('locator_name')
                    locator_value_data = mydoc.getElementsByTagName('locator_value')
                    select_by_name_data = mydoc.getElementsByTagName('select_by_name')
                    select_by_value_data = mydoc.getElementsByTagName('select_by_value')
                    locator_name = xml.Element('locator_name')
                    locator_value = xml.Element('locator_value')
                    select_by_name = xml.Element('select_by_name')
                    select_by_value = xml.Element('select_by_value')
                    locator_name.text = locator_name_data[0].firstChild.data
                    locator_value.text = locator_value_data[0].firstChild.data
                    select_by_name.text = select_by_name_data[0].firstChild.data
                    select_by_value.text = select_by_value_data[0].firstChild.data
                    action.append(locator_name)
                    action.append(locator_value)
                    action.append(select_by_name)
                    action.append(select_by_value)
                    root.append(action)
                if(item[0].firstChild.data == "drag_and_drop"):
                    action = xml.Element('Action')
                    action.set('type', 'drag_and_drop')
                    locator_name_data = mydoc.getElementsByTagName('locator_name')
                    locator_value_data = mydoc.getElementsByTagName('locator_value')
                    locator_name_target_data = mydoc.getElementsByTagName('locator_name_target')
                    locator_value_target_data = mydoc.getElementsByTagName('locator_value_target')
                    locator_name = xml.Element('locator_name')
                    locator_value = xml.Element('locator_value')
                    locator_name_target = xml.Element('locator_name_target')
                    locator_value_target = xml.Element('locator_value_target')
                    locator_name.text = locator_name_data[0].firstChild.data
                    locator_value.text = locator_value_data[0].firstChild.data
                    locator_name_target.text = locator_name_target_data[0].firstChild.data
                    locator_value_target.text = locator_value_target_data[0].firstChild.data
                    action.append(locator_name)
                    action.append(locator_value)
                    action.append(locator_name_target)
                    action.append(locator_value_target)
                    root.append(action)
                if(item[0].firstChild.data == "messagebox"):
                    variable_data = mydoc.getElementsByTagName('variable')
                    print(variable_data[0].firstChild.data)
                    action = xml.Element('Action')
                    variable_name = xml.Element('variable')
                    variable_name.text = variable_data[0].firstChild.data
                    action.set('type', 'messagebox')
                    action.append(variable_name)
                    root.append(action)
                if(item[0].firstChild.data == "excel_open"):
                    session_data = mydoc.getElementsByTagName('session')
                    location_data = mydoc.getElementsByTagName('location')
                    filename_data = mydoc.getElementsByTagName('filename')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    location = xml.Element('location')
                    filename = xml.Element('filename')
                    session.text = session_data[0].firstChild.data
                    location.text = location_data[0].firstChild.data
                    filename.text = filename_data[0].firstChild.data
                    action.set('type', 'excel_open')
                    action.append(session)
                    action.append(location)
                    action.append(filename)
                    root.append(action)
                if(item[0].firstChild.data == "excel_create"):
                    session_data = mydoc.getElementsByTagName('session')
                    location_data = mydoc.getElementsByTagName('location')
                    filename_data = mydoc.getElementsByTagName('filename')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    location = xml.Element('location')
                    filename = xml.Element('filename')
                    session.text = session_data[0].firstChild.data
                    location.text = location_data[0].firstChild.data
                    filename.text = filename_data[0].firstChild.data
                    action.set('type', 'excel_create')
                    action.append(session)
                    action.append(location)
                    action.append(filename)
                    root.append(action)
                if(item[0].firstChild.data == "excel_save_workbook"):
                    session_data = mydoc.getElementsByTagName('session')
                    location_data = mydoc.getElementsByTagName('location')
                    filename_data = mydoc.getElementsByTagName('filename')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    location = xml.Element('location')
                    filename = xml.Element('filename')
                    session.text = session_data[0].firstChild.data
                    location.text = location_data[0].firstChild.data
                    filename.text = filename_data[0].firstChild.data
                    action.set('type', 'excel_save_workbook')
                    action.append(session)
                    action.append(location)
                    action.append(filename)
                    root.append(action)
                if(item[0].firstChild.data == "excel_delete_file"):
                    location_data = mydoc.getElementsByTagName('location')
                    filename_data = mydoc.getElementsByTagName('filename')
                    action = xml.Element('Action')
                    location = xml.Element('location')
                    filename = xml.Element('filename')
                    location.text = location_data[0].firstChild.data
                    filename.text = filename_data[0].firstChild.data
                    action.set('type', 'excel_delete_file')
                    action.append(location)
                    action.append(filename)
                    root.append(action)
                if(item[0].firstChild.data == "excel_delete_worksheet"):
                    session_data = mydoc.getElementsByTagName('session')
                    sheetname_data = mydoc.getElementsByTagName('sheetname')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    sheetname = xml.Element('sheetname')
                    session.text = session_data[0].firstChild.data
                    sheetname.text = sheetname_data[0].firstChild.data
                    action.set('type', 'excel_delete_worksheet')
                    action.append(session)
                    action.append(sheetname)
                    root.append(action)
                if(item[0].firstChild.data == "excel_create_worksheet"):
                    session_data = mydoc.getElementsByTagName('session')
                    sheetname_data = mydoc.getElementsByTagName('sheetname')
                    position_data = mydoc.getElementsByTagName('position')
                    value_data = mydoc.getElementsByTagName('value')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    sheetname = xml.Element('sheetname')
                    position = xml.Element('position')
                    value = xml.Element('value')
                    session.text = session_data[0].firstChild.data
                    sheetname.text = sheetname_data[0].firstChild.data
                    position.text = position_data[0].firstChild.data
                    value.text = value_data[0].firstChild.data
                    action.set('type', 'excel_create_worksheet')
                    action.append(session)
                    action.append(sheetname)
                    action.append(position)
                    action.append(value)
                    root.append(action)
                if(item[0].firstChild.data == "excel_set_value"):
                    session_data = mydoc.getElementsByTagName('session')
                    sheetname_data = mydoc.getElementsByTagName('sheetname')
                    cell_data = mydoc.getElementsByTagName('cell')
                    value_data = mydoc.getElementsByTagName('value')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    sheetname = xml.Element('sheetname')
                    cell = xml.Element('cell')
                    value = xml.Element('value')
                    session.text = session_data[0].firstChild.data
                    sheetname.text = sheetname_data[0].firstChild.data
                    cell.text = cell_data[0].firstChild.data
                    value.text = value_data[0].firstChild.data
                    action.set('type', 'excel_set_value')
                    action.append(session)
                    action.append(sheetname)
                    action.append(cell)
                    action.append(value)
                    root.append(action)
                if(item[0].firstChild.data == "excel_get_value"):
                    session_data = mydoc.getElementsByTagName('session')
                    sheetname_data = mydoc.getElementsByTagName('sheetname')
                    cell_data = mydoc.getElementsByTagName('cell')
                    save_to_data = mydoc.getElementsByTagName('variable')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    sheetname = xml.Element('sheetname')
                    cell = xml.Element('cell')
                    save_to = xml.Element('variable')
                    session.text = session_data[0].firstChild.data
                    sheetname.text = sheetname_data[0].firstChild.data
                    cell.text = cell_data[0].firstChild.data
                    save_to.text = save_to_data[0].firstChild.data
                    action.set('type', 'excel_get_value')
                    action.append(session)
                    action.append(sheetname)
                    action.append(cell)
                    action.append(save_to)
                    root.append(action)
                if(item[0].firstChild.data == "excel_set_formula"):
                    session_data = mydoc.getElementsByTagName('session')
                    sheetname_data = mydoc.getElementsByTagName('sheetname')
                    cell_data = mydoc.getElementsByTagName('cell')
                    formula_data = mydoc.getElementsByTagName('formula')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    sheetname = xml.Element('sheetname')
                    cell = xml.Element('cell')
                    formula = xml.Element('formula')
                    session.text = session_data[0].firstChild.data
                    sheetname.text = sheetname_data[0].firstChild.data
                    cell.text = cell_data[0].firstChild.data
                    formula.text = formula_data[0].firstChild.data
                    action.set('type', 'excel_set_formula')
                    action.append(session)
                    action.append(sheetname)
                    action.append(cell)
                    action.append(formula)
                    root.append(action)
                if(item[0].firstChild.data == "excel_merge_unmerge"):
                    session_data = mydoc.getElementsByTagName('session')
                    sheetname_data = mydoc.getElementsByTagName('sheetname')
                    merge_unmerge_data = mydoc.getElementsByTagName('merge_unmerge')
                    from_cell_data = mydoc.getElementsByTagName('from_cell')
                    to_cell_data = mydoc.getElementsByTagName('to_cell')
                    action = xml.Element('Action')
                    session = xml.Element('session')
                    sheetname = xml.Element('sheetname')
                    merge_unmerge = xml.Element('merge_unmerge')
                    from_cell = xml.Element('from_cell')
                    to_cell = xml.Element('to_cell')
                    session.text = session_data[0].firstChild.data
                    sheetname.text = sheetname_data[0].firstChild.data
                    merge_unmerge.text = merge_unmerge_data[0].firstChild.data
                    from_cell.text = from_cell_data[0].firstChild.data
                    to_cell.text = to_cell_data[0].firstChild.data
                    action.set('type', 'excel_merge_unmerge')
                    action.append(session)
                    action.append(sheetname)
                    action.append(merge_unmerge)
                    action.append(from_cell)
                    action.append(to_cell)
                    root.append(action)
                if(item[0].firstChild.data == "excel_copy_paste"):
                    copy_session_data = mydoc.getElementsByTagName('copy_session')
                    copy_sheetname_data = mydoc.getElementsByTagName('copy_sheetname')
                    copy_start_data = mydoc.getElementsByTagName('copy_start')
                    copy_end_data = mydoc.getElementsByTagName('copy_end')
                    paste_session_data = mydoc.getElementsByTagName('paste_session')
                    paste_sheetname_data = mydoc.getElementsByTagName('paste_sheetname')
                    paste_start_data = mydoc.getElementsByTagName('paste_start')
                    paste_end_data = mydoc.getElementsByTagName('paste_end')
                    action = xml.Element('Action')
                    copy_session = xml.Element('copy_session')
                    copy_sheetname = xml.Element('copy_sheetname')
                    copy_start = xml.Element('copy_start')
                    copy_end = xml.Element('copy_end')
                    paste_session = xml.Element('paste_session')
                    paste_sheetname = xml.Element('paste_sheetname')
                    paste_start = xml.Element('paste_start')
                    paste_end = xml.Element('paste_end')
                    copy_session.text = copy_session_data[0].firstChild.data
                    copy_sheetname.text = copy_sheetname_data[0].firstChild.data
                    copy_start.text = copy_start_data[0].firstChild.data
                    copy_end.text = copy_end_data[0].firstChild.data
                    paste_session.text = paste_session_data[0].firstChild.data
                    paste_sheetname.text = paste_sheetname_data[0].firstChild.data
                    paste_start.text = paste_start_data[0].firstChild.data
                    paste_end.text = paste_end_data[0].firstChild.data
                    action.set('type', 'excel_copy_paste')
                    action.append(copy_session)
                    action.append(copy_sheetname)
                    action.append(copy_start)
                    action.append(copy_end)
                    action.append(paste_session)
                    action.append(paste_sheetname)
                    action.append(paste_start)
                    action.append(paste_end)
                    root.append(action)
                if(item[0].firstChild.data == "create_variable"):
                    action = xml.Element('Action')
                    action.set('type', 'create_variable')
                    variable_name_data = mydoc.getElementsByTagName('variable_name')
                    variable_value_data = mydoc.getElementsByTagName('variable_value')
                    type_data = mydoc.getElementsByTagName('type')
                    variable_name = xml.Element('variable_name')
                    variable_value = xml.Element('variable_value')
                    _type = xml.Element('type')
                    variable_name.text = variable_name_data[0].firstChild.data
                    variable_value.text = variable_value_data[0].firstChild.data
                    _type.text = type_data[0].firstChild.data
                    action.append(variable_name)
                    action.append(variable_value)
                    action.append(_type)
                    root.append(action)
                if(item[0].firstChild.data == "for_loop"):
                    init_variable_data = mydoc.getElementsByTagName('init_variable')
                    condition_for_data = mydoc.getElementsByTagName('condition_for')
                    condition_data = mydoc.getElementsByTagName('condition')
                    variable1_data = mydoc.getElementsByTagName('variable1')
                    variable2_data = mydoc.getElementsByTagName('variable2')
                    action = xml.Element('Action')
                    action.set('type', 'inputtext')
                    init_variable = xml.Element('init_variable')
                    condition_for = xml.Element('condition_for')
                    condition = xml.Element('condition')
                    variable1 = xml.Element('variable1')
                    variable2 = xml.Element('variable2')
                    init_variable.text = init_variable_data[0].firstChild.data
                    condition_for.text = condition_for_data[0].firstChild.data
                    condition.text = condition_data[0].firstChild.data
                    variable1.text = variable1_data[0].firstChild.data
                    variable2.text = variable2_data[0].firstChild.data
                    action.append(init_variable)
                    action.append(condition_for)
                    action.append(condition)
                    action.append(variable1)
                    action.append(variable2)
                    root.append(action)
                if(item[0].firstChild.data in ['split_string', 'list_get_value']):
                    delimiter_data = mydoc.getElementsByTagName('delimiter')
                    variable1_data = mydoc.getElementsByTagName('variable1')
                    variable2_data = mydoc.getElementsByTagName('variable2')
                    action = xml.Element('Action')
                    action.set('type', item[0].firstChild.data)
                    delimiter = xml.Element('delimiter')
                    variable1 = xml.Element('variable1')
                    variable2 = xml.Element('variable2')
                    delimiter.text = delimiter_data[0].firstChild.data
                    variable1.text = variable1_data[0].firstChild.data
                    variable2.text = variable2_data[0].firstChild.data
                    action.append(variable1)
                    action.append(variable2)
                    action.append(delimiter)
                    root.append(action)
                if(item[0].firstChild.data in ['count', 'index', 'find', 'strip', 'lstrip','rstrip']):
                    variable1_data = mydoc.getElementsByTagName('variable1')
                    variable2_data = mydoc.getElementsByTagName('variable2')
                    action = xml.Element('Action')
                    action.set('type', item[0].firstChild.data )
                    variable1 = xml.Element('variable1')
                    variable2 = xml.Element('variable2')
                    variable1.text = variable1_data[0].firstChild.data
                    variable2.text = variable2_data[0].firstChild.data
                    action.append(variable1)
                    action.append(variable2)
                    root.append(action)
                if(item[0].firstChild.data == "concate_string"):
                    string1_data = mydoc.getElementsByTagName('string1')
                    string2_data = mydoc.getElementsByTagName('string2')
                    save_to_data = mydoc.getElementsByTagName('save_to')
                    action = xml.Element('Action')
                    action.set('type', item[0].firstChild.data )
                    string1 = xml.Element('string1')
                    string2 = xml.Element('string2')
                    save_to = xml.Element('save_to')
                    string1.text = string1_data[0].firstChild.data
                    string2.text = string2_data[0].firstChild.data
                    save_to.text = save_to_data[0].firstChild.data
                    action.append(string1)
                    action.append(string2)
                    action.append(save_to)
                    root.append(action)
                if(item[0].firstChild.data in ["increment", 'decrement']):
                    _variable_data = mydoc.getElementsByTagName('_variable')
                    _variable_by_data = mydoc.getElementsByTagName('_variable_by')
                    save_to_data = mydoc.getElementsByTagName('save_to')
                    action = xml.Element('Action')
                    action.set('type', item[0].firstChild.data )
                    _variable = xml.Element('_variable')
                    _variable_by = xml.Element('_variable_by')
                    save_to = xml.Element('save_to')
                    _variable.text = _variable_data[0].firstChild.data
                    _variable_by.text = _variable_by_data[0].firstChild.data
                    save_to.text = save_to_data[0].firstChild.data
                    action.append(_variable)
                    action.append(_variable_by)
                    action.append(save_to)
                    root.append(action)
    
        tree = xml.ElementTree(root)   
        save_path_file = self.file_path + "testtest" + ".xml"
        xmlstr = minidom.parseString(xml.tostring(root)).toprettyxml(indent="   ")
        with open(save_path_file, "w") as f:
            f.write(xmlstr)
            
