# Spotify Playlist Reader and Exporter
A script that, given a public Spotify playlist URL, creates an HTML file containing title, artists and album of the tracks in that playlist.  
This script is a test for GitHub Actions.

## Usage (Deploy to your own GitHub Pages)
1. Fork this repo
1. Edit the `url` parameter in `main.py` with a public Spotify Playlist URL
1. Commit and push changes to branches `main` and `pages`
1. Set GitHub pages to source from the `pages` branch (Your repo > Settings > GitHub Pages (under "Options") > Source Branch: `pages`, Source folder: `/ (root)` > Save)

## GitHub Actions
The file `.github/workflows/update_playlist.yml` will run `python3 main.py` in a Ubuntu environment every Tuesday and Saturday at 17:29 UTC.  
The script will create the file `index.html` and the workflow will push the changes to the `pages` branch.  
`github_token` is automatically filled.

## Notes
1. cron time may not be correct/exact: When set to 5:29 PM UTC, I've found that it executes the workflow on 6:19 PM UTC
1. When setting GitHub Pages, the website build (Deployment) can fail if there is no `index.html` file. In this case, wait for the workflow to be executed.

### [Results here (My "On Repeat" Playlist)](https://0x07cc.github.io/spotify-exporter/)
