from PIL import Image
import numpy as np
import os

def images_to_arraysDD(folder_path):
    arraysDD = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Open only files that are 300x300 images in grayscale (black and white)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    # Check if the image is 300x300 and in grayscale mode
                    if img.size == (300, 300) and img.mode == 'L':
                        # Convert image to a numpy array and add it to the list
                        img_array = np.array(img)
                        arraysDD.append(img_array)
                        # print(f"Converted: {filename} to array")
                    else:
                        print(f"Skipped: {filename} (not 300x300 or not grayscale)")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    return arraysDD

# Specify the folder path containing the images
folder_path = "/Users/benjaminyang/Desktop/DDImagesData"
arraysDD = np.array(images_to_arraysDD(folder_path))

# Now `arraysDD` contains a list of numpy arraysDD for each 300x300 black and white image
print(f"Total images converted to arraysDD: {len(arraysDD)}")
