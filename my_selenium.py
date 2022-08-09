from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import messagebox
from global_instance import *

class MySelenium():

    def __init__(self, *args, **kwargs):
        self.driver = None

    def openurl(self, url, browser):
        if(browser == "Google Chrome"):
            self.driver = webdriver.Chrome(executable_path= my_path + "driver\chromedriver_win32\chromedriver.exe")
            self.driver.get(url)
        elif(browser == "Mozilla Firefox"):
            self.driver = webdriver.Firefox(executable_path= my_path + "driver\geckodriver-v0.29.1-win64\geckodriver.exe")
            self.driver.get(url)
        elif(browser == "Internet Explorer"):
            self.driver = webdriver.Edge(executable_path= my_path + "driver\edgedriver_win32\msedgedriver.exe")
            self.driver.get(url)
        elif(browser == "Microsoft Edge"):
            self.driver = webdriver.Edge(executable_path= my_path + "driver\edgedriver_win32\msedgedriver.exe")
            self.driver.get(url)

    def navigation(self, navigation):
        if(navigation == 'forward'):
            self.driver.forward()
        elif(navigation == 'back'):
            self.driver.back()
    
    def close_browser(self, session):
        self.driver.close()

    def click_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()
    
    def click_by_id(self, id):
        self.driver.find_element_by_id(id).click()

    def click_by_name(self, name):
        self.driver.find_element_by_name(name).click()

    def click_by_tag_name(self, tag_name):
        self.driver.find_element_by_tag_name(tag_name).click()

    def click_by_class_name(self, class_name):
        self.driver.find_element_by_class_name(class_name).click()

    def click_by_css_selector(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).click()
    
    def click_by_link_text(self, link_text):
        self.driver.find_element_by_link_text(link_text).click()
    
    def click_by_partial_link_text(self, partial_link_text):
        self.driver.find_element_by_partial_link_text(partial_link_text).click()
    
    def click_by_element(self, element):
        variable_dict[element].click()

    def readtext_by_xpath(self, xpath, save_to):
        self.text = self.driver.find_element_by_xpath(xpath).text
        variable_dict[save_to] = self.text
    
    def readtext_by_id(self, id, save_to):
        self.text = self.driver.find_element_by_id(id).text
        variable_dict[save_to] = self.text

    def readtext_by_name(self, name, save_to):
        self.text = self.driver.find_element_by_name(name).text
        variable_dict[save_to] = self.text

    def readtext_by_tag_name(self, tag_name, save_to):
        self.text = self.driver.find_element_by_tag_name(tag_name).text
        variable_dict[save_to] = self.text

    def readtext_by_class_name(self, class_name, save_to):
        self.text = self.driver.find_element_by_class_name(class_name).text
        variable_dict[save_to] = self.text

    def readtext_by_css_selector(self, css_selector, save_to):
        self.text = self.driver.find_element_by_css_selector(css_selector).text
        variable_dict[save_to] = self.text
    
    def readtext_by_link_text(self, link_text, save_to):
        self.text = self.driver.find_element_by_link_text(link_text).text
        variable_dict[save_to] = self.text
    
    def readtext_by_partial_link_text(self, partial_link_text, save_to):
        self.text = self.driver.find_element_by_partial_link_text(partial_link_text).text
        variable_dict[save_to] = self.text
    
    def readtext_by_element(self, element, save_to):
        self.text = variable_dict[element].text
        variable_dict[save_to] = self.text

    def get_element_by_xpath(self, xpath, save_to):
        elem = self.driver.find_element_by_xpath(xpath)
        variable_dict[save_to] = elem
    
    def get_element_by_id(self, id, save_to):
        elem = self.driver.find_element_by_xpath(id)
        variable_dict[save_to] = elem

    def get_element_by_name(self, name, save_to):
        elem = self.driver.find_element_by_name(name)
        variable_dict[save_to] = elem

    def get_element_by_tag_name(self, tag_name, save_to):
        elem = self.driver.find_element_by_tag_name(tag_name)
        variable_dict[save_to] = elem

    def get_element_by_class_name(self, class_name, save_to):
        elem = self.driver.find_element_by_class_name(class_name)
        variable_dict[save_to] = elem
    
    def get_elements_by_xpath(self, xpath, save_to):
        elem = self.driver.find_elements_by_xpath(xpath)
        variable_dict[save_to] = elem
    
    def get_elements_by_id(self, id, save_to):
        elem = self.driver.find_elements_by_xpath(id)
        variable_dict[save_to] = elem

    def get_elements_by_name(self, name, save_to):
        elem = self.driver.find_elements_by_name(name)
        variable_dict[save_to] = elem

    def get_elements_by_tag_name(self, tag_name, save_to):
        elem = self.driver.find_elements_by_tag_name(tag_name)
        variable_dict[save_to] = elem

    def get_elements_by_class_name(self, class_name, save_to):
        elem = self.driver.find_elements_by_class_name(class_name)
        variable_dict[save_to] = elem

    def get_element_by_css_selector(self, css_selector, save_to):
        elem = self.driver.find_element_by_css_selector(css_selector)
        variable_dict[save_to] = elem
    
    def get_element_by_link_text(self, link_text, save_to):
        elem = self.driver.find_element_by_link_text(link_text)
        variable_dict[save_to] = elem
    
    def get_element_by_partial_link_text(self, partial_link_text, save_to):
        elem = self.driver.find_element_by_partial_link_text(partial_link_text)
        variable_dict[save_to] = elem

    def get_elements_by_css_selector(self, css_selector, save_to):
        elem = self.driver.find_elements_by_css_selector(css_selector)
        variable_dict[save_to] = elem
    
    def get_elements_by_link_text(self, link_text, save_to):
        elem = self.driver.find_elements_by_link_text(link_text)
        variable_dict[save_to] = elem
    
    def get_elements_by_partial_link_text(self, partial_link_text, save_to):
        elem = self.driver.find_elements_by_partial_link_text(partial_link_text)
        variable_dict[save_to] = elem

    def inputtext_by_xpath(self, xpath, value):
        self.driver.find_element_by_xpath(xpath).send_keys(value)
    
    def inputtext_by_id(self, id, value):
        self.driver.find_element_by_id(id).send_keys(value)

    def inputtext_by_name(self, name, value):
        self.driver.find_element_by_name(name).send_keys(value)

    def inputtext_by_tag_name(self, tag_name, value):
        self.driver.find_element_by_tag_name(tag_name).send_keys(value)

    def inputtext_by_class_name(self, class_name, value):
        self.driver.find_element_by_class_name(class_name).send_keys(value)

    def inputtext_by_css_selector(self, css_selector, value):
        self.driver.find_element_by_css_selector(css_selector).send_keys(value)
    
    def inputtext_by_link_text(self, link_text, value):
        self.driver.find_element_by_link_text(link_text).send_keys(value)
    
    def inputtext_by_partial_link_text(self, partial_link_text, value):
        self.driver.find_element_by_partial_link_text(partial_link_text).send_keys(value)

    def inputtext_by_element(self, element, value):
        variable_dict[element].send_keys(value)

    def select_option_by_xpath(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_xpath(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()
    
    def select_option_by_id(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_id(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()

    def select_option_by_name(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_name(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()

    def select_option_by_tag_name(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_tag_name(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()

    def select_option_by_class_name(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_class_name(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()

    def select_option_by_css_selector(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_css_selector(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()
    
    def select_option_by_link_text(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_link_text(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()
    
    def select_option_by_partial_link_text(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_partial_link_text(locator_value))
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()
    
    def select_option_by_element(self, locator_value, select_by_name, select_by_value):
        from selenium.webdriver.support.ui import Select
        select = Select(variable_dict[locator_value])
        if(select_by_name == 'index'):
            select.select_by_index(select_by_value)
        elif(select_by_name == 'value'):
            select.select_by_value(select_by_value)
        elif(select_by_name == 'visible_text'):
            select.select_by_visible_text(select_by_value)
        elif(select_by_name == 'deselect_all'):
            select.deselect_all()

    def clear_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).clear()
    
    def clear_by_id(self, id):
        self.driver.find_element_by_id(id).clear()

    def clear_by_name(self, name):
        self.driver.find_element_by_name(name).clear()

    def clear_by_tag_name(self, tag_name):
        self.driver.find_element_by_tag_name(tag_name).clear()

    def clear_by_class_name(self, class_name):
        self.driver.find_element_by_class_name(class_name).clear()

    def clear_by_css_selector(self, css_selector):
        self.driver.find_element_by_css_selector(css_selector).clear()
    
    def clear_by_link_text(self, link_text):
        self.driver.find_element_by_link_text(link_text).clear()
    
    def clear_by_partial_link_text(self, partial_link_text):
        self.driver.find_element_by_partial_link_text(partial_link_text).clear()

    def clear_by_element(self, element):
        variable_dict[element].clear()
    
    def send_keys_by_xpath(self, xpath, key):
        self.driver.find_element_by_xpath(xpath).send_keys(key)
    
    def send_keys_by_id(self, id, key):
        self.driver.find_element_by_id(id).send_keys(key)

    def send_keys_by_name(self, name, key):
        self.driver.find_element_by_name(name).send_keys(key)

    def send_keys_by_tag_name(self, tag_name, key):
        self.driver.find_element_by_tag_name(tag_name).send_keys(key)

    def send_keys_by_class_name(self, class_name, key):
        self.driver.find_element_by_class_name(class_name).send_keys(key)

    def send_keys_by_css_selector(self, css_selector, key):
        self.driver.find_element_by_css_selector(css_selector).send_keys(key)
    
    def send_keys_by_link_text(self, link_text, key):
        self.driver.find_element_by_link_text(link_text).send_keys(key)
    
    def send_keys_by_partial_link_text(self, partial_link_text, key):
        self.driver.find_element_by_partial_link_text(partial_link_text).send_keys(key)

    def my_messagebox(self, variable_name):
        messagebox.showinfo("Information", str(variable_dict[variable_name]))

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
    
    def getElementById(self, id):
        element = self.driver.find_element_by_id(id)
        return element
    
    def getElementByXpath(self, xPath):
        element = self.driver.find_element_by_xpath(xPath)
        return element
    
    def getElementByName(self, name):
        element = self.driver.find_element_by_name(name)
        return element
    
    def getElementByClassName(self, class_name):
        element = self.driver.find_element_by_class_name(class_name)
        return element
    
    def getElementByTagName(self, tag_name):
        element = self.driver.find_element_by_tag_name(tag_name)
        return element
    
    def getElementByCssSelector(self, css_selector):
        element = self.driver.find_element_by_css_selector(css_selector)
        return element
    
    def getElementByLinkText(self, link_text):
        element = self.driver.find_element_by_link_text(link_text)
        return element
    
    def getElementByPartialLinkText(self, partial_link_text):
        element = self.driver.find_element_by_partial_link_text(partial_link_text)
        return element
    
    def getElementByElement(self, element):
        element = variable_dict[element]
        return element
    
    def drag_and_drop(self, elem_source, elem_target):
        from selenium.webdriver import ActionChains
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(elem_source, elem_target).perform()
        action_chains.click_and_hold(elem_source).move_to_element(elem_target).release(elem_target).click(elem_target).perform()