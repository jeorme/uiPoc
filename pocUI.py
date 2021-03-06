#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.23
#  in conjunction with Tcl version 8.6
#    May 20, 2019 06:37:46 AM CEST  platform: Windows NT

import sys
from backend import getTrade, price,pushTrade, priceBatch
from functools import partial


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pocUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    pocUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    pocUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 10 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

        top.geometry("1073x683+536+116")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.menubar = tk.Menu(top, font=('Segoe UI', 9, ), bg=_bgcolor
                ,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font=('Segoe UI',9,),
                foreground="#000000",
                label="trade capture")
        self.sub_menu1 = tk.Menu(top,tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                compound="left",
                font=('Segoe UI',9,),
                foreground="#000000",
                label="marketData")

        self.output = tk.Text(top)
        self.output.place(relx=0.699, rely=0.015, relheight=0.182
                , relwidth=0.181)
        self.output.configure(background="white")
        self.output.configure(font=font9)
        self.output.configure(foreground="black")
        self.output.configure(highlightbackground="#d9d9d9")
        self.output.configure(highlightcolor="black")
        self.output.configure(insertbackground="black")
        self.output.configure(selectbackground="#c4c4c4")
        self.output.configure(selectforeground="black")
        self.output.configure(width=194)
        self.output.configure(wrap="word")

        self.tradeIdLabel = tk.Label(top)
        self.tradeIdLabel.place(relx=0.019, rely=0.144, height=56, width=92)
        self.tradeIdLabel.configure(background="#d9d9d9")
        self.tradeIdLabel.configure(disabledforeground="#a3a3a3")
        self.tradeIdLabel.configure(foreground="#000000")
        self.tradeIdLabel.configure(text='''trade ID''')
        self.tradeIdLabel.configure(width=92)

        self.tradeTypeCombo = ttk.Combobox(top,state="readonly")  # 3
        self.tradeTypeCombo.place(relx=0.121, rely=0.044, height=24, relwidth=0.19)
        self.tradeTypeCombo['values'] = ["FXO VANILLA","FX SPOT","FX FORWARD","FX SWAP", "SWAP"]
        self.tradeTypeCombo.current(0)

        self.tradeIdCombo = ttk.Combobox(top)  # 3
        self.tradeIdCombo.place(relx=0.121, rely=0.144, height=24, relwidth=0.19)
        self.tradeIdCombo['values'] = getTrade(self.tradeTypeCombo.get())
        self.tradeTypeCombo.bind("<<ComboboxSelected>>", self.getTradeId)

        self.price = tk.Button(top, command=partial(price, self.tradeIdCombo, self.output))
        self.price.place(relx=0.475, rely=0.029, height=53, width=106)
        self.price.configure(activebackground="#ececec")
        self.price.configure(activeforeground="#000000")
        self.price.configure(background="#d9d9d9")
        self.price.configure(disabledforeground="#a3a3a3")
        self.price.configure(foreground="#000000")
        self.price.configure(highlightbackground="#d9d9d9")
        self.price.configure(highlightcolor="black")
        self.price.configure(pady="0")
        self.price.configure(text='''price''')
        self.price.configure(width=106)

        self.PathTypeCombo = ttk.Combobox(top, state="readonly")  # 3
        self.PathTypeCombo.place(relx=0.499, rely=0.315, height=24, relwidth=0.19)
        self.PathTypeCombo['values'] = ["FXO VANILLA", "FX SPOT", "FX FORWARD", "FX SWAP", "SWAP"]
        self.PathTypeCombo.current(0)

        self.tradePath = tk.Text(top)
        self.tradePath.place(relx=0.699, rely=0.315, relheight=0.182
                          , relwidth=0.181)
        self.tradePath.configure(background="white")
        self.tradePath.configure(font=font9)
        self.tradePath.configure(foreground="black")
        self.tradePath.configure(highlightbackground="#d9d9d9")
        self.tradePath.configure(highlightcolor="black")
        self.tradePath.configure(insertbackground="black")
        self.tradePath.configure(selectbackground="#c4c4c4")
        self.tradePath.configure(selectforeground="black")
        self.tradePath.configure(width=194)
        self.tradePath.configure(wrap="word")

        self.push = tk.Button(top, command=partial(pushTrade, self.tradePath, self.PathTypeCombo,self.output))
        self.push.place(relx=0.475, rely=0.129, height=53, width=106)
        self.push.configure(activebackground="#ececec")
        self.push.configure(activeforeground="#000000")
        self.push.configure(background="#d9d9d9")
        self.push.configure(disabledforeground="#a3a3a3")
        self.push.configure(foreground="#000000")
        self.push.configure(highlightbackground="#d9d9d9")
        self.push.configure(highlightcolor="black")
        self.push.configure(pady="0")
        self.push.configure(text='''push''')
        self.push.configure(width=106)

        self.batch = tk.Button(top, command=partial(priceBatch, self.tradePath, self.PathTypeCombo,self.output))
        self.batch.place(relx=0.475, rely=0.229, height=53, width=106)
        self.batch.configure(activebackground="#ececec")
        self.batch.configure(activeforeground="#000000")
        self.batch.configure(background="#d9d9d9")
        self.batch.configure(disabledforeground="#a3a3a3")
        self.batch.configure(foreground="#000000")
        self.batch.configure(highlightbackground="#d9d9d9")
        self.batch.configure(highlightcolor="black")
        self.batch.configure(pady="0")
        self.batch.configure(text='''price bash''')
        self.batch.configure(width=106)

    def getTradeId(self,event):
        self.tradeIdCombo["values"] = getTrade(self.tradeTypeCombo.get())

if __name__ == '__main__':
    vp_start_gui()





