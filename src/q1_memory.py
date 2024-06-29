from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter, defaultdict

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    #Usamos defaultdict para almacenar usuarios por fechas
    date_user_counter = defaultdict(Counter)

    #Cargamos y procesamos los datos linea por linea para optimizar el uso de memoria
    with open(file_path, 'r') as file:
        for line in file:            
            tweet = json.loads(line)
            #convertimos la fecha en datetime.date
            date = datetime.strptime(tweet['date'], "%Y-%m-%dT%H:%M:%S%z").date()
            #obtenemos el nombre de usuario de tweet
            user = tweet['user']['username']
            #incrimentamos el contador del usuario para la fecha correspondiente
            date_user_counter[date][user] += 1
    
    #Primero encontramos las 10 fechas con mas tweets
    top_dates = sorted(date_user_counter.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    #Para cada fecha, encontramos el usuario que más publicó
    results = [(date, max(users.items(), key=lambda x: x[1])[0]) for date, users in top_dates]    

    return results