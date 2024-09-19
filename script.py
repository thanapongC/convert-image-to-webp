from PIL import Image, UnidentifiedImageError
import os

def convert_all_images_to_webp(input_folder, quality=80):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(input_folder):
        # Check if any .png or .jpeg/.jpg files exist in the current folder
        image_files = [f for f in files if f.lower().endswith((".png", ".jpg", ".jpeg"))]
        
        if image_files:
            # Create an export folder in the current folder
            output_folder = os.path.join(root, "export")
            os.makedirs(output_folder, exist_ok=True)
            
            # Loop through all image files and convert them to .webp
            for filename in image_files:
                input_path = os.path.join(root, filename)
                output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.webp")
                
                try:
                    # Open the image (PNG, JPEG/JPG)
                    with Image.open(input_path) as img:
                        # Convert to WebP format
                        img.save(output_path, 'webp', quality=quality)
                        print(f"Converted {input_path} to {output_path}")
                except UnidentifiedImageError:
                    print(f"Could not identify image file: {input_path}")
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")


# Example usage
input_folder = "/Volumes/data/skinsolution"  # Replace with your input folder path
convert_all_images_to_webp(input_folder)
