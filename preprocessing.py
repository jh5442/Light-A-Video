import cv2


def process_video(original_video_path, save_video_path):
    cap = cv2.VideoCapture(original_video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {original_video_path}")
        return

    # Output properties
    out_fps = 8
    frame_size = (512, 512)

    # Define the video writer (MP4 with H.264 encoding)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # You can use 'XVID' or others
    out = cv2.VideoWriter(save_video_path, fourcc, out_fps, frame_size)

    frame_count = 0
    while frame_count < 16:
        ret, frame = cap.read()
        if not ret:
            break  # Stop if the video ends before 16 frames

        # Resize to 512x512
        resized_frame = cv2.resize(frame, frame_size)

        # Write to output video
        out.write(resized_frame)

        frame_count += 1

    cap.release()
    out.release()
    print(f"Processed video saved to: {save_video_path}")


if __name__ == "__main__":
    process_video(original_video_path="/home/ubuntu/jin/data/test_03_and_04/test_03.mp4",
                  save_video_path="input_animatediff/test_03_processed.mp4")

    process_video(original_video_path="/home/ubuntu/jin/data/test_03_and_04/test_04.mp4",
                  save_video_path="input_animatediff/test_04_processed.mp4")
