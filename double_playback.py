from PIL import Image, ImageSequence
import sys


def double_gif_speed(input_path, output_path):
    # Open the original GIF
    original_gif = Image.open(input_path)

    # Extract frames and adjust duration
    frames = []
    durations = []
    for frame in ImageSequence.Iterator(original_gif):
        frames.append(frame.copy())
        # Get the frame duration in milliseconds and halve it
        frame_duration = frame.info.get('duration', 100)  # default 100ms
        durations.append(max(1, frame_duration // 2))  # minimum 1ms to avoid zero

    # Save new GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2
    )
    print(f"Saved doubled-speed GIF as: {output_path}")
    
input_path = "Supplemental_Video_2.gif"
output_path = "Supplemental_Video_2x2.gif"
double_gif_speed(input_path, output_path)
