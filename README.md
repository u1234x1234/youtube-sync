## What's this

Keep any YouTube playlists in sync with your local directory.

`youtube-sync` will download videos on a schedule to local directory. If video already has been there, it will be skipped.

## Usage

Create `to_sync.yml` with the following format:
```yaml
- path: local_dir01
  playlist_url: https://www.youtube.com/user/user01/videos
- path: local_dir02
  playlist_url: https://www.youtube.com/user/user02/videos
```

Then run a docker image:
```bash
docker run -t -d -i -v $PWD/do:/downloads -v $PWD/to_sync.yml:/to_sync.yml youtube-sync
```
