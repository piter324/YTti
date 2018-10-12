# YTti - YouTube to iTunes
This piece of software automatically downloads audio streams from selected YouTube video, converts it to MP3, adds ID3 tags and opens in iTunes, so the track is automatically added to the iTunes library.

## Requirements
- Some version of Windows (tested on Windows 10)
- Python 3
- ffmpeg.exe in the program root folder
- exactly the same folder structure as in this repo
- iTunes set as default *.mp3 file player
- dependencies from "requirements.txt* installed using command: `pip install -r requirements.txt`

## Usage
1. Launch server.py on your computer.
1. Access it using your favorite web browser on your host IP address (port = 80 for simplicity)
1. Follow instuctions displayed in your web browser
1. Be patient, as it takes longer to download and convert some videos (and others not nessesarily)
### Remember!
There's a "downloaded" folder in the program root, where all tracks are saved after conversion. They're not removed automatically, so keep this folder tidy by yourself, unless you want it to take a lot of disk space.



## Changelog
### 0.1
- Downloading audio, converting it to MP3, adding ID3 tags and opening to add to iTunes library
- Added volume adjustment for too loud or too quiet audio
### 0.2
- Added audio trimming