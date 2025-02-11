# deep Learning

Why Deep Learning?
ML algorithms by nature stop improving after certain point even when provided with more data over time. They tend to plateau on performance / accuracy. Whereas in the same scenario if a deep learning neural network is provided more data, over time it learns more dimensions and hence starts giving us better accuracy.


What is Deep Learning?
DL is a subset of ML algorithms. In ML algorithms, everything is flattened in a single dimension array; whereas in DL we use something called tensors. Tensors are small matrices inside a bigger matrix. Simplest DL algorithm is basically a perceptron. Perceptron allows us to build a binary classification. It accepts multiple inputs in the form of a matrix and then based on the probability distribution value we can know which class they belong to.
The inputs to the perceptron are matrices, say x1, x2, x3, x4 of same size and each matrix is assigned a weight. This weight represents what share of this value is contributing to the output. A perceptron is an algorithm used for supervised learning of binary classifiers. Binary classifiers decide whether an input usually represented by a series of vectors, belongs to a specific class; it is a single layer neural network.
When we combine multiple perceptrons, we get Dense layer. It becomes a feed forward artificial neural network.
A single layer perceptron is a logistic regression function dealing with single dimension.
With MLP (multiple layer perceptron) have multiple dense layer. With each layer, we can extract multiple features based on the inputs enhancing the accuracy as we go through more layers.

In this project, I am using CNN - convolutional neural network which is a deep learning model used widely for image processing and pattern recognition. It, by virtue,detects features like shape, edges, textures, etc from an image using convolutional layers.

Convolution filter(kernel) is a small matrix (e.g. 3x5,5x5 ) used to extract features from input image. It slides over the image and performs element-wise multiplication followed by summation, highlighting important patterns like edges, corners, textures. An edge detection filter/matrix will look like:
[ -1 -1 -1 ]
[ -1  8 -1 ]
[ -1 -1 -1 ]
Applying this to image detects sharp transitions in pixel intensity.

A **Pooling Layer** is used to reduce the spatial size of feature maps while retaining essential information.
**Max Pooling** selects the max value
**Average Pooling** computes the average of all values in the window

**Max Pooling** is a down sampling operation that reduces the size of the feature map while keeping important information. It slides a small window (2x2) over the feature map and selects the max value in that window.

Feature Map:  After 2x2 max pooling: 
[ 1 3 2 1]  -> [ 4 6 ]
[ 4 2 0 6]     [ 9 8 ]
[ 5 1 7 4]
[ 2 9 8 3]
This reduces computation and prevents overfitting while preserving important details.

**Padding** is the addition of extra pixels around an image before applying a convolution operation. It helps control the output size and preserves imp edge information.


**Transfer Learning**
Transfer learning is a technique in deep learning where a pre trained model is used as a starting point for a new task. Instead of training a neural network from scratch, we take an existing model and fine-tune it for a specific task, saving time and resources. Common transfer learning models are ** VGG, ResNet, MobileNet, Inception **

The CNN architecture comprises of:
1. Convolution Layer -> extracts features using filters/kernels
2. Activation function (ReLU) -> Introduces non-linearity
3. Pooling Layer -> Downsamples feature maps to reduce dimensions
4. Fully Connected Layer -> Makes final predictions
