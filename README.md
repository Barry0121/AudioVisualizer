# Audio Visualizer
Audio Visualization with Python (Early Scoping)

## Quick Setup to Work on this Project
1. Create venv/conda environment with `requirement.txt` and `environment.yaml` <br>
- If you are using `pip` as your dependency manager: 
  1. create a venv (python virtual environment) at desired location by running: `python3 -m venv [/path/to/new/virtual/environment]`
     1. For example, on windows: `c:\>python -m venv c:\path\to\myenv`
  2. make sure to activate that environment: 
     1. Bash: `$ source <venv>/bin/activate`
     2. Cmd: `C:\> <venv>\Scripts\activate.bat`
     3. PowerShell: `PS C:\> <venv>\Scripts\Activate.ps1`
  3. run `pip install -r requiremnt.txt` to install all the required dependency
  * Note: `pip` can only work with `requirement.txt`
- If you are using `conda`, there are two options: 
    1. create a new `conda env` with `environment.yaml` (you can't specify environment's name): `conda env create -f environment.yml`
    2. create a new environment with `requiremnt.txt` (you have to specify environment's name): `conda create --name <env_name> --file requirements.txt`

## Folder Description
* `app`: This is where the approved features will be saved. All features that gets pushed here is ready to be refactored and compiled into ready-to-use application. This means that a `__init__.py`, `config.yaml`, and other module that connect all the modules will be here. 
* `dev`: This is the development channel. There is no rigid structure to be implemented in this directory. We will be relying on naming to divide each features/modules, because they are still in development. Most of the time, we will be working with files in this directory. 
* `files`: We store all of the utility files here, including images, audio, text, etc. The purpose of having this folder is to separate the code and other files so the development environment is clean.  
* `util`: This is technically also a part of the development channel, we will constantly update this folder with python files containing useful functions we have written that can during both application development and feature creation. 

Please make sure to follow the general structure of the repository. (When in doubt, put the files in `dev`).
