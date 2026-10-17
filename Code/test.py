import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("crack_model.keras")

# Load image
img_path = "test.jpg"
img = image.load_img(img_path, target_size=(224,224))
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Prediction
prediction = model.predict(img_array)
if prediction[0][0] > 0.5:
    print("Crack Detected")
else:
    print("No Crack Detected")
print("Confidence:", prediction[0][0])
