from typing import List, Tuple
import json
from collections import Counter
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    #Usamos un Counter para contar las menciones
    mention_counter = Counter()
    #Usamos regex para encontrar menciones en el formato @username
    mention_pattern = re.compile(r'@\w+')

    #Procesamos los datos línea por línea para optimizar el uso de memoria
    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            #Encontramos las menciones en el contenido del tweet
            mentions = mention_pattern.findall(tweet['content'])
            #Actualizamos el contador de menciones
            mention_counter.update(mentions)
    
    # Encontramos las 10 menciones más comunes
    top_mentions = mention_counter.most_common(10)

    return top_mentions