from PIL import Image
import os

def resize_images(folder_path, size=(100, 100)):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif')
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Process only supported image formats
        if os.path.isfile(file_path) and file_path.lower().endswith(supported_formats):
            try:
                with Image.open(file_path) as img:
                    # Convert to grayscale (L mode) if not already
                    if img.mode != 'L':
                        img = img.convert('L')
                    
                    # Resize the image to 100x100 without preserving aspect ratio
                    resized_img = img.resize(size)
                    # Save the resized image, overwriting the original
                    resized_img.save(file_path)
                    print(f"Resized: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Specify the folder path containing the images
folder_path = "/Users/benjaminyang/Desktop/AI-Image-Recognition-Project/BB"
resize_images(folder_path)
