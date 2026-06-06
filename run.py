import os
from decouple import config

#Leer el Puerto .env
port = config('API_PORT')

#Ejecutar el Servidor DJango
os.system(f'python manage.py runserver {port}')