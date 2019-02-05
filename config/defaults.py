# Mail client configuration
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
# Mail login info
MAIL_USERNAME = "YOUR_EMAIL_ADDRESS_HERE"
MAIL_PASSWORD = "YOUR_PASSWORD_HERE"
# Datebase connection info
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = "mysql://server:web_connection@localhost/improvisor"
# Secret Key
SECRET_KEY = "b'\\x19~t\\x97o\\x99\\x05\\x99\\xc3x\\xfdESe\\t\\x15m\\x9ePW\\x12\\xc3M\\xcc'"
