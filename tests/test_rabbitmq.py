# test_rabbitmq.py
import threading
import pytest
from unittest.mock import patch
from sender import send_message
from receiver import MessageReceiver, receive_message

@pytest.fixture
def start_receiver():
    receiver_thread = threading.Thread(target=receive_message)
    receiver_thread.start()
    yield
    receiver_thread.join()

@patch('sender.pika.BlockingConnection')
def test_rabbitmq_communication(mock_blocking_connection):
    message = "hello, world!"

    mock_connection = mock_blocking_connection.return_value
    mock_channel = mock_connection.channel.return_value

    send_message(message)


@patch('receiver.pika.BlockingConnection')
def test_receive_message(mock_blocking_connection):
    connection_params = {'host': 'localhost'}

    mock_connection = mock_blocking_connection.return_value
    mock_channel = mock_connection.channel.return_value

    mock_channel.basic_consume.side_effect = lambda queue, on_message_callback, auto_ack: on_message_callback(None, None, None, 'hello, world!')

    receiver_instance = MessageReceiver(connection_params)
    receive_message(receiver_instance)

    assert receiver_instance.received_message == 'hello, world!'
