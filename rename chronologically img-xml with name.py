import os

# Specify the directory containing the images, XML, and JSON files
directory = r'D:\after tagging\fox\remove bounding box'

# Define a function to generate new filenames
def generate_new_filename(index):
    # Create a new filename with the desired pattern
    new_filename = f'BACK{index:03d}'
    return new_filename

# List all files in the directory
files = os.listdir(directory)

# Filter image, XML, and JSON files
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
xml_files = [file for file in files if file.lower().endswith('.xml')]
json_files = [file for file in files if file.lower().endswith('.json')]

# Sort image, XML, and JSON files
image_files.sort()
xml_files.sort()
json_files.sort()

# Rename image and its corresponding XML or JSON file
count = 1
for image_file in image_files:
    base_name = os.path.splitext(image_file)[0]

    # Find the corresponding XML or JSON file
    xml_file = next((file for file in xml_files if file.startswith(base_name)), None)
    json_file = next((file for file in json_files if file.startswith(base_name)), None)

    if xml_file is None and json_file is None:
        print(f"Warning: No corresponding XML or JSON file found for {image_file}. Skipping.")
        continue

    # Generate new filenames for the image and XML or JSON files
    new_image_filename = generate_new_filename(count) + os.path.splitext(image_file)[-1]
    new_annotation_filename = generate_new_filename(count) + ('.xml' if xml_file else '.json')

    # Create the full file paths
    old_image_path = os.path.join(directory, image_file)
    new_image_path = os.path.join(directory, new_image_filename)

    old_annotation_path = os.path.join(directory, xml_file or json_file)
    new_annotation_path = os.path.join(directory, new_annotation_filename)

    # Rename the image and XML or JSON files
    os.rename(old_image_path, new_image_path)
    os.rename(old_annotation_path, new_annotation_path)

    # Increment the count
    count += 1

print(f'{count - 1} pairs of image and XML/JSON files renamed successfully.')