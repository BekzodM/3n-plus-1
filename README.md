# 3n-plus-1
Python script that lets you test the 3n+1 conjecture and save the graph image of the results.

## Getting Started
To run this program you will need to install 4 things
- This repository (3n-plus-1)
- Python version 3.4+ (Latest recommended)
- numpy
- matplotlib

### Downloading this repo
From the main page of this repo, click on "Code" and choose a method of downloading.  
Below is a way to download with ZIP
![how to download repo](https://github.com/BekzodM/3n-plus-1/blob/main/images/download_howto.jpg?raw=true)  
When the download is finished, extract the zip file.  
For Windows:  
Right-click -> Extract All  
For MacOS:  
Simply double-click  

### Installing Python
First check if you already have Python installed in your system.  
Windows/MacOS/Linux: Open your command prompt/terminal and type 
```
python3 --version
```
If it outputs a Python version (ex: "Python 3.7.3"), then your system already has Python and you can skip the "Installing Python" step.  
If you do not have Python, download the latest Python installer from [here](https://www.python.org/downloads/) for your OS.  
Open the installer/setup file and go through the basic installation process.  

### Installing matplotlib and numpy
We will install numpy and matplotlib through pip command.  
If you have Python version 3.4 or later, then pip should be pre-installed in your system. (check [here](https://pip.pypa.io/en/stable/installation/) if pip is not installed)  
Before installing numpy and matplotlib we will create a virtual environment.  
Open your command prompt/terminal -> navigate to the folder that conjecture.py file is stored -> type 
```
python3 -m venv newenv 
```
This will create a virtual environment with the name "newenv" so we can install numpy and matplotlib in this new environment.  
(For Windows) In your command prompt type 
```
newenv\Scripts\activate
```
(For Mac/Linux) In your terminal type
```
source newenv/bin/activate
```
This will activate your virtual environment.  
Now that the environment is activated, type 
```
pip install numpy
```
to install numpy.  
Once the installation is finished go ahead and install matplotlib
```
pip install matplotlib
```

## How to use
Once you have everything set up and your virtual environment is active and in the same folder as conjecture.py, run the program through your command line/terminal.
```
python conjecture.py
```
The rest is simple!  
You should be asked to enter a number, so enter a valid number and press 'Enter'  
Your command prompt will print all the values of the conjecture and other information. Then a graph will appear with the values of the 3n+1 (collatz) conjecture based on your entered number.  
Don't worry an image of the graph is also saved in the same folder as your script. The name of this image file will correspond to the number you entered in the beginning. 
