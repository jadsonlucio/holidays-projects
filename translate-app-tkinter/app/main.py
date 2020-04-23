from gui.window import Window

__version__ = "0.0.1"
__author__ = "Jadson Lucio"
__email__ = "jadson.santos@arapiraca.ufal.br"


if __name__ == "__main__":
    main_window = Window(f"Tradutor v{__version__}", 808, 770)
    main_window.mainloop()