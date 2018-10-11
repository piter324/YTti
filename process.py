def getInfo(address):
    from pytube import YouTube
    try:
        yt = YouTube(address)
    except:
        print ("Video is not available")
        return

    if yt.streams.filter(only_audio=True, mime_type='audio/mp4').count() < 1:
        print("Audio tracks not available")
        return

    fileInfo = {
        "name":yt.title,
        "title":"",
        "artist":""
    }

    artistTitle = yt.title.split(" - ")
    if len(artistTitle)<2:
        artistTitle = yt.title.split("-")
    
    fileInfo['artist'] = artistTitle[0]
    if len(artistTitle)>1:
        fileInfo['title'] = artistTitle[1]
    
    return fileInfo

def download(address, name):
    from pytube import YouTube
    try:
        yt = YouTube(address)
    except:
        print ("Video is not available")
        return None

    outputFullPath = yt.streams.filter(only_audio=True, mime_type='audio/mp4').order_by('bitrate').first().download(filename=name, output_path="downloaded")
    return outputFullPath

def convertMP4toMP3(filepath, changeVol):
    import subprocess
    import os

    newName = filepath[:-4]+".mp3"
    completed = subprocess.run(["ffmpeg","-y","-i",filepath,"-filter:a","volume="+str(float(changeVol))+"dB",newName])
    if completed.returncode == 0:
        os.remove(filepath)
        print("File converted to MP3. MP4 is removed")
        return newName
    else:
        print("Error converting to MP3")
        return 0 

def addID3(filepath, artist, title):
    import mutagen
    from mutagen.easyid3 import EasyID3

    try:
        audiofile = EasyID3(filepath)
    except mutagen.id3.ID3NoHeaderError:
        audiofile = mutagen.File(filepath, easy=True)
        audiofile.add_tags()

    audiofile['artist'] = artist
    audiofile['title'] = title
    audiofile.save()

def openFromCMD(filepath):
    import subprocess
    subprocess.call(["explorer", filepath])

def wholeProcess(address, info):
    outputFilePath = download(address, info['name'])
    if outputFilePath == None:
        return False
    outputFilePath = convertMP4toMP3(outputFilePath, info['changeVol'])
    if outputFilePath == 0:
        return False
    addID3(outputFilePath, info['artist'], info['title'])
    if info['addToiTunes']: openFromCMD(outputFilePath)
    return True