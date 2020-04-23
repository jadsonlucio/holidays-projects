import tkinter as tk

from .frames.frame_initial import FrameInitial
from ..api.services import ServiceManager

class Window(tk.Tk):
    def __init__(self, title, width, height, pos_x=0, pos_y=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.service_manager = ServiceManager()

        self.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
        self.minsize(120, 1)
        self.maxsize(770, 808)
        self.resizable(0, 0)
        self.title(title)
        self.configure(background="#d9d9d9")
        self.frame_inicial = FrameInitial(self)
