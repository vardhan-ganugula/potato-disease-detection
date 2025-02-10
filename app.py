import tensorflow as tf 
from flask import Flask, request, jsonify, render_template
import numpy as np
from PIL import Image
import io

app = Flask(__name__)

def predict_model(test_image):
    model = tf.keras.models.load_model('leaf_disease_model.keras')
    input_arr = tf.keras.preprocessing.image.img_to_array(test_image.resize((128, 128)))
    input_arr = np.array([input_arr])
    predictions = model.predict(input_arr)
    return int(np.argmax(predictions))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'no file found'})
    test_image = request.files['image']
    img = Image.open(test_image)
    prediction = predict_model(img)
    result = ['early_blight','late_blight', 'healthy' ]
    return jsonify({'prediction': result[prediction]})


if __name__ == '__main__':
    app.run(debug=True)