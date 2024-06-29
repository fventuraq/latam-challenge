from typing import List, Tuple
import json
from collections import Counter
import re #importamos para  trabajar con expresiones regulares.

def q2_time(file_path: str) -> List[Tuple[str, int]]:

    #Usamos un Counter para contar la frecuencia de cada emoji
    emoji_counter = Counter()
    
    emoji_pattern = re.compile(
        r'['
        r'\U0001F600-\U0001F64F'  # Emoticons
        r'\U0001F300-\U0001F5FF'  # Símbolos y pictogramas
        r'\U0001F680-\U0001F6FF'  # Símbolos de transporte y mapas
        r'\U0001F1E0-\U0001F1FF'  # Banderas (iOS)
        r']', 
        flags=re.UNICODE
    )
    #Cargamos todos los datos con el fin de optimizar el tiempo de ejecucion
    with open(file_path, 'r') as file:
        data = file.readlines()  
          
    #Procesamos los los datos
    for line in data:
        tweet = json.loads(line)
        ##Encontramos los emojis en el contenido del tweet
        emojis = emoji_pattern.findall(tweet['content'])
        #Actualizamos el contados de emojis
        emoji_counter.update(emojis)
    
    #encontramos los 10 emojis mas usados        
    top_emojis = emoji_counter.most_common(10)

    return top_emojis