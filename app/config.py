class Config:
    # SQLite en la carpeta instance/ (se crea sola).
    SQLALCHEMY_DATABASE_URI = "sqlite:///pedidos.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
