[![Docker Pulls](https://img.shields.io/docker/pulls/u1234x1234/youtube-sync.svg?style=flat-square)](https://hub.docker.com/r/u1234x1234/youtube-sync/)

## youtube-sync

`youtube-sync` is a containerized daemon that syncs a YouTube playlists with files stored in a local directory.

`youtube-sync` can download any YouTube playlists (audio or video).

`youtube-sync` will check updates from the listed YouTube playlists each day.

Essentially, it is containerized [youtube-dl](https://github.com/rg3/youtube-dl/), working on a schedule.

## Usage

Create `config.yml` with the following format:
```yaml
# Download videos
- name: videos_of_user01
  playlist_url: https://www.youtube.com/user/user01/videos
# Download only audio
- name: music_of_user02
  playlist_url: https://www.youtube.com/user/user02/videos
  args: --extract-audio --audio-format mp3 --audio-quality 0 # best quality
```

[Available args](https://github.com/rg3/youtube-dl/blob/master/README.md#post-processing-options)


Then run a docker (daemon):
```bash
mkdir downloads
docker run -t -d -i -v $PWD/downloads:/downloads -v $PWD/config.yml:/config.yml u1234x1234/youtube-sync:0.0.3
```
