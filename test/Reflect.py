import os
from PIL import Image

# Set the folder containing the images
folder_path = "/Users/benjaminyang/Desktop/BBImagesData"  # Change this to your folder path

# Get a list of all files in the folder
file_names = os.listdir(folder_path)

# Filter only the image files (assuming .png and .jpg files for this example)
image_files = [f for f in file_names if f.endswith(('.png', '.jpg'))]

# Iterate over each image file
for image_file in image_files:
    # Construct the full file path
    file_path = os.path.join(folder_path, image_file)
    
    # Open the image
    with Image.open(file_path) as img:
        # Check if the image is black and white (mode '1' or 'L')
        if img.mode not in ['1', 'L']:
            print(f"Skipping {image_file} as it is not black and white.")
            continue
        
        # Reflect the image horizontally (flip left to right)
        reflected_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        # Save the reflected image with a new name
        new_file_name = f"reflected_{image_file}"
        reflected_img.save(os.path.join(folder_path, new_file_name))

        print(f"Saved reflected image: {new_file_name}")
