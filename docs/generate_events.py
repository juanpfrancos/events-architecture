import random
import requests
from faker import Faker
from datetime import datetime, timedelta

# Inicializa Faker para generar datos aleatorios
fake = Faker()

# URL del endpoint
url = 'http://localhost:8008/events/'

# Función para generar un tiempo aleatorio
def generate_random_time():
    # Genera un número aleatorio de días y horas a partir del día de hoy
    start_date = datetime.utcnow()
    random_days = random.randint(1, 30)  # Aleatorio entre 1 y 30 días
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)
    
    random_time = start_date + timedelta(days=random_days, hours=random_hours,
                                          minutes=random_minutes, seconds=random_seconds)
    return random_time.isoformat() + 'Z'


# Opciones posibles para el status
statuses = ["planned", "ongoing", "completed", "cancelled"]

# Función para asignar un status aleatorio
def obtener_status_aleatorio():
    return random.choice(statuses)

# Ejemplo de cómo usarlo
mi_status = obtener_status_aleatorio()

# Función para crear un evento aleatorio
def generate_random_event():
    event = {
        "title": fake.sentence(nb_words=4),
        "description": fake.text(max_nb_chars=200),
        "location": fake.city(),
        "start_time": generate_random_time(),
        "end_time": generate_random_time(),
        "status": obtener_status_aleatorio(),
        "capacity": random.randint(50, 5000)
    }
    return event

# Función para enviar solicitudes
def send_requests(num_requests):
    for _ in range(num_requests):
        event = generate_random_event()
        try:
            response = requests.post(url, json=event, headers={'Accept': 'application/json', 'Content-Type': 'application/json'})
            if response.status_code == 200:
                print("Evento creado con éxito")
            else:
                print(f"Error al crear evento: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud: {e}")

# Enviar 1000 solicitudes
send_requests(50)
