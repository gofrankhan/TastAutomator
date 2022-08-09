import tkinter as tk
import os
from tkinter import ttk
from actions import Actions
from project_explorer import ProjectExplorer
from menubar import Menubar
from toolbar import Toolbar
from canvas import Canvas
from resources import Resources
from properties import Properties
from cardbutton import Imgbutton
from global_instance import *

class MainApplication():
    def __init__(self, *args, **kwargs):

        self.parent = None
        self.panedwindow = None
        self.panedwindow_left = None
        self.panewindow_middle = None
        self.project_explorer = None
        self.properties = None
        self.left_pane = None
        self.middle_pane = None
        self.right_pane = None
        self.toolbar = None
        self.pane_projects = None
        self.pane_actions = None
        self.pane_canvas = None
        self.pane_resources = None
    
    def create_main_ui(self, parent):
        self.parent = parent
        self.parent.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()-70))
        self.parent.title("Task Automator")

    def paned_window(self):
        self.panedwindow = ttk.Panedwindow(self.parent, orient = tk.HORIZONTAL)
        self.panedwindow.pack(expand = True, fill = tk.BOTH)

        self.left_pane = ttk.Frame(self.panedwindow, height = root.winfo_screenheight() - 140, relief = tk.SUNKEN)
        self.middle_pane = ttk.Frame(self.panedwindow, height = (root.winfo_screenheight() - 140), relief = tk.SUNKEN)
        self.right_pane = ttk.Frame(self.panedwindow, height = (root.winfo_screenheight() - 140), relief = tk.SUNKEN)
        self.panedwindow.add(self.left_pane, weight = 1)
        self.panedwindow.add(self.middle_pane, weight = 1) 
        self.panedwindow.add(self.right_pane, weight = 10)

        self.panedwindow_left = ttk.Panedwindow(self.left_pane, orient = tk.VERTICAL)
        self.panedwindow_left.pack(expand = True, fill = tk.BOTH)
        self.pane_projects = ttk.Frame(self.panedwindow_left, height = (root.winfo_screenheight() - 140) / 2, relief = tk.SUNKEN)
        self.pane_actions = ttk.Frame(self.panedwindow_left, height = (root.winfo_screenheight() - 140) / 2, relief = tk.SUNKEN)
        self.panedwindow_left.add(self.pane_projects, weight = 1)
        self.panedwindow_left.add(self.pane_actions, weight = 1)

        self.panewindow_middle = ttk.PanedWindow(self.middle_pane, orient = tk.VERTICAL)
        self.panewindow_middle.pack(expand = True, fill = tk.BOTH)
        self.pane_canvas = ttk.Frame(self.panewindow_middle, relief = tk.SUNKEN)
        self.pane_resources = ttk.Frame(self.panewindow_middle, width = 100, relief = tk.SUNKEN)
        self.panewindow_middle.add(self.pane_canvas, weight = 5)
        self.panewindow_middle.add(self.pane_resources, weight = 1)

        self.menubar = Menubar(self.parent)
        self.properties = Properties(self.right_pane)
        self.canvas = Canvas(self.properties)
        self.toolbar = Toolbar(self.pane_canvas, self.canvas)
        self.project_explorer = ProjectExplorer(self.pane_projects)
        self.canvas.create_Ui(self.pane_canvas)
        self.actions = Actions(self.pane_actions, self.canvas, self.properties)
        self.resources = Resources(self.pane_resources)
    
    def delete_files(self):
        dir = my_path + 'files\\'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApplication()
    main_app.create_main_ui(root)
    main_app.paned_window()
    root.mainloop()
    main_app.delete_files()



