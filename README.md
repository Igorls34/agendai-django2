# 🚀 **AgendAI - Sistema de Agendamentos Django**

Sistema completo de agendamentos com notificações por email, SMS e WhatsApp. Pronto para produção e deploy na nuvem.

## 🌐 **Deploy no Vercel (Recomendado)**

### **Passo 1: Configurar Repositório**
1. Certifique-se de que o código está no GitHub: `https://github.com/Igorls34/agendai-django2`
2. O projeto já está configurado com `vercel.json` e `api/index.py`

### **Passo 2: Deploy no Vercel**
1. Acesse: [vercel.com/new](https://vercel.com/new)
2. Conecte sua conta do GitHub
3. Selecione o repositório `agendai-django2`
4. Configure:
   - **Framework Preset:** `Other`
   - **Root Directory:** `./`
   - **Build Command:** `pip install -r requirements.txt`
   - **Output Directory:** `./`

### **Passo 3: Configurar Variáveis de Ambiente**
No Vercel Dashboard → Project Settings → Environment Variables:

```bash
# Django
SECRET_KEY=sua-secret-key-muito-segura-aqui
DEBUG=False
ALLOWED_HOSTS=agendai-django2.vercel.app,agendai-django2-10bfs7t1z-igors-projects-3b05ccee.vercel.app

# Banco de dados (PostgreSQL)
DATABASE_URL=postgresql://usuario:senha@host:porta/database

# Email (Gmail)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=seu-email@gmail.com
EMAIL_HOST_PASSWORD=sua-senha-de-app-gmail

# Twilio
TWILIO_ACCOUNT_SID=seu-account-sid
TWILIO_AUTH_TOKEN=seu-auth-token
TWILIO_PHONE_NUMBER=+5511999999999
```

### **Passo 4: Executar Migrações**
Após o primeiro deploy, execute:
```bash
# Via terminal local ou Vercel CLI
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
```

### **Passo 5: URLs Após Deploy**
- **Aplicação:** `https://agendai-django2.vercel.app`
- **Admin:** `https://agendai-django2.vercel.app/admin/`
- **Dashboard:** `https://agendai-django2.vercel.app/dashboard/`

---

## 🖥️ **Desenvolvimento Local**

### **Pré-requisitos:**
- Python 3.12+
- Git

### **Instalação:**
```bash
# Clone o repositório
git clone https://github.com/Igorls34/agendai-django2.git
cd agendai-django2

# Instale dependências
pip install -r requirements.txt

# Execute migrações
python manage.py migrate

# Crie dados de exemplo
python manage.py seed_demo

# Crie superusuário
python manage.py createsuperuser

# Execute servidor
python manage.py runserver
```

### **Acesse:**
- **Aplicação:** `http://127.0.0.1:8000/`
- **Admin:** `http://127.0.0.1:8000/admin/`
- **Dashboard:** `http://127.0.0.1:8000/dashboard/`

---

## 📱 **Funcionalidades**

### ✅ **Sistema Completo:**
- 📅 **Agendamentos** com validação de horários
- 👥 **Dashboard administrativo** com tabela responsiva
- 📧 **Notificações por email** automáticas
- 📱 **SMS** para qualquer número brasileiro
- 💬 **WhatsApp** (configurado para produção)
- � **Busca e filtros** avançados
- � **Export CSV** de agendamentos
- 🎨 **Interface moderna** com Tailwind CSS

### 🎯 **Fluxo de Uso:**
1. **Cliente** acessa a página inicial
2. **Escolhe** um serviço disponível
3. **Preenche** dados pessoais
4. **Seleciona** data e horário disponível
5. **Confirma** agendamento
6. **Recebe** notificações automáticas
7. **Administrador** gerencia via dashboard

---

## ⚙️ **Configurações**

### **Email (Gmail SMTP):**
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-de-app-gmail'
```

### **Twilio (SMS/WhatsApp):**
```python
TWILIO_ACCOUNT_SID = 'seu-account-sid'
TWILIO_AUTH_TOKEN = 'seu-auth-token'
TWILIO_PHONE_NUMBER = '+5511999999999'
```

---

## 🗂️ **Estrutura do Projeto**

```
agendai-django2/
├── agendai/                 # Configurações Django
├── bookings/                # App principal
├── templates/               # Templates HTML
├── static/                  # Arquivos estáticos
├── api/                     # Ponto de entrada Vercel
├── vercel.json             # Configuração Vercel
└── requirements.txt        # Dependências Python
```

---

## 💰 **Custos**

- **Vercel:** Plano gratuito inclui 100GB bandwidth/mês
- **PostgreSQL:** Neon/Supabase (~$0-5/mês)
- **Email:** Gratuito via Gmail
- **SMS:** ~$0.05 cada (~R$ 0,25)
- **WhatsApp:** Gratuito em produção

---

## 🔧 **Comandos Úteis**

```bash
# Desenvolvimento
python manage.py runserver              # Iniciar servidor
python manage.py migrate                # Executar migrações
python manage.py seed_demo              # Criar dados exemplo
python manage.py createsuperuser        # Criar admin

# Produção
python manage.py collectstatic          # Coletar arquivos estáticos
python manage.py check --deploy         # Verificar configurações produção
```

---

## 📞 **Suporte**

Para dúvidas ou problemas:
1. Verifique os **logs do Vercel**
2. Teste localmente primeiro
3. Consulte a documentação do [Django](https://docs.djangoproject.com/) e [Vercel](https://vercel.com/docs)

---

**🎉 Pronto para produção! Seu sistema de agendamentos está completo e funcional.**
2. **Ative o WhatsApp Sandbox**:
   - No console do Twilio, vá para "Messaging" > "Try it out" > "WhatsApp"
   - Siga as instruções para ativar o sandbox
3. **Configure as credenciais** no `settings.py`:
   ```python
   TWILIO_ACCOUNT_SID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Do seu dashboard
   TWILIO_AUTH_TOKEN = 'your_auth_token_here'               # Do seu dashboard
   TWILIO_WHATSAPP_NUMBER = 'whatsapp:+14155238886'         # Número do sandbox
   ```
4. **Teste a configuração**:
   ```bash
   python test_twilio.py
   ```

### Formato dos Números de Telefone
Para o WhatsApp funcionar, o número deve estar no formato internacional:
- ✅ **Correto**: `11999999999` (sistema adiciona +55 automaticamente)
- ✅ **Correto**: `+551199999999`
- ❌ **Errado**: `(11) 99999-9999`
- ❌ **Errado**: `11 99999-9999`

### Limitações do Sandbox
- ❌ **Cada número precisa ser adicionado manualmente**
- ❌ **Limitação de 100 mensagens por dia**
- ❌ **Apenas números verificados funcionam**
- ❌ **Não é adequado para produção**

### Para Produção Real
1. **WhatsApp Business API** (Recomendado):
   - Aprovação da Meta necessária
   - Sem limitações de números
   - Funciona com qualquer cliente
   - Custo baseado no uso

2. **Alternativas mais simples**:
   - **SMS via Twilio**: Funciona com qualquer número
   - **Email**: Já implementado e funcionando
   - **Telegram Bot**: Mais fácil de implementar

### Recomendação Atual
Para testes/desenvolvimento: Use apenas **email** (já funciona perfeitamente)
Para produção: Considere SMS ou WhatsApp Business API

### Como Desabilitar WhatsApp Temporariamente
Se quiser usar apenas email por enquanto, comente as linhas do WhatsApp no código.

### Como Funciona
- Quando um agendamento é confirmado no dashboard, o sistema:
  - Envia email para o cliente (se email fornecido)
  - Envia WhatsApp para o cliente (se telefone fornecido)
  - A mensagem inclui detalhes do serviço, data/hora e status

Ideias de Próximos Passos (quando for vender)
Confirmação por e-mail/WhatsApp (integração externa).
Pagamento adiantado (checkout simples por serviço).
Usuário final com login para reagendar/cancelar.
Calendário semanal no dashboard (grid visual).
Regras de disponibilidade por dia da semana e feriados.

## 🚀 Deploy para Produção

### Railway (Recomendado - Deploy Automático)
1. **Acesse:** [railway.app](https://railway.app)
2. **Conecte seu GitHub** e selecione o repositório `agendai-django`
3. **Configure variáveis de ambiente:**
   ```bash
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app.railway.app
   DATABASE_URL=postgresql://...
   
   # Email (opcional)
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-gmail-app-password
   
   # Twilio (opcional)
   TWILIO_ACCOUNT_SID=your-twilio-sid
   TWILIO_AUTH_TOKEN=your-twilio-token
   TWILIO_PHONE_NUMBER=+1234567890
   ```
4. **Deploy automático!** 🚀

### Heroku
```bash
# 1. Instale Heroku CLI
heroku create seu-app-agendai

# 2. Configure variáveis de ambiente
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=seu-app.herokuapp.com

# 3. Deploy
git push heroku master
```

### Configuração Local de Produção
```bash
# 1. Instale dependências de produção
pip install -r requirements.txt

# 2. Configure variáveis de ambiente
export SECRET_KEY=your-secret-key
export DEBUG=False
export ALLOWED_HOSTS=localhost,127.0.0.1

# 3. Execute com gunicorn
gunicorn agendai.wsgi --bind 0.0.0.0:8000
```

---
