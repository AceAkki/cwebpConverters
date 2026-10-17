import os
import subprocess

def convert_images_in_folder(input_folder, output_folder):
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        input_image_path = os.path.join(input_folder, filename)
        
        # Only convert image files (jpg, png, etc.)
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            # Create the output image path
            output_image_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')
            
            # Run the cwebp command for each file
            command = ['cwebp', input_image_path, '-o', output_image_path]
            try:
                result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print(f"Converted {filename} to {output_image_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error converting {filename}: {e.stderr.decode('utf-8')}")

# Example usage
input_folder = r'D:\input'  # Change to your input folder path
output_folder = r'D:\output'  # Change to your output folder path
convert_images_in_folder(input_folder, output_folder)
