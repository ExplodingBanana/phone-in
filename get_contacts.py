# Establishing basic RabbitMQ things
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# Getting da phones (hardocded, duh) from mock API
import requests

r = requests.get('http://demo6884121.mockable.io/get_phones')
# Just in case
try:
    phones = r.json()['phones']
except Exception as e:
    print(f'Died from cringe. {e}')


# You can't send an array in RabbitMQ
for phone in phones:
    channel.basic_publish(exchange='', routing_key='phones', body=phone)
connection.close()
