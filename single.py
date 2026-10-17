import subprocess
import os

def convert_to_webp(input_image, output_image):
    # Run the cwebp command
    command = ['cwebp', 'free-service-img', '-o', 'test.webp']
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Conversion successful:", result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print("Error during conversion:", e.stderr.decode('utf-8'))

# Example usage:
input_image = 'free-service-img'
output_image = 'output_image.webp'
convert_to_webp(input_image, output_image)
