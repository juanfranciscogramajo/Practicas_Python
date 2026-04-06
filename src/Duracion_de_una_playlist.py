def obtener_segundos(duracion_texto):
    """
    Toma un texto como '5:55' y lo convierte a segundos totales (entero).
    """
    partes = duracion_texto.split(':')
    return int(partes[0]) * 60 + int(partes[1])

def analizar_playlist(playlist):
    """
    Recibe una lista de canciones, calcula la duración total 
    y encuentra la canción más larga y la más corta.
    """
    longest_song = playlist[0]
    shortest_song = playlist[0]
    total_seconds = 0
    
    # obtenemos los segundos de la primera canción para inicializar max_sec y min_sec
    max_sec = obtener_segundos(longest_song['duration'])
    min_sec = obtener_segundos(shortest_song['duration'])
    
    for song in playlist: 
        current_seconds = obtener_segundos(song['duration'])
        total_seconds += current_seconds
        
        # Evaluamos si la canción más larga
        if current_seconds > max_sec:
            max_sec = current_seconds
            longest_song = song
            
        # Evaluamos si la canción más corta
        if current_seconds < min_sec:
            min_sec = current_seconds
            shortest_song = song
            
    # Devolvemos los 3 datos calculados
    return total_seconds, longest_song, shortest_song