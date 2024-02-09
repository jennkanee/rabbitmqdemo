'''sender.py'''
import pika

def send_message(message):
    '''Est connection and sends message'''
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='demo_queue')
    channel.basic_publish(exchange='', routing_key='demo_queue', body=message)

    print(f"Sent '{message}'")

    connection.close()
