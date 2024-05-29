import pathlib
import os
import cv2
import face_recognition
import subprocess
import sys
import pyttsx3

# Load known face encodings & names
known_face_encodings = []
known_face_names = []

# load known faces & names
known_person1_image = face_recognition.load_image_file(r"C:\\Users\\bambo\\OneDrive\\Desktop\\projects\\ProjectNova\\AI intelligence\\person1.jpg")
known_person2_image = face_recognition.load_image_file(r"C:\\Users\\bambo\\OneDrive\Desktop\\projects\\ProjectNova\\AI intelligence\\person2.JPG")
known_person3_image = face_recognition.load_image_file(r"C:\\Users\\bambo\\OneDrive\\Desktop\\projects\\ProjectNova\\AI intelligence\\person3.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]

known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person1_encoding)

known_face_names.append("Micheal")
known_face_names.append("Tien")
known_face_names.append("Tien")

# Camera init
video_capture = cv2.VideoCapture(0)

# get absolute path for hello_tts
hello_tts_path = pathlib.Path(__file__).parent.parent / "hello_tts.py"


while True:
    #capture frame by frame
    ret, frame = video_capture.read()
    #find all face locations in current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    #loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #check if the face mathces any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            #call hello file w/ recogonized name
            python_path = sys.executable #uses the current interp
            subprocess.run([python_path, str(hello_tts_path), name])
        #draw box around the face and label with name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    #display the resulting frame
    cv2.imshow("Video", frame)
    #break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release the cam and close OpenCV 
video_capture.release()

