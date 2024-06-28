from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter, defaultdict

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    #Usamos defaultdict para almacenar usuarios por fechas
    date_user_counter = defaultdict(Counter)

    #Cargamos todos los datos con el fin de optimizar el tiempo de ejecucion
    with open(file_path, 'r') as file:
        data = file.readlines()  
          
    #Procesamos los los datos
    for line in data:
        tweet = json.loads(line)
        #convertimos la fecha en datetime.date
        date = datetime.strptime(tweet['date'], "%Y-%m-%dT%H:%M:%S%z").date()
        #obtenemos el nombre de usuario de tweet
        user = tweet['user']['username']
        #incrimentamos el contador del usuario para la fecha correspondiente
        date_user_counter[date][user] += 1
    
    #primero encontramos las 10 fechas con mas tweets
    top_dates = Counter({date: sum(users.values()) for date, users in date_user_counter.items()}).most_common(10)
    #encontramos los usuarios con las twees por cada fecha (10)
    results = [(date, date_user_counter[date].most_common(1)[0][0]) for date, _ in top_dates]

    return results  