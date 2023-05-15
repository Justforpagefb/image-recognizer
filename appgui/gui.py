import PySimpleGUI as sg
import os

# absolute_path = os.path.dirname(__file__)
# relative_path = "image.png"
# full_path = os.path.join(absolute_path, relative_path)

sg.theme('DarkAmber')
sg.set_options(font=('Arial', 12))

layout: list = [
    [sg.Titlebar('Image Recognition', icon="./image.png")],
    [sg.Text('Image Processor - Amritsar')], [sg.HSeparator()],
    [
        sg.Text('Source Directory:', s=(14, 1)),
        sg.VSeperator(),
        sg.Input(key='-SourceFolderInput-', expand_x=True),
        sg.VSeperator(),
        sg.FolderBrowse(
            key='-SourceFolder-',
            target=(sg.ThisRow, -2),
            tooltip=
            'Browse for directory containing the all images - you wish to inspect and transfer.')
    ],
    [
        sg.Text('Destination Folder:', s=(14, 1)),
        sg.VSeperator(),
        sg.Input(key='-TargetFolderInput-', expand_x=True),
        sg.VSeperator(),
        sg.FolderBrowse(
            key='-TargetFolder-',
            target=(sg.ThisRow,
                    -2),
            tooltip='Browse for target directory you wish to transfer files to.'
        )
    ],
    [
        sg.Text('Select Image :', s=(14, 1)),
        sg.VSeperator(),
        sg.Input(key='-faceFileFaceImage-', expand_x=True),
        sg.VSeperator(),
        sg.FileBrowse(
            key='-faceFileFileBrowse-',
            target=(sg.ThisRow,
                    -2),
            tooltip='Select the face'
        )
    ],
    [
        sg.Text('%age transfer :', s=(14, 1)),
        sg.VSeperator(),
        sg.Slider(range=(10, 90), default_value=60,
                  expand_x=True, enable_events=True,
                  orientation='horizontal', key='-SL-',
                  tooltip='More %age more images will be transferred'
                  ),
        sg.VSeperator(),
    ],
    [
        sg.Button('Start Transfer',
                  key='-Transfer-',
                  button_color=('white', 'green'))
    ],
    [
        sg.ProgressBar(max_value=25,
                       size=(30, 10),
                       orientation='horizontal',
                       key='-ProgressBar-',
                       expand_x=True)
    ], [sg.HSeparator()],
    [
        sg.Multiline(s=(30, 30),
                     expand_x=True,
                     expand_y=True,
                     disabled=True,
                     key='-Log-',
                     reroute_stdout=True,
                     write_only=True,
                     auto_refresh=True,
                     autoscroll=True)
    ], [sg.HSeparator()], [sg.Exit(button_color=('white', 'firebrick4'))]
]

window: sg.Window = sg.Window('Image Recognition',
                              layout,
                              auto_size_buttons=True,
                              text_justification='c',
                              element_justification='c',
                              size=(1200, 600),
                              icon="./image.png"
                              )
