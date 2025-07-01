def sistema_deteccao_reconhecimento(imagem_path):
    # Detecção de faces
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    imagem = cv2.imread(imagem_path)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Reconhecimento de faces
    embeddings_list = []
    for (x, y, w, h) in faces:
        face = imagem[y:y+h, x:x+w]
        face = cv2.resize(face, (160, 160))  # Redimensionar para FaceNet
        face = np.expand_dims(face, axis=0) / 255.0  # Normalizar
        embeddings = model.predict(face)
        embeddings_list.append(embeddings)

        # Desenhar retângulos ao redor da face detectada
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Exibir a imagem com as faces detectadas
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

    print("Características extraídas das faces:", embeddings_list)

# Testar o sistema
sistema_deteccao_reconhecimento("sua_imagem.jpg")
