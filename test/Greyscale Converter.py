import os
from PIL import Image, ImageFile, UnidentifiedImageError

# Allow processing of truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

def fix_and_convert_to_grayscale(folder_path):
    """
    Open and save each image to fix potential corruption, then convert to grayscale.
    Ensures files remain in correct .jpg format and handles corrupted files gracefully.
    """
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            # Process only .jpg or .jpeg files
            if file.lower().endswith(('.jpg', '.jpeg')):
                try:
                    # Open the image
                    with Image.open(file_path) as img:
                        # Fix potential corruption by saving and reopening the file
                        fixed_path = file_path + ".fixed.jpg"
                        img = img.convert("RGB")  # Ensure valid color mode
                        img.save(fixed_path, "JPEG", quality=95)

                        # Reopen the fixed file
                        with Image.open(fixed_path) as fixed_img:
                            # Convert to grayscale
                            grayscale_img = fixed_img.convert("L")
                            # Save the grayscale image back in the original location
                            grayscale_img.save(file_path, "JPEG", quality=95)
                        # Delete the temporary fixed file
                        os.remove(fixed_path)

                        print(f"Processed and converted: {file_path}")

                except UnidentifiedImageError:
                    print(f"Skipped (not a valid image): {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    # Replace 'your_folder_path' with the path to the folder you want to process
    folder_path = input("Enter the folder path: ").strip()
    
    if os.path.isdir(folder_path):
        fix_and_convert_to_grayscale(folder_path)
        print("All eligible images have been processed and converted to grayscale.")
    else:
        print("Invalid folder path.")
