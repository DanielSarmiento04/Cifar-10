import tensorflow as tf
import cv2
import numpy as np

from tensorflow.keras import Model
from tensorflow.keras.layers import (
    Dense, 
    Conv2D, 
    MaxPool2D, 
    Flatten, 
    Dropout,
    BatchNormalization, 
    MaxPooling2D
)

CLASSES =  np.array([
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
])


class Model(Model):

    def __init__(self):
        '''            
        '''
        super(Model, self).__init__()

        self.model = tf.keras.models.load_model('cifar_10.keras')

        self.conv1 = Conv2D(64, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3))
        self.bn1 = BatchNormalization()
        self.conv2 = Conv2D(64, (3, 3), activation='relu', padding='same')
        self.bn2 = BatchNormalization()
        self.pool1 = MaxPooling2D((2, 2))
        self.dropout1 = Dropout(0.25)

        self.conv3 = Conv2D(128, (3, 3), activation='relu', padding='same')
        self.bn3 = BatchNormalization()
        self.conv4 = Conv2D(128, (3, 3), activation='relu', padding='same')
        self.bn4 = BatchNormalization()
        self.pool2 = MaxPooling2D((2, 2))
        self.dropout2 = Dropout(0.25)

        self.conv5 = Conv2D(256, (3, 3), activation='relu', padding='same')
        self.bn5 = BatchNormalization()
        self.conv6 = Conv2D(256, (3, 3), activation='relu', padding='same')
        self.bn6 = BatchNormalization()
        self.pool3 = MaxPooling2D((2, 2))
        self.dropout3 = Dropout(0.25)

        self.flatten = Flatten()
        self.dense1 = Dense(512, activation='relu')
        self.bn7 = BatchNormalization()
        self.dropout4 = Dropout(0.5)
        self.dense2 = Dense(256, activation='relu')
        self.bn8 = BatchNormalization()
        self.dropout5 = Dropout(0.5)
        self.dense3 = Dense(len(self.classes), activation = "softmax")


    @property
    def classes(self):
        return CLASSES
    
    def load_model(self):
        self.model = tf.keras.models.load_model('cifar_10.keras')
        

    def call(self, inputs):
        '''
            Args:
                inputs : tf.Tensor shape (Any, 32, 32, 3)

            Returns:
                tf.Tensor shape (Any, 10)
        '''
        x = self.conv1(inputs)
        x = self.bn1(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.pool1(x)
        x = self.dropout1(x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = self.conv4(x)
        x = self.bn4(x)
        x = self.pool2(x)
        x = self.dropout2(x)

        x = self.conv5(x)
        x = self.bn5(x)
        x = self.conv6(x)
        x = self.bn6(x)
        x = self.pool3(x)
        x = self.dropout3(x)

        x = self.flatten(x)
        x = self.dense1(x)
        x = self.bn7(x)
        x = self.dropout4(x)
        x = self.dense2(x)
        x = self.bn8(x)
        x = self.dropout5(x)
        x = self.dense3(x)
        return x

    def preprocess_image(self, img:np.ndarray):
        '''
            Args:
                img : np.ndarray shape (Any, Any, 3)
        '''
        img_manipulated = img.copy()
        img_manipulated = cv2.resize(img_manipulated, (32, 32))
        img_manipulated = img_manipulated / 255.0
        return np.expand_dims(img_manipulated, axis=0)
        

    def posprocess_prediction(self, pred:np.ndarray):
        '''
            Args:
                pred : np.ndarray shape (1, 10)
        '''
        pred = pred[0]
        pred = np.argmax(pred)
        return self.classes[pred]

    def predict(self, img:np.ndarray):
        '''
            Args:
                img : np.ndarray shape (Any, Any, 3)
        '''
        img_manipulated = self.preprocess_image(img)
        pred = self.model.predict(img_manipulated)
        pred = self.posprocess_prediction(pred)
        return pred
