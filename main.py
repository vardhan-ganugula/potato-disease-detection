import tensorflow as tf 
from tensorflow import keras
import os 


training_path = os.path.join(os.getcwd(), 'datasets', 'Train')
testing_path = os.path.join(os.getcwd(), 'datasets', 'Test')
validation_path = os.path.join(os.getcwd(), 'datasets', 'Valid')

training_set = keras.utils.image_dataset_from_directory( training_path, labels='inferred', label_mode='categorical', color_mode='rgb', batch_size=32, image_size=(128,128), shuffle=True, interpolation='bilinear')
testing_set = keras.utils.image_dataset_from_directory(testing_path, labels='inferred', label_mode = 'categorical', color_mode = 'rgb', batch_size = 32, image_size=(128, 128), shuffle=True, interpolation='bilinear' )
validation_set = keras.utils.image_dataset_from_directory(validation_path, labels='inferred', label_mode = 'categorical', color_mode = 'rgb', batch_size = 32, image_size=(128, 128), shuffle=True, interpolation='bilinear' )



cnn = keras.models.Sequential()
cnn.add(keras.Input(shape=[128, 128, 3]))
cnn.add(keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', padding='same'))
cnn.add(keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(keras.layers.MaxPool2D(pool_size=2, strides=2))


cnn.add(keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu', padding='same'))
cnn.add(keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'))
cnn.add(keras.layers.MaxPool2D(pool_size=2, strides=2))


cnn.add(keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu', padding='same'))
cnn.add(keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu'))
cnn.add(keras.layers.MaxPool2D(pool_size=2, strides=2))

cnn.add(keras.layers.Conv2D(filters=256, kernel_size=3, activation='relu', padding='same'))
cnn.add(keras.layers.Conv2D(filters=256, kernel_size=3, activation='relu'))
cnn.add(keras.layers.MaxPool2D(pool_size=2, strides=2))


cnn.add(keras.layers.Conv2D(filters=512, kernel_size=3, activation='relu', padding='same'))
cnn.add(keras.layers.Conv2D(filters=512, kernel_size=3, activation='relu'))
cnn.add(keras.layers.MaxPool2D(pool_size=2, strides=2))


cnn.add(keras.layers.Dropout(0.25))
cnn.add(keras.layers.Flatten())
cnn.add(keras.layers.Dense(units=1500, activation='relu'))
cnn.add(keras.layers.Dropout(0.4))

cnn.add(keras.layers.Dense(units=3, activation='softmax'))

cnn.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

cnn.summary()

trainig_histrory = cnn.fit(x = training_set, validation_data=validation_set, epochs=10)

cnn.save('leaf_disease_model.keras')