import cv2
import matplotlib.pyplot as plt

# Função para detectar faces em uma imagem
def detectar_faces(imagem_path):
    # Carregar o modelo pré-treinado do OpenCV (Haar Cascade)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    # Carregar a imagem
    imagem = cv2.imread(imagem_path)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)  # Converter para escala de cinza

    # Detectar faces
    faces = face_cascade.detectMultiScale(imagem_cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor das faces
    for (x, y, w, h) in faces:
        cv2.rectangle(imagem, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Exibir a imagem com as faces detectadas
    plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

# Testar a função
detectar_faces("sua_imagem.jpg")  # Substitua pelo caminho da sua imagem
