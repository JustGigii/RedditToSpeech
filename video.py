import os
import shutil
import moviepy.editor as mp
from moviepy.config import change_settings
import script as sub
import loadgameplay
import reddit

change_settings(
    {"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"}
)

# function to generate new video using moviepy


def generate_new_video(folder_path, backgroundvideo, name):
    # Set up paths to input and output files
    video_path = backgroundvideo["path"]
    audio_path = os.path.join(folder_path, "audio.wav")
    script_path = os.path.join(folder_path, "script.txt")
    output_path = os.path.join(folder_path, name + ".mp4")

    if os.path.exists(output_path):
        return 0
    if os.path.exists(video_path):
        # Check if video file exists
        # Load video and audio files
        video_clip = mp.VideoFileClip(video_path)
        audio_clip = mp.AudioFileClip(audio_path)

        # Get audio duration
        audio_duration = audio_clip.duration
        start_clip, end_clip = (
            backgroundvideo["currentTime"],
            backgroundvideo["currentTime"] + audio_duration,
        )
        if end_clip > video_clip.duration:
            backgroundvideo["isfhnish"] = True
            return -1
        backgroundvideo["currentTime"] = end_clip
        # Trim video clip to audio duration
        new_video_clip = video_clip.subclip(start_clip, end_clip)

        # Add audio and text
        new_video_clip = new_video_clip.set_audio(audio_clip)
        new_video_clip = (
            new_video_clip.subclip(0, audio_duration)
            .set_duration(audio_duration)
            .set_fps(video_clip.fps)
        )
        # Set the target aspect ratio and resolution
        target_width = 1080
        target_height = 1920
        # Resize the video clip
        new_video_clip = new_video_clip.resize((target_width, target_height))

        # Add text
        with open(script_path, "r", encoding="utf8") as f:
            script = f.read()
            subtitle = sub.subtitle(script, audio_path)
            clips = []
            for i in subtitle:
                text, duration = subtitle[i]
                if text != " ":
                    clips.append(
                        mp.TextClip(
                            text,
                            fontsize=55,
                            color="white",
                            font="Tahoma-Bold",
                            stroke_width=3,
                            stroke_color="black",
                            method="caption",
                            kerning=-2,
                            interline=-1,
                            size=(target_width, target_height),
                        )
                        .set_start(i)
                        .set_duration(duration)
                    )
            #
            # text_clip = mp.CompositeVideoClip([mp.TextClip(word_at(t), fontsize=50, color='white', bg_color='black', font='Arial')
            #                                    .resize((target_width, target_height))
            #                                    .set_position((target_width/2, target_height/2)).set_start(t).set_duration(d)
            #                                    for t, d in zip(word_times, word_durations)])
            text_clip = mp.CompositeVideoClip(clips)
            new_video_clip = mp.CompositeVideoClip([new_video_clip, text_clip])

        # Write new video file
        new_video_clip.write_videofile(
            output_path,
            threads=8,
            codec="libx264",
        )

        # Close clips
        video_clip.close()
        audio_clip.close()
    else:
        print(f"Video file {video_path} not found.")
    shutil.copy(output_path, "done")
    return 0


def handelervideo(trying):
    if trying == 0:
        raise "some erro in the code pls cheak the json"
    index = loadgameplay.loadvideo(backgroundvideos)
    if index != -1:
        status = generate_new_video(dir_path, backgroundvideos[index], dir)
        if status == -1:
            handelervideo(trying - 1)
        else:
            return 0
    raise "pls add more video"


# main program
if __name__ == "__main__":
    # for i in range(9):
    #     reddit.loadstories()
    backgroundvideos = loadgameplay.InitJson()
    recordings_dir = "recordings"
    json_data = []
    for subdir, dirs, files in os.walk(recordings_dir):
        for dir in dirs:
            dir_path = os.path.join(subdir, dir)
            handelervideo(3)
    loadgameplay.updatefile(backgroundvideos)
