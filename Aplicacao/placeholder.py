from tkinter import *

"""
Essa classe personalizada cria uma entry com placeholder.
"""


class EntPlaceHold(Entry):

    def __init__(self, master=None, placeholder='PLACEHOLDER', color='black'):
        super().__init__(master)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind('<FocusIn>', self.Focus)  # '<FocusIn>' é o evento em que o mouse passa por cima da entry
        self.bind('<FocusOut>', self.FocusOut)  # '<FocusOut>' é o contrario do In.

        self.PutPlaceHolder()

    def PutPlaceHolder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def Focus(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def FocusOut(self, *args):
        if not self.get():
            self.PutPlaceHolder()
