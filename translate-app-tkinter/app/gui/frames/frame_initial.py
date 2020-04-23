import pyperclip
import tkinter as tk

from tkinter import ttk
from tkinter import filedialog

from ..frames.frame_initial_w import FrameInitialWidgets
from ...utils.thread import run_async

class FrameInitial(tk.Frame):
    def __init__(self, window, *args, **kwargs):
        super().__init__(window, *args, **kwargs)
        self.window = window
        self.widgets = FrameInitialWidgets(self)
        self.manager = self.window.service_manager
        self._set_available_services()

        self.widgets.translate_button.bind("<Button-1>", self.translate_text)
        self.widgets.combobox_t_from.bind("<<ComboboxSelected>>", self._set_source_language)
        self.widgets.combobox_t_into.bind("<<ComboboxSelected>>", self._set_target_language)
        self.widgets.comboxbox_service.bind("<<ComboboxSelected>>", self._set_translate_languages)
        self.widgets.button_load_file.bind("<Button-1>", self.load_file)
        self.widgets.button_save.bind("<Button-1>", self.save_translated_text)
        self.widgets.button_copy.bind("<Button-1>", self.copy_translated_text)

        self.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

    @property
    def service_name(self):
        return self.widgets.comboxbox_service.get()

    def load_file(self, event):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                        filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        with open(filename, "r", encoding="utf-8") as f:
            text = "".join(f.readlines())
            self.set_source_text(text)

    def save_translated_text(self, event):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text = str(self.widgets.Scrolledtext2.get(1.0, tk.END))
        f.write(text)
        f.close()

    def copy_translated_text(self, event):
        text = str(self.widgets.Scrolledtext2.get(1.0, tk.END))
        pyperclip.copy(text)

    def set_source_text(self, text):
        text_w = self.widgets.Scrolledtext1
        text_w.delete('1.0', tk.END)
        text_w.insert('end', text)

    def set_target_text(self, text):
        text_w = self.widgets.Scrolledtext2
        text_w.configure(state='normal')
        text_w.delete('1.0', tk.END)
        text_w.insert('end', text)
        text_w.configure(state='disabled')

    def _set_available_services(self):
        self.widgets.comboxbox_service["values"] = self.manager.get_avaliable_services()

    @run_async
    def _set_translate_languages(self, event):

        try:
            self.widgets.create_progress_bar()
            self.manager.set_service(self.service_name, 10, 10)
            translator = self.manager.get_translator(self.service_name)

            self.widgets.combobox_t_from["values"] = translator.get_valid_languages()
            self.widgets.combobox_t_into["values"] = translator.get_valid_languages()
            self.widgets.combobox_t_into.current(0)
            self._set_target_language(None)
        finally:
            self.widgets.destroy_progress_bar()

    def _set_source_language(self, event):
        language = self.widgets.combobox_t_from.get()
        translator = self.manager.get_translator(self.service_name)
        translator.set_source_language(language)

    def _set_target_language(self, event):
        language = self.widgets.combobox_t_into.get()
        translator = self.manager.get_translator(self.service_name)
        translator.set_target_language(language)

    @run_async
    def translate_text(self, event):
        def set_variable(translator):
            variable.set(int(100 * len(translator._cache_translated_source)/len(text)))
            self.set_target_text(translator._cache_translated_target)

        try:
            variable = tk.IntVar()
            text = self.widgets.Scrolledtext1.get("1.0", tk.END)
            translator = self.manager.get_translator(self.service_name)
            translator.callback = set_variable

            self.widgets.create_progress_bar(variable)
            source_language = self.widgets.combobox_t_from.get()
            target_language = self.widgets.combobox_t_into.get()
            text_tranlated = translator.translate_text(text, target_language=target_language, source_language=source_language)
            self.set_target_text(text_tranlated)
        finally:
            self.widgets.destroy_progress_bar()



