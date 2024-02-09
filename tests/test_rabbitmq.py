'''test_rabbitmq.py'''
import threading
import pytest
from sender import send_message
from receiver import receive_messages

@pytest.fixture
def start_receiver():
    '''starts receiver'''
    receiver_thread = threading.Thread(target=receive_messages)
    receiver_thread.start()
    yield
    receiver_thread.join()

def test_rabbitmq_communication():
    '''sends message and check it was received'''
    message = "hello, world!"
    send_message(message)
    msg_received = receive_messages()

    assert msg_received, "Receiver did not receive the message"
