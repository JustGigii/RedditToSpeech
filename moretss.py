import os
import shutil


def move(recordings_dir):
    for subdir, dirs, files in os.walk(recordings_dir):
        for file in files:
            dir_path = os.path.join(subdir, file)
            if ".mp4" in file:
                shutil.copy(dir_path, "done")


move("recordings")

# https://github.com/MiniGlome/Tiktok-uploader next step
