import os
import moviepy.editor as mp
from moviepy.config import change_settings
import script as sub
change_settings(
    {"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"})

# function to generate new video using moviepy


def generate_new_video(folder_path):
    # Set up paths to input and output files
    video_path = os.path.join("fullvideo.mp4")
    audio_path = os.path.join(folder_path, "audio.mp3")
    script_path = os.path.join(folder_path, "script.txt")
    output_path = os.path.join(folder_path, "new_video.mp4")

    # Check if video file exists
    if os.path.exists(video_path):
        # Load video and audio files
        video_clip = mp.VideoFileClip(video_path)
        audio_clip = mp.AudioFileClip(audio_path)

# Get audio duration
        audio_duration = audio_clip.duration

        # Trim video clip to audio duration
        new_video_clip = video_clip.subclip(0, audio_duration)

        # Add audio and text
        new_video_clip = new_video_clip.set_audio(audio_clip)
        new_video_clip = new_video_clip.subclip(0, audio_duration).\
            set_duration(audio_duration).\
            set_fps(video_clip.fps)
        # Set the target aspect ratio and resolution
        target_width = 1080
        target_height = 1920
        # Resize the video clip
        new_video_clip = new_video_clip.resize((target_width, target_height))

        # Add text
        with open(script_path, "r") as f:
            script = f.read()
            subtitle = sub.subtitle(script)
            clips = []
            for i in subtitle:
                text, duration = subtitle[i]
                if (text != " "):
                    clips.append(mp.TextClip(
                        text, fontsize=55, color='yellow', font='Tahoma', stroke_width=30, kerning=-2, interline=-1, size=(target_width, target_height), method='caption').set_start(i).set_duration(duration))

            # text_clip = mp.CompositeVideoClip([mp.TextClip(word_at(t), fontsize=50, color='white', bg_color='black', font='Arial')
            #                                    .resize((target_width, target_height))
            #                                    .set_position((target_width/2, target_height/2)).set_start(t).set_duration(d)
            #                                    for t, d in zip(word_times, word_durations)])
            text_clip = mp.CompositeVideoClip(clips)
            new_video_clip = mp.CompositeVideoClip([new_video_clip, text_clip])

        # Write new video file
        new_video_clip.write_videofile(
            output_path, threads=8, fps=24, preset='ultrafast')

        # Close clips
        video_clip.close()
        audio_clip.close()
    else:
        print(f"Video file {video_path} not found.")


# main program
if __name__ == '__main__':
    recordings_dir = 'recordings'
    for subdir, dirs, files in os.walk(recordings_dir):
        for dir in dirs:
            dir_path = os.path.join(subdir, dir)
            generate_new_video(dir_path)
