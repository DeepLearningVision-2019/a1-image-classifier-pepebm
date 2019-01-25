import cv2 # computer vision library
import helpers
import pry
import numpy as np
import matplotlib.pyplot as plt

# Find the average Value or brightness of an image
def avg_brightness(rgb_image):
    ## TODO: Get the average brightness from an image using the HSV color space.
    
    # Convert image to HSV

    # Add up all the pixel values in the V channel
        
    # find the avg
    avg = None
    
    return avg
  
# This function should take in RGB image input
def estimate_label(rgb_image):
    ## TODO: Use the avg brightness feature to predict a label (0, 1)
    # Extract average brightness feature from an RGB image 
    avg = avg_brightness(rgb_image)
        
    predicted_label = 0
    # Define a threshold value
    threshold = 0
    
    # if the average brightness is above the threshold value, we classify it as "day"
    # else, the predcted_label can stay 0 (it is predicted to be "night")
    
    return predicted_label


# Image data directories
image_dir_training = "day_night_images/training/"
image_dir_test = "day_night_images/test/"

# Using the load_dataset function in helpers.py
# Load training data
# This implements cv2.imread
IMAGE_LIST = helpers.load_dataset(image_dir_training)

# Select an image and its label by list index
image_index = 6
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]

## TODO: Create a subplot of a day image and a night image. The titles should consist of the shape and label
# of the image
image = cv2.cvtColor(selected_image, cv2.COLOR_BGR2RGB)
plt.imshow(image)

# Standardize all training images

## TODO: Code the needed functions in the helpers file in order to return a standardized list.
STANDARDIZED_LIST = helpers.standardize(IMAGE_LIST)

# Display a standardized image and its label

# Select an image by index
image_num = 0
selected_image = STANDARDIZED_LIST[image_num][0]
selected_label = STANDARDIZED_LIST[image_num][1]

# Display image and data about it
plt.imshow(selected_image)
print("Shape: "+str(selected_image.shape))
print("Label [1 = day, 0 = night]: " + str(selected_label))

# Testing average brightness levels
# Look at a number of different day and night images and think about 
# what average brightness value separates the two types of images

# As an example, a "night" image is loaded in and its avg brightness is displayed
image_num = 190
test_im = STANDARDIZED_LIST[image_num][0]

avg = avg_brightness(test_im)
print('Avg brightness: ' + str(avg))
plt.imshow(test_im)