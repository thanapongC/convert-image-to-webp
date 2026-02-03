import os
import shutil
from PIL import Image

# ================== CONFIG ==================
SOURCE_DIR = "C:/Users/ThanapongChun/Desktop/Work/wordpress/uploads"
DEST_DIR = "C:/Users/ThanapongChun/Desktop/Work/wordpress/new_upload"

SKIP_SIZE_KB = 100        # ไฟล์เล็กกว่านี้จะไม่ resize (copy อย่างเดียว)
RESIZE_PERCENT = 50       # ลดขนาดลงเหลือ %
JPEG_QUALITY = 85         # คุณภาพ JPEG
# ============================================

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")


def process_images():
    for root, _, files in os.walk(SOURCE_DIR):
        for file in files:
            if not file.lower().endswith(SUPPORTED_EXTENSIONS):
                continue

            src_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, SOURCE_DIR)
            dest_folder = os.path.join(DEST_DIR, relative_path)
            os.makedirs(dest_folder, exist_ok=True)

            dest_path = os.path.join(dest_folder, file)
            file_size_kb = os.path.getsize(src_path) / 1024

            # ---------- CASE 1: copy ----------
            if file_size_kb < SKIP_SIZE_KB:
                shutil.copy2(src_path, dest_path)
                print(f"📄 Copied (small): {dest_path}")
                continue

            # ---------- CASE 2: resize ----------
            try:
                with Image.open(src_path) as img:
                    width, height = img.size
                    new_width = int(width * RESIZE_PERCENT / 100)
                    new_height = int(height * RESIZE_PERCENT / 100)

                    resized_img = img.resize(
                        (new_width, new_height),
                        Image.LANCZOS
                    )

                    save_kwargs = {}
                    if img.format == "JPEG":
                        save_kwargs["quality"] = JPEG_QUALITY
                        save_kwargs["optimize"] = True

                    resized_img.save(dest_path, **save_kwargs)
                    print(f"🖼 Resized: {dest_path}")

            except Exception as e:
                print(f"❌ Error: {src_path} ({e})")


if __name__ == "__main__":
    process_images()