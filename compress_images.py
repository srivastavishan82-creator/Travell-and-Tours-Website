import os
from PIL import Image

def compress_images(directory):
    max_size = 1920
    quality = 80
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(directory, filename)
            filesize = os.path.getsize(filepath) / (1024 * 1024)
            
            # Compress files larger than 1.5MB
            if filesize > 1.5:
                print(f"Compressing {filename} ({filesize:.2f} MB)...")
                try:
                    img = Image.open(filepath)
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
                    img.save(filepath, optimize=True, quality=quality)
                    
                    new_size = os.path.getsize(filepath) / (1024 * 1024)
                    print(f"Done: {filename} is now {new_size:.2f} MB")
                except Exception as e:
                    print(f"Failed to compress {filename}: {e}")

if __name__ == "__main__":
    compress_images(r"c:\Users\Dell\OneDrive\Desktop\ISHAN SRIVASTAV\practice")
    print("All done!")
