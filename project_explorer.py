import tkinter as tk
from tkinter import ttk

class ProjectExplorer(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent , *args, **kwargs)
        self.parent_frame = parent

        self.project_explorer_treeview = ttk.Treeview(self.parent_frame, selectmode ='browse')
        self.project_explorer_treeview.pack(expand = True, fill = tk.BOTH, side = 'left')
        self.project_explorer_treeview.insert(parent="", index=0, iid=0, text="Projects")
        self.project_explorer_treeview.insert(parent="", index=1, iid=1, text="Tasks")
        self.project_explorer_treeview.insert(parent="", index=2, iid=2, text="Events")
        self.project_explorer_treeview.insert(parent="", index=3, iid=3, text="Process")
        self.project_explorer_treeview.insert(parent="", index=4, iid=4, text="Resources")
        



        

        
