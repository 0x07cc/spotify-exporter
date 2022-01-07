#!/usr/bin/env python3
'''
Spotify Playlist Reader and Exporter:
Given a public Spotify playlist URL, it creates an HTML file containing
title, artists and album of the tracks in that playlist.
This script is a test for GitHub Actions.
Tested on Jan 2022.
'''
import json
import re
import requests
import htmlexporter

# Parameters
url = "https://open.spotify.com/playlist/37i9dQZF1EpyzGli8mJhi9"
outputFile = "index.html"


class Track:
    def __init__(self, name, artist, album, coverURL):
        self.name = name
        self.artist = artist
        self.album = album
        self.coverURL = coverURL


def abort():
    print("Aborting.")
    exit(-1)


# Page downloading
try:
    r = requests.get(url)
except (requests.exceptions.RequestException, ConnectionError):
    print("Error while downloading the playlist page.")
    print("Is the URL correct?")
    abort()

if r.status_code != 200:
    print("Error while downloading the playlist page.")
    abort()

HTMLpage = r.text

# Searching for the JSON data.
# This will omit the two leading characters: {"
match = re.search("session.+}</script>", HTMLpage)

if match:
    # Adding {" for a valid JSON string and removing the </script> tag
    dataString = jsonss = '{"' + HTMLpage[match.start():match.end() - 9]

else:
    print("Cannot find the JSON string in the page.")
    print("Is the URL a valid Spotify Playlist URL?")
    print("Is the page format changed again?")
    abort()

# Parsing JSON data
try:
    data = json.loads(dataString)
except json.JSONDecodeError:
    print("Error while decoding JSON string.")
    abort()

if "entities" in data:
    items = data["entities"]["items"]
else:
    print("Error while getting items")
    abort()

lastItem = ""
for item in items:
    print(f'item found: "{item}"')
    lastItem = item

if len(lastItem) == 0:
    print("Error while getting last item")
    abort()

try:
    data = items[lastItem]
except KeyError:
    print(f'Error while getting data for the item "{lastItem}"')
    abort()

# Playlist name
if "name" in data:
    playlistName = data["name"]
else:
    print("Error while getting playlist name.")
    playlistName = ""

exporter = htmlexporter.HTMLExporter(playlistName, outputFile)

if "tracks" not in data or "items" not in data["tracks"]:
    print("No tracks found in JSON data. Is this a playlist?")
    abort()

for track in data["tracks"]["items"]:
    try:
        # Album
        album = track["track"]["album"]
        # Album name
        albumString = album["name"]
        # Picture (300x300)
        coverURL = album["images"][1]

        # Artist : A track can have several artists.
        artistString = ""
        artists = track["track"]["artists"]

        artistsSize = len(artists)
        if artistsSize == 1:
            artistString = artists[0]["name"]
        elif artistsSize > 1:
            for i in range(artistsSize):
                # If this is not the last artist, add a comma.
                if i < (artistsSize - 1):
                    artistString += artists[i]["name"] + ", "
                else:
                    artistString += artists[i]["name"]

        # A track has only a name
        nameString = track["track"]["name"]
        exporter.addRow(Track(nameString, artistString, albumString, coverURL))
    except (ValueError, KeyError):
        print("Error while getting data for a song")
