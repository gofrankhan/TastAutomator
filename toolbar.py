import tkinter as tk
import os
from tkinter import ttk
from merge_xmls import merge_xmls
from global_instance import *

class Toolbar(ttk.Frame):
    def __init__(self, parent, canvas, *args, **kwargs):
        ttk.Frame.__init__(self, parent , *args, **kwargs)
        self.parent_frame = parent
        self.canvas = canvas
        self.merge_xml_files = merge_xmls(self.canvas)
        self.file_path = my_path

        self.toolbarFrame = ttk.Frame(self.parent_frame, width=640, relief = tk.SUNKEN)
        self.toolbarFrame.pack(anchor = tk.CENTER, fill = tk.X, side = tk.TOP)


        self.btnCut = tk.Button(self.toolbarFrame, text = "Cut", padx = 5, pady = 5)
        self.btnCut.grid(row=0, column=0, padx = 5, pady = 3)

        self.btnCopy = tk.Button(self.toolbarFrame, text = "Copy", padx = 5, pady = 5)
        self.btnCopy.grid(row=0, column=1, padx = 5, pady = 5)

        self.btnPaste = tk.Button(self.toolbarFrame, text = "Paste", padx = 5, pady = 5)
        self.btnPaste.grid(row=0, column=2, padx = 5, pady = 5)

        self.btnUndo = tk.Button(self.toolbarFrame, text = "Undo", padx = 5, pady = 5)
        self.btnUndo.grid(row=0, column=3, padx = 5, pady = 5)

        self.btnRedo = tk.Button(self.toolbarFrame, text = "Redo", padx = 5, pady = 5)
        self.btnRedo.grid(row=0, column=4, padx = 5, pady = 5)

        self.btnRun = tk.Button(self.toolbarFrame, text = "Run", padx = 5, pady = 5, command= self.run_script)
        self.btnRun.grid(row=0, column=5, padx = 5, pady = 5)

        self.btnStop = tk.Button(self.toolbarFrame, text = "Stop", padx = 5, pady = 5)
        self.btnStop.grid(row=0, column=6, padx = 5, pady = 5)

        self.btnStep = tk.Button(self.toolbarFrame, text = "Step Info", padx = 5, pady = 5)
        self.btnStep.grid(row=0, column=7, padx = 5, pady = 5)

        self.btnSave = tk.Button(self.toolbarFrame, text = "Save", padx = 5, pady = 5, command=self.merge_xml_files.read_xmls)
        self.btnSave.grid(row=0, column=8, padx = 5, pady = 5)

        self.btnDelete = tk.Button(self.toolbarFrame, text = "Delete", padx = 5, pady = 5)
        self.btnDelete.grid(row=0, column=9, padx = 5, pady = 5)

        self.btnZoomIn = tk.Button(self.toolbarFrame, text = "Zoom In", padx = 5, pady = 5)
        self.btnZoomIn.grid(row=0, column=10, padx = 5, pady = 5)

        self.btnZoomOut = tk.Button(self.toolbarFrame, text = "Zoom Out", padx = 5, pady = 5)
        self.btnZoomOut.grid(row=0, column=11, padx = 5, pady = 5)

    def run_script(self):
         os.system('python ' + self.file_path + 'readxml.py')