from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha
from email.mime.multipart import MIMEMultipart  # padrão de e-mail com assunto, destinatário, etc.
from email.mime.text import MIMEText  # corpo do e-mail ou texto em html
from email.mime.image import MIMEImage  # recebe uma imagem para o e-mail.
import smtplib  # é quem realmente vai enviar o e-mail.

with open('template.html', 'r') as html:
    template = Template(html.read())  # faz a leitura do que está dentro do arquivo html
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Derick Deiró', data=data_atual)  # é o corpo da msg com os placeholders

msg = MIMEMultipart()
msg['from'] = 'Luiz Otávio Miranda'  # nome da pessoa que está enviando
msg['to'] = meu_email  # e-mail de destino (DESTINATÁRIO)
msg['subject'] = 'Atenção este é um e-mail de teste.'  # assunto do e-mail.

corpo = MIMEText(corpo_msg, 'html')  # pode ser texto simples, ou informar que é html
msg.attach(corpo)  # está anexando o texto do MIMItext na msg.

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)


# liberar acesso de app menos seguros através do link https://myaccount.google.com/lesssecureapps
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)  # e-mail que está enviando a msg.
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)
