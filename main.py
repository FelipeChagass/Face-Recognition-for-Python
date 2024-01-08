import face_recognition as fr

def recognize_face(url_photo):
    photo = fr.load_image_file(url_photo)
    faces = fr.face_encodings(photo)
    if(len(faces) > 0):
        return True, faces
    
    return False, []

def get_faces():
    recognized_faces = []
    face_name = []

    felipe = recognize_face("./photos/Me.jpeg")

    if(felipe[0]):
        recognized_faces.append(felipe[1][0])
        face_name.append("Creator")

    chaquile = recognize_face("./photos/chaquile.png")
    if(chaquile[0]):
        recognized_faces.append(chaquile[1][0])
        face_name.append("Chaquille")
    return recognized_faces, face_name