import psutil
import requests
from datetime import datetime
from time import sleep

MEMORY_LIMIT_PERCENT = 70
API_URL = 'http://127.0.0.1:8080/api/v1/item'

while True:
    memory_use = psutil.virtual_memory().percent
    if memory_use > MEMORY_LIMIT_PERCENT:
        current_time = datetime.now().strftime('%H:%M:%S')
        
        data = {
            'key': current_time,
            'value': memory_use
        }
        response = requests.post(
            url=API_URL,
            json=data,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code // 100 == 2:
            print('Alarm sent successfully')
        else:
            print(f'Failed! Status code: {response.status_code}')
    
    sleep(60)
