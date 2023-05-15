import face_recognition
from typing import NoReturn
import os
import shutil
import datetime


def file_transfer(source, target, face_file, slider_value):
    # print(slider_value)
    no_of_files = 0
    known_face_encodings_list = []
    # Load the known face image
    known_image = face_recognition.load_image_file(face_file)
    if face_file.endswith(".jpg") or face_file.endswith(".jpeg") or face_file.endswith(".png"):
        for known_face in face_recognition.face_encodings(known_image):
            known_face_encodings_list.append(known_face)
        # known_face_encoding = face_recognition.face_encodings(known_image)[0]
    else:
        print('File format is not appropriate')

    # get the directory name
    now = datetime.datetime.now()

    # Create a new directory for the matched files
    matched_dir = target
    os.makedirs(matched_dir, exist_ok=True)

    # Loop through each file in the directory and compare its face to the known face
    directory = source

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Load the image
            image = face_recognition.load_image_file(os.path.join(directory, filename))

            # Find all the faces in the image
            face_locations = face_recognition.face_locations(image)
            face_encodings = face_recognition.face_encodings(image, face_locations)

            for face_encoding in face_encodings:
                for known_face_enc in known_face_encodings_list:
                    # Compare the face encoding with the known face encoding
                    results = face_recognition.compare_faces([known_face_enc], face_encoding,
                                                             tolerance=slider_value / 100)

                    if results[0]:
                        no_of_files = no_of_files + 1
                        print(f"{filename} matched with Face!! >>>>>> File successfully transferred...")
                        # Copy the matched file to the new directory
                        src = os.path.join(directory, filename)
                        dst = os.path.join(matched_dir, filename)
                        shutil.copy(src, dst)
                    else:
                        print(f"{filename} is not matching with Face!! >> Failed ...")
    return no_of_files


class Exit:
    def __init__(self) -> None:
        self.exit_code = 0

    def success(self) -> NoReturn | None:
        self.exit_code = 0
        return exit(self.exit_code)

    def error(self, msg: str) -> NoReturn | None:
        self.exit_code = 1
        return exit(self.exit_code)


exit_program = Exit()
