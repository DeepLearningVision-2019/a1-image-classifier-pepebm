import cv2 # computer vision library
import helpers

import numpy as np
import matplotlib.pyplot as plt

import random

# Constructs a list of misclassified images given a list of test images and their labels
def get_misclassified_images(test_images):
    # Track misclassified images by placing them into a list
    misclassified_images_labels = []

    # Iterate through all the test images
    # Classify each image and compare to the true label
    for image in test_images:

        # Get true data
        im = image[0]
        true_label = image[1]

        ## TODO:
        # Get predicted label from your classifier
        predicted_label = none

        # Compare true and predicted labels 
        # If these labels are not equal, the image has been misclassified. Append a tuple of
        # image, prediction, and true label to the misclassified list.
            
    # Return the list of misclassified [image, predicted_label, true_label] values
    return misclassified_images_labels

# Using the load_dataset function in helpers.py
# Load test data
TEST_IMAGE_LIST = helpers.load_dataset(image_dir_test)

# Standardize the test data
STANDARDIZED_TEST_LIST = helpers.standardize(TEST_IMAGE_LIST)

# Shuffle the standardized test data
random.shuffle(STANDARDIZED_TEST_LIST)

# Find all misclassified images in a given test set
MISCLASSIFIED = get_misclassified_images(STANDARDIZED_TEST_LIST)

## TODO: Calculate the accuracy of the classifier. Accuracy = number of correct / total number of images
# Accuracy calculations
accuracy = 0

print('Accuracy: ' + str(accuracy))
print("Number of misclassified images = " + str(len(MISCLASSIFIED)) +' out of '+ str(total))

# Visualize misclassified example(s)
## TODO: Display an image in the `MISCLASSIFIED` list 
## TODO: Print out its predicted label - to see what the image *was* incorrectly classified as5