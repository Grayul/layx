# layx
![Alt text](layx.png)
# Requirements/Dependencies
* Python3.x
* pip3
* MPV
* Get MPV from here: https://mpv.io/

# Installation
Run the following command in the root directory to install playx.
`pip install -e .`
Or install using setup.py as:
`python setup.py install`

# Features
* play by query
* play by youtube url
* play a youtube playlist
* play a billboard chart
* play a spotify playlist
* play from soundcloud playlist
* play from JioSaavn playlist
* play from gaana playlist.
* play from local playlist
* cache support
* CLI using mpv
* auto generate playlist

# Usage
For now, the application is in development phase.
`
usage: playx [-h] [-p] [-n] [-auto] [-d] [-r] [--sync-playlist SYNC_PLAYLIST]
             [-l] [--pl-start PL_START] [--pl-end PL_END]
             [song [song ...]]

playx - Search and play any song that comes to your mind. If you have any
issues, raise an issue in the github (https://github.com/NISH1001/playx) page

positional arguments:
  song                  Name or youtube link of song to download

optional arguments:
  -h, --help            show this help message and exit
  -p, --play-cache      Play all songs from the cache. The cache is located at
                        ~/.playx/songs/ by default
  -n, --no-cache        Don't download the song for later use.
  -auto, --auto         Auto generate playlist
  -d, --dont-cache-search
                        Don't search the song in the cache.
  -r, --no-related      Disable playing related songs extracted from YouTube
  --sync-playlist SYNC_PLAYLIST
                        Sync the playlists. Pass the name as arguement. If all
                        the playlists are to be synced, just pass [All].
  -l, --lyrics          Show lyircs of the song.
  --pl-start PL_START   Start position in case a playlist is passed. If passed
                        without a playlist it has no effect.
  --pl-end PL_END       End position in case a playlist is passed. If passed
                        without a playlist it has no effect.`
             
  
 # Example
Play by song name

`playx man sold world nirvana`
This plays the song titled "The man who sold the world by Nirvana"

# Play by youtube link

`playx https://www.youtube.com/watch?v=4zLfCnGVeL4`
This plays the song The Sound of Silence.

# Play by soundcloud links

`playx https://api.soundcloud.com/tracks/232673157`
This plays soundcloud track

# Play from youtube playlist

`playx https://www.youtube.com/playlist?list=PLwg22VSCR0W6cwuCKUJSkX72xEvYXS0Zx`
This plays the songs from my personal (and public) playlist named Chilld and Wisdom.

# Play from a Billboard Chart

`playx hot-100`
This plays the songs from Billboards hot-100 chart. The billboard charts can be found here

# Play from spotify playlist

`playx https://open.spotify.com/playlist/37i9dQZF1DX5Ozry5U6G0d`
This plays the songs from Spotify Summer Party playlist.

# Play from soundcloud playlist

`playx https://soundcloud.com/devintracy/sets/goodafternoon`
This plays the songs from SoundCloud playlist

# Play from JioSaavn playlist

`playx https://www.jiosaavn.com/featured/magical-amit-trivedi/IGYxX3V4T7w_`
This plays songs from the JioSaavn playlist

# Play from local playlist

The local playlist should have an extension `.playx` in order for us to recognize it as a playlist.

`playx example.playx`


This plays a playlist named example.playx

For a playlist every line is considered an entry.

# Auto-Generate Playlist
`playx --auto`
This will automatically generate a playlist by using the frequency of songs played that has been logged in the log file.


# TO-DO
* use Markov Chains to improve auto-playlist
* use Factorization Machines to improve auto-playlist
* use logs to create simple recommendations
