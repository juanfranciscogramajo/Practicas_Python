def analizar_estadisticas_texto(text):
    """
    Recibe un texto y calcula la cantidad de líneas, palabras, 
    el promedio de palabras por línea y qué líneas superan ese promedio.
    """
    # 1. Calculamos la cantidad de líneas y palabras
    linesCount = text.count(".") + text.count("!") 
    wordCount = len(text.split()) 
      
    # 2. Calculamos el promedio
    lineAverage = round(wordCount / linesCount, 2)
    
    # 3. Filtramos las líneas que superan el promedio
    linesOverAverage = [line for line in text.split("\n") if len(line.split()) > lineAverage]
    
    # Devolvemos todos los datos calculados para que el Notebook los use
    return linesCount, wordCount, lineAverage, linesOverAverage
