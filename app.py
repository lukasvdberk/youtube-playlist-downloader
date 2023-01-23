import youtube_dl
import os
from youtube_dl_options import get_youtube_dl_download_options

# TODO refactor to get from environment as option
DEFAULT_STORAGE_LOCATION = '/music/'


def get_playlist_to_download_from_env():
    """
    Get the playlist to download from the environment variable YOUTUBE_PLAYLIST
    :return: Playlist URL
    """
    return os.getenv('YOUTUBE_PLAYLIST').strip('"')  # removes " " from the string


def get_storage_location_from_env():
    """
    Get the storage location from the environment variable STORAGE_LOCATION
    :return: Storage location
    """

    storage_location = os.getenv('STORAGE_LOCATION')

    if storage_location:
        # removes " " from the string
        return storage_location.strip('"')

    return DEFAULT_STORAGE_LOCATION


def download_youtube_playlist(playlist_url, config):
    """
    Download a playlist from YouTube
    :param playlist_url: URL of the playlist to download
    :param config: Configuration for youtube_dl to use when downloading the playlist
    (use get_youtube_dl_download_options function to get default configuration)
    :return: None
    """
    with youtube_dl.YoutubeDL(config) as ydl:
        try:
            ydl.download([playlist_url])
        except Exception as e:
            print(f'Something went wrong downloading the playlist: {playlist_url}')
            print(e)


def main():
    youtube_playlist_to_download = get_playlist_to_download_from_env()
    storage_location = get_storage_location_from_env()

    # exit if no playlist to download
    if not youtube_playlist_to_download:
        print("Set the YOUTUBE_PLAYLIST_TO_DOWNLOAD environment variable so we know which playlist to download")
        return

    youtube_dl_config = get_youtube_dl_download_options(storage_location)
    download_youtube_playlist(youtube_playlist_to_download, youtube_dl_config)
    print('Finished download!')


if __name__ == '__main__':
    main()
