from typing import List, Tuple
import json
from collections import Counter
import re

def q3_time(file_path: str) -> List[Tuple[str, int]]:

    #Usamos un Counter para contar las menciones
    mention_counter = Counter()
    #Usamos regex para encontrar menciones en el formato @username
    mention_pattern = re.compile(r'@\w+')

    # Cargamos todo el archivo con el fin de optimizar el tiempo de ejecución
    with open(file_path, 'r') as file:
        data = file.readlines()
    
    # Procesamos cada línea del archivo
    for line in data:
        tweet = json.loads(line)
        #Encontramos las menciones en el contenido del tweet
        mentions = mention_pattern.findall(tweet['content'])
        #Actualizamos el contador de menciones
        mention_counter.update(mentions)
    
    # Encontramos las 10 menciones más comunes
    top_mentions = mention_counter.most_common(10)

    return top_mentions