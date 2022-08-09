from xml.dom import minidom
from my_selenium import MySelenium
from excel_test import MyExcel
from my_variables import MyVariables
from global_instance import *

# parse an xml file by name
mydoc = minidom.parse(my_path + 'testtest.xml')

items = mydoc.getElementsByTagName('Action')
sel = None

# all item attributes
for elem in items:
    actionName = elem.attributes['type'].value
    if(actionName == 'openurl'):
        url = elem.getElementsByTagName('url')
        browser = elem.getElementsByTagName('browser')
        sel = MySelenium()
        MySelenium.openurl(sel, url[0].firstChild.data, browser[0].firstChild.data)
    elif(actionName == 'close_browser'):
        session = elem.getElementsByTagName('session')
        MySelenium.close_browser(sel, session[0].firstChild.data)
    elif(actionName == 'navigation'):
        navigation = elem.getElementsByTagName('navigation')
        MySelenium.navigation(sel, navigation[0].firstChild.data)
    elif(actionName == 'click'):
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.click_by_xpath(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.click_by_id(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.click_by_name(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.click_by_class_name(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.click_by_tag_name(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.click_by_css_selector(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.click_by_link_text(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.click_by_partial_link_text(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'element'):
            MySelenium.click_by_element(sel, locator_value[0].firstChild.data)
    elif(actionName == 'clear'):
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.clear_by_xpath(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.clear_by_id(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.clear_by_name(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.clear_by_class_name(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.clear_by_tag_name(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.clear_by_css_selector(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.clear_by_link_text(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.clear_by_partial_link_text(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'element'):
            MySelenium.clear_by_element(sel, locator_value[0].firstChild.data)
    elif(actionName == 'inputtext'):
        value = elem.getElementsByTagName('value')
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.inputtext_by_xpath(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.inputtext_by_id(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.inputtext_by_name(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.inputtext_by_class_name(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.inputtext_by_tag_name(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.inputtext_by_css_selector(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.inputtext_by_link_text(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.inputtext_by_partial_link_text(sel, locator_value[0].firstChild.data, value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'element'):
            MySelenium.inputtext_by_element(sel, locator_value[0].firstChild.data)
    elif(actionName == 'readtext'):
        save_to = elem.getElementsByTagName('variable')
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.readtext_by_xpath(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.readtext_by_id(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.readtext_by_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.readtext_by_class_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.readtext_by_tag_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.readtext_by_css_selector(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.readtext_by_link_text(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.readtext_by_partial_link_text(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'element'):
            MySelenium.readtext_by_element(sel, locator_value[0].firstChild.data)
    elif(actionName == 'get_element'):
        save_to = elem.getElementsByTagName('variable')
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.get_element_by_xpath(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.get_element_by_id(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.get_element_by_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.get_element_by_class_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.get_element_by_tag_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.get_element_by_css_selector(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.get_element_by_link_text(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.get_element_by_partial_link_text(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
    elif(actionName == 'get_elements'):
        save_to = elem.getElementsByTagName('variable')
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.get_elements_by_xpath(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.get_elements_by_id(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.get_elements_by_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.get_elements_by_class_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.get_elements_by_tag_name(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.get_elements_by_css_selector(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.get_elements_by_link_text(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.get_elements_by_partial_link_text(sel, locator_value[0].firstChild.data, save_to[0].firstChild.data)        
    elif(actionName == 'select_option'):
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        select_by_name = elem.getElementsByTagName('select_by_name')
        select_by_value = elem.getElementsByTagName('select_by_value')
        if(locator_name[0].firstChild.data == 'xpath'):
            MySelenium.select_option_by_xpath(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            MySelenium.select_option_by_id(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            MySelenium.select_option_by_name(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            MySelenium.select_option_by_class_name(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            MySelenium.select_option_by_tag_name(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            MySelenium.select_option_by_css_selector(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            MySelenium.select_option_by_link_text(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            MySelenium.select_option_by_partial_link_text(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'element'):
            MySelenium.select_option_by_element(sel, locator_value[0].firstChild.data, select_by_name[0].firstChild.data, select_by_value[0].firstChild.data)
    elif(actionName == 'drag_and_drop'):
        locator_name = elem.getElementsByTagName('locator_name')
        locator_value = elem.getElementsByTagName('locator_value')
        locator_name_target = elem.getElementsByTagName('locator_name_target')
        locator_value_target = elem.getElementsByTagName('locator_value_target')
        elem_source = None
        elem_target = None
        if(locator_name[0].firstChild.data == 'xpath'):
            elem_source = MySelenium.getElementByXpath(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'id'):
            elem_source = MySelenium.getElementById(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'name'):
            elem_source = MySelenium.getElementByName(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'class_name'):
            elem_source = MySelenium.getElementByClassName(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'tag_name'):
            elem_source = MySelenium.getElementByTagName(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'css_selector'):
            elem_source = MySelenium.getElementByCssSelector(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'link_text'):
            elem_source = MySelenium.getElementByLinkText(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'partial_link_text'):
            elem_source = MySelenium.getElementByPartialLinkText(sel, locator_value[0].firstChild.data)
        elif(locator_name[0].firstChild.data == 'element'):
            elem_source = MySelenium.getElementByElement(sel, locator_value[0].firstChild.data)
        if(locator_name_target[0].firstChild.data == 'xpath'):
            elem_target = MySelenium.getElementByXpath(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'id'):
            elem_target = MySelenium.getElementById(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'name'):
            elem_target = MySelenium.getElementByName(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'class_name'):
            elem_target = MySelenium.getElementByClassName(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'tag_name'):
            elem_target = MySelenium.getElementByTagName(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'css_selector'):
            elem_target = MySelenium.getElementByCssSelector(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'link_text'):
            elem_target = MySelenium.getElementByLinkText(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'partial_link_text'):
            elem_target = MySelenium.getElementByPartialLinkText(sel, locator_value_target[0].firstChild.data)
        elif(locator_name_target[0].firstChild.data == 'element'):
            elem_source = MySelenium.getElementByElement(sel, locator_value[0].firstChild.data)
        MySelenium.drag_and_drop(sel, elem_source, elem_target)
    elif(actionName == 'messagebox'):
        variable_name = elem.getElementsByTagName('variable')
        MySelenium.my_messagebox(sel, variable_name[0].firstChild.data)
    elif(actionName == 'clear'):
        xpath = elem.getElementsByTagName('xpath')
        MySelenium.clear_by_xpath(sel, xpath[0].firstChild.data)
    elif(actionName == 'sendkeys'):
        key_value = elem.getElementsByTagName('key_value')
        xpath = elem.getElementsByTagName('xpath')
        if(len(xpath) > 0):
            MySelenium.send_keys_by_xpath(sel, xpath[0].firstChild.data, key_value[0].firstChild.data)
        id = elem.getElementsByTagName('id')
        if(len(id) > 0):
            MySelenium.send_keys_by_id(sel, id[0].firstChild.data, key_value[0].firstChild.data)
        name = elem.getElementsByTagName('name')
        if(len(name) > 0):
            MySelenium.send_keys_by_name(sel, name[0].firstChild.data, key_value[0].firstChild.data)
    elif(actionName == 'wait'):
        seconds = elem.getElementsByTagName('seconds')
        MySelenium.wait(sel, int(seconds[0].firstChild.data))
    elif(actionName == 'excel_create'):
        session = elem.getElementsByTagName('session')
        location = elem.getElementsByTagName('location')
        filename = elem.getElementsByTagName('filename')
        MyExcel.excel_create(session[0].firstChild.data, location[0].firstChild.data, filename[0].firstChild.data)
    elif(actionName == 'excel_open'):
        session = elem.getElementsByTagName('session')
        location = elem.getElementsByTagName('location')
        filename = elem.getElementsByTagName('filename')
        MyExcel.excel_open(session[0].firstChild.data, location[0].firstChild.data, filename[0].firstChild.data)
    elif(actionName == 'excel_delete_file'):
        location = elem.getElementsByTagName('location')
        filename = elem.getElementsByTagName('filename')
        MyExcel.excel_delete_file(location[0].firstChild.data, filename[0].firstChild.data)
    elif(actionName == 'excel_create_worksheet'):
        session = elem.getElementsByTagName('session')
        sheetname = elem.getElementsByTagName('sheetname')
        position = elem.getElementsByTagName('position')
        value = elem.getElementsByTagName('value')
        MyExcel.excel_create_worksheet(session[0].firstChild.data, sheetname[0].firstChild.data, position[0].firstChild.data, value[0].firstChild.data)
    elif(actionName == 'excel_delete_worksheet'):
        session = elem.getElementsByTagName('session')
        sheetname = elem.getElementsByTagName('sheetname')
        MyExcel.excel_delete_worksheet(session[0].firstChild.data, sheetname[0].firstChild.data)
    elif(actionName == 'excel_save_workbook'):
        session = elem.getElementsByTagName('session')
        location = elem.getElementsByTagName('location')
        filename = elem.getElementsByTagName('filename')
        MyExcel.excel_save_workbook(session[0].firstChild.data, location[0].firstChild.data, filename[0].firstChild.data)
    elif(actionName == 'excel_set_value'):
        print('hello')
        session = elem.getElementsByTagName('session')
        sheetname = elem.getElementsByTagName('sheetname')
        cell = elem.getElementsByTagName('cell')
        value = elem.getElementsByTagName('value')
        MyExcel.excel_set_value(session[0].firstChild.data, sheetname[0].firstChild.data, cell[0].firstChild.data, value[0].firstChild.data)
    elif(actionName == 'excel_get_value'):
        session = elem.getElementsByTagName('session')
        sheetname = elem.getElementsByTagName('sheetname')
        cell = elem.getElementsByTagName('cell')
        variable = elem.getElementsByTagName('variable')
        MyExcel.excel_get_value(session[0].firstChild.data, sheetname[0].firstChild.data, cell[0].firstChild.data, variable[0].firstChild.data)
    elif(actionName == 'excel_set_formula'):
        session = elem.getElementsByTagName('session')
        sheetname = elem.getElementsByTagName('sheetname')
        cell = elem.getElementsByTagName('cell')
        formula = elem.getElementsByTagName('formula')
        MyExcel.excel_get_value(session[0].firstChild.data, sheetname[0].firstChild.data, cell[0].firstChild.data, formula[0].firstChild.data)
    elif(actionName == 'excel_merge_unmerge'):
        session = elem.getElementsByTagName('session')
        sheetname = elem.getElementsByTagName('sheetname')
        merge_unmerge = elem.getElementsByTagName('merge_unmerge')
        from_cell = elem.getElementsByTagName('from_cell')
        to_cell = elem.getElementsByTagName('to_cell')
        MyExcel.excel_merge_unmerge(session[0].firstChild.data, sheetname[0].firstChild.data, merge_unmerge[0].firstChild.data, from_cell[0].firstChild.data , to_cell[0].firstChild.data)
    elif(actionName == 'excel_copy_paste'):
        copy_session = elem.getElementsByTagName('copy_session')
        copy_sheetname = elem.getElementsByTagName('copy_sheetname')
        copy_start = elem.getElementsByTagName('copy_start')
        copy_end = elem.getElementsByTagName('copy_end')
        paste_session = elem.getElementsByTagName('paste_session')
        paste_sheetname = elem.getElementsByTagName('paste_sheetname')
        paste_start = elem.getElementsByTagName('paste_start')
        paste_end = elem.getElementsByTagName('paste_end')
        MyExcel.excel_copy_paste(copy_session[0].firstChild.data, copy_sheetname[0].firstChild.data, copy_start[0].firstChild.data, copy_end[0].firstChild.data, paste_session[0].firstChild.data, paste_sheetname[0].firstChild.data, paste_start[0].firstChild.data, paste_end[0].firstChild.data)
    elif(actionName == 'create_variable'):
        variable_name = elem.getElementsByTagName('variable_name')
        variable_value = elem.getElementsByTagName('variable_value')
        _type = elem.getElementsByTagName('type')
        MyVariables.create_variable(variable_name[0].firstChild.data, variable_value[0].firstChild.data, _type[0].firstChild.data)
    elif(actionName == 'split_string'):
        variable1 = elem.getElementsByTagName('variable1')
        variable2 = elem.getElementsByTagName('variable2')
        delimiter = elem.getElementsByTagName('delimiter')
        MyVariables.split_string(variable1[0].firstChild.data, variable2[0].firstChild.data, delimiter[0].firstChild.data)
    elif(actionName == 'list_get_value'):
        variable1 = elem.getElementsByTagName('variable1')
        variable2 = elem.getElementsByTagName('variable2')
        delimiter = elem.getElementsByTagName('delimiter')
        MyVariables.list_get_value(variable1[0].firstChild.data, variable2[0].firstChild.data, delimiter[0].firstChild.data)
    elif(actionName in ['count', 'index', 'find', 'strip', 'rstrip', 'lstrip']):
        variable1 = elem.getElementsByTagName('variable1')
        variable2 = elem.getElementsByTagName('variable2')
        MyVariables.manipulate_string(variable1[0].firstChild.data, variable2[0].firstChild.data, actionName)
    elif(actionName == 'concate_string'):
        string1 = elem.getElementsByTagName('string1')
        string2 = elem.getElementsByTagName('string2')
        save_to = elem.getElementsByTagName('save_to')
        MyVariables.concate_string(string1[0].firstChild.data, string2[0].firstChild.data,save_to[0].firstChild.data)
    elif(actionName in ['increment', 'decrement']):
        _variable = elem.getElementsByTagName('_variable')
        _variable_by = elem.getElementsByTagName('_variable_by')
        save_to = elem.getElementsByTagName('save_to')
        MyVariables.increment_decrement(_variable[0].firstChild.data, _variable_by[0].firstChild.data,save_to[0].firstChild.data, actionName)


    

        
        

