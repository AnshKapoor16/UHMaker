# UHMaker
UHMaker is a desktop app developed using Python. It is used to draw smoothened FER UNIT HYDROGRAPHS along with providing the discharge for unit time intervals.

**REFER TO THE PROVIDED RESOURCES BELOW TO KNOW ABOUT UNIT HYDROGRAPH**
https://serc.carleton.edu/hydromodules/steps/derivation_unit.html


## Algorithm
The algorithm used is developed in Python using libraries such as:

**SciPy -** Used for interpolation and formation of the graph.

**Matplotlib -** Used to plot the graph.

**Numpy -** Used to access functions of numpy.

**OpenPyxl -** Used to connect the algorithm and export the graph to excel.

## Graphical User Interface(GUI)
The GUI is also developed in Python and the libraries used include:

**QT -** Qt is cross-platform software for creating graphical user interfaces as well as cross-platform applications that run on various software and hardware platforms.

**->PyQT -** PyQt is a Python binding of the cross-platform GUI toolkit Qt, implemented as a Python plug-in used to import widgets and load UI screens. 

**->QTDesigner -** Qt Designer is a Qt tool used for designing and building graphical user interfaces (GUIs) with Qt Widgets

## HOW TO RUN THE APP?
**STEP - 1 : Download all the given files and place them in a single folder of your choice.**

**STEP - 2 : Now make a virtual environment for python or use your global environment of python to install the required libraries: SciPy, Matplotlib, Numpy, Openpyxl, PyQt5 and QtDesigner. You can use 'pip' command in the console to install the libraries(pip install library_name).**

**STEP - 3 : Now after installation of the libraries, restart your IDE.**

**STEP - 4 : Run the file named "HomeScreenUpdated.py".**

**STEP - 5 : Input the values(you can use these values for trial(Select the subzone: 3(e), L = 128.48, A = 2532.6, S = 0.69, Lc =	55.27).**

**STEP - 6 : Enter the name of the excel file in which your graph and values will be exported.**

**STEP - 7 : Click on 'Export to Excel'.**

**STEP-8 : You can access your excel file in the same folder.**






