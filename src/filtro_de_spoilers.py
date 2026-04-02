review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""

spoiler_words = input('Ingrese lista de palabras spoiler separadas por ",": ').split(',')
for word in spoiler_words:
    word = word.strip()
    asteriscos = '*' * len(word)
    review = review.replace(word.lower(),asteriscos)
    review = review.replace(word.capitalize(),asteriscos)
    review = review.replace(word.upper(),asteriscos)
print(review)
