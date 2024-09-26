import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma_chave_muito_secreta'
    DATA_FOLDER = os.path.join(os.getcwd(), 'data')
