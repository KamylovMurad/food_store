import os
from django.core.mail import send_mail
from dotenv import load_dotenv
from config.settings import LOGGER
from config.celery import app

load_dotenv()
promotion = 'Новое сообщение'
# emails = os.getenv('TEST_EMAIL')

# @app.task
# def send_email_promotion():
#     send_email_new_promotion(promotion, emails)
#     LOGGER.debug('Сообщение отправлено')


@app.task
def send_email_promotion(promotion_name, emails):
    send_email_new_promotion(promotion_name, emails)


def send_email_new_promotion(promotion, emails):
    send_mail(subject='Новая акция',
              message=promotion,
              from_email=os.getenv('SMTP_USER'),
              recipient_list=emails,
              fail_silently=False
              )
