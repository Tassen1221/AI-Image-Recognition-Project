import os
from PIL import Image

def convert_to_greyscale(input_folder, output_folder):
    """
    Converts all images in the input folder (and its subfolders) to greyscale
    and saves them in the output folder, maintaining the folder structure.

    Args:
        input_folder (str): Path to the input folder containing images.
        output_folder (str): Path to the output folder for greyscale images.
    """
    for root, _, files in os.walk(input_folder):
        # Preserve the directory structure in the output folder
        relative_path = os.path.relpath(root, input_folder)
        target_folder = os.path.join(output_folder, relative_path)
        os.makedirs(target_folder, exist_ok=True)

        for file in files:
            # Process only image files
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(target_folder, file)

                try:
                    # Open the image, convert to greyscale, and save
                    with Image.open(input_path) as img:
                        greyscale_img = img.convert('L')
                        greyscale_img.save(output_path)
                    print(f"Converted: {input_path} -> {output_path}")
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")


# Example usage:
input_folder = "/Users/benjaminyang/Desktop/Images/DD"
output_folder = "/Users/benjaminyang/Desktop/Images/DD"

convert_to_greyscale(input_folder, output_folder)
