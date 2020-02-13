# Random Pixel Drop
This is a library written for `ImageDataGenerator()` from `keras.preprocessing` library.

Random pixel drop is inspired from dropout regularisation technique and cutout image augmentation technique. This library will randomly set image pixel values of the image to zeros for a given range of number. Which will be similar to dropout than switching neurons randomly to reduce over fitting this will introduce randomness in the input image to reduce over fitting 
# Implementation
```
git clone https://github.com/chekoduadarsh/Random-Pixel-Drop
```
The above given command will download the repository to your working directory, then in your python code tou can import the library as following,

## With ImageDataGenerator in Keras

It is very easy to use if you are using ImageDataGenerator in Keras, get `drop` function from `get_random_pixel_drop()` which can be passed to `ImageDataGenerator` as `preprocessing_function`. This function uses 3 hyper parameters

`Drop_num` -> Number of dropped pixels

`l_rand_bound` -> lower boundry for random pixel value generation

`u_rand_bound` -> upper boundry for random pixel value generation
