from PIL import Image
import numpy as np
import os

def images_to_arraysCA(folder_path):
    arraysCA = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Open only files that are 100x100 images in grayscale (black and white)
        if os.path.isfile(file_path):
            try:
                with Image.open(file_path) as img:
                    # Check if the image is 100x100 and in grayscale mode
                    if img.size == (100, 100) and img.mode == 'L':
                        # Convert image to a numpy array and add it to the list
                        img_array = np.array(img)
                        arraysCA.append(img_array)
                        # print(f"Converted: {filename} to array")
                    else:
                        print(f"Skipped: {filename} (not 100x100 or not grayscale)")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    return arraysCA

# Specify the folder path containing the images
folder_path = "/Users/benjaminyang/Desktop/AI-Image-Recognition-Project/CA"
arraysCA = np.array(images_to_arraysCA(folder_path))

# Now `arraysCA` contains a list of numpy arraysCA for each 100x100 black and white image
print(f"Total images converted to arraysCA: {len(arraysCA)}")
