class Config:
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///assistant.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'bw09061983@gmail.com'
    MAIL_PASSWORD = 'rxxkjqrgrkasguxz'
    MAIL_DEFAULT_SENDER = 'flask@example.com'