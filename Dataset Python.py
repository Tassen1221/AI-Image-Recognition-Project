import os
import requests

# Define the input text file, base URL, and output folder
input_file = '/Users/benjaminyang/desktop/CA3.txt'  # Text file containing lines to check
base_url = "https://ww2db.com/images/"
output_folder = '/Users/benjaminyang/desktop/CAImages'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to check if a URL exists
def url_exists(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

# Open the input file and process each line
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()  # Remove leading/trailing whitespace
        if not line:  # Skip empty lines
            continue
        
        # Construct the URL
        url = f"{base_url}{line}.jpg"
        print(f"Checking URL: {url}")
        
        # Check if the URL exists
        if url_exists(url):
            print(f"URL exists: {url}. Downloading...")
            try:
                # Download the image
                response = requests.get(url)
                response.raise_for_status()  # Raise exception for HTTP errors
                
                # Save the image to the output folder
                output_path = os.path.join(output_folder, f"{line}.jpg")
                with open(output_path, "wb") as img_file:
                    img_file.write(response.content)
                print(f"Downloaded: {output_path}")
            except requests.RequestException as e:
                print(f"Failed to download {url}: {e}")
        else:
            print(f"URL does not exist: {url}")

print("Processing complete.")

# Define the folder to save the images
save_folder = '/Users/benjaminyang/desktop/CAImages'
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

# Function to download the image
def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {url}")
            return True  # Return True if download succeeds
        else:
            print(f"Failed to download (status code {response.status_code}): {url}")
            return False  # Return False if download fails
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False  # Return False if there is an exception

# Read the lines from the text file
with open('/Users/benjaminyang/desktop/CA4.txt', 'r') as file:
    lines = file.readlines()

# Iterate over each line in the text file
for line in lines:
    line = line.strip()
    failure_count = 0  # Reset failure counter for each line
    for i in range(1, 201):  # Try appending numbers 1 to 200
        url = f"https://ww2db.com/images/{line}{i}.jpg"
        filename = os.path.join(save_folder, f"{line}{i}.jpg")
        
        if download_image(url, filename):
            failure_count = 0  # Reset failure count if download succeeds
        else:
            failure_count += 1
        
        # If 10 consecutive failures, skip this line and stop trying for this line
        if failure_count >= 10:
            print(f"10 consecutive failures for {line}, skipping this line.")
            break
