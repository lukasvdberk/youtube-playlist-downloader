# Youtube Playlist Downloader
This is a simple script that downloads all the songs from a youtube playlist and converts them to mp3 files.

# Running
Use the docker-compose file to get up and running quickly

Edit the docker-compose file to update the youtube playlist environment variable to the playlist you want to download.


Start the script
```bash
docker-compose up
```

When the script is done all the files will be in the `./music` folder

Enjoy!

Docker hub link: https://hub.docker.com/r/lukasberk/youtube_playlist_downloader

# Tips
To create a youtube playlist from almost any source (like Spotify, Tidal, Apple Music, etc) use [this](https://soundiiz.com/) tool.