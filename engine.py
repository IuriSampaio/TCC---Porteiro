import face_recognition as fr

def reconhece_face(url_foto):
    foto = fr.load_image_file(url_foto)
    rostos = fr.face_encodings(foto)
    if(len(rostos) > 0):
        return True, rostos
    
    return False, []

def get_rostos():
    rostos_conhecidos = []
    nomes_dos_rostos = []

    iuri = reconhece_face("./rostos_conhecidos/iuri.jpg")
    if(iuri[0]):
        rostos_conhecidos.append(iuri[1][0])
        nomes_dos_rostos.append("Iuri")

    ney = reconhece_face("./rostos_conhecidos/neymar.jpg")
    if(ney[0]):
        rostos_conhecidos.append(ney[1][0])
        nomes_dos_rostos.append("Neymar")
    
    leo = reconhece_face("./rostos_conhecidos/leo.jpg")
    if(leo[0]):
        rostos_conhecidos.append(leo[1][0])
        nomes_dos_rostos.append("Leo")

    leandro = reconhece_face("./rostos_conhecidos/leandro.jpg")
    if(leandro[0]):
        rostos_conhecidos.append(leandro[1][0])
        nomes_dos_rostos.append("Leandro")

    mat = reconhece_face("./rostos_conhecidos/mateus.jpeg")
    if(mat[0]):
        rostos_conhecidos.append(mat[1][0])
        nomes_dos_rostos.append("Mateus")

    will = reconhece_face("./rostos_conhecidos/will.jpeg")
    if(will[0]):
        rostos_conhecidos.append(will[1][0])
        nomes_dos_rostos.append("Will")

    
    
    return rostos_conhecidos, nomes_dos_rostos