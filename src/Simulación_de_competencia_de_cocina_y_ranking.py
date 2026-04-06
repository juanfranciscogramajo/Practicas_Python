def obtener_PuntajeTotal(puntajes_jueces):
    """Obtiene el puntaje total de un chef a partir de los puntajes de los jueces."""
    return sum(puntajes_jueces.values())

def calcular_promedio(puntaje_total, rondas):
    """Calcula el promedio de puntaje por ronda."""
    return puntaje_total / rondas if rondas > 0 else 0

def actualizar_mejor_ronda(chef, puntos_actuales, ranking, ronda_actual):
    """Compara y actualiza si el puntaje actual es el mejor del chef."""
    if puntos_actuales > ranking[chef]['Mejor ronda']:
        ranking[chef]['Mejor ronda'] = puntos_actuales
def actualizar_ranking(chef, puntos_actuales, ranking):
    """Actualiza el ranking del chef con el puntaje actual."""
    ranking[chef]['Puntaje'] += puntos_actuales
    actualizar_mejor_ronda(chef, puntos_actuales, ranking)
    ranking[chef]['Promedio'] = calcular_promedio(ranking[chef]['Puntaje'], ronda_actual)
def imprimir_tabla_posiciones(dict_ranking, titulo="Tabla de posiciones"):
    """Ordena el ranking por puntaje e imprime la tabla."""
    print(f"\n{titulo}:")
    
    # 1. Ordenamos de mayor a menor puntaje
    ranking_ordenado = sorted(dict_ranking.items(), key=lambda x: x[1]['Puntaje'], reverse=True)
    
    # 2. Imprimimos fila por fila
    for chef, stats in ranking_ordenado:
        # Usamos {chef:10} para que todos los nombres ocupen 10 espacios y quede alineado
        print(f"{chef:10} | Puntaje: {stats['Puntaje']:3} | Rondas ganadas: {stats['Rondas ganadas']} | Mejor ronda: {stats['Mejor ronda']:2} | Promedio: {stats['Promedio']}")
    
    print("-" * 65) # Una línea divisoria para que quede prolijo

def simular_competencia(rondas):
    """Ejecuta la simulación completa de la competencia ronda por ronda."""
    
    # El diccionario inicial debe estar dentro de la función
    ranking = { 
        'Valentina': {'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
        'Lucía': {'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
        'Mateo': {'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
        'Camila': {'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
        'Santiago': {'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0}
    }
    
    cant_rondas = 1
    
    for ronda in rondas:
        puntaje_ronda = ronda['scores']
        ganador_puntaje = -1
        ganador_nombre = ''
        
        for chef in puntaje_ronda:
            puntaje_jueces = puntaje_ronda[chef]
            puntaje_total = obtener_PuntajeTotal(puntaje_jueces)
            
            if ganador_puntaje < puntaje_total:
                ganador_nombre = chef 
                ganador_puntaje = puntaje_total
                
            # Llamamos a la función con el parámetro extra (cant_rondas)
            actualizar_ranking(chef, puntaje_total, ranking, cant_rondas)
            
        ranking[ganador_nombre]['Rondas ganadas'] += 1   
        
        print(f"Ronda {cant_rondas} - {ronda['theme']}:\n Ganador: {ganador_nombre} ({ganador_puntaje} pts)")
        imprimir_tabla_posiciones(ranking)
        
        cant_rondas += 1
        
    imprimir_tabla_posiciones(ranking, titulo="Ranking final")