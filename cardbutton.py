import tkinter as tk
from PIL import Image, ImageTk

class Imgbutton(tk.Canvas):

    def __init__(self, master=None, image=None, command=None, **kw):

        super(Imgbutton, self).__init__(master=master, **kw)
        self.set_img = self.create_image(0, 0, anchor='nw', image=image)
        self.bind_class( self, '<Button-1>',
                    lambda _: self.config(relief='sunken'), add="+")

        self.bind_class( self, '<ButtonRelease-1>',
                    lambda _: self.config(relief='groove'), add='+')

        self.bind_class( self, '<Button-1>',
                    lambda _: command() if command else None, add="+")