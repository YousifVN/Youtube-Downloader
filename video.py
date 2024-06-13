import os
from pytube import YouTube

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\nDownloaded {percentage_of_completion}% of the video")

def download_video(url):
    print(f"\nStarting download of {url}")
    youtube = YouTube(url)
    youtube.register_on_progress_callback(progress_function)

    video = youtube.streams.get_highest_resolution()

    # Save the video to a directory named "downloads"
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    video.download(output_path)
    print(f"\nCompleted download of {url}\n")

# Read the video URL from a text file
with open('url.txt', 'r') as file:
    video_url = file.readline().strip()
    download_video(video_url)

# Clear the text file
with open('url.txt', 'w') as file:
    file.write('')