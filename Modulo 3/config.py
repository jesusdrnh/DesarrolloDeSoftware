import os
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env si existe
load_dotenv()

class Config:
    """Configuración base para la aplicación Flask"""
    
    # Clave secreta para protección contra CSRF
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta-por-defecto'
    
    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///todo_app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False