import keras
from PIL import Image
import numpy as np
import os

"""
Model Architecture

model = keras.Sequential([,
    keras.layers.Conv2D(64, (3,3), padding='same', activation="relu", input_shape=(180, 180, 3)),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, (3,3), padding='same', activation="softmax"),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(16, (3,3), padding='same', activation="softmax"),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.2),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation="sigmoid"),
    keras.layers.Dense(1, activation="sigmoid")
])
"""
class Model:

    def __init__(self):
        father_folder = os.path.dirname(os.path.abspath(__file__))
        self.model = keras.models.load_model(os.path.join(father_folder, "model.keras"))

    def predict(self, img) -> bool:
        processed_img = img.resize((180, 180))
        processed_img = keras.preprocessing.image.img_to_array(processed_img)
        processed_img = np.expand_dims(processed_img, axis=0)
        prediction = self.model.predict(processed_img)
        print(prediction)
        return prediction[0][0] < 0.5


if __name__ == "__main__":
    model = Model()
    print(model.predict(Image.open("TestImages/fire109.png")))
