# MusicSort
Generate genre playlists from the metadata found within music files. Playlist are sorted by newest file first.

## Terminal output
```
Scanning for music in directory: Pop
Scanning for music in directory: Rock
Scanning for music in directory: C418 - Minecraft - Volume Alpha
Organising music by genre...
Found new genre: Pop
Found new genre: Unknown
Found new genre: Rock
Found new genre: Films/Games Film Scores
Creating playlists...
Creating playlist: meta_Pop.m3u8
Creating playlist: meta_Unknown.m3u8
Creating playlist: meta_Rock.m3u8
Creating playlist: meta_Films - Games Film Scores.m3u8
```
## Directory listing
- `./Pop/`
- `./Rock/`
- `./C418 - Minecraft - Volume Alpha/`
- `./meta_Pop.m3u8`
- `./meta_Unknown.m3u8`
- `./meta_Rock.m3u8`
- `./meta_Films - Games Film Scores.m3u8`

## Playlist file contents
`./meta_Films - Games Film Scores.m3u8`:
```
C418 - Minecraft - Volume Alpha/C418 - Moog City.flac
C418 - Minecraft - Volume Alpha/C418 - Subwoofer Lullaby.flac
C418 - Minecraft - Volume Alpha/C418 - Door.flac
```
