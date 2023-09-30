# youtube-sync

[![Docker Pulls](https://img.shields.io/docker/cloud/build/u1234x1234/youtube-sync.svg?style=flat-square)](https://hub.docker.com/r/u1234x1234/youtube-sync/)
[![Size](https://badgen.net/docker/size/u1234x1234/youtube-sync/1.0.12/arm64)](https://hub.docker.com/r/u1234x1234/youtube-sync/)


* `youtube-sync` is a containerized daemon that downloads YouTube playlists.

* `youtube-sync` will check for updates from the listed YouTube playlists every day and download only new items.

* `youtube-sync` can download any YouTube playlists in a specified format (audio or video).


Essentially, it is Docker containerized [yt-dlp](https://github.com/yt-dlp/yt-dlp) (which is fork of [youtube-dl](https://github.com/rg3/youtube-dl/)), working on a schedule.

## Usage

* Create `config.yml` with the following content:
```yaml
#Download audio only
- name: tensorflow_channel_audio
  playlist_url: https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ/videos
  args: --extract-audio --audio-format mp3 --audio-quality 0 # best quality
#or video
- name: tensorflow_channel_video
  playlist_url: https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ/videos
```

* Then run docker:
```
mkdir downloads
docker run --name youtubesync --restart=always -d -v $PWD/downloads:/downloads -v $PWD/config.yml:/config.yml u1234x1234/youtube-sync:1.0.15
```
All downloads will be available in the local dir `downloads`.

* To view logs:
```
docker logs youtubesync
```


### [Available usage options](https://github.com/yt-dlp/yt-dlp#usage-and-options)
