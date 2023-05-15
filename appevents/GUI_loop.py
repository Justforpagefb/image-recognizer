from random import uniform
from time import sleep
from datetime import date

from appevents.events import exit_program, file_transfer
from appgui.gui import sg, window

# pyinstaller --onefile --windowed --clean --add-data 'C:/Users/MYNAME/AppData/Local/Programs/Python/Python311/Lib/site-packages/face_recognition_models/;face_recognition_models' --hidden-import 'face_recognition_models' --icon=./icon.ico main.py

def GUI_loop() -> None:
    """Main GUI loop.

    - Starts processing of window events.

    ---

    :return: program window
    :rtype: None
    """

    while True:
        event, vals = window.read()  # Get events from GUI window

        # logger.info(f'{event} : {vals}')  # Log events

        if event in [sg.WIN_CLOSED, 'Exit', 'Cancel']:  # Exit events
            break

        if event == 'sg.WIN_CLOSED' or event == 'Cancel' :  
            break

        if event == '-Transfer-':  # Process Transfer button event

            # No source directory entered
            if len(vals['-SourceFolderInput-']) < 1:
                sg.Popup('Make sure all fields are filled out!')
                continue

            # No target directory entered
            if len(vals['-TargetFolderInput-']) < 1:
                sg.Popup('Make sure all fields are filled out!')
                continue

            # No file extension entered
            if len(vals['-faceFileFaceImage-']) < 1:
                sg.Popup('Make sure all fields are filled out!')
                continue

            today = date.today()
            expiration_date = date(2023, 5, 27)
            if today > expiration_date:
                print(" ***************************************************************************** ")
                print(" ************ Application is expired .. Contact Owner ...  ")
                print(" ***************************************************************************** ")
            else:
                # Start Transfer
                transfer: int = file_transfer(vals['-SourceFolderInput-'],
                                              vals['-TargetFolderInput-'],
                                              vals['-faceFileFaceImage-'],
                                              vals['-SL-'])
                print(" ************************************************************************************* ")
                print(f" >>>> Completed! {transfer} files transferred Successfully ....  ")
                print(" ************************************************************************************* ")

    window.close()  # Close window and return system resources

    return exit_program.success()  # Return successful exit status
