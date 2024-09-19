from PIL import Image, UnidentifiedImageError
import os

def convert_all_png_to_webp(input_folder, output_folder, quality=80):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
            
            try:
                # Open the PNG image
                with Image.open(input_path) as img:
                    # Convert to WebP format
                    img.save(output_path, 'webp', quality=quality)
                    print(f"Converted {input_path} to {output_path}")
            except UnidentifiedImageError:
                print(f"Could not identify image file: {input_path}")
            except Exception as e:
                print(f"Error processing {input_path}: {e}")

# Example usage
input_folder = "/Volumes/data/งาน"  # Replace with your input folder path
output_folder = "/Volumes/data/งาน/export"  # Replace with your desired output folder path

convert_all_png_to_webp(input_folder, output_folder)
