# Create m3u playlists from directory names

import os
from pathlib import Path

music_formats = ['.flac', '.mp3']

def listfiles(directory):
    files = os.listdir(directory)
    return files

def scan_music(directory):
    
    # Get list of all files in the directory
    files = reversed(  # Reverse so the order is newest first
        sorted(
        Path(directory).iterdir(),
        key=os.path.getctime  # Sort by file creation date
        )
    )
    music_files = []
    # Iterate through every file found in the directory
    for file in files:
        # If the file is an acceptable file format
        if Path(file).suffix in music_formats:
            # Add to music found list
            music_files.append(file)
            print(f'Valid file: {file}')
            
    # Return results
    return music_files

def create_playlist(directory, music_files):
    playlist_name = directory + '.m3u8'
    
    with open(playlist_name, 'w') as f:
        for file in music_files:
            file_entry = os.path.join(file)
            #print(f'Playlist Entry: {file_entry}')
            f.write(file_entry + '\n')
    print(f'Created playlist: {directory}')

root_directory = '.'
for directory in listfiles(root_directory):
    if os.path.isdir(directory):
        # Scan folder for music
        print(f'Processing directory: {directory}')
        music_files = scan_music(directory)
        
        create_playlist(directory, music_files)
