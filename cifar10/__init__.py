import tensorflow as tf
import cv2
import numpy as np

CLASSES =  np.array([
    'airplane', 'automobile', 'bird', 'cat', 'deer',
    'dog', 'frog', 'horse', 'ship', 'truck'
])


class Model:

    def __init__(self):

        self.model = tf.keras.models.load_model('cifar.h5')
        self.classes = CLASSES

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
