import face_recognition as fr
from main import recognize_face, get_faces

unknown = recognize_face("./photos/Chagas.jpeg")
if(unknown[0]):
    unknown_faces = unknown[1][0]
    recognized_faces, nomes_dos_rostos = get_faces()
    results = fr.compare_faces(recognized_faces, unknown_faces)
    print(results)

    for i in range(len(recognized_faces)):
        result = results[i]
        if(result):
            print("Face", nomes_dos_rostos[i], "recognized")


else:
    print ("No faces found")

