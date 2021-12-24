# Establishing basic RabbitMQ things
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Doubling this line cuz no setup.py, later
channel.queue_declare('phones')


# Getting da phones (hardocded, duh) from mock API
import requests

r = requests.get('http://demo6884121.mockable.io/get_phones')
# Just in case
try:
    phones = r.json()['phones']
except Exception as e:
    print('Died from cringe. {}'.format(e))


# Sending phones one by one because for the love of God I can not figure out the normal way
for phone in phones:
    channel.basic_publish(exchange='', routing_key='phones', body=phone)
connection.close()
