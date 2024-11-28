from PIL import Image
import os

# Path to the folder containing grayscale images
folder_path = "/Users/benjaminyang/Desktop/Images/DD"  # Change this to your folder path

def invert_image(image_file):
    # Open the image
    with Image.open(image_file) as img:
        # Ensure it is in grayscale mode ('L')
        if img.mode != 'L':
            print(f"Skipping {image_file} as it is not in grayscale mode.")
            return
        
        # Invert the image
        inverted_img = Image.eval(img, lambda pixel: 255 - pixel)
        
        # Save the inverted image with a new name
        inverted_image_file = os.path.splitext(image_file)[0] + "_inverted.jpg"
        inverted_img.save(inverted_image_file)
        print(f"Saved inverted image: {inverted_image_file}")

# Process all images in the folder
for file_name in os.listdir(folder_path):
    # Check if file is an image (you can add more extensions if needed)
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        invert_image(os.path.join(folder_path, file_name))
