mport pytube

# URL of the YouTube playlist
playlist_url = "https://www.youtube.com/playlist?list=PL3pGy4HtqwD2kwldm81pszxZDJANK3uGV"

# Initialize a YouTubePlaylist object
yt_playlist = pytube.Playlist(playlist_url)

# Iterate through each video in the playlist
for url in yt_playlist:
    video = pytube.YouTube(url)
    video.streams.get_highest_resolution().download()
