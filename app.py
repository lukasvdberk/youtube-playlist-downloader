import youtube_dl
import os
from youtube_dl_options import get_youtube_dl_download_options

YOUTUBE_PLAYLIST_TO_DOWNLOAD = get_youtube_dl_download_options()

# TODO refactor to get from environment as option
STORAGE_LOCATION = '/music/'

def get_playlist_to_download_from_env():
    return os.getenv('YOUTUBE_PLAYLIST').strip()

def download_youtube_playlist(playlist_url, config):
    with youtube_dl.YoutubeDL(config) as ydl:
        try:
            ydl.download([playlist_url])
        except:
            print(f'Something went wrong downloading the playlist')


def main():
    if not YOUTUBE_PLAYLIST_TO_DOWNLOAD:
        print("Set the YOUTUBE_PLAYLIST_TO_DOWNLOAD environment variable so we know which playlist to download")
        return

    print('Starting download!')

    youtube_dl_config = get_youtube_dl_download_options(STORAGE_LOCATION)
    download_youtube_playlist(YOUTUBE_PLAYLIST_TO_DOWNLOAD, youtube_dl_config)

    print('Stopping download!')

if __name__ == '__main__':
    main()