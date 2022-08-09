from tkinter.constants import NUMERIC
from global_instance import *

class MyVariables():

    def __init__(self, *args, **kwargs):
        pass

    def create_variable(variable_name, variable_value, type_name):
        if(type_name == 'string'):
            variable_dict[variable_name] = variable_value
        elif(type_name == 'number'):
            variable_dict[variable_name] = float(variable_value) if '.' in variable_value else int(variable_value)
        elif(type_name == 'list'):
            variable_dict[variable_name] = [variable_value]
        elif(type_name == 'dictionary'):
            variable_dict[variable_name] = {}
        else:
            variable_dict[variable_name] = None

    def split_string(variable1, variable2, delimiter):
        variable_dict[variable2] = variable_dict[variable1].split(delimiter)
    
    def manipulate_string(variable1, variable2, action):
        if(action == "index"):
            variable_dict[variable2] = variable_dict[variable1]
        if(action == "count"):
            variable_dict[variable2] = variable_dict[variable1]
        if(action == "find"):
            variable_dict[variable2] = variable_dict[variable1]
        if(action == "strip"):
            variable_dict[variable2] = variable_dict[variable1].strip()
        if(action == "rstrip"):
            variable_dict[variable2] = variable_dict[variable1].rstrip()
        if(action == "lstrip"):
            variable_dict[variable2] = variable_dict[variable1].ltrip()

    def list_get_value(variable1, variable2, delimiter):
        variable_dict[variable1]= variable_dict[variable2][int(delimiter)]
    
    def concate_string(string1, string2, save_to):
        variable_dict[save_to]= str(variable_dict[string1]) + str(variable_dict[string2])

    def increment_decrement(_variable, _variable_by, save_to, opt_type):
        if(opt_type == 'increment'):
            variable_dict[save_to] = variable_dict[_variable] + int(_variable_by)
        elif(opt_type == 'decrement'):
            variable_dict[save_to] = variable_dict[_variable] - int(_variable_by)