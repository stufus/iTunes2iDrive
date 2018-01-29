import os, shutil
from libpytunes import Library

home = os.path.expanduser("~")
lib = Library(home + "\\Music\\iTunes\\iTunes Music Library.xml")
songs = {}
destination_drive = "D:\\"

for id, song in lib.songs.items():
    song_location = song.location
    try:
        if (song_location and song.kind.find("audio file") != -1):
            new_filename = str(id) + '_' + os.path.basename(song.location)
            songs[id] = { 'drive_location': song_location,
            'new_filename': new_filename,
            'song_length': song.length,
            'song_artist': song.artist,
            'song_name': song.name,
                }

        else:
            print "Error: Song " + str(id) + "has no location"
    except:
        pass

for playlists in lib.getPlaylistNames():
    output_file = open(destination_drive + '//Playlists//' + playlists + '.m3u', 'w')
    for song in lib.getPlaylist(playlists).tracks:
        try:
            actual_song = songs[song.track_id]
            #output_file.write("#EXTINF:" + str(actual_song['song_length']) + "," + str(actual_song['song_artist'].encode('ascii')) + " - " + str(actual_song['song_name'].encode('ascii')) + "\r\n../" + str(actual_song['new_filename']) + "\r\n\r\n")
            if song.kind.find("audio file") != -1:
                output_file.write("../" + str(actual_song['new_filename']) + "\r\n")
                shutil.copy2(actual_song['drive_location'],destination_drive+actual_song['new_filename'])
        except:
            pass
    output_file.close()





