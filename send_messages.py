# Establishing basic RabbitMQ things
from sys import exit
import pika, requests

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


def callback(ch, method, properties, body):
    # Telling (mock) API to message ma bitchez
    r = requests.post('http://demo6884121.mockable.io/send_message', {'phone': str(body)})

    # Again, just in case
    try:
        response = r.json()['msg']
        print(f' [*] Recived from API: {response}')
    except Exception as e:
        print('Died from cringe. {}'.format(e))
    
def main():
    channel.basic_consume(queue='phones', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    # To allow Ctrl+C'ving your soul
    except KeyboardInterrupt:
        print('Interrupted')
        exit(0)