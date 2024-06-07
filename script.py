import os
import smtplib
import ssl
from email.message import EmailMessage
import socket

email_remetente = 'russelmytho@gmail.com'  # Substitua pelo seu e-mail
email_senha = os.environ.get("SENHA_EMAIL")  # A senha deve ser definida como variável de ambiente
email_destinatario = 'dudaz.rabelo10@gmail.com'  # Substitua pelo e-mail do destinatário

# Definir o assunto e o corpo do e-mail
assunto = 'Testando'
corpo = '''<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Teste</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
        <tr>
            <td align="center">
                <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                    <tr>
                        <td align="center" style="padding: 40px 0;">
                            <img src="https://img.freepik.com/fotos-gratis/paisagem-de-nevoeiro-matinal-e-montanhas-com-baloes-de-ar-quente-ao-nascer-do-sol_335224-794.jpg" alt="Paisagem" width="400" style="display: block; margin: 0 auto;">
                            <p style="margin-top: 20px; text-align: center;">Olá,</p>
                            <p style="text-align: center;">Este é um e-mail de teste com uma imagem embutida.</p>
                            <p style="text-align: center;">Agradecemos por ter recebido este e-mail de teste.</p>
                            <p style="text-align: center;">Este e-mail foi enviado apenas para fins de demonstração e teste.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>'''

# Criar a mensagem de e-mail
em = EmailMessage()
em['From'] = email_remetente
em['To'] = email_destinatario
em['Subject'] = assunto
em.set_content(corpo, subtype='html')

# Adicionar SSL (camada de segurança)
contexto = ssl.create_default_context()

# Teste de Conexão ao Servidor SMTP
try:
    print("Testando conexão ao servidor SMTP...")
    host = 'smtp.gmail.com'
    port = 465  # Porta correta para SSL
    socket.create_connection((host, port), timeout=10)
    print(f"Conexão ao servidor SMTP {host}:{port} foi bem-sucedida.")
except Exception as e:
    print(f"Falha ao conectar ao servidor SMTP: {e}")

# Fazer login e enviar o e-mail
try:
    print("Conectando ao servidor SMTP...")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto, timeout=60) as smtp:
        print("Conexão estabelecida.")
        print("Fazendo login...")
        smtp.login(email_remetente, email_senha)
        print("Login bem-sucedido.")
        print("Enviando e-mail...")
        smtp.sendmail(email_remetente, email_destinatario, em.as_string())
    print("E-mail enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar o e-mail: {e}")

