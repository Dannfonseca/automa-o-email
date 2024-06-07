import smtplib
import ssl
from email.message import EmailMessage
from google.cloud import secretmanager

def send_email(request):
    email_remetente = 'russelmytho@gmail.com'
    email_senha = 'fswwjozaaufielil'
    email_destinatario = 'pgcnseg@gmail.com'

    assunto = 'Testando'
    corpo = '''<!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Teste</title>
        <style>
            .image-container {
                text-align: center;
                padding: 40px 0;
            }
            .zoom-image {
                display: block;
                margin: 0 auto;
                transition: transform 0.3s ease;
            }
            .zoom-image:hover {
                transform: scale(1.2);
            }
            .email-body {
                margin: 0;
                padding: 0;
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
            }
            .content-table {
                background-color: #ffffff;
            }
            .content-cell {
                padding: 40px 0;
                text-align: center;
            }
        </style>
    </head>
    <body class="email-body">
        <table border="0" cellpadding="0" cellspacing="0" width="100%">
            <tr>
                <td align="center">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" class="content-table">
                        <tr>
                            <td align="center" class="content-cell">
                                <div class="image-container">
                                    <img src="https://img.freepik.com/fotos-gratis/paisagem-de-nevoeiro-matinal-e-montanhas-com-baloes-de-ar-quente-ao-nascer-do-sol_335224-794.jpg" alt="Paisagem" width="400" class="zoom-image">
                                </div>
                                <p>Olá,</p>
                                <p>Este é um e-mail de teste com uma imagem embutida.</p>
                                <p>Agradecemos por ter recebido este e-mail de teste.</p>
                                <p>Este e-mail foi enviado apenas para fins de demonstração e teste.</p>
                                <p>Obrigado!</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>'''

    em = EmailMessage()
    em['From'] = email_remetente
    em['To'] = email_destinatario
    em['Subject'] = assunto
    em.set_content(corpo, subtype='html')

    contexto = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto, timeout=60) as smtp:
            smtp.login(email_remetente, email_senha)
            smtp.sendmail(email_remetente, email_destinatario, em.as_string())
        return 'E-mail enviado com sucesso!'
    except Exception as e:
        return f"Erro ao enviar o e-mail: {e}"

def get_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/YOUR_PROJECT_ID/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=name)
    secret_payload = response.payload.data.decode('UTF-8')
    return secret_payload
