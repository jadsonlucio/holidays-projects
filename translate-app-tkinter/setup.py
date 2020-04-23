import os
import sys
from cx_Freeze import setup, Executable
from main import __version__, __email__, __author__

RELEASE = "dev"
os.environ["TCL_LIBRARY"] = "C:\\Users\\Jadson\\AppData\\Local\\Programs\\Python\Python37\\tcl\\tcl8.6"
os.environ["TK_LIBRARY"] = "C:\\Users\\Jadson\\AppData\\Local\\Programs\\Python\Python37\\tcl\\tk8.6"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages":["tkinter"] ,"include_files":["drivers/", "C:\\Users\\Jadson\\AppData\\Local\\Programs\\Python\Python37\\DLLs\\tcl86t.dll",
                                            "C:\\Users\\Jadson\\AppData\\Local\\Programs\\Python\Python37\\DLLs\\tk86t.dll"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None

if RELEASE == "prod":
    if sys.platform == "win32":
        base = "Win32GUI"



setup(name="tranlator",
        version=__version__,
        description="Translator application based on web services",
        options={"build_exe": build_exe_options},
        executables=[Executable("main.py", base=base, icon="icon.ico")])