import tensorflow as tf
import cv2
from matplotlib import pyplot as plt
import numpy as np
from cifar10 import Model
import argparse
from colorama import Fore


parser = argparse.ArgumentParser()
parser.add_argument('--model', type=str, default='./cifar.h5')
parser.add_argument('--image', type=str, default='./docs/test.jpg')


args = parser.parse_args()

print(args)

model = Model()

img = cv2.imread(args.image)

results = model.predict(img)
print(
    f"""
        {Fore.GREEN}Results:{Fore.RESET} {results} {Fore.RESET}
    """
)


plt.imshow(img)
plt.title(f'Prediction: {results}')
plt.axis(False)
plt.show()