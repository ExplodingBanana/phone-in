# Establishing basic RabbitMQ things
import sys
import pika, requests

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Doubling this line cuz no setup.py, later
channel.queue_declare('phones')


def callback(ch, method, properties, body):
    # Telling (mock) API to message ma bitchez
    r = requests.post('http://demo6884121.mockable.io/send_message', {'phone': str(body)})

    # Again, just in case
    response = r.json()['msg']
    print(response)
    
# To allow Ctrl+C'ving your soul
def main():
    channel.basic_consume(queue='phones', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)