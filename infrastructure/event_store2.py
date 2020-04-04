from kafka import KafkaProducer
import time

producer = KafkaProducer()
for _ in range(100):
    time.sleep(1)
    producer.send('test', b'some_message_bytes')

