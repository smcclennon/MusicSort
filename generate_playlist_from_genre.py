# Generate playlists from the 'genre' metadata within the music files

import os
from pathlib import Path
import mutagen

root_directory = '.'
music_formats = ['.flac', '.mp3']
music_files = []


def listfiles(directory):
    files = os.listdir(directory)
    return files

# Assume music is 1 directory level lower from current position
# Return valid music files as list
def scan_music(directory):
    print(f'Scanning for music in directory: {directory}')
    
    # Get list of all files in the directory
    files = Path(directory).iterdir()
    music_files = []
    # Iterate through every file found in the directory
    for file in files:
        # If the file is an acceptable file format
        if Path(file).suffix in music_formats:
            # Add to music found list
            music_files.append(file)
            #print(f'Found valid file: {file}')
            
    # Return results
    return music_files

def split_genres(files):
    print(f'Organising music by genre...')
    # Sort by file creation date, newest first
    files = reversed(
        sorted(files, key=os.path.getctime)
    )

    organised = {}
    
    # For every file passed in
    for f in files:
      
        # Try and extract the genre from metadata
        try:
            genre = mutagen.File(f)['genre'][0]
        
        # If genre metadata does not exist
        except KeyError:
            genre = 'Unknown'
        
        # If genre of the current file is new
        if genre not in organised:
          
            # Initialise it
            organised[genre] = []
            print(f'Found new genre: {genre}')
        
        # Enter file into the list within the appropriate genre key
        organised[genre].append(f)
    
    return organised

def create_playlist(music_data):
    print('Creating playlists...')
    
    genres = list(music_data.keys())
    for genre in genres:
        playlist_name = 'meta_' + genre.replace('/', ' - ') + '.m3u8'
        print(f'Creating playlist: {playlist_name}')
        
        # List of files from that genre
        music_files = music_data[genre]

        with open(playlist_name, 'w') as f:
          
            # Enter the file paths into the playlist file
            for file in music_files:
                file_entry = os.path.join(file)
                #print(f'Playlist Entry: {file_entry}')
                f.write(file_entry + '\n')



for directory in listfiles(root_directory):
    if os.path.isdir(directory):
        # Scan folder for music
        music_files += scan_music(directory)

genre_organised = split_genres(music_files)
create_playlist(genre_organised)
