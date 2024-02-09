'''Receiver.py'''
import pika

def receive_messages():
    '''Establishes connection to channel, receives and prints messages'''
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='demo_queue')
    method_frame, _,  body = channel.basic_get(queue='demo_queue', auto_ack=True)

    if method_frame:
        print(f"Received message: '{body.decode('utf-8')}'")
        return True
    print("No messages in the queue")
    return False
