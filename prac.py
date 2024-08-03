import yt_dlp


def download_video(video_url, output_path='C:/Users/Lenovo/Desktop/celebrity_recogniton/downloded_videos'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best',
        'ffmpeg_location': 'C:/ffmpeg', 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video_url, download=True)
            print(f"Title: {info['title']}")
            #print(f"URL: {info['webpage_url']}")
            #print(f"Downloaded to: {output_path}")
        except yt_dlp.utils.DownloadError as e:
            #print(e)
            #print("Error downloading video. Trying to list available formats.")
            ydl_opts['format'] = None  # List all formats
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_list:
                info = ydl_list.extract_info(video_url, download=True)
                formats = info.get('formats', [info])
                for f in formats:{}
                    #print(f"Format code: {f['format_id']}, Extension: {f['ext']}, Note: {f.get('format_note', 'No note')}, Resolution: {f.get('resolution', 'Unknown')}")
            #print("Please choose a valid format and update the 'format' in 'ydl_opts'.")

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
