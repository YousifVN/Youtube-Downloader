# YouTube Downloader

This project contains two Python scripts, `video.py` and `playlist.py`, that use the `pytube` library to download YouTube videos and playlists.

## Benefits

- Download individual YouTube videos or entire playlists with a single command.
- Download videos in their highest quality
- Progress tracking for downloads.
- Automatically saves videos to a specified directory.
- Reads URLs from a text file, so you don't have to paste them into the code.

## Usage

### video.py

1. Put the URL of the video you want to download in a text file named `url.txt`.
2. Run `video.py`. The script will read the URL from `url.txt`, download the video, and save it to a directory named "downloads".
3. After the download is complete, `url.txt` will be cleared so you can use it again.

### playlist.py

1. Put the URL of the playlist you want to download in a text file named `url.txt`.
2. Run `playlist.py`. The script will read the URL from `url.txt`, download all the videos in the playlist, and save them to a directory named after the playlist.
3. After the download is complete, `url.txt` will be cleared so you can use it again.

## Documentation

### video.py

- `progress_function(stream, chunk, bytes_remaining)`: This function is called periodically during the download to track the progress. It calculates the percentage of the video that has been downloaded and prints it.
- `download_video(url)`: This function downloads a YouTube video. It takes the URL of the video as a parameter. The video is saved to a directory named "downloads".

### playlist.py

- `progress_function(stream, chunk, bytes_remaining)`: This function is called periodically during the download to track the progress. It calculates the percentage of the video that has been downloaded and prints it.
- `download_video(url, output_path)`: This function downloads a YouTube video. It takes the URL of the video and the path where the video should be saved as parameters.
- `download_playlist(playlist_url)`: This function downloads a YouTube playlist. It takes the URL of the playlist as a parameter. The videos are saved to a directory named after the playlist.

## Dependencies

- Python 3.11.1
- pytube 15.0.0


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

