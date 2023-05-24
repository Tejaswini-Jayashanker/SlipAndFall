import cv2
import os
import sys

def video_to_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Initialize frame count
    frame_count = 0

    # Read the first frame
    success, frame = video.read()

    while success:
        # Save the frame as an image file
        frame_path = os.path.join(output_folder, f"frame_{frame_count:06d}.jpg")
        cv2.imwrite(frame_path, frame)

        # Read the next frame
        success, frame = video.read()

        # Increment frame count
        frame_count += 1

    # Release the video object
    video.release()

    print("Frames saved successfully.")

if __name__ == "__main__":
    # Check if the required arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python video_to_frames.py <video_path> <output_folder>")
        sys.exit(1)

    # Get the video path and output folder path from command-line arguments
    video_path = sys.argv[1]
    output_folder = sys.argv[2]

    # Call the function to convert video to frames
    video_to_frames(video_path, output_folder)
