import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model

# Carregar o modelo FaceNet pré-treinado
model = load_model("facenet_keras.h5")  # Certifique-se de que o modelo está no diretório correto

# Função para processar a imagem e extrair características
def processar_face(imagem_path):
    # Carregar e redimensionar a imagem
    imagem = tf.keras.preprocessing.image.load_img(imagem_path, target_size=(160, 160))
    imagem_array = tf.keras.preprocessing.image.img_to_array(imagem)
    imagem_array = np.expand_dims(imagem_array, axis=0)
    imagem_array /= 255.0  # Normalizar

    # Extrair características da face
    embeddings = model.predict(imagem_array)
    return embeddings

# Testar a função
embeddings = processar_face("sua_imagem.jpg")
print("Características da face:", embeddings)
