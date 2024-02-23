'''receiver.py'''
import pika

class MessageReceiver:
    '''message receiver class'''
    def __init__(self, connection_params):
        self.connection_params = connection_params
        self.received_message = None

    def receive_message(self):
        connection = pika.BlockingConnection(self.connection_params)
        channel = connection.channel()
        channel.queue_declare(queue='demo_queue')
        
        def callback(ch, method, properties, body):
            print(f"Received '{body}'")
            self.received_message = body

        channel.basic_consume(queue='demo_queue', on_message_callback=callback, auto_ack=True)

def receive_message(receiver_instance):
    receiver_instance.receive_message()
