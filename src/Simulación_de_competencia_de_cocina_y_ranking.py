rounds = [
{
'theme': 'Entrada',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Santiago': {'judge_1': 6, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 8},
}
},
{
'theme': 'Plato principal',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Mateo': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Camila': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Lucía': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
}
},
{
'theme': 'Postre',
'scores': {
'Valentina': {'judge_1': 7, 'judge_2': 8,
'judge_3': 7},
'Mateo': {'judge_1': 9, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 8, 'judge_2': 7,
'judge_3': 9},
'Santiago': {'judge_1': 7, 'judge_2': 7,
'judge_3': 6},
'Lucía': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
}
},
{
'theme': 'Cocina internacional',
'scores': {
'Valentina': {'judge_1': 8, 'judge_2': 9,
'judge_3': 9},
'Mateo': {'judge_1': 7, 'judge_2': 6,
'judge_3': 7},
'Camila': {'judge_1': 9, 'judge_2': 8,
'judge_3': 8},
'Santiago': {'judge_1': 8, 'judge_2': 9,
'judge_3': 7},
'Lucía': {'judge_1': 7, 'judge_2': 7,
'judge_3': 8},
}
},
{
'theme': 'Final libre',
'scores': {
'Valentina': {'judge_1': 9, 'judge_2': 8,
'judge_3': 9},
'Mateo': {'judge_1': 8, 'judge_2': 9,
'judge_3': 8},
'Camila': {'judge_1': 7, 'judge_2': 7,
'judge_3': 7},
'Santiago': {'judge_1': 9, 'judge_2': 9,
'judge_3': 9},
'Lucía': {'judge_1': 8, 'judge_2': 8,
'judge_3': 7},
}
}
]
ranking = { 'Valentina':{'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
           'Lucía':{'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
           'Mateo':{'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
           'Camila':{'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0},
           'Santiago':{'Puntaje': 0, 'Rondas ganadas': 0, 'Mejor ronda':0, 'Promedio': 0.0}}
cant_rondas = 1
for ronda in rounds:
    puntaje_ronda = ronda['scores']
    ganador_puntaje = -1
    ganador_nombre = ''
    for chef in puntaje_ronda:
        puntaje_jueces = puntaje_ronda[chef]
        puntaje_total = sum(puntaje_jueces.values())
        if ganador_puntaje < puntaje_total:
            ganador_nombre = chef // preguntar
            ganador_puntaje = puntaje_total
        ranking[chef]['Puntaje'] += puntaje_total
        if ranking[chef]['Mejor ronda'] < puntaje_total:
            ranking[chef]['Mejor ronda'] = puntaje_total
        ranking[chef]['Promedio'] = ranking[chef]['Puntaje'] / cant_rondas
    ranking[ganador_nombre]['Rondas ganadas'] += 1   
    print(f"Ronda {cant_rondas} - {ronda['theme']}:\n Ganador: {ganador_nombre} ({ganador_puntaje} pts)")
    print(f" tabla de posiciones: \n")
    for chef, stats in ranking.items():
        print(f"{chef}: Puntaje: {stats['Puntaje']}, Rondas ganadas: {stats['Rondas ganadas']}, Mejor ronda: {stats['Mejor ronda']}, Promedio: {stats['Promedio']}")
    cant_rondas += 1

print('Tabla final de posiciones final:')
# Ordenamos el ranking: 'reverse=True' para que el mayor puntaje vaya primero
ranking_final = sorted(ranking.items(), key=lambda x: x[1]['Puntaje'], reverse=True)

for chef, stats in ranking_final:
    print(f"{chef}: Puntaje: {stats['Puntaje']}, Rondas ganadas: {stats['Rondas ganadas']}, Mejor ronda: {stats['Mejor ronda']}, Promedio: {stats['Promedio']}")

