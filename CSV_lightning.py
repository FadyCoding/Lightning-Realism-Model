import os
import csv

def write_to_csv(writer, directory, class_label, file_extension, folder_name):
    num_files = 0
    for filename in os.listdir(directory):
        if filename.lower().endswith(file_extension):
            writer.writerow([filename, class_label, folder_name])
            num_files += 1
    print(f"Processed {num_files} images from {directory}")

# CSV file creation with UTF-8 encoding
with open('image_classification.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Image Name', 'Class', 'Folder Name'])

    # Class 0 images from RefLightning directory (JPEG)
    ref_lightning_dir = 'C:\\Users\\Fady\\Desktop\\IA_Project\\RefLightning'
    write_to_csv(writer, ref_lightning_dir, 0, (".jpeg", ".jpg"), "RefLightning")

    # Paths for RenderedLightning subdirectories (only names)
    rendered_lightning_subdirs = [
        '412-1.251', '494-3.241', '507-1.991', '687-1.371', 
        '710-1.691', '876-0.991', '1055-1.021', '1133-3.701'
    ]
    rendered_lightning_base_path = 'C:\\Users\\Fady\\Desktop\\IA_Project\\RenderedLightning'

    # Class 1 images from RenderedLightning subdirectories (PNG)
    for subdir_name in rendered_lightning_subdirs:
        subdir_path = os.path.join(rendered_lightning_base_path, subdir_name)
        if os.path.exists(subdir_path) and os.path.isdir(subdir_path):
            write_to_csv(writer, subdir_path, 1, (".png",), subdir_name)
        else:
            print(f"Directory not found or is not a directory: {subdir_path}")
