import tkinter as tk
from tkinter import ttk

class Resources(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent , *args, **kwargs)
        self.parent_frame = parent

        self.tabControl = ttk.Notebook(self.parent_frame, width=640, height = 140)

        self.variables_tab = ttk.Frame(self.tabControl)
        self.console_tab = ttk.Frame(self.tabControl)
        self.watch_tab = ttk.Frame(self.tabControl)
        self.logs_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.variables_tab, text="Variables")
        self.tabControl.add(self.console_tab, text="Console")
        self.tabControl.add(self.watch_tab, text="Watch")
        self.tabControl.add(self.logs_tab, text="Logs")
        self.tabControl.pack(expand = 1, fill = tk.BOTH)
