import os
from pytube import YouTube, Playlist
from urllib.parse import urlparse, parse_qs

def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\nDownloaded {percentage_of_completion}% of the video")

def download_video(url, output_path):
    youtube = YouTube(url)
    youtube.register_on_progress_callback(progress_function)

    video = youtube.streams.get_highest_resolution()
    video.download(output_path)

def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)

    # Extract the playlist name from the URL
    parsed_url = urlparse(playlist_url)
    playlist_id = parse_qs(parsed_url.query)['list'][0]
    playlist_name = playlist.title

    # Create the directory with the playlist name if it doesn't exist
    directory_name = playlist_name.replace(' ', '_')
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    print(f"\nNumber of videos in playlist: {len(playlist.video_urls)}")

    downloaded_videos = []  # List to store the names of downloaded videos

    for i, url in enumerate(playlist.video_urls, start=1):
        download_video(url, directory_name)
        downloaded_videos.append(url)  # Append the downloaded video URL to the list
        print(f"\nDownloaded video {i} of {len(playlist.video_urls)}")

    print("\nAll videos in the playlist have been downloaded successfully.\n")

    # Clear the text file
    with open('url.txt', 'w') as file:
        file.write('')

# Read the playlist URL from a text file
with open('url.txt', 'r') as file:
    playlist_url = file.readline().strip()
    download_playlist(playlist_url)