import youtube_dl
import os
from youtube_dl_options import get_youtube_dl_download_options

# TODO refactor to get from environment as option
storage_location = '/music/'


# TODO docs

def get_playlist_to_download_from_env():
    return os.getenv('YOUTUBE_PLAYLIST').strip('"')  # removes " " from the string


# TODO docs
def download_youtube_playlist(playlist_url, config):
    with youtube_dl.YoutubeDL(config) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f'Something went wrong downloading the playlist: {playlist_url}')
            print(e)


def main():
    youtube_playlist_to_download = get_playlist_to_download_from_env()

    if not youtube_playlist_to_download:
        print("Set the YOUTUBE_PLAYLIST_TO_DOWNLOAD environment variable so we know which playlist to download")
        return

    print('Starting download!')

    youtube_dl_config = get_youtube_dl_download_options(storage_location)

    download_youtube_playlist(youtube_playlist_to_download, youtube_dl_config)

    print('Finished download!')


if __name__ == '__main__':
    main()
