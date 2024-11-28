import os
import re

# Specify the folder containing the files
folder_path = "/Users/benjaminyang/Desktop/CAImages0"
output_file = "/Users/benjaminyang/Desktop/CA1.txt"

# Initialize a list to store the extracted names
names = []

# Iterate through each file in the folder
for file_name in os.listdir(folder_path):
    # Check if the file matches the format
    if file_name.startswith("tmb_") and file_name.endswith(".jpg"):
        # Extract the [NAME] part
        name = file_name[4:-4]  # Remove "tmb_" and ".jpg"
        
        # Check if the first part is a proper word
        if re.match(r"^[a-zA-Z]+", name):  # Starts with letters
            # Remove trailing numbers, but only if it's a proper word
            name = re.sub(r"\d+$", "", name)  # Remove trailing digits
        
        names.append(name)

# Write the names to a text file, one name per line
with open(output_file, "w") as f:
    for name in sorted(names):  # Optional: sort names alphabetically
        f.write(name + "\n")

print(f"Names have been extracted and saved to {output_file}.")


input_file = "/Users/benjaminyang/Desktop/CA0.txt"  # Replace with your input file name
output_file = "/Users/benjaminyang/Desktop/CA2.txt"

# Function to format a name
def format_name(name):
    # Remove spaces and convert to lowercase
    formatted_name = name.replace(" ", "").lower()
    return f"ship_{formatted_name}"

# Read names from the input file
with open(input_file, "r") as infile:
    names = infile.read().splitlines()

# Convert each name
converted_names = [format_name(name) for name in names]

# Write the converted names to the output file
with open(output_file, "w") as outfile:
    for converted_name in converted_names:
        outfile.write(converted_name + "\n")

print(f"Converted names have been saved to {output_file}.")

# Define input and output files
file1 = "/Users/benjaminyang/Desktop/CA1.txt"  # Replace with your first file name
file2 = "/Users/benjaminyang/Desktop/CA2.txt"  # Replace with your second file name
output_file = "/Users/benjaminyang/Desktop/CA3.txt"

# Read contents of both files
with open(file1, "r") as f1, open(file2, "r") as f2:
    lines1 = f1.read().splitlines()
    lines2 = f2.read().splitlines()

# Combine, remove duplicates, and sort
combined_lines = sorted(set(lines1 + lines2))

# Write the result to the output file
with open(output_file, "w") as outfile:
    for line in combined_lines:
        outfile.write(line + "\n")

print(f"Combined and sorted list has been saved to {output_file}.")
