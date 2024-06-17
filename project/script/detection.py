import cv2
import numpy as np
import database import *
import random
import time

select = cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
resultado = cursor.fetchall()
print(resultado)

ids = []
a = ''
if not resultado:
    print('vazio')
    cursor.execute("INSERT INTO users (identif) VALUES (1)")
    connection.commit()
    a = 1
    print("if")
else:
    ids = []
    for x in resultado:
        ids.append(str(x).strip('()[].,'))
        b = ids[0]
        a = int(b) + 1
        print("else")
        print(a)
        time.sleep(2)
        cursor.execute("INSERT INTO users (indetif) VALUES (?)",(str(a),))
        connection.commit()

print(a)
#Verifica se existem IDs de usuário existentes no banco de dados.
#Se vazio ("vazio" em português), insere um novo usuário com ID 1 e atualiza a variável a para 1.
#Se as entradas existirem, recupera o último ID, incrementa-o em 1 e armazena-o em a.
#Imprime o ID do usuário atual (a) e insere um novo registro de usuário com este ID no banco de dados.   

#CONFIGURAÇÕES DE CAMERA
webcam = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("./lib/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("./lib/haarcascade_eye.xml")

amostra = 1
numeroAmostras = 8
largura, altura = 220, 220

print("Capturando as faces")
#nicializa um objeto de captura de webcam (webcam).
#Carrega classificadores pré-treinados para detecção de rosto (face_cascade) e detecção de olhos (eye_cascade) de locais especificados.
#Define as dimensões da imagem para rostos capturados (largura - largura, altura - altura).
#Imprime uma mensagem indicando o início da captura de rosto

while(True):
    s, video = webcam.read()
    imagemCinza = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    video = cv2.flip(video, 180)
    video = cv2.resize(video, (480, 360))
    faces = face_cascade.detectMultiScale(video, minNeighbors=20, minSize=(30, 30), maxSize=(400, 400))
    for (x, y, w, h) in faces:
        cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 4)
        region = video[y:y+h, x:x+w]
        if (amostra == 1):
            print(a)
            cv2.imwrite("./treinamento/pessoa." + str(a) + "." + str(amostra) + ".jpg", region)
        eyeCinza = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
        eyeDetected = eye_cascade.detectMultiScale(eyeCinza)
        for (ox, oy, ow, oh) in eyeDetected:
            cv2.rectangle(region, (ox, oy), (ox + ow, oy + oh), (0, 255, 0), 2)
    cv2.imshow("Face Detection", video)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        imagemFace = cv2.resize(
            imagemCinza[y:y + w, x:x + h], (largura, altura))
        cv2.imwrite("./treinamento/pessoa." + str(a) + "." +
                    str(amostra) + ".jpg", imagemFace)
        print("foto" + str(amostra) + " Capturada com Sucesso")
        amostra += 1
    if (amostra >= numeroAmostras + 1):
        break
    if cv2.getWindowProperty("Face Detection", cv2.WND_PROP_VISIBLE) < 1:
        break
print("Faces capturadas com sucesso")

from training import *

webcam.release()
cv2.destroyAllWindows()