# Arquivo de configuração de exemplo para AgendAI
# Copie este arquivo para settings_local.py e configure suas credenciais

# Configurações de Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'  # Substitua pelo seu email
EMAIL_HOST_PASSWORD = 'sua-senha-app-gmail'  # Senha de app do Gmail

# Configurações do Twilio
TWILIO_ACCOUNT_SID = 'seu-account-sid'  # Do seu dashboard Twilio
TWILIO_AUTH_TOKEN = 'seu-auth-token'    # Do seu dashboard Twilio
TWILIO_PHONE_NUMBER = '+1234567890'     # Seu número Twilio

# Outras configurações
SECRET_KEY = 'sua-secret-key-unica'  # Gere uma chave secreta segura
DEBUG = True  # False para produção
