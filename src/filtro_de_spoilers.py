
def censurar_review(review, spoiler_words):
    """
    Recibe un texto (review) y una lista de palabras (spoiler_words).
    Devuelve el texto con las palabras spoiler reemplazadas por asteriscos.
    """
    # Recorremos cada palabra de la lista proporcionada
    for word in spoiler_words:
        # Eliminamos espacios en blanco accidentales al inicio o final
        word = word.strip()
        
        # Creamos una cadena de asteriscos del mismo tamaño que la palabra
        asteriscos = '*' * len(word)
        
        # Reemplazamos las variaciones de la palabra en el texto original
        review = review.replace(word.lower(), asteriscos)
        review = review.replace(word.capitalize(), asteriscos)
        review = review.replace(word.upper(), asteriscos)
        
    return review