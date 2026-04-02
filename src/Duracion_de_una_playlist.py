playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "8:02"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]
longest_song = playlist[0]
shortest_song = playlist[0]
total_seconds = 0
for song in playlist: 
    current_song_parts = song['duration'].split(':')
    current_seconds = int(current_song_parts[0])*60 + int(current_song_parts[1])
    total_seconds += current_seconds
    max_parts = longest_song['duration'].split(':')
    max_sec = int(max_parts[0]) * 60 + int(max_parts[1])
    if max_sec < current_seconds:
        longest_song = song
    min_parts = shortest_song['duration'].split(':')
    min_sec = int(min_parts[0]) * 60 + int(min_parts[1])
    if min_sec > current_seconds:
        shortest_song = song
print(f"Duracion total: {total_seconds//60}m {total_seconds%60:02d}s")
print(f'Cancion mas larga: "{longest_song["title"]}" ({longest_song["duration"]})')
print(f'Cancion mas corta: "{shortest_song["title"]}" ({shortest_song["duration"]})')
