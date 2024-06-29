from typing import List, Tuple
import json
from collections import Counter
import re

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    #Usamos un Counter para contar la frecuencia de cada emoji
    emoji_counter = Counter()
    
    #expresion regular para encontrar emojis en un texto
    emoji_pattern = re.compile(
        r'['
        r'\U0001F600-\U0001F64F'  # Emoticons
        r'\U0001F300-\U0001F5FF'  # Símbolos y pictogramas
        r'\U0001F680-\U0001F6FF'  # Símbolos de transporte y mapas
        r'\U0001F1E0-\U0001F1FF'  # Banderas (iOS)
        r']', 
        flags=re.UNICODE
    )
    #Cargamos los datos linea por linea con el fin de optimizar el uso de memoria
    with open(file_path, 'r') as file: 
        #Procesamos los los datos
        for line in file:            
            tweet = json.loads(line)
            ##Encontramos los emojis en el contenido del tweet
            emojis = emoji_pattern.findall(tweet['content'])
            #Actualizamos el contados de emojis
            emoji_counter.update(emojis)
    
    #encontramos los 10 emojis mas usados        
    top_emojis = emoji_counter.most_common(10)

    return top_emojis