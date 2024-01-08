# Cifar 10 Neural Network

## Overview

This repository contains all the necessary code, documentation, and resources to help you understand, implement, and train the neural network model effectively.

## Table of Contents
- [Introduction](#introduction)
- [Training](#training)
- [Results](#results)
- [Test yourself](#test-yourself)
- [Reference](#reference)
- [license](#license)


## Introduction

The CIFAR-10 dataset is a well-known benchmark in the field of computer vision, consisting of 60,000 32x32 color images in 10 different classes, with 6,000 images per class. In this repository, we present a state-of-the-art neural network architecture designed to achieve high accuracy on this challenging dataset. Our architecture leverages the power of deep learning to achieve outstanding results, and we provide all the necessary tools for you to understand, implement, and extend this model.

## Training

[Google Colab](https://colab.research.google.com/drive/13RTWHPjCDT1bu5PZu7Zen5Jww5Mb7PVa?usp=sharing)

## Results


<p align="center">
  <img src="docs/graph.svg" height ="300px">
</p>

<p align="center">
  <img src="docs/model_sgd.png" height ="300px">
</p>

> Note: The pre trainer model (use separate) tested are the follow
> - NASNetMobile
> - MobileNetV2
> - MobileNetV3Large
> - VGG19
> - VGG16 
> - DenseNet201
> - ResNet101
> The results show an improvement in precision and loss on **VGG19**, **VGG16** , **DenseNet201**, **MobileNetV2**

## Test yourself

```
    python test.py --model cifar10.h5 --image ./docs/test.jpg
```

```
docker run -d --name cifar_10 -p8000:80 danielsarmiento04/cifar10:4
```
## Reference
1. [Datasets]() - [Learning Multiple Layers of Features from Tiny Images,](https://www.cs.toronto.edu/~kriz/learning-features-2009-TR.pdf) Alex Krizhevsky, 2009
2. [Layers Available](https://www.tensorflow.org/api_docs/python/tf/keras/layers)
3. [Fundamental Theory](https://books.google.com.co/books?id=RaRbNBqGR1oC&lpg=PA1&ots=2kkwXs9tJ4&dq=build%20a%20neural%20network&lr&hl=es&pg=PA1#v=onepage&q=build%20a%20neural%20network&f=false)
4. [Course Guide](https://platzi.com/cursos/redes-neuronales-tensorflow/)


## License

This repository is licensed under the [Apache 2.0](LICENSE) License. 

## Reference 

A. Bäuerle, C. van Onzenoodt and T. Ropinski, "Net2Vis – A Visual Grammar for Automatically Generating Publication-Tailored CNN Architecture Visualizations," in IEEE Transactions on Visualization and Computer Graphics, vol. 27, no. 6, pp. 2980-2991, 1 June 2021, doi: 10.1109/TVCG.2021.3057483.