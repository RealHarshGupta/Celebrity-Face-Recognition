
# Celebrity Face Recognition in YouTube Videos

This project uses machine learning to recognize and label celebrities in YouTube videos. The recognized faces are then saved into separate video files named after the detected celebrity.

## Features
- Download videos from YouTube using `yt-dlp`.
- Recognize faces in the downloaded videos using a pre-trained SVM model.
- Save the processed videos into separate folders named after the recognized celebrities.

## Requirements

- Python 3.x
- `yt-dlp`
- `opencv-python`
- `face_recognition`
- `joblib`
- `numpy`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RealHarshGupta/celebrity-face-recognition.git
    cd celebrity-face-recognition
    ```

2. Install the required Python packages:

    ```bash
    pip install yt-dlp opencv-python face_recognition joblib numpy
    ```
    # ffmpeg file to make yt_dlp work
    # dlib file to install face_recognition library is must download
    watch tutorial on youtube how to install them

## Usage

### Downloading YouTube Videos

To download YouTube videos, use the `download_videos.py` script:

```python
import yt_dlp

def download_video(video_url, output_path='C:/Users/Lenovo/Desktop/celebrity_recogniton/downloded_videos'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best',
        'ffmpeg_location': 'C:\\ffmpeg', 
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        print(f"Title: {info['title']}")
        print(f"URL: {info['webpage_url']}")
        print(f"Downloaded to: {output_path}")

# Example usage
video_urls = [
    'https://www.youtube.com/shorts/nGFHDXn7kU8',
    'https://www.youtube.com/shorts/jv8YRJ6-zuU',
    'https://www.youtube.com/shorts/xVLrZlMcG8I',
    'https://www.youtube.com/shorts/gn8VEO_KzBA',
    'https://www.youtube.com/shorts/O9WJX_pApBo',
    'https://www.youtube.com/shorts/gSTNBrTun9k',
    'https://www.youtube.com/shorts/ckTdsqwqX8M',
    'https://www.youtube.com/shorts/iAnr5vj-KkY',
    'https://www.youtube.com/shorts/Q_7a8SI39qM'
]

for url in video_urls:
    download_video(url)

# Notes
Ensure that ffmpeg is installed and its path is correctly set in the yt_dlp options.
Update the paths in the script to match your directory structure.
