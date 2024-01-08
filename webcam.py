import numpy as np
import face_recognition as fr
import cv2
from main import get_faces

recognized_faces, face_name = get_faces()

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

    face_location = fr.face_locations(rgb_frame)
    unknown_faces = fr.face_encodings(rgb_frame, face_location)

    for (top, right, bottom, left), unknown_faces in zip(face_location, unknown_faces):
        resultados = fr.compare_faces(recognized_faces, unknown_faces)
        print(resultados)

        face_distances = fr.face_distance(recognized_faces, unknown_faces)

        better_id = np.argmin(face_distances)
        if resultados[better_id]:
            name = face_name [better_id]
        else:
            name = "Unknown"

        #Ao redor do rosto
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #Embaixo
        cv2.rectangle(frame, (left, bottom -35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_SIMPLEX

        #Texto
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('Cool Recognizer Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()