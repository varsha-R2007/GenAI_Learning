# pip,virtual environment,.env files
# pip: pip installs packages. package manager
#virtual environment: A 'venv' is a directory that contains
# 1. A copy of the python interpreter
# 2. its own 'pip'
# 3. its own site-packages directory. Default target location
# where python installs third party libraries
# 4. Activation scripts that modify PATH

python --version #windows 
python3 --version #mac

#to create virtual environment
python -m venv .venv #windows
python3 -m venv .venv #mac

#Activate
.venv\Scripts\activate.bat #windows
source .venv/bin/activate #mac

#deactivate
deactivate

# pip installation (install dependencies/libraries)
pip install package_name #syntax

pip install python-dotenv