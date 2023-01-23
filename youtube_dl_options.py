# logger for yt dl
# only write errors to the console
class YtLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def get_youtube_dl_download_options(storage_location):
    """
    Get YouTube dl configuration for downloading music
    :param storage_location: - Full path so start with root
    :return:
    """
    return {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredquality': '192',
        }],
        'logger': YtLogger(),
        'quiet': True,
        'restrictfilenames': True,
        'outtmpl': storage_location + '/%(title)s.%(ext)s',
        'prefer_ffmpeg': True,
    }
