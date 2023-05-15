# Image-recognize-transfer
Python Application for transferring the image files containing certain face. 

# Steps to run this program on Windows 
- You need to install python. This code is for Python Version 3.11. 
- You need to install microsoft Visual Studio from the official website by selecting the desktop environment with C++ installed. 
- Install the CMAKE from the official website and add to the path variable too.  
- Then pip install dlib globally. 
- If all the above libraries are installed correctly then, pip install image_recognition will work. Install it globally. 
- Then make a new folder for virtual environment. Python -m venv image-venv  
- Activate the virtual environment 
- It requires PySimpleGUI library. 

# This Application is used to transfer image files. 
- Source Folder is the folder where the all the image files are stored. 
- Destination Folder is the folder where the images has to be transferred. 
- Then Select the image that must contain a face that has to be identified from the source images. 
- You can select the %age level, of matching the faces. 

# For a standalone application, you needs to run following command.
pyinstaller --onefile --windowed --clean --add-data 'C:/Users/MYNAME/AppData/Local/Programs/Python/Python311/Lib/site-packages/face_recognition_models/;face_recognition_models' --hidden-import 'face_recognition_models' --icon=./icon.ico main.py
