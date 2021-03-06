# Assignment 001: Image Processing

import numpy as np
from skimage import *

# Task 1: Image Smoothing - Define a function to perform 
# mean/average filtering for blurring the given image from scratch

# Define the function here
def MeanFilter(image, kernel):
    '''
    Perform average filtering for blurring the given image
    :param image: Input image(greyscale or coloured)
    :param kernel: Box filter
    :return: image_pad, image_filtered
    '''
    # your code here..

    # Your function must return the padded image
    # Hints:
    # Step 1: Define the kernel(box filter)
    # Step 2: Pad the image according to the kernel conditioned for both grayscale and coloured images and
    # store as 'Image_pad'
    # Step 3: Convolve the image with the kernel and store resulting image as 'image_filtered'

    return image_pad, image_filtered


# Task 2: Image Smoothing - Define a function to perform 
# gaussian filtering for blurring the given image from scratch

# Define the function here
def GaussianFilter(image, kernel):
    '''
    Perform gaussian filtering for blurring the given image
    :param image: Input image(greyscale or coloured)
    :param kernel: Box filter
    :return: gaussian_image_pad, gaussian_image_filtered
    '''
    # your code here..

    # Your function must return the padded image
    # Hints:
    # Step 1: Define the kernel(box filter)
    # Step 2: Pad the image according to the kernel conditioned for both grayscale and coloured images and
    # store as 'gaussian_image_pad'
    # Step 3: Convolve the image with the kernel and store resulting image as 'gaussian_image_filtered'

    return gaussian_image_pad, gaussian_image_filtered


# Task 3: Image Thresholding - Define a function to 
# perform thresholding on given image from scratch

input_image = io.imread('edge.jpg')

def thresholding(input_image, threshold):
    '''
    Perform thresholding on given image
    :param input_image: Input image(greyscale or coloured)
    :param threshold:
    :return: mask, threshold_image
    '''
    # your code here...
    # Hints
    # Step 1. Applying average filter for smoothing image

    kernel = (1 / 9) * np.ones((3, 3))
    input_image = color.rgb2gray(input_image)
    image_pad, image_filtered = MeanFilter(input_image, kernel)

    # Step 2. Creating a binary image 'mask' for selecting shapes
    # Turn on pixels greater than threshold and store result as 'mask'
    mask = image_filtered < threshold

    # Step 3. Apply the mask to the original colored image and store as threshold_image'

    return mask, threshold_image
