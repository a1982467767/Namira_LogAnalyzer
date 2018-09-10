import os
import sys
import platform
import shutil

# finding os platform
os_type = platform.system()

if os_type == 'Linux':
    from setuptools import setup
    setuptools_available = True
    print(os_type + " detected!")
else:
    print('This script is only work for GNU/Linux or BSD!')
    sys.exit(1)
# Checking dependencies!
not_installed = ''

# python3-requests
try:
    import shapely
    print('Shapely is found!')
except:
    print('Error : Shapely is not installed!')
    not_installed = not_installed + 'shapely, '

# show warning , if dependencies not installed!
if not_installed != '':
    print('########################')
    print('####### WARNING ########')
    print('########################')
    print('Some dependencies are not installed .It causes some problems for Lingua Lyrics! : \n')
    print(not_installed + '\n\n')
    print('Read this link for more information: \n')
    print('')
    answer = input('Do you want to continue?(y/n)')
    if answer not in ['y', 'Y', 'yes']:
        sys.exit(1)
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
    author_email='shahryarbahmeie@gmail.com',
    url='https://github.com/Farzin-Negahbani/Namira_LogAnalyzer',
    packages=['loganalyzer',],
    entry_points={  # Optional
        'console_scripts': [
            'loganalyzer=loganalyzer.__main__:main',
        ],
    },
    install_requires=['shapely',]
)