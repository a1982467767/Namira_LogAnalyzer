import os
import sys
import platform
import shutil

cwd = os.path.abspath(__file__)
setup_dir = os.path.dirname(cwd)

# clearing __pycache__
root_pycache = os.path.join(setup_dir, '__pycache__')
src_pycache = os.path.join(setup_dir, 'loganalyzer', '__pycache__')
gui_pycache = os.path.join(setup_dir, 'loganalyzer', '__pycache__')
scripts_pycache = os.path.join(setup_dir, 'loganalyzer', 'scripts', '__pycache__')
gui_mainwindow_pycache = os.path.join(setup_dir, 'loganalyzer', '__pycache__')
scripts_lyricsources_pycache = os.path.join(setup_dir, 'loganalyzer', 'scripts', '__pycache__')
setup(
    name="loganalyzer",
    version='1.0',
    description='Python Script for parsing and analyzing agent2D socer simulation rcl and rcg logs',
    long_description=open("README.md").read(),
    author='Shahryar Bhm & Farzin Negahbani',
    author_email='shahryarbahmeie@gmail.com , farzin.negahbani@gmail.comh',
    url='https://github.com/Farzin-Negahbani/Namira_LogAnalyzer',
    packages=['loganalyzer',],
    entry_points={  # Optional
        'console_scripts': [
            'loganalyzer=loganalyzer.__main__:main',
        ],
    },
    install_requires=['shapely',]
)