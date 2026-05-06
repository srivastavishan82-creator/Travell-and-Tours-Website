import os
import subprocess
import imageio_ffmpeg

def compress_videos(directory):
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.mp4', '.mov', '.avi')):
            filepath = os.path.join(directory, filename)
            filesize = os.path.getsize(filepath) / (1024 * 1024)
            
            # Compress videos larger than 2MB
            if filesize > 2:
                print(f"Compressing {filename} ({filesize:.2f} MB)...")
                outpath = os.path.join(directory, "temp_" + filename)
                try:
                    cmd = [
                        ffmpeg_exe, "-y", "-i", filepath,
                        "-vcodec", "libx264", "-crf", "28", "-preset", "veryfast",
                        outpath
                    ]
                    # We print a message because it can take a few seconds
                    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                    
                    new_size = os.path.getsize(outpath) / (1024 * 1024)
                    print(f"Done: {filename} is now {new_size:.2f} MB")
                    
                    # replace old file with new file
                    os.replace(outpath, filepath)
                except Exception as e:
                    print(f"Failed to compress {filename}: {e}")
                    if os.path.exists(outpath):
                        os.remove(outpath)
            else:
                print(f"Skipping {filename} ({filesize:.2f} MB) as it is already small.")

if __name__ == "__main__":
    compress_videos(r"c:\Users\Dell\OneDrive\Desktop\ISHAN SRIVASTAV\practice")
    print("Video compression done!")
