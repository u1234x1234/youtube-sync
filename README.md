[![Docker Pulls](https://img.shields.io/docker/pulls/u1234x1234/youtube-sync.svg?style=flat-square)](https://hub.docker.com/r/u1234x1234/youtube-sync/)

## youtube-sync

Keep any YouTube playlists in sync with your local directory.

`youtube-sync` will download videos on a schedule to local directory. If video already has been there, it will be skipped.

## Usage

Create `config.yml` with the following format:
```yaml
# Download videos
- name: local_dir01
  playlist_url: https://www.youtube.com/user/user01/videos
# Download only audio
- name: local_dir02
  playlist_url: https://www.youtube.com/user/user02/videos
  args: --extract-audio --audio-format mp3 --audio-quality 0 # best quality
```

[Available args](https://github.com/rg3/youtube-dl/blob/master/README.md#post-processing-options)


Then run a docker image (daemon):
```bash
mkdir downloads
docker run -t -d -i -v $PWD/downloads:/downloads -v $PWD/config.yml:/config.yml youtube-sync
```
