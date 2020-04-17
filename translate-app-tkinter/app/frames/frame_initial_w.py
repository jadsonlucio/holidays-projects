import tkinter as tk
from tkinter import ttk
from frames.tk_widgets.custom_widgets import ScrolledText

class FrameInitialWidgets(tk.Frame):
    def __init__(self, frame_initial, *args, **kwargs):
        super().__init__(frame_initial, *args, **kwargs)
        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.configure(relief='groove')
        self.configure(borderwidth="2")
        self.configure(relief="groove")
        self.configure(background="#d9d9d9")

        self.construct()

    def construct(self):
        font10 = "-family {Tahoma} -size 14 -weight bold"
        font13 = "-family {Tahoma} -size 10 -weight bold"
        font9 = "-family {Segoe UI} -size 9 -weight bold"

        self.comboxbox_service = ttk.Combobox(self)
        self.comboxbox_service.place(relx=0.297, rely=0.035, relheight=0.027, relwidth=0.177)
        self.comboxbox_service.configure(state='readonly')
        self.comboxbox_service.configure(takefocus="")

        self.label1 = tk.Label(self)
        self.label1.place(relx=0.012, rely=0.026, height=31, width=215)
        self.label1.configure(activebackground="#f9f9f9")
        self.label1.configure(activeforeground="black")
        self.label1.configure(background="#d9d9d9")
        self.label1.configure(borderwidth="0")
        self.label1.configure(disabledforeground="#a3a3a3")
        self.label1.configure(font="-family {Tahoma} -size 14 -weight bold")
        self.label1.configure(foreground="#000000")
        self.label1.configure(highlightbackground="#d9d9d9")
        self.label1.configure(highlightcolor="black")
        self.label1.configure(padx="0")
        self.label1.configure(pady="0")
        self.label1.configure(text='''Available services''')

        self.label2 = tk.Label(self)
        self.label2.place(relx=0.037, rely=0.13, height=21, width=147)
        self.label2.configure(activebackground="#f9f9f9")
        self.label2.configure(activeforeground="black")
        self.label2.configure(background="#d9d9d9")
        self.label2.configure(disabledforeground="#a3a3a3")
        self.label2.configure(font="-family {Tahoma} -size 10 -weight bold")
        self.label2.configure(foreground="#000000")
        self.label2.configure(highlightbackground="#d9d9d9")
        self.label2.configure(highlightcolor="black")
        self.label2.configure(text='''Translate from''')

        self.combobox_t_from = ttk.Combobox(self)
        self.combobox_t_from.place(relx=0.223, rely=0.13, relheight=0.027, relwidth=0.177)
        self.combobox_t_from.configure(state='readonly')
        self.combobox_t_from.configure(takefocus="")

        self.label3 = tk.Label(self)
        self.label3.place(relx=0.594, rely=0.13, height=21, width=92)
        self.label3.configure(activebackground="#f9f9f9")
        self.label3.configure(activeforeground="black")
        self.label3.configure(background="#d9d9d9")
        self.label3.configure(disabledforeground="#a3a3a3")
        self.label3.configure(font="-family {Tahoma} -size 10 -weight bold")
        self.label3.configure(foreground="#000000")
        self.label3.configure(highlightbackground="#d9d9d9")
        self.label3.configure(highlightcolor="black")
        self.label3.configure(text='''Translate into''')

        self.combobox_t_into = ttk.Combobox(self)
        self.combobox_t_into.place(relx=0.743, rely=0.13, relheight=0.027, relwidth=0.177)
        self.combobox_t_into.configure(state='readonly')
        self.combobox_t_into.configure(takefocus="")

        self.translate_button = tk.Button(self)
        self.translate_button.place(relx=0.408, rely=0.753, height=94, width=137)

        self.translate_button = tk.Button(self)
        self.translate_button.place(relx=0.408, rely=0.753, height=94, width=137)

        self.translate_button.configure(activebackground="#ececec")
        self.translate_button.configure(activeforeground="#000000")
        self.translate_button.configure(background="#d9d9d9")
        self.translate_button.configure(disabledforeground="#a3a3a3")
        self.translate_button.configure(font="-family {Tahoma} -size 14 -weight bold")
        self.translate_button.configure(foreground="#000000")
        self.translate_button.configure(highlightbackground="#d9d9d9")
        self.translate_button.configure(highlightcolor="black")
        self.translate_button.configure(pady="0")
        self.translate_button.configure(text='''Translate''')

        self.Scrolledtext2 = ScrolledText(self)
        self.Scrolledtext2.place(relx=0.569, rely=0.169, relheight=0.526
                                 , relwidth=0.412)
        self.Scrolledtext2.configure(background="white")
        self.Scrolledtext2.configure(font="TkTextFont")
        self.Scrolledtext2.configure(foreground="black")
        self.Scrolledtext2.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext2.configure(highlightcolor="black")
        self.Scrolledtext2.configure(insertbackground="black")
        self.Scrolledtext2.configure(insertborderwidth="3")
        self.Scrolledtext2.configure(selectbackground="#c4c4c4")
        self.Scrolledtext2.configure(selectforeground="black")
        self.Scrolledtext2.configure(wrap="none")
        self.Scrolledtext2.configure(state="disable")

        self.Scrolledtext1 = ScrolledText(self)
        self.Scrolledtext1.place(relx=0.05, rely=0.169, relheight=0.526
                                 , relwidth=0.412)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")


        self.button_load_file = ttk.Button(self)
        self.button_load_file.place(relx=0.928, rely=0.013, height=40, width=40)
        self.button_load_file.configure(text='''Open''')

        self.button_copy = tk.Button(self)
        self.button_copy.place(relx=0.916, rely=0.714, height=44, width=47)
        self.button_copy.configure(activebackground="#ececec")
        self.button_copy.configure(activeforeground="#000000")
        self.button_copy.configure(background="#d9d9d9")
        self.button_copy.configure(disabledforeground="#a3a3a3")
        self.button_copy.configure(font=font9)
        self.button_copy.configure(foreground="#000000")
        self.button_copy.configure(highlightbackground="#d9d9d9")
        self.button_copy.configure(highlightcolor="black")
        self.button_copy.configure(pady="0")
        self.button_copy.configure(text='''Copy''')

        self.button_save = tk.Button(self)
        self.button_save.place(relx=0.842, rely=0.714, height=44, width=47)
        self.button_save.configure(activebackground="#ececec")
        self.button_save.configure(activeforeground="#000000")
        self.button_save.configure(background="#d9d9d9")
        self.button_save.configure(disabledforeground="#a3a3a3")
        self.button_save.configure(font=font9)
        self.button_save.configure(foreground="#000000")
        self.button_save.configure(highlightbackground="#d9d9d9")
        self.button_save.configure(highlightcolor="black")
        self.button_save.configure(pady="0")
        self.button_save.configure(text='''Save''')


    def disable(self, enable=False):
        if not enable:
            self.Scrolledtext1.configure(state="disable")
            self.comboxbox_service.configure(state="disable")
            self.combobox_t_into.configure(state="disable")
            self.combobox_t_from.configure(state="disable")
            self.translate_button.configure(state="disable")
            self.button_load_file.state(["disabled"])
        else:
            self.Scrolledtext1.configure(state="normal")
            self.comboxbox_service.configure(state="readonly")
            self.combobox_t_into.configure(state="readonly")
            self.combobox_t_from.configure(state="readonly")
            self.translate_button.configure(state="normal")
            self.button_load_file.state(["!disabled"])

    def create_progress_bar(self, variable = None):
        self.disable()
        if variable:
            self.progress_bar = ttk.Progressbar(self, variable=variable, maximum=100)
        else:
            self.progress_bar = ttk.Progressbar(self, mode="indeterminate")
            self.progress_bar.start(50)
        self.progress_bar.place(relx=0.198, rely=0.935, relwidth=0.619, relheight = 0.0, height = 22)
        self.progress_bar.configure(length="500")

    def destroy_progress_bar(self):
        self.progress_bar.destroy()
        self.disable(enable=True)