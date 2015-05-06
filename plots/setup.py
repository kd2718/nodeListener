from distutils.core import setup
import py2exe
import matplotlib

setup( 
    windows=[{'script': r'live_plots.py'}], 

    data_files=matplotlib.get_py2exe_datafiles(), 

    # options={
        # r'py2exe': {
            # r'includes': r'ElementConfig', 
            # r'includes': r'ColorConv', 
            # r'includes': r'Tkinter', 
            # r'includes': r're', 
            # r'includes': r'math', 
            # r'includes': r'sys', 
            # r'includes': r'matplotlib', 
            # r'includes': r'mpl_toolkits',
            # r'includes': r'matplotlib.backends.backend_wx',
            # r'dll_excludes': [r'MSVCP90.dll'], 
        # }
    # }, 

) 


# import pymssql
# import matplotlib.pyplot as plt
# import time
# from datetime import datetime
# import numpy as np
# import matplotlib.animation as animation